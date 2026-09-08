# 國語圖片式語文頁規則

版本：1.4

本參考文件供 `presentation-engine` 與 `vmax-image-renderer` 製作國語圖片式簡報時使用。形近字與多音字的專門規則仍以 `skills/character-group-visual-comparison/SKILL.md` 為準。

## 1. 共通教學邏輯

所有頁型優先採：

> 課文證據 → 視覺理解 → 教學發現 → 學生應用

每頁只保留一個主要教學焦點，最多一個必要追問。學生頁不得直接呈現答案、完整結論、正確選項或講者備註。

## 2. 圖片與文字分工

圖片模型負責人物、場景、動作、表情、物件、留白、視線與情境關係；不得承載課文、注音、形近字、成語、句型、修辭名稱、題目、部件拆解等關鍵文字。

受控文字層負責學生可見正式文字。文字須逐字可追溯來源，並與 Object Composition 共同構圖；禁止背景完成後再硬貼大量文字、卡片牆、大量白色矩形或文字框遮圖。

## 2.1 字型與 Font Safety

本檔不硬綁單一字型 family。正式字型選擇唯一依據：`skills/traditional-chinese-font-safety/SKILL.md`、`font-registry.yaml` 與當次實際 font preflight。

必須記錄／驗證 `font_role`、selected font、TW region（適用時）、glyph coverage、Bopomofo coverage（需要時）、fallback 與 font QA。課文正文依 body role、生字／形近字依 character_learning、注音依 bopomofo_safe、活動標題依核准 title role。

### Font Change = Text Reflow

字型 family／file、字級、字距、行距、欄寬、換行、文字位置或內容改變，都視為 text reflow。必須更新 `text_layout_revision`、重新量測 glyph bbox／baseline、使舊文字 anchor 失效並重新計算 annotation。

## 2.2 Verified Raster Text Components

圖片式簡報正式文字由可控文字工具產生，逐元件校對，再與視覺物件合成。`TEXT_READING_PAGE` 可使用真正可控的連續文字層；其他圖片式頁使用 Verified Raster Text Components。

## 2.3 Vocabulary Marking System

語詞定位 → `UNDERLINE_HIGHLIGHT`；整句／金句 → 核准 `BACKGROUND_HIGHLIGHT`。

固定 anchor 流程：`最終文字排版 → text_layout_revision → term_text + occurrence_index → line/char indices → glyph_bbox + baseline_y → mark_bbox → underline`。

同詞多次出現必須指定 occurrence。無法唯一定位 → `VOCAB_ANCHOR_FAIL`；reflow 後沿用舊標記 → `STALE_VOCAB_MARK_ANCHOR`。

字下標記位於主要字框下方，淨距約字高 8–12%，筆刷厚度約 10–16%，只涵蓋語詞本身，標點預設排除，文字在上、標記在下，不遮注音，同一 `term_color_id` 原文／詞義一致。

有語詞標記頁必須通過：`VOCAB_ANCHOR_PASS`、`VOCAB_REFLOW_PASS`、`VOCAB_MARK_ALIGNMENT_PASS`、`VOCAB_MARK_SPAN_PASS`、`VOCAB_MARK_LAYER_PASS`、`TERM_COLOR_CONSISTENCY_PASS`。

## 3. 課文圖片的教學功能與證據

課文圖片不是裝飾。每張圖至少完成一項：交代人物／地點／時間、呈現事件、動作或情緒、連結關鍵詞、呈現前後變化、支持推論。無法說明圖片對應哪段／哪句／哪個關鍵詞，就不得使用。不得增加未授權劇情、人物關係或答案性畫面。

## 4. Object Composition

一般圖片式頁採 Object Composition First，不採「完整大底圖＋最後塞字」。正文／正式文字先取得閱讀安全區，小插圖、角色、道具、標記作為獨立物件服務理解。核准的 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 不算碰撞；遮到課文、注音、人物臉部、關鍵動作或教材證據才是 fail。

## 5. 每頁文字層級

最多三層：主訊息、證據文字、操作提示。文字容器由功能與畫面動線決定，不先套固定框。

## 6. 課文循環頁

可依需要使用初讀 → 關鍵詞回看 → 段落功能 → 全文線索 → 主旨統整；不強迫固定輪數。保留原文與順序，同一段維持連續閱讀區，語詞標記直接回原文位置，文字過多時拆頁而不改寫、刪節或縮字。

## 7. 文意理解頁

情境畫面／角色引題 → 必要課文證據 → 一個主問題（最多一追問）→ 學生口頭思考或短答。問題靠近證據，不做考卷式密集排列。

## 8. 修辭發現頁

固定順序：課文原句 → 關鍵詞突出 → 看見特色 → 猜想效果 → 修辭名稱 → 小練習。每頁一種主要修辭，不做名稱／定義／例句三欄表。

## 9. 句型發現頁

固定順序：課文例句 → 句意理解 → 關鍵詞對應 → 句型骨架 → 新情境 → 分層仿說／仿寫。課文例句比公式重要。

## 10. 成語教學頁

### 10.1 教學順序

固定邏輯：

> 情境畫面 → 猜意思 → 成語出現 → 口語語意確認 → 課文連結 → 實際應用

一般一頁一個成語；只有同一故事線、前後發展、明確對照或同一場景中的兩個語意角色時，才可一頁兩個。沒有可見關係的兩個成語不得為了省頁數硬塞同頁。成語不標注音；學生頁不放答案。

