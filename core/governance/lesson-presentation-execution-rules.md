# Lesson Presentation Execution Rules

版本：1.1

本檔是每課簡報製作期間，教師追加並確認的具體視覺、版面、角色、素材再利用與違規處理決策主檔。它不是教材知識來源，也不得改寫官方 Source Master 或 Lesson Knowledge Book。

## 載入優先順序

續作、修圖、生圖或重新渲染前，依序讀取：

`Runtime State → Lesson Execution Rules → 最新 Slide/Page Layout Brief → Slide Script → 當頁 Source → Visual/Role assets`

最新且已確認的本檔高於歷史 Slide Script、歷史 Render Request、舊代表頁與舊渲染結果；但不得高於官方 Source Master／LKB 的教材事實。若發生衝突，標記 `EXECUTION_RULE_CONFLICT`，保留衝突並停止，不得自行選邊。

## 規則分層

- `LESSON_LOCAL`：只適用本課，寫入本課的 Execution Rules。
- `REUSABLE_PATTERN`：跨課可能適用的觀察，先記錄觀察與驗證課次，不直接改全域技能。
- `GLOBAL_SKILL_RULE`：至少跨課驗證後，才升級到共用技能與 Manifest 版本。

每筆規則至少記錄 `rule_id`、`scope`、`decision`、`source`、`teacher_confirmation`、`affected_page_families` 與 `status`。未確認內容只能標記 `PROPOSED`，不得控制輸出。

## 固定角色與語意輔助人物

- `CANONICAL_CHARACTER`：課文主要人物、引導角色、教師角色或跨頁反覆出現人物。必須使用 Role／Character Library，保持外觀、服裝、比例與視覺 DNA 一致。
- `SEMANTIC_SUPPORTING_FIGURE`：成語情境人物、形近字詞義示意人物、單次生活情境人物或只為理解而存在的人物。可以即頁生成，不得寫入固定角色庫，也不得被誤認為 canonical character。

## 頁型角色策略

每個 `page_family` 必須指定 `character_policy`：

`CANONICAL_REQUIRED`、`CANONICAL_OPTIONAL`、`SUPPORTING_FIGURE_ALLOWED`、`CHARACTER_DISCOURAGED` 或 `NO_CHARACTER`。

風格矩陣與角色策略共同決定頁面是否出現人物；不得因有角色庫就讓固定角色出現在每一頁。

## 逐頁角色配置與金句策略

完成 Visual Grammar / Slide Architecture 後，`working/slide-page-layout-brief.md` 不得只描述文字區與插圖需求；每一頁都必須明確完成角色配置與金句／核心句判斷。角色與金句都是版面物件，必須在 Renderer 前規劃，不得到生圖或排版階段臨時塞入。

### CHARACTER_PLAN

每頁必須有 `CHARACTER_PLAN`，即使不使用角色也要明確記錄 `appear: no`。至少包含：

- `appear`: yes / no
- `character`: 角色名稱或 `NONE`
- `character_type`: `CANONICAL_CHARACTER` / `SEMANTIC_SUPPORTING_FIGURE` / `NONE`
- `role`: 主角、引導、旁觀、提示、情緒反應、串場或其他已確認功能
- `position`: 預定區域，例如左下、右側、畫面中央偏下；PAGE_PLAN 階段不要求像素級座標
- `scale`: 建議比例／視覺份量
- `facing`: 視線或身體朝向，應服務文字、事件或視覺動線
- `action`: 本頁動作／表情／教學任務
- `speech_mode`: none / dialogue / prompt / task / label
- `overlap_mode`: `SEPARATE_OBJECT` / `SCENE_INTEGRATED` / `FOREGROUND_OVERLAP`
- `overlap_targets`: 允許與哪些場景、道具、情境插圖或人物產生視覺交疊；若無則 `NONE`
- `avoid_zone`: 不可遮擋的課文、語詞、注音、主要事件、其他角色與核心插圖區

角色出現必須有教學或敘事功能；不得只因角色庫存在而裝飾性塞入。若 canonical character 在前段已設定為貫穿角色，逐頁 brief 必須明確標出其出場節奏，避免角色在中段無理由消失。

### 場景融入與交疊

