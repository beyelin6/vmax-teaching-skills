# 國語圖片式語文頁規則

版本：1.3

本參考文件供 `presentation-engine` 與 `vmax-image-renderer` 製作國語圖片式簡報時使用。形近字與多音字的專門規則仍以 `skills/character-group-visual-comparison/SKILL.md` 為準。

## 1. 共通教學邏輯

所有頁型優先採：

> 課文證據 → 視覺理解 → 教學發現 → 學生應用

每頁只保留一個主要教學焦點，最多一個必要追問。學生頁不得直接呈現答案、完整結論、正確選項或講者備註。

## 2. 圖片與文字分工

圖片模型負責人物、場景、動作、表情、物件、留白、視線與情境關係；不得承載課文、注音、形近字、成語、句型、修辭名稱、題目、部件拆解等關鍵文字。

受控文字層負責學生可見正式文字。文字須逐字可追溯來源，並與 Object Composition 共同構圖；禁止背景完成後再硬貼大量文字、卡片牆、大量白色矩形或文字框遮圖。

## 2.1 字型與 Font Safety

**本檔不再硬綁 `LXGWWenKaiTC` 或任何單一字型 family。**

正式字型選擇唯一依據：`skills/traditional-chinese-font-safety/SKILL.md`、`font-registry.yaml` 與當次實際 font preflight。

必須記錄／驗證：
- `font_role`
- `selected_font_file/family`
- TW/Taiwan region（思源系列適用）
- glyph coverage
- Bopomofo coverage（需要時）
- fallback_used
- font QA result

建議角色：
- 課文正文／一般說明：依 `body_serif` 或 `body_sans` 角色選取核准字型。
- 生字／形近字：依 `character_learning`，但每個目標字必須實際 glyph check。
- 注音：依 `bopomofo_safe`。
- 活動標題／短提示：依 `rounded_title` 等核准角色。

不得因本參考文件的舊範例名稱，覆蓋 Font Safety 的當次檢查結果。

### Font Change = Text Reflow

字型 family／file、字級、字距、行距、欄寬、換行、文字位置或內容改變，都視為 `text reflow`。

發生 reflow 必須：
1. 更新 `text_layout_revision`。
2. 重新量測 glyph bbox／baseline。
3. 使所有舊語詞底線／圈選／文字 anchor 失效。
4. 重新計算所有依附文字的 annotation。

不得因 fallback 字型成功顯示，就沿用舊標記座標。

## 2.2 Verified Raster Text Components

圖片式簡報正式文字由可控文字工具產生，逐元件校對，再與視覺物件合成。文字圖片元件錯誤時只修該元件，不重生已確認視覺物件。

`TEXT_READING_PAGE` 可使用真正可控的連續文字層；其他圖片式頁使用 Verified Raster Text Components。文字正確性優先於裝飾效果。

## 2.3 Vocabulary Marking System

課文中的指定語詞必須依最新 Execution Rules／Renderer Contract：

- 語詞定位 → `UNDERLINE_HIGHLIGHT`
- 整句／金句 → 核准 `BACKGROUND_HIGHLIGHT`

語詞標記是獨立 annotation object，不可只是「大概畫在某一行」。

固定 anchor 流程：

```text
最終文字排版
→ text_layout_revision
→ term_text + occurrence_index
→ line_id + start/end char index
→ glyph_bbox + baseline_y
→ mark_bbox
→ underline
```

同詞多次出現必須指定 occurrence。無法唯一定位 → `VOCAB_ANCHOR_FAIL`。

文字 reflow 後仍沿用舊標記 → `STALE_VOCAB_MARK_ANCHOR`。

字下標記規則：
- 位於主要字框下方。
- 淨距約字高 8–12%。
- 筆刷厚度約 10–16%。
- 只涵蓋語詞本身，標點預設排除。
- 文字在上、標記在下，不遮注音。
- 同一 `term_color_id` 原文／詞義一致。

有語詞標記頁必須通過：`VOCAB_ANCHOR_PASS`、`VOCAB_REFLOW_PASS`、`VOCAB_MARK_ALIGNMENT_PASS`、`VOCAB_MARK_SPAN_PASS`、`VOCAB_MARK_LAYER_PASS`、`TERM_COLOR_CONSISTENCY_PASS`。

## 3. 課文圖片的教學功能與證據

課文圖片不是裝飾。每張圖至少完成一項：交代人物／地點／時間、呈現事件、動作或情緒、連結關鍵詞、呈現前後變化、支持推論。

Render Request 前建立 `image_evidence_map`：

```yaml
image_evidence_map:
  source_paragraph_or_unit:
  source_sentence_or_keyword:
  visual_facts_from_source: []
  reasonable_visual_supplements: []
  prohibited_inferences: []
  student_observation_prompt:
```

