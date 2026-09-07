# Lesson Presentation Execution Rules

版本：1.4

本檔是每課簡報製作期間，教師追加並確認的具體視覺、版面、角色、素材再利用與違規處理決策主檔。它不是教材知識來源，也不得改寫官方 Source Master 或 Lesson Knowledge Book。

## 載入優先順序

續作、修圖、生圖或重新渲染前，依序讀取：

`Runtime State → Lesson Execution Rules → 最新 Slide/Page Layout Brief → Slide Script → 當頁 Source → Visual/Role assets`

最新且已確認的本檔高於歷史 Slide Script、歷史 Render Request、舊代表頁與舊渲染結果；但不得高於官方 Source Master／LKB 的教材事實。若發生衝突，標記 `EXECUTION_RULE_CONFLICT`，保留衝突並停止，不得自行選邊。

## 下游相容與衝突裁決

本檔對逐頁施工與 Renderer 的要求屬於簡報執行期必要欄位。若下游舊版文字只列出較少欄位，該清單視為基礎欄位而非排他性完整清單；不得因此省略 `OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、`VOCAB_MARK_PLAN`、交疊或場景融入檢查。

圖像碰撞依語意判斷；核准的 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 屬 `APPROVED_SCENE_OVERLAP`，不得因相切而自動判錯。

逐頁規劃固定順序：
`Visual Grammar / Slide Architecture → 逐頁物件式場景組版＋角色配置＋金句策略＋語詞標記＋交疊規劃 → 頁型風格矩陣／Style Recipe → 教師確認 → 頁數估算 → 代表頁驗證 → Renderer`

## Object-based Scene Composition｜物件式場景組版

圖片式國語簡報預設不得以「先生成一張完整滿版大底圖，再找空位挪字」作為一般施工模式。除核准的沉浸式例外頁外，每頁先把教學內容拆成可配置物件，再共同構圖。

標準施工順序：
`教學焦點 → 正式文字／閱讀安全區占位 → 主場景物件 → 課文小插圖／情境物件 → 角色物件 → 道具／箭頭／語詞標記 → 金句／對話 → 前中後景與交疊關係 → 整體合成`

### OBJECT_COMPOSITION_PLAN

每頁至少包含：
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

背景只是底層；小插圖、角色、道具與文字是可配置物件。正式文字在視覺生成前先取得空間。插圖內容允許時優先自然輪廓、去背、局部淡出或遮罩。局部修改優先重排／替換單一物件，不重畫整張成功畫面。

### Monolithic Background Regression

一般教學頁若一張完整 AI 場景幾乎吃滿畫布、文字只能在縫隙中搬移，或角色／小插圖／道具全部烘焙在同一底圖，標記 `MONOLITHIC_BACKGROUND_REGRESSION`。不得靠縮字、白色遮罩或持續挪字補救；回到 `OBJECT_COMPOSITION_PLAN` 重排。

### IMMERSIVE_FULL_SCENE 例外

只限有教學理由的封面、情緒停格、故事高潮、環境沉浸或單一大情境觀察頁；正式文字仍須事前規劃安全區。

## Vocabulary Marking System｜語詞標記系統

語詞標記與整句／金句強調是兩種不同視覺語法，不得混用。

### VOCAB_MARK_PLAN

只要學生可見課文中有指定語詞標記，每個語詞都必須記錄：
- `term`
- `source_ref`
- `term_color_id`
- `mark_mode`: `UNDERLINE_HIGHLIGHT`
- `include_punctuation`: 預設 `no`
- `layer_order`: `MARK_BELOW_TEXT`
- `clearance_ratio`: 建議字高的 `0.08–0.12`
- `stroke_height_ratio`: 建議字高的 `0.10–0.16`
- `span_rule`: 只涵蓋指定語詞字元，不延伸到前後文字或標點
- `paired_definition_ref`: 若同頁／後續有詞義標示，記錄對應來源

### UNDERLINE_HIGHLIGHT｜語詞字下螢光筆

語詞預設使用字下螢光筆，而不是把色塊刷在字體中央：
- 標記位於中文字主要字框下方，與字保留約字高 8–12% 的淨距。
- 筆刷厚度約字高 10–16%，呈手繪螢光筆／襯線感，可略不規則，但不可穿過中文字主要筆畫。
- 長度只覆蓋語詞本身；逗號、句號、頓號等標點預設不納入。
- 標記層固定在正式文字層下方；文字永遠保持最高辨識優先。
- 同一語詞在原文定位與詞語解釋中使用同一 `term_color_id`。
- 文字位置確認後，不得為了遷就標記而搬動正式文字；優先修正標記物件。
- 注音存在時，標記不得侵入注音安全區。

### BACKGROUND_HIGHLIGHT｜整句／金句背景筆刷

`BACKGROUND_HIGHLIGHT` 只用於整句重點、金句、段落核心句等較高層級強調，不作為一般語詞定位的預設模式。它可位於文字後方形成淡色筆刷底，但必須低對比、不遮筆畫，且需由 `KEY_LINE_PLAN` 或正式句子強調策略核准。

因此預設語法為：
- **語詞定位 → `UNDERLINE_HIGHLIGHT`**
- **整句／金句 → `BACKGROUND_HIGHLIGHT`**

若教師明確指定其他教材視覺語法，需在當課 Execution Rules 記錄例外；不得由 Renderer 自行變更。

### VOCAB_HIGHLIGHT_COLLISION

以下任一情況標記 `VOCAB_HIGHLIGHT_COLLISION`，不得交付：
- 筆刷／底線穿過中文字主要筆畫，造成像「刷在字上」而非「襯在字下」。
- 遮到注音或其他正式文字。
- 標錯詞、少字、多字，或標記範圍包含非指定文字。
- 無理由把逗號、句號等標點一起畫入。
- 同一語詞原文與詞義標示 `term_color_id` 不一致。
- 標記高到變成字後大色塊，與整句背景強調混淆。
- 標記長度、位置明顯偏離語詞，造成學生誤判語詞範圍。

修正 `VOCAB_HIGHLIGHT_COLLISION` 時，只調整標記物件；若正式文字本身位置正確，不得藉機移動課文文字。

## 固定角色與語意輔助人物

`CANONICAL_CHARACTER` 必須使用角色庫並保持 DNA 一致；`SEMANTIC_SUPPORTING_FIGURE` 可即頁生成但不得污染角色庫。

每個 `page_family` 指定 `character_policy`：`CANONICAL_REQUIRED`、`CANONICAL_OPTIONAL`、`SUPPORTING_FIGURE_ALLOWED`、`CHARACTER_DISCOURAGED` 或 `NO_CHARACTER`。

## CHARACTER_PLAN

每頁必須有 `CHARACTER_PLAN`，不用也記錄 `appear: no`。至少包含 `appear`、`character`、`character_type`、`role`、`position`、`scale`、`facing`、`action`、`speech_mode`、`overlap_mode`、`overlap_targets`、`avoid_zone`。角色必須有教學／敘事功能。

場景參與可使用 `SCENE_INTEGRATED` 或 `FOREGROUND_OVERLAP`；交疊不得遮臉、關鍵動作、核心物件與閱讀安全區。

## KEY_LINE_PLAN

每頁必須有 `KEY_LINE_PLAN`，不用也記錄 `use: no`。至少包含 `use`、`source`、`text`、`function`、`placement`、`hierarchy`、`relation_to_character`。`TEXTBOOK` 保留來源；`TEACHER` 為教師補充；`AI_TRANSITION` 只作引導，不得偽裝教材。

## 圖文與物件避讓

角色、金句、課文、詞語解釋、小插圖、道具與標記都是獨立配置物件。先保留閱讀安全區與教學重點，再配置視覺物件。

若 `OBJECT_COMPOSITION_PLAN`、角色位置、金句位置、主要文字區或必要 overlap 尚未決定，標記 `PAGE_LAYOUT_INCOMPLETE`。

## 既有定稿教材再利用

已有 `APPROVED`、`LOCKED` 或 `FINAL` artifact 時優先 reuse 並保留來源；不得自行改寫內容。

## 生圖前門檻

Render Request 前至少檢查：Execution Rules、來源核准、`OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、適用時的 `VOCAB_MARK_PLAN`、閱讀安全區、場景交疊、`MONOLITHIC_BACKGROUND_REGRESSION`、`VOCAB_HIGHLIGHT_COLLISION`、圖文對應、答案洩漏、密度、文字模式與歷史污染。未通過 → `PRE_RENDER_RULE_BLOCKED`。

## 逐頁施工稿層級

先 `PAGE_PLAN`，再 `REPRESENTATIVE_CONSTRUCTION`，最後 `SLIDE_SCRIPT`。PAGE_PLAN 不要求像素級座標。

PAGE_PLAN 每頁至少包含頁面目的、學生可見文字、教材證據、頁型、構圖、文字區、留白區、插圖需求、`OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`；有語詞標記的頁另必須包含 `VOCAB_MARK_PLAN`。