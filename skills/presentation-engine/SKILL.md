---
name: presentation-engine
description: 將已核准教材與教學策略轉換為 Slide Script、Render Request 與選定輸出；圖片式簡報採 Object Composition First，國語語詞標記採可追溯的字下螢光筆系統。
---

# Presentation Engine

版本：0.10.5

`SLIDE_SCRIPT` 是逐頁簡報唯一內容主檔。圖片式簡報實際渲染交給 `vmax-image-renderer`；不得只交 prompt 宣稱完成。

## 前置條件

執行前讀取核准 LKB、Learning Module Profile、Teaching Strategy Profile、Output Profile、Style/Role/Layout、Canvas/Text policies、最新 Lesson Presentation Execution Rules、Renderer Contract 與 artifact registry（若有）。未核准的上游內容不得進正式輸出。

## 核心來源規則

教材、延伸、教學策略、角色與視覺都只使用已核准來源。學生頁不得含答案、內部 ID、來源 metadata 或教師解題步驟。頁數依內容與投影閱讀密度動態決定。

## 逐頁施工稿三層契約

### PAGE_PLAN
每頁至少包含：`page_purpose`、`student_visible_text`、`source_refs`、`page_family`、`style_variant`、`character_policy`、`OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、`canvas_lock`、`visual_density_profile`、拆頁判斷；有指定語詞標記時另必填 `VOCAB_MARK_PLAN`。

### OBJECT_COMPOSITION_PLAN
包含 `composition_mode`、`background_role`、`text_objects`、`primary_visual_object`、`supporting_visual_objects`、`character_objects`、`annotation_objects`、`layer_order`、`planned_overlaps`、`protected_zones`、`organic_edge_strategy`。一般頁預設 `OBJECT_SCENE`，禁止簡化成「文字區＋一張底圖」。

### VOCAB_MARK_PLAN
每個學生可見的指定語詞至少記錄：
- `term`
- `source_ref`
- `term_color_id`
- `mark_mode: UNDERLINE_HIGHLIGHT`
- `include_punctuation: no`（預設）
- `layer_order: MARK_BELOW_TEXT`
- `clearance_ratio: 0.08–0.12`（字高比例建議值）
- `stroke_height_ratio: 0.10–0.16`（字高比例建議值）
- `span_rule: TERM_ONLY`
- `paired_definition_ref`（適用時）

語詞定位與整句強調不得混用：
- 語詞 → `UNDERLINE_HIGHLIGHT`
- 整句／金句 → `BACKGROUND_HIGHLIGHT`，且須由 `KEY_LINE_PLAN` 或句子強調策略核准。

`UNDERLINE_HIGHLIGHT` 必須位於中文字主要字框下方，與字保留淨距；筆刷可有手繪不規則感，但不得穿過主要筆畫。標點預設不納入。同一語詞在原文與詞語解釋使用同一 `term_color_id`。

### REPRESENTATIVE_CONSTRUCTION
每個啟用頁型補充實際物件位置、文字層級、角色交疊、protected zones、自然輪廓策略與閱讀動線。課文＋語詞代表頁必須實際驗證至少一組 `UNDERLINE_HIGHLIGHT`，不可只在文字規格中宣告。

### SLIDE_SCRIPT
鎖定正式文字、來源、素材、Render Request、版本與教師確認。每頁記錄 object/character/key-line plans；有語詞標記時記錄 `vocab_mark_plan` 與 `term_color_map`。

舊 `image_layout_plan` 只可作兼容摘要，不得取代 Object Composition。

## Object Composition First

施工順序：
`教學焦點 → 正式文字／注音安全區 → 主場景 → 小插圖 → 角色 → 道具／語詞標記 → 金句 → 前中後景與 planned overlaps → Renderer 合成`

不得輸出「完整無字／少字大底圖 → 最後找位置放文字」的舊式 Render Request。文字只能靠搬動才能塞入完整插畫時 → `MONOLITHIC_BACKGROUND_REGRESSION`。

合法 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 不算碰撞。`IMMERSIVE_FULL_SCENE` 只用於有教學理由的封面、高潮、情緒停格、環境沉浸或單一大情境觀察。

## 語詞標記與文字施工

Verified Teaching Text 先鎖定再渲染。課文、注音、生字、形近字、多音字、成語、題目與正式例句不得由圖片模型自由生成。

語詞標記是 `annotation_object`，不是文字本身，也不是烘焙進 AI 圖片的色塊。正式文字位置確認後，若底線位置不準，只修 `VOCAB_MARK_PLAN`／標記物件，不移動正確的課文文字。

以下任一情況在送 Renderer 前即標記 `VOCAB_HIGHLIGHT_COLLISION`：標記穿字、遮注音、範圍錯誤、包含非指定標點、同詞顏色不一致、語詞標記高到變成背景色塊。

## 頁型與代表頁

教師口述型簡報一頁一焦點，不縮字硬塞。小插圖優先自然輪廓。課文閱讀頁以正文為主要物件；形近字一頁一組優先，多音字一頁一字優先；評量頁不放答案。

代表頁至少涵蓋 `TEXT_READING_PAGE`、一般 `OBJECT_SCENE`、高風險語文頁、Lesson Visual Map（若啟用）與其他獨立 page family。若本課有課文語詞標記，代表頁組中至少一頁必須驗證 Vocabulary Marking System。

## Render Request Contract

Render Request 必須帶入 source refs、verified text、canvas lock、object composition plan、character plan、key line plan、protected zones、planned overlaps、role anchors（適用時）、benchmark refs（適用時）；有語詞標記時必須帶 `vocab_mark_plan`。

Acceptance checks 至少包含 `MONOLITHIC_BACKGROUND_PASS`；有語詞標記時另包含 `VOCAB_MARK_ALIGNMENT_PASS`、`VOCAB_MARK_SPAN_PASS`、`VOCAB_MARK_LAYER_PASS`、`TERM_COLOR_CONSISTENCY_PASS`。

## 工作流程

1. 驗證上游來源與核准狀態。
2. 建立全課 PAGE_PLAN。
3. 建立 page-family style matrix。
4. 教師確認逐頁規劃與風格混搭。
5. 確認頁數帳本。
6. 建立各頁型 Representative Construction；課文語詞頁實測字下標記。
7. 教師核准實際看見的代表頁型。
8. 產生正式 Slide Script 與 Render Requests。
9. 路由 Image Renderer 小批次生成。
10. Quality Gate 通過後交付。

## 核心金句

> 語詞標記不是在字後面刷一塊顏色，而是精準告訴學生「這幾個字是一個要注意的語詞」。

> 正式文字位置正確時，標記錯了就修標記，不要再搬課文。