「角色是獨立版面物件」不代表角色必須永遠與其他圖片分離。當角色在語意上屬於場景中的參與者，例如採訪、觀察、對話、陪伴、操作器材、指向景物、與事件人物互動時，可以採 `SCENE_INTEGRATED` 或 `FOREGROUND_OVERLAP`，合理與背景、道具、情境插圖或其他人物交疊，使角色真正融入場景。

允許交疊必須同時符合：

- 交疊有敘事或教學理由，不是為了塞滿版面。
- 不遮住人物臉部、手勢、關鍵動作、核心物件或教材重點。
- 不侵入課文、語詞、注音、金句等學生閱讀安全區。
- 前後景層級、比例、視線方向與接觸關係合理，不得像貼紙懸浮在場景上。
- 若角色與場景人物互動，視線、姿勢、手部動作與距離必須能支持該互動。

因此 Renderer 應區分「不合理遮擋」與「有意義的場景融合」；不得因偵測到圖像交疊就一律判定違規。

### KEY_LINE_PLAN

每頁必須有 `KEY_LINE_PLAN`，先判斷是否需要金句、核心句、引導句或過場句；不需要時明確記錄 `use: no`，不得為了版面漂亮強行加句子。

至少包含：

- `use`: yes / no
- `source`: `TEXTBOOK` / `TEACHER` / `AI_TRANSITION` / `NONE`
- `text`: 實際學生可見文字；若 `use: no` 則為空
- `function`: 課文核心、概念統整、角色引導、章節過場、情緒收束或其他已確認功能
- `placement`: 預定區域
- `hierarchy`: 與標題、課文、詞語解釋之視覺層級
- `relation_to_character`: 是否由角色說出、角色視線指向、與角色分離，或 `NONE`

`TEXTBOOK` 金句必須保留原文與來源；`TEACHER` 金句視為教師補充；`AI_TRANSITION` 只能作教學引導或過場，不得偽裝成課文原句。三者在內容層與視覺層都不得混淆。

### 圖文與物件避讓

角色、金句、課文文字、詞語解釋與小課文插圖都應視為可獨立配置的版面物件。逐頁 brief 必須先保留文字安全區與教學重點區，再配置角色和插圖；不得讓文字覆蓋人物臉部、關鍵動作或主要插圖，也不得讓角色／插圖侵入注音與學生閱讀區。

物件避讓的核心是保護「文字閱讀區、教學重點與關鍵視覺」，不是禁止所有圖像彼此交疊。角色與場景插圖若符合 `overlap_mode` 與場景融入規則，可以有計畫地交疊。

若角色位置、金句位置、主要文字區或必要的 overlap 關係尚未決定，該頁標記 `PAGE_LAYOUT_INCOMPLETE`，不得進入 Representative Validation 或 Renderer。

## 既有定稿教材再利用

若教學模組已有 `APPROVED`、`LOCKED` 或 `FINAL` artifact，Presentation Engine 必須優先搜尋、登錄並引用該 artifact。內容來源不變，呈現媒介可以變；不得自行改寫短文、補題、換句型、替換詞語清單或新增未核准內容。

## 生圖前門檻

每一頁建立 Render Request 前，必須先產生 `PRE_RENDER_RULE_COMPLIANCE_CHECK` 並通過。至少檢查：最新 Execution Rules、來源與核准狀態、角色分類與 asset、頁型 character_policy、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、角色／文字／插圖避讓、`overlap_mode` 與場景融入合理性、課文連續性、語詞原文標記、圖文對應、構圖退化、卡片牆、答案洩漏、頁型密度、文字模式與歷史 Render Request 污染。

未通過不得生圖；狀態使用 `PRE_RENDER_RULE_BLOCKED`，並列出違規規則與唯一修正決定。

## 逐頁施工稿層級

當課簡報規劃應先產生 `PAGE_PLAN`，再針對每個啟用頁型產生 `REPRESENTATIVE_CONSTRUCTION`，最後才建立正式 `SLIDE_SCRIPT`。PAGE_PLAN 是內容與結構確認稿，不要求像素級座標；比例以範圍表示，頁數以 `PROPOSED_PAGE_COUNT` 表示，教師確認後才可升級為本課固定頁數。

PAGE_PLAN／`working/slide-page-layout-brief.md` 每頁至少必須包含：頁面目的、學生可見文字、教材證據、頁型、構圖、文字區、留白區、插圖需求、`CHARACTER_PLAN` 與 `KEY_LINE_PLAN`。缺少後兩者視為逐頁規劃未完成。