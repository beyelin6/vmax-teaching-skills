# Lesson Presentation Execution Rules

版本：1.3

本檔是每課簡報製作期間，教師追加並確認的具體視覺、版面、角色、素材再利用與違規處理決策主檔。它不是教材知識來源，也不得改寫官方 Source Master 或 Lesson Knowledge Book。

## 載入優先順序

續作、修圖、生圖或重新渲染前，依序讀取：

`Runtime State → Lesson Execution Rules → 最新 Slide/Page Layout Brief → Slide Script → 當頁 Source → Visual/Role assets`

最新且已確認的本檔高於歷史 Slide Script、歷史 Render Request、舊代表頁與舊渲染結果；但不得高於官方 Source Master／LKB 的教材事實。若發生衝突，標記 `EXECUTION_RULE_CONFLICT`，保留衝突並停止，不得自行選邊。

## 下游相容與衝突裁決

本檔對逐頁施工與 Renderer 的要求屬於簡報執行期必要欄位。若 Presentation Engine、Image Renderer、Renderer Contract 或 Quality Gate 的舊版文字只列出較少欄位，該清單視為基礎欄位而非排他性完整清單；不得因此省略本檔已明列的 `OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、`overlap_mode`、`overlap_targets` 或場景融入檢查。

圖像碰撞類規則必須依語意判斷：未規劃、無理由、破壞主次或閱讀安全區的交疊才是 `IMAGE_COLLISION`；核准的 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP` 屬 `APPROVED_SCENE_OVERLAP`，不得因相切、遮住局部背景而自動判錯。

逐頁規劃固定順序：

`Visual Grammar / Slide Architecture → 逐頁物件式場景組版＋角色配置＋金句策略＋交疊規劃 → 頁型風格矩陣／Style Recipe → 教師確認 → 頁數估算 → 代表頁驗證 → Renderer`

## Object-based Scene Composition｜物件式場景組版

圖片式國語簡報預設不得以「先生成一張完整滿版大底圖，再找空位挪字」作為一般施工模式。除核准的沉浸式例外頁外，每頁應先把教學內容拆成可配置物件，再共同構圖。

標準施工順序：

`教學焦點 → 正式文字／閱讀安全區占位 → 主場景物件 → 課文小插圖／情境物件 → 角色物件 → 道具／箭頭／螢光筆／標記 → 金句／對話 → 前中後景與交疊關係 → 整體合成`

### OBJECT_COMPOSITION_PLAN

每頁 PAGE_PLAN 必須包含 `OBJECT_COMPOSITION_PLAN`：
- `composition_mode`: `OBJECT_SCENE` / `IMMERSIVE_FULL_SCENE`
- `background_role`: 背景只承擔環境、氣氛或空間連續性，不得預先吃滿所有可用區域
- `text_objects`: 課文、語詞、注音、標題、任務、金句等正式文字物件及安全區
- `primary_visual_object`: 本頁主要理解物件／場景
- `supporting_visual_objects`: 可獨立移動、縮放、裁切的小插圖、道具、情境物件
- `character_objects`: 對應 `CHARACTER_PLAN`
- `annotation_objects`: 箭頭、圈選、螢光筆、底線、標籤等
- `layer_order`: 背景／中景／前景／文字與標記的層級
- `planned_overlaps`: 核准的物件交疊及理由
- `protected_zones`: 文字閱讀區、注音區、人物臉部、關鍵動作、核心教材證據
- `organic_edge_strategy`: 插圖是否使用去背、自然輪廓、局部淡出、遮罩或其他非硬矩形邊界

### 物件原則

- 背景不是整張投影片；它只是眾多物件中的底層。
- 課文小插圖原則上是獨立物件，不必被烘焙進一張不可拆的大場景。
- 角色是獨立物件，但可透過合理前後景、遮擋與互動融入場景。
- 正式文字必須在視覺生成前先取得空間，不得最後才尋找剩餘空白。
- 插圖不預設使用方方正正的圖片框；若內容允許，優先自然輪廓、去背或局部場景邊界。
- 修改單一角色、小插圖或文字位置時，優先局部物件重排／替換，不重畫整張成功畫面。

### Monolithic Background Regression｜大底圖退化

一般教學頁若出現以下現象，標記 `MONOLITHIC_BACKGROUND_REGRESSION`：
- 一張完整 AI 場景幾乎占滿畫布，文字只能在剩餘縫隙中移動。
- 課文、詞語、注音或金句沒有預留閱讀區，只能壓在插畫上或加大白框補救。
- 角色、小插圖、道具已全部烘焙在同一底圖，導致修改任何一項都必須整頁重生。
- 為容納文字反覆把文字往上／下／左／右挪，而不是重新平衡物件構圖。
- 圖像本身是一張完整海報，移除文字後仍幾乎是一張不可拆的成品插畫，文字沒有參與原始構圖。

