# Lesson Presentation Execution Rules

版本：1.0

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

## 既有定稿教材再利用

若教學模組已有 `APPROVED`、`LOCKED` 或 `FINAL` artifact，Presentation Engine 必須優先搜尋、登錄並引用該 artifact。內容來源不變，呈現媒介可以變；不得自行改寫短文、補題、換句型、替換詞語清單或新增未核准內容。

## 生圖前門檻

每一頁建立 Render Request 前，必須先產生 `PRE_RENDER_RULE_COMPLIANCE_CHECK` 並通過。至少檢查：最新 Execution Rules、來源與核准狀態、角色分類與 asset、頁型 character_policy、課文連續性、語詞原文標記、圖文對應、構圖退化、卡片牆、答案洩漏、頁型密度、文字模式與歷史 Render Request 污染。

未通過不得生圖；狀態使用 `PRE_RENDER_RULE_BLOCKED`，並列出違規規則與唯一修正決定。
