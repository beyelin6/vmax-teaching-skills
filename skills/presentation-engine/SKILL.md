---
name: presentation-engine
description: 將已核准的 Lesson Knowledge Book、Learning Module Profile、Teaching Strategy Profile 與 Output Profile 轉換為 Slide Script、Render Request、講者備註、平台匯入來源與其他選定輸出；圖片式簡報採 Object Composition First，實際圖片必須路由至 vmax-image-renderer。
---

# Presentation Engine

版本：0.10.4

Presentation work 使用當課 `00_施工中_接續區` 保存分析、教師確認、逐頁 brief、代表頁與修訂紀錄。`SLIDE_SCRIPT` 是逐頁簡報唯一內容主檔；NotebookLM、Google Slides、Canva、PPTX、PNG/PDF 都是下游派生物，不得回寫 Source Master。

## 使命

本技能只負責把已核准教材、學習模組、教學策略映射成頁面與輸出；不得重新判斷教材真值、擅自新增成語／修辭／句型／題目或改寫課文。

## 前置條件

執行前確認：
1. `lkb/lesson-knowledge-book.md`
2. `learning/learning-module-profile.md`
3. `teaching/teaching-strategy-profile.md`
4. `config/output-profile.md`
5. `AGENTS.md`
6. 已核准 Style / Role / Layout
7. `core/presentation/classroom-image-slide-policy.md`
8. `core/presentation/canvas-lock-policy.md`
9. `core/presentation/text-layer-construction-policy.md`
10. `core/visual/visual-reference-library.md`
11. `core/visual/visual-text-dna.md`
12. 最新 `core/governance/lesson-presentation-execution-rules.md`
13. lesson artifact registry（若有）
14. `core/renderer/image-first-hybrid-renderer.md`

任何上游必要內容未核准 → output blocked。

## 可選輸出

依 Output Profile 產生：lesson knowledge / curated briefing / NotebookLM source & instruction / teacher & student markdown / slide source / slide script / speaker notes / worksheet source / assessment source / output manifest / render request。

不產生未選取格式。預設教師簡報交付為高畫質圖片化投影片與 PDF；PPTX 只有教師明確要求時才派生，人工修改不得回寫 Slide Script。

## 唯一來源與學生分流

- 官方教材：只來自核准 LKB。
- 延伸內容：只來自核准 Learning Module Profile。
- 教學流程：只來自核准 Teaching Strategy Profile。
- 視覺／版型／角色：只來自已確認 Style、Layout、Role 與 Lesson Execution Rules。

學生可見頁不得含答案、來源 metadata、內部 ID、教師解題步驟與系統驗證訊息。答案與詳細說明放教師層／speaker notes。

## 動態頁數

頁數依內容、課堂時間與投影閱讀密度動態決定；不使用固定全課頁數。頁數先為 `PROPOSED_PAGE_COUNT`，教師確認後才升級為 lesson-local 固定頁數。

---

## 逐頁施工稿三層契約

`working/slide-page-layout-brief.md` 必須先完成，再進 Representative Construction 與正式 Slide Script。

### 1. PAGE_PLAN

每頁至少包含：
- `page_purpose`
- `student_visible_text`
- `source_refs`
- `page_family`
- `style_variant`
- `character_policy`
- `OBJECT_COMPOSITION_PLAN`
- `CHARACTER_PLAN`
- `KEY_LINE_PLAN`
- `canvas_lock`
- `visual_density_profile`
- 是否需拆頁

PAGE_PLAN 不要求像素級座標，但必須先決定閱讀安全區、主要物件關係與是否為沉浸式例外。

### OBJECT_COMPOSITION_PLAN

每頁必填：
- `composition_mode`: `OBJECT_SCENE` / `IMMERSIVE_FULL_SCENE`
- `background_role`
- `text_objects`
- `primary_visual_object`
- `supporting_visual_objects`
- `character_objects`
- `annotation_objects`
- `layer_order`
- `planned_overlaps`
- `protected_zones`
- `organic_edge_strategy`

一般圖片式國語頁預設 `OBJECT_SCENE`。

**禁止把 PAGE_PLAN 簡化成「文字區＋一張底圖」。** 背景只承擔環境／氣氛；課文小插圖、角色、道具、標記均應以可配置物件規劃。

### 2. REPRESENTATIVE_CONSTRUCTION

每個啟用頁型至少做一張代表頁，補充：
- 實際物件位置與尺度
- 文字層級與標色
- 角色出現與交疊方式
- `protected_zones`
- 自然輪廓／去背／遮罩策略
- 閱讀節奏與視線動線
- `MONOLITHIC_BACKGROUND_REGRESSION` 檢查

### 3. SLIDE_SCRIPT

鎖定正式文字、來源、素材、Render Request、版本與教師確認狀態。每頁至少記錄：
- slide_id / section / lesson_stage
- title / student_visible_content / teacher_notes
- source_nodes / learning_modules / strategy_step
- page_class
- page_family / style_variant
- illustration_requirement
- answer_visibility
- `object_composition_plan`
- `character_plan`
- `key_line_plan`
- `canvas_lock`
- `text_rendering`
- `visual_text_dna`
- `term_color_map`（適用時）
- benchmark refs/alignment（若有）

舊欄位 `image_layout_plan` 若仍存在，只能視為兼容摘要，不得取代 `OBJECT_COMPOSITION_PLAN`。

---

## Object Composition First

圖片式簡報施工主線固定為：

```text
教學焦點
→ 正式文字／注音／閱讀安全區占位
→ 主場景物件
→ 小插圖／情境物件
→ 角色物件
→ 道具／箭頭／螢光筆／標記
→ 金句／對話
→ 前中後景與 planned overlaps
→ Renderer 合成
```