無法說明圖片對應哪段／哪句／哪個關鍵詞，就不得使用。

### 圖片功能

- 情境圖：交代時間、地點、人物與背景。
- 動作圖：呈現正在發生的動作與變化。
- 理解圖：把抽象語意轉成可觀察線索。

不得增加未授權劇情、人物關係或答案性畫面。

## 4. Object Composition

一般圖片式頁採 Object Composition First，不採「完整大底圖＋最後塞字」。

課文閱讀頁：正文先取得閱讀安全區，小插圖與角色作為獨立物件服務理解。近滿版場景只有 PAGE_PLAN 明確核准 `IMMERSIVE_FULL_SCENE` 時可使用。

角色、小插圖、道具可合理交疊；核准的 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 不算碰撞。遮到課文、注音、人物臉部、關鍵動作或教材證據才是 fail。

## 5. 每頁文字層級

最多三層：
1. 主訊息：唯一主要發現／焦點。
2. 證據文字：課文原句、關鍵詞、部件、句型例句等。
3. 操作提示：短小的找一找、想一想、圈選等。

文字容器由功能與畫面動線決定，不先套固定框。

## 6. 課文循環頁

可依需要使用：初讀 → 關鍵詞回看 → 段落功能 → 全文線索 → 主旨統整；不強迫固定輪數。

- 保留原文、自然段／語意單位與順序。
- 同一段維持連續閱讀區，不每句切卡片。
- 語詞標記直接回原文位置，以 glyph-anchored underline 為預設。
- 文字過多時拆連續課文頁，不改寫、刪節或縮字。
- 每次回看只新增必要標記，不一次畫滿全文。

## 7. 文意理解頁

情境畫面／角色引題 → 必要課文證據 → 一個主問題（最多一追問）→ 學生口頭思考或短答。問題要靠近證據，不做考卷式密集排列，不用顏色暗示答案。

## 8. 修辭發現頁

固定順序：

> 課文原句 → 關鍵詞突出 → 看見特色 → 猜想效果 → 修辭名稱 → 小練習

每頁一種主要修辭，不做名稱／定義／例句三欄表。

## 9. 句型發現頁

固定順序：

> 課文例句 → 句意理解 → 關鍵詞對應 → 句型骨架 → 新情境 → 分層仿說／仿寫

課文例句比公式重要；投影頁以口頭發想與圖像引導為主，書寫線另放學習單。

## 10. 成語教學頁

固定順序：

> 情境畫面 → 猜意思 → 成語出現 → 口語語意確認 → 課文連結 → 實際應用

一般一頁一成語；同一故事線／對照關係才可一頁兩個。成語不標注音。學生頁不放答案。

## 11. 形近字頁分流

沿用 `skills/character-group-visual-comparison/SKILL.md`；本檔只要求大字、注音、部件、詞語與情境形成可讀關係，不得用圖片模型生成正式國字。

## 12. 代表頁與批次

1. 每個實際啟用頁型先做代表頁。
2. 教師確認原文、焦點、證據、構圖、角色、文字與投影可讀性。
3. 通過後才 5–8 頁小批次生成。
4. 每批逐頁檢查文字、Object Composition、角色、答案可見性。
5. 有課文語詞標記時，代表頁至少實測一次**字型或欄寬改變造成 reflow 後，anchor 自動失效並重算**。

教師確認前不得定稿、覆蓋雲端原檔。

## 13. 頁面檢核

- 一頁一主訊息。
- 正式文字逐字正確。
- Font Safety 通過。
- Vocabulary anchor/reflow 通過（適用時）。
- 課文證據與問題靠近。
- 不是卡片牆、背景圖＋文字框或密集講義。
- 圖像服務動作、關係、情緒或變化。
- 角色有功能且符合角色庫。
- 學生頁無答案／講者備註。
- 尺寸、字級、換行、安全邊界與投影可讀性通過。

主要失敗碼：`TEXT_CYCLE_FOCUS_MISSING`、`COMPREHENSION_WITHOUT_EVIDENCE_PATH`、`RHETORIC_LABEL_FIRST`、`PATTERN_WITHOUT_SOURCE`、`IDIOM_LITERAL_IMAGE`、`SEMANTIC_IMAGE_MISMATCH`、`TYPED_TEXT_LAYOUT_FAIL`、`REPRESENTATIVE_PAGE_NOT_APPROVED`、`VOCAB_ANCHOR_FAIL`、`STALE_VOCAB_MARK_ANCHOR`、`TEXT_RENDERING_RISK`。

## 核心金句

> 字型是排版幾何的一部分；字型一換，所有精準對位都要重新算。

> 語詞標記必須綁在正確的字上，不是綁在「那一行附近」。