發生時不得靠縮字、加白色遮罩或繼續挪字修補；應回到 `OBJECT_COMPOSITION_PLAN` 重排物件。

### IMMERSIVE_FULL_SCENE 例外

封面、情緒停格、故事高潮、環境沉浸、單一大情境觀察等頁型可使用 `IMMERSIVE_FULL_SCENE`，但必須在 PAGE_PLAN 說明教學理由，且正式文字仍需有天然留白或事先規劃的安全區。不得因「比較漂亮」就把一般課文、語詞、生字、句型頁改成滿版大底圖。

## 固定角色與語意輔助人物

- `CANONICAL_CHARACTER`：課文主要人物、引導角色、教師角色或跨頁反覆出現人物。必須使用 Role／Character Library，保持外觀、服裝、比例與視覺 DNA 一致。
- `SEMANTIC_SUPPORTING_FIGURE`：成語情境人物、形近字詞義示意人物、單次生活情境人物或只為理解而存在的人物。可以即頁生成，不得寫入固定角色庫。

## 頁型角色策略

每個 `page_family` 必須指定 `character_policy`：`CANONICAL_REQUIRED`、`CANONICAL_OPTIONAL`、`SUPPORTING_FIGURE_ALLOWED`、`CHARACTER_DISCOURAGED` 或 `NO_CHARACTER`。

## CHARACTER_PLAN

每頁必須有 `CHARACTER_PLAN`，即使不用角色也記錄 `appear: no`。至少包含：
- `appear`
- `character`
- `character_type`
- `role`
- `position`
- `scale`
- `facing`
- `action`
- `speech_mode`
- `overlap_mode`: `SEPARATE_OBJECT` / `SCENE_INTEGRATED` / `FOREGROUND_OVERLAP`
- `overlap_targets`
- `avoid_zone`

角色必須有教學或敘事功能。貫穿角色須在逐頁 brief 標出出場節奏。

### 場景融入與交疊

角色是獨立物件不代表永遠與其他圖片分離。採訪、觀察、對話、陪伴、操作器材、指向景物或與事件人物互動時，可採 `SCENE_INTEGRATED` 或 `FOREGROUND_OVERLAP`，合理與背景、道具、情境插圖或其他人物交疊。

交疊須有教學／敘事理由，不遮臉、手勢、關鍵動作、核心物件與閱讀安全區，並維持合理比例、視線、前後景與接觸關係。

## KEY_LINE_PLAN

每頁必須有 `KEY_LINE_PLAN`，即使不用也記錄 `use: no`。至少包含：
- `use`
- `source`: `TEXTBOOK` / `TEACHER` / `AI_TRANSITION` / `NONE`
- `text`
- `function`
- `placement`
- `hierarchy`
- `relation_to_character`

不得為裝飾強加金句。`TEXTBOOK` 保留原文來源；`TEACHER` 明確屬教師補充；`AI_TRANSITION` 只作引導／過場，不得偽裝成教材。

## 圖文與物件避讓

角色、金句、課文文字、詞語解釋、小插圖、道具與標記都是可獨立配置物件。先保留閱讀安全區與教學重點，再配置視覺物件。保護重點不是禁止圖像彼此交疊，而是避免遮住學生真正需要閱讀或觀察的證據。

若 `OBJECT_COMPOSITION_PLAN`、角色位置、金句位置、主要文字區或必要 overlap 尚未決定，標記 `PAGE_LAYOUT_INCOMPLETE`，不得進入代表頁或 Renderer。

## 既有定稿教材再利用

已有 `APPROVED`、`LOCKED` 或 `FINAL` artifact 時優先 reuse 並保留來源；不得自行改寫短文、補題、換句型、替換詞語或新增未核准內容。

## 生圖前門檻

每頁 Render Request 前必須通過 `PRE_RENDER_RULE_COMPLIANCE_CHECK`，至少檢查：Execution Rules、來源與核准狀態、`OBJECT_COMPOSITION_PLAN`、角色分類與 asset、`character_policy`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、閱讀安全區、`overlap_mode`、場景融入合理性、`MONOLITHIC_BACKGROUND_REGRESSION`、圖文對應、卡片牆、答案洩漏、密度、文字模式與歷史 Render Request 污染。

未通過即 `PRE_RENDER_RULE_BLOCKED`。

## 逐頁施工稿層級

先 `PAGE_PLAN`，再 `REPRESENTATIVE_CONSTRUCTION`，最後 `SLIDE_SCRIPT`。PAGE_PLAN 不要求像素級座標。

PAGE_PLAN／`working/slide-page-layout-brief.md` 每頁至少包含：頁面目的、學生可見文字、教材證據、頁型、構圖、文字區、留白區、插圖需求、`OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`。缺少任一三項核心計畫即視為逐頁規劃未完成。