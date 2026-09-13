---
name: presentation-engine
description: 將核准教材與教學策略轉換為 Slide Script 與 Render Request；採 Object Composition First，語詞標記以最終 Verified Text glyph anchor 精準對位，成語頁以例句應用情境驅動構圖。
---

# Presentation Engine

版本：0.10.11

`SLIDE_SCRIPT` 是逐頁簡報唯一內容主檔。教材、教學策略、角色與視覺只使用已核准來源。

## SLIDE_ARCHITECTURE_LOCK

Slide Script 頂層必須保存 `SLIDE_ARCHITECTURE_LOCK` 與 `architecture_mapping`。Baseline 順序固定為：開頭導入 → 課文總說 → 圖像式心智圖 → 各段（課文／語詞解釋／修辭或句型／文意理解）→ 形近字 → 成語 → 教材語文活動 → 總結與學習遷移。頁數上限、模板或 Renderer 不得自行重排；外加變體只能透過明確 mapping 改變教學呈現。

驗證必須拒絕：缺少任一必修區段、段內順序錯誤、`architecture_mapping` 未回指學習結果，或將外加模板內容冒充 Baseline。

## PAGE_PLAN

每頁至少包含 page purpose、student visible text、source refs、page family/style、character policy、`OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、canvas lock、density；有語詞標記時另含 `VOCAB_MARK_PLAN`；`page_family = IDIOM` 時另含 `IDIOM_APPLICATION_PLAN`。

正式 Slide Script 只能由已核准的 `PAGE_DETAIL_CONFIRMATION` 產生。每頁必須逐項帶入核准的學生可見文字、來源、圖片目的與細節、人物／物件／動作、禁止誤畫、閱讀順序、文字區、圖片區、留白與 protected zones。若有角色，還必須逐頁帶入相同的 `base_character_id`、`core_dna_ref`、`approved_asset_id` 與 `asset_version`；姿勢、表情、鏡位與道具只能使用母檔列出的允許變化。若頁面資料與母檔不一致，或角色識別資料缺失，標記 `PAGE_DETAIL_SOURCE_CONFLICT` 或 `CHARACTER_ANCHOR_MISSING`，不得送 Renderer。

批次 Slide Script 必須建立 `BATCH_CONSTRUCTION_LOCK`，帶入整份 PAGE_DETAIL_CONFIRMATION hash、Style Selection Profile hash、選定 `style_core_id` 與每頁 `page_spec_sha256`；每頁和 Render Request 都要回指相同 hash。缺少或不一致時標記 `BATCH_CONSTRUCTION_LOCK_FAIL`，不得以模板、上一頁或平台預設補齊。

一般頁預設 `OBJECT_SCENE`，禁止簡化成文字區＋一張底圖。完整場景吃滿畫布、文字只能搬移 → `MONOLITHIC_BACKGROUND_REGRESSION`。

課文閱讀頁另受 `core/presentation/paragraph-text-page-policy.md` 約束：預設一頁一個自然段＋緊跟在旁的該段語詞解釋；語詞解釋不得脫離課文另成清單頁。單段過長才可依完整句子拆成連續頁。PAGE_DETAIL_CONFIRMATION 必須帶 `text_coverage`，確認完整原文、段落來源、拆頁理由、相鄰語詞版位與該段全部核准語詞覆蓋；不能用代表句、摘要或改寫代替。

### 課文頁文字層與段落語詞施工契約

- 課文頁插圖的最高原則是「幫助理解課文」；每個角色、場景、道具或裝飾都必須回指當頁段落、句子或關鍵詞，不能只因畫面漂亮而加入。
- 課文插圖可使用單一靜態主畫面，也可使用分格漫畫、日式漫畫風、連續鏡格或前後對照；採分格時，PAGE_DETAIL_CONFIRMATION 必須列出每格對應內容、閱讀順序與理解功能。
- 課文原文必須逐字完整呈現，保留標點、語氣詞、引號與段落順序；不得自行增加「第一段」等解釋性標題、摘要或教師講解。必要的 `①`、`②` 只作段落導覽記號。
- 課文、插圖、語詞標記與投影片序號必須是分開的可調整物件；課文不得烘焙在圖片，`image_spec.text_in_image` 必須為 `false`。
- 原文中的指定語詞在實際 occurrence 直接用淡色 `PALE_BRUSH_BEHIND_TEXT` 標示，筆刷位於文字後方、略微超出詞語、不遮字；不得以單純底線取代筆刷。解釋區只呈現簡潔的「詞語：解釋」，並與所屬段落相鄰。
- 投影片頁碼使用實際簡報順序（例如 `P04`）並置於角落，通常右下角；教材來源頁碼只留在施工資料或備註。段落記號可有設計感，但必須回指 `sequence_index` 與 `section_id`。

## IDIOM_APPLICATION_PLAN

成語頁必須記錄：`idiom`、`student_friendly_meaning`、`example_sentence`、`example_scene_subject`、`example_scene_action`、`semantic_relation`、`literal_image_risk`、`source_refs`。

固定推導順序：

`核准成語語意 → 四年級可懂短解釋 → 自然且正確的生活例句 → 例句人物／動作／情境 → primary visual → supporting objects / character interaction`。

禁止反向流程：不得先想漂亮圖片，再扭曲例句配圖。圖跟著正確例句走，不是例句跟著圖走。

例句必須同時通過：語法通順、成語使用正確、符合四年級可理解的生活語境 → `IDIOM_EXAMPLE_NATURALNESS_PASS`。不自然、為了畫面硬湊、語意牽強不得進 Render Request。

成語頁預設層級：`大成語 → 短解釋 → 大字例句＋情境圖`。不得固定做成三個同等卡片或三欄表。一頁兩成語只有在同一故事線、前後事件、對照或共享場景有可見關係時成立，否則拆頁。

## VOCAB_MARK_PLAN

每個指定語詞記錄 `term_text`、來源、顏色、occurrence、char indices、glyph bbox、baseline、mark bbox、text layout revision 等 anchor metadata。PAGE_PLAN 不得猜最終底線 x/y；必須等 Verified Text 最終排版後建立。

任何字型、字級、字距、行距、欄寬、換行、文字位置或內容變更，都使舊 anchor 失效。找不到唯一 occurrence → `VOCAB_ANCHOR_FAIL`；reflow 後沿用舊 anchor → `STALE_VOCAB_MARK_ANCHOR`。

## Vocabulary Visual Grammar

語詞定位 → `UNDERLINE_HIGHLIGHT`（相容 mark mode，課文頁 visual style 必須為 `PALE_BRUSH_BEHIND_TEXT`）；整句／金句 → `BACKGROUND_HIGHLIGHT`。淡色筆刷位於主要字框後方，與字高接近、左右只略微超出、不遮字，不得以單純底線取代筆刷；只涵蓋指定語詞，標點預設排除，文字層在上，不侵入注音。

## CHARACTER / KEY LINE / OBJECT COMPOSITION

角色有教學或敘事功能，可依核准 overlap 融入場景。金句來源須區分教材、教師補充、AI 過場。正式文字／注音在視覺生成前先取得安全區，小插圖與角色盡量維持獨立物件。成語頁角色若參與例句，應成為例句情境互動者，不作角落裝飾。

## Representative Construction

代表頁需實際驗證物件位置、閱讀動線、角色交疊與 protected zones。有課文語詞標記時至少實測一次正確 anchor 與 reflow 重算；有成語頁時至少實測一次：成語語意、例句自然度、例句情境圖三者一致。

## SLIDE_SCRIPT / Render Request

Slide Script 鎖定正式文字、來源、object/character/key-line plans；有語詞標記時記錄 vocab anchors；成語頁必須傳遞完整 `idiom_application_plan`，不得只傳成語名稱或抽象 visual prompt。

若存在 `LANGUAGE_CANDIDATE_COVERAGE.character_related_idioms`，每個保留項目必須有 `final_idiom_section_refs`，且至少回指一個最終成語頁；重複成語可共用頁面，但不得失去生字 `character_refs` provenance。缺少對應時標記 `IDIOM_CHARACTER_COVERAGE_INCOMPLETE`。

Render Request 有語詞標記時必須帶入六項 Vocabulary checks；成語頁必須帶入：`IDIOM_TEXT_PASS`、`IDIOM_HIERARCHY_PASS`、`IDIOM_EXAMPLE_READABILITY_PASS`、`IDIOM_EXAMPLE_NATURALNESS_PASS`、`IDIOM_EXAMPLE_VISUAL_MATCH_PASS`、`IDIOM_OBJECT_COMPOSITION_PASS`。

正式送 Renderer 前使用目前 Renderer 技能內 launcher 的絕對路徑執行 Slide Script 驗證（`--require-ready`）；參照 Render Request Schema 的完整命令與安裝路徑解析。先以 PRE_LAYOUT 完成文字排版，再量測 anchor，取得自然度審閱證據並轉 RENDER_READY。Slide 與 Render Request 的 page_family、成語／語詞／物件／角色／金句 plans、revision、canvas 必須一致。非零退出碼不得送出。

## Verified Teaching Text

課文、注音、生字、形近字、多音字、成語、題目與正式例句不得由圖片模型自由生成。文字是構圖物件，先排版再產生依附於它的標記與視覺關係。

## 代表頁與批次

代表頁覆蓋實際 page families。教師核准後才進小批次 Renderer；任何 anchor、文字、成語語意／例句／情境不一致、Object Composition blocker 立即停批。

## 核心金句

> 底線跟著字走，不是字跟著底線走。

> 成語圖跟著正確例句走，不是為了好畫圖而改造句。