Presentation Engine 不得輸出以下舊式 Render Request：

`完整無字／少字大底圖 → 最後再找位置放文字`

若逐頁 brief 顯示文字只能靠反覆移動才能塞進一張完整插畫，標記 `MONOLITHIC_BACKGROUND_REGRESSION`，回到 PAGE_PLAN 重構，不得送 Renderer。

### 合法交疊

`CHARACTER_PLAN.overlap_mode = SCENE_INTEGRATED | FOREGROUND_OVERLAP` 或 `planned_overlaps` 已核准時，交疊屬場景關係，不得要求自動分離。只保護課文、注音、核心教材證據、人物臉部／關鍵動作等 `protected_zones`。

### IMMERSIVE_FULL_SCENE

只用於已說明教學理由的封面、情緒停格、故事高潮、環境沉浸或單一大情境觀察頁。一般課文、語詞、生字、形近字、多音字、句型、修辭頁不得因方便而使用。

---

## 頁型風格矩陣

進代表頁前必須建立 `working/page-family-style-matrix.md` 並由教師確認。

同一 page family 沿用同一 style variant；不同頁型可合理混搭，但共享 canvas、角色 DNA、正式文字、字體系統與安全邊界。

`character_policy` 使用：
- `CANONICAL_REQUIRED`
- `CANONICAL_OPTIONAL`
- `SUPPORTING_FIGURE_ALLOWED`
- `CHARACTER_DISCOURAGED`
- `NO_CHARACTER`

角色不是裝飾；固定角色來自 Role／Character Library，語意輔助人物不得污染角色庫。

---

## 教師口述型簡報

- 不是講義、學習單、考卷或滿版資訊表。
- 一頁一個主要教學焦點。
- 內容過量：刪減／拆頁／Reveal／教師口述，不縮字硬塞。
- 插圖可局部、半頁、雙物件或合理近滿版，但不可每頁近滿版。
- 小插圖不預設方框；內容允許時優先自然輪廓、去背或局部淡出。
- 課文閱讀頁以正文為主要物件，小插圖服務理解，不把原文拆成卡片牆。

若已有 Approved Visual Benchmark，需記錄並持續檢查留白、文字密度、局部插畫、角色干擾度與講義感。

---

## Verified Teaching Text

課文、注音、生字、形近字、多音字、成語本體與正式定義、題目與正式例句先鎖為 Verified Teaching Text，再進 Renderer。

- `TEXT_READING_PAGE`：可控連續文字層。
- 其他圖片式頁：`VERIFIED_RASTER_TEXT_COMPONENTS`。

文字是構圖物件，需在 PAGE_PLAN 先占位；不得最後才找背景空白。

---

## 國語頁型

- 課文＋詞語：完整保留當前自然段／意義段／詩節；語詞回原文定位。
- 語文特色：一頁一個句型／修辭／寫法，先感受再命名。
- 文意：一個主問題，最多一個追問；答案留教師層。
- 形近字：一頁一組優先，最多兩組；大字、注音與語意物件都需閱讀安全區。
- 多音字：一頁一字優先；不同讀音與語意情境清楚比較。
- 成語：情境插圖呈現實際語意，不只畫字面。
- 仿作／遷移：口頭發想與圖像引導，不留書寫線。
- 評量：學生頁不放答案。

已核准 artifact 必須優先 reuse，保留 `source_artifact_ref`，不得重新寫內容。

---

## Representative Validation

至少涵蓋本課實際啟用的：
- `TEXT_READING_PAGE`
- 一般 `OBJECT_SCENE`
- 高風險語文頁
- Lesson Visual Map（若啟用）
- 其他獨立 page family

教師核准只涵蓋實際看見的頁型。代表頁未全數通過，不得全量 Renderer。

---

## Render Request Contract

Render Request 必須帶入：
- source refs + verified text
- canvas lock
- object composition plan
- character plan
- key line plan
- protected zones
- planned overlaps
- role anchor refs（適用時）
- visual benchmark refs/alignment（適用時）
- acceptance checks，包括 `MONOLITHIC_BACKGROUND_PASS`

實際圖片生成／修改交給 `vmax-image-renderer`；Presentation Engine 不得只產 prompt 就宣稱完成。

---

## 工作流程

1. 驗證上游與來源核准狀態。
2. 讀 Output Profile。
3. 建立內容選取表。
4. 完成全課 PAGE_PLAN：Object Composition + Character + Key Line。
5. 建立 page-family style matrix。
6. 教師確認逐頁規劃與風格混搭規則。
7. 確認頁數帳本。
8. 建立每個頁型的 Representative Construction。
9. 教師逐頁型核准。
10. 建立正式 Slide Script。
11. 產生 Render Requests。
12. 路由 Image Renderer 小批次渲染。
13. 每批檢查文字、Object Composition、Visual Drift、角色一致性與大底圖退化。
14. Quality Gate 通過後才交付／歸檔。

## Fail Conditions

- `PAGE_LAYOUT_INCOMPLETE`
- `MISSING_OBJECT_COMPOSITION_PLAN`
- `MONOLITHIC_BACKGROUND_REGRESSION`
- `TYPED_TEXT_LAYOUT_FAIL`
- `CANVAS_SPEC_BLOCKED`
- `VISUAL_BENCHMARK_DRIFT`
- `CHARACTER_STYLE_GATE_FAILED`
- `SEMANTIC_IMAGE_MISMATCH`
- 未核准來源／答案洩漏／教材文字錯誤

## 核心金句

> 簡報腳本不是先決定一張底圖長什麼樣，而是先決定孩子要讀什麼、看什麼，以及這些物件如何一起說明概念。