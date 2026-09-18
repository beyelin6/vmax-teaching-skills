# Lesson Presentation Execution Rules

版本：1.7

本檔是每課簡報製作期間，教師追加並確認的具體視覺、版面、角色、素材再利用與違規處理決策主檔。教材真值仍以官方 Source Master／LKB 為準。

## 載入與裁決

續作、修圖、生圖或重新渲染前：`Runtime State → Lesson Execution Rules → 最新 Slide/Page Layout Brief → Slide Script → 當頁 Source → Visual/Role assets`。

本檔的執行期必要欄位不得因下游舊版清單較短而省略。核准的場景交疊不得因相切自動判錯。

逐頁規劃的完整順序為：`Visual Grammar / Slide Architecture → 頁型與教學功能草案 → 風格候選與教師選擇 HOLD → 已確認 Style Selection Profile／Style Matrix、角色與畫布 → 頁數帳本確認 → 正式 PAGE_DETAIL_CONFIRMATION → 教師確認 HOLD → 代表頁逐類確認 HOLD → 小批次 Renderer／逐批確認 HOLD`。本檔下方的 Object Composition 與 PAGE_PLAN 是執行細節，不得省略上游的風格鎖、版型契約或正式逐頁母檔。未啟用的 Baseline 章節可依教材需求或教師確認省略，但已啟用章節不得重排。

## Object-based Scene Composition

一般國語圖片式簡報採 `OBJECT_SCENE`，不是完整大底圖＋後貼文字。正式文字／注音先取得閱讀安全區，再配置主場景、小插圖、角色、道具、標記、金句與前後景。

每頁 `OBJECT_COMPOSITION_PLAN` 至少記錄 composition mode、background role、text/visual/character/annotation objects、layer order、planned overlaps、protected zones、organic edge strategy。

完整 AI 場景吃滿畫布、文字只能反覆搬移、所有物件烘焙成不可拆底圖 → `MONOLITHIC_BACKGROUND_REGRESSION`。不得縮字、蓋白框或繼續搬字補救。

`IMMERSIVE_FULL_SCENE` 只限有教學理由的封面、情緒停格、故事高潮、環境沉浸或單一大情境觀察。

## Vocabulary Marking System

語詞定位與整句強調使用不同視覺語法：
- 語詞 → `UNDERLINE_HIGHLIGHT`
- 整句／金句 → `BACKGROUND_HIGHLIGHT`

## Paragraph Vocabulary Placement

課文閱讀頁的語詞預設與所屬自然段同頁，使用 `IN_PARAGRAPH` 或 `ADJACENT_ON_SAME_PAGE`。每個段落語詞項目須保留 `paragraph_ref`、`vocab_refs` 與 `language_placement`，並從 Slide Script 原樣傳入 Render Request。重跑、換模型、換 Renderer 或只修改圖片時沿用既有 placement；不得因版面習慣或重新規劃而自行拆出獨立語詞頁。

只有完整自然段在核准畫布與投影字級下無法容納、教師明確要求獨立語文活動，或語詞活動已成為新的主要教學焦點時，才可使用 `SEPARATE_LANGUAGE_PAGE`，且必須同時附具體 `reason`、`approval_ref` 與教師核准的頁面確認。缺少 placement 或拆頁證據 → `PARAGRAPH_LANGUAGE_PLACEMENT_MISSING` / `UNAPPROVED_LANGUAGE_SPLIT`。

### VOCAB_MARK_PLAN

每個指定語詞記錄：
- `term_text`
- `source_ref`
- `term_color_id`
- `mark_mode: UNDERLINE_HIGHLIGHT`
- `include_punctuation: no`
- `layer_order: MARK_BELOW_TEXT`
- `clearance_ratio: 0.08–0.12`
- `stroke_height_ratio: 0.10–0.16`
- `span_rule: TERM_ONLY`
- `occurrence_index`
- `line_id`
- `start_char_index`
- `end_char_index`
- `glyph_bbox`
- `baseline_y`
- `mark_bbox`
- `text_layout_revision`
- `paired_definition_ref`（適用時）

## TEXT_ANCHORED_VOCAB_MARK｜文字錨定語詞標記

**語詞標記不得用人工估算 x/y 座標定位。** 必須從「最終排版後的 Verified Text」取得指定語詞實際 glyph／字框，再由該字框生成標記。

固定施工順序：

`正式課文排版完成 → 鎖定 text_layout_revision → 依 term_text + occurrence_index 找到正確出現位置 → 取得 line_id / char indices / glyph_bbox / baseline_y → 計算 mark_bbox → 生成 UNDERLINE_HIGHLIGHT → QA`

規則：
1. `term_text` 必須與來源文字完全一致。
2. 同一頁同詞出現多次時，必須以 `occurrence_index` 指定正確一次；不得只搜尋第一個相符字串。
3. `start_char_index`／`end_char_index` 必須指向實際指定語詞，不得以「大概在第幾行」代替。
4. `glyph_bbox` 來自最終文字層，不得由插圖座標或舊版畫線位置反推。
5. `mark_bbox` 必須由 glyph bbox／baseline 計算，不得保存為與文字無關的永久絕對座標。
6. 字型、字級、字距、行距、欄寬、換行、文字位置或內容任何一項改變，即建立新的 `text_layout_revision`；舊 `glyph_bbox`、`baseline_y`、`mark_bbox` 全部失效，必須重新計算。
7. 文字重新排版後沿用舊底線座標 → `STALE_VOCAB_MARK_ANCHOR`，不得交付。
8. 文字本身正確時，標記錯位只修標記；不得搬文字去追舊標記。

### UNDERLINE_HIGHLIGHT

標記位於中文字主要字框下方，與字保留約字高 8–12% 淨距；厚度約字高 10–16%；可有手繪筆刷感但不可穿過主要筆畫。只涵蓋指定語詞，標點預設不納入。文字在上、標記在下；不得侵入注音安全區。同一語詞原文與詞義標示使用相同 `term_color_id`。

### BACKGROUND_HIGHLIGHT

只供已核准整句／金句使用，可在文字後方形成低對比淡色筆刷；不得替代一般語詞字下標記。

### Vocabulary Mark Failures

以下任一不得交付：
- `VOCAB_HIGHLIGHT_COLLISION`：穿字、遮注音、錯詞、多／少字、含非指定標點、顏色不一致、底線高到成背景色塊、位置明顯偏離。
- `VOCAB_ANCHOR_FAIL`：term 未綁定正確 occurrence／char indices／glyph bbox，或標記不是由最終文字字框生成。
- `STALE_VOCAB_MARK_ANCHOR`：文字 reflow 後仍沿用舊 anchor／mark bbox。

必須通過：
- `VOCAB_ANCHOR_PASS`
- `VOCAB_REFLOW_PASS`
- `VOCAB_MARK_ALIGNMENT_PASS`
- `VOCAB_MARK_SPAN_PASS`
- `VOCAB_MARK_LAYER_PASS`
- `TERM_COLOR_CONSISTENCY_PASS`

## CHARACTER_PLAN / KEY_LINE_PLAN

每頁均須記錄；不用也明確記錄 no。角色有教學／敘事功能，可用 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 合理融入場景，但不得遮核心閱讀／視覺證據。金句來源需區分教材、教師補充與 AI 過場。

## 生圖前門檻

Render Request 前檢查 Object Composition、Character、Key Line、適用時 Vocabulary Mark Plan、閱讀安全區、場景交疊、大底圖退化、Vocabulary anchor/reflow/highlight、教材文字、答案洩漏與密度。未通過 → `PRE_RENDER_RULE_BLOCKED`。

## PAGE_PLAN

每頁至少包含頁面目的、學生可見文字、教材證據、頁型、構圖、文字區、留白區、插圖需求、`OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`；有語詞標記另含 `VOCAB_MARK_PLAN`。

## 國語簡報施工前確認（GLOBAL_SKILL_RULE）

語文規劃、簡報施工或每次續作／下一步／確認前，必須載入 `core/governance/presentation-preconstruction-policy.md`。先讀最新 Drive Runtime，完成成語雙軌與每個正式生字的延伸成語覆蓋；缺漏為 `VOCABULARY_IDIOM_COVERAGE_INCOMPLETE`。風格、角色、畫布與頁數帳本鎖定後，建立逐頁施工稿並停等確認；核准後才選代表頁，逐類核准後才進每批最多 8 頁的小批次，每批完成必須停等教師確認。每個 stage／HOLD 都回寫並驗證 Runtime State 與 Runtime Index；不得以舊流程簡寫跳過這些關卡。