### 10.2 成語頁 Layout Contract

成語頁不得固定切成「成語／解釋／例句」三個同等卡片或三欄表。三者必須有清楚層級：

1. **成語**：本頁最大、最醒目的文字物件。
2. **解釋**：一句四年級學生能懂的短解釋，視覺層級次於成語，不與例句擠成同一文字團塊。
3. **例句**：必須是可理解的實際使用情境，字級需達投影可讀，不得縮成角落小字；例句與情境圖共同形成本頁主要應用區。

預設閱讀動線：`大成語 → 短解釋 → 大字例句＋情境圖`。可依 Object Composition 改成環繞、上下、斜向或場景整合式動線，但不得退化為固定左文字右插圖或三格講義。

### 10.3 例句與插圖必須語意配對

成語插圖優先支援**例句中的實際用法／引申義**，而不是只畫成語字面拆解。

每個成語頁必須建立：

```yaml
idiom_application_plan:
  idiom:
  student_friendly_meaning:
  example_sentence:
  example_scene_subject:
  example_scene_action:
  semantic_relation:
  literal_image_risk:
```

`example_scene_subject`、`example_scene_action` 必須能直接回到例句中的人物、行動或情境。學生看圖後應能理解「這句話為什麼可以用這個成語」。

例如例句是「媽媽耳提面命地提醒我出門前要檢查用品」，主要情境就應呈現媽媽反覆叮嚀孩子、孩子聽取提醒的互動，而不是只畫耳朵、嘴巴或抽象說話符號。

若圖只符合字面、不符合成語實際語意 → `IDIOM_LITERAL_IMAGE`。若圖與例句人物／行動／語意不一致 → `IDIOM_EXAMPLE_VISUAL_MISMATCH`。

### 10.4 Object Composition for Idioms

成語、短解釋、例句都是 `text_objects`；情境圖原則上是 `primary_visual_object`；必要的表情、動作細節、生活物件可作 supporting visual objects；角色若參與例句，應成為情境中的互動者，而不是角落裝飾。

若使用既有角色，角色可採 `SCENE_INTEGRATED` 或 `FOREGROUND_OVERLAP` 融入例句情境。不得因角色存在而壓縮例句字級或遮擋關鍵動作。

一頁兩成語時，不得預設左右兩張等尺寸卡片。必須以同一故事線、前後事件、對照情境或共享場景串聯；若無法形成共同視覺語意，拆成兩頁。

### 10.5 成語頁驗收

成語頁必須通過：
- `IDIOM_TEXT_PASS`：成語、解釋、例句逐字正確且語句通順。
- `IDIOM_HIERARCHY_PASS`：成語／解釋／例句層級清楚，不擠成同一文字團。
- `IDIOM_EXAMPLE_READABILITY_PASS`：例句投影可讀，不縮成附註。
- `IDIOM_EXAMPLE_VISUAL_MATCH_PASS`：情境圖支持例句中的成語用法／引申義。
- `IDIOM_OBJECT_COMPOSITION_PASS`：圖文共同構圖，不是三格講義或固定左文右圖。

任一失敗不得以「把圖縮小、把例句縮字、再塞一個框」作為預設修復。優先重新平衡 Object Composition；必要時拆頁。

## 11. 形近字頁分流

沿用 `skills/character-group-visual-comparison/SKILL.md`；大字、注音、部件、詞語與情境必須形成可讀關係，不得用圖片模型生成正式國字。

## 12. 代表頁與批次

每個實際啟用頁型先做代表頁。教師確認原文、焦點、證據、構圖、角色、文字與投影可讀性後才小批次生成。有課文語詞標記時，代表頁至少實測一次 reflow 後 anchor 重算；有成語頁時，代表頁至少驗證一次「例句 ↔ 情境圖 ↔ 成語引申義」三者一致。

教師確認前不得定稿、覆蓋雲端原檔。

## 13. 頁面檢核

- 一頁一主訊息。
- 正式文字逐字正確。
- Font Safety 通過。
- Vocabulary anchor/reflow 通過（適用時）。
- 成語頁的例句與插圖語意一致（適用時）。
- 課文證據與問題靠近。
- 不是卡片牆、背景圖＋文字框或密集講義。
- 圖像服務動作、關係、情緒或變化。
- 角色有功能且符合角色庫。
- 學生頁無答案／講者備註。
- 尺寸、字級、換行、安全邊界與投影可讀性通過。

主要失敗碼：`TEXT_CYCLE_FOCUS_MISSING`、`COMPREHENSION_WITHOUT_EVIDENCE_PATH`、`RHETORIC_LABEL_FIRST`、`PATTERN_WITHOUT_SOURCE`、`IDIOM_LITERAL_IMAGE`、`IDIOM_EXAMPLE_VISUAL_MISMATCH`、`SEMANTIC_IMAGE_MISMATCH`、`TYPED_TEXT_LAYOUT_FAIL`、`REPRESENTATIVE_PAGE_NOT_APPROVED`、`VOCAB_ANCHOR_FAIL`、`STALE_VOCAB_MARK_ANCHOR`、`TEXT_RENDERING_RISK`。

## 核心金句

> 成語頁不是把成語、解釋、例句排進三個框；要讓學生從情境看懂這個成語怎麼用。

> 圖要配合例句，例句要呈現成語真正的用法。