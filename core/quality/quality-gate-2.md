# V-MAX Quality Gate 3.1

## 定位
正式簡報交付前檢查教材真值、Object Composition、文字／注音、語詞標記、成語應用情境、角色與教師後製負擔。

## Gate A｜Teaching Integrity
教材與教師核准內容必須正確；一頁一主要焦點；學生頁不洩漏答案。教材真值錯誤 → FAIL。

## Gate B｜Object Composition
一般頁可追溯 Object/Character/Key Line plans；有語詞標記時可追溯 Vocabulary Mark Plan；成語頁可追溯 Idiom Application Plan。完整 AI 場景吃滿畫布、文字只能搬動、物件全烘焙 → `MONOLITHIC_BACKGROUND_REGRESSION` → FAIL。核准 overlap 不算碰撞。

## Gate C｜Text & Vocabulary Marking
課文、生字、注音、多音字、形近字、成語、題目與需辨識文字零錯誤。每個語詞 anchor 必須對應目前最終文字層；任何 reflow 強制重算。語詞使用 `UNDERLINE_HIGHLIGHT`，整句／金句才用核准 `BACKGROUND_HIGHLIGHT`。

有語詞標記頁必須通過：`VOCAB_ANCHOR_PASS`、`VOCAB_REFLOW_PASS`、`VOCAB_MARK_ALIGNMENT_PASS`、`VOCAB_MARK_SPAN_PASS`、`VOCAB_MARK_LAYER_PASS`、`TERM_COLOR_CONSISTENCY_PASS`。錯詞、穿字、遮注音、舊 anchor → FAIL。

## Gate D｜Idiom Application & Layout

成語頁逐頁檢查：
1. 成語、解釋、例句逐字正確。
2. 例句必須語法通順、成語使用正確、符合四年級學生可理解的生活語境。
3. 不得為了配合某張圖或方便生成畫面而扭曲、硬湊或改壞例句。
4. 成語為主要文字焦點；短解釋次之；例句具足夠投影字級與獨立閱讀空間。
5. 不得固定退化成「成語／解釋／例句」三個同等卡片、三欄表或密集文字團。
6. 情境圖支援例句中的實際用法／引申義，而非只畫成語字面拆解。
7. 圖中人物、動作、關係或事件能回到例句。
8. 角色若參與例句，融入情境，不作無功能角落裝飾。
9. 一頁兩成語只有在故事線、前後事件、對照或共享場景有可見關係時成立；否則拆頁。

必須通過：
- `IDIOM_TEXT_PASS`
- `IDIOM_HIERARCHY_PASS`
- `IDIOM_EXAMPLE_READABILITY_PASS`
- `IDIOM_EXAMPLE_NATURALNESS_PASS`
- `IDIOM_EXAMPLE_VISUAL_MATCH_PASS`
- `IDIOM_OBJECT_COMPOSITION_PASS`

例句文法正確但不像四年級生活語言、成語搭配牽強、為了圖片硬湊句子 → `IDIOM_EXAMPLE_UNNATURAL` → FAIL。
只畫字面意思 → `IDIOM_LITERAL_IMAGE` → FAIL。
圖與例句人物／動作／語意不一致 → `IDIOM_EXAMPLE_VISUAL_MISMATCH` → FAIL。

依賴方向固定為：`正確成語語意 → 自然例句 → 情境圖`。禁止 `想畫的圖 → 硬改例句`。

## Gate E｜Render Readiness

## Gate E0｜Slide Architecture & Idiom Coverage

正式渲染前必須驗證 `SLIDE_ARCHITECTURE_LOCK`：

1. 頁面區段符合 `opening → overview → visual_mind_map → paragraph_learning → character_comparison → idiom_learning → textbook_language_activity → summary_transfer`。
2. 每個 `paragraph_learning` 依序包含課文、語詞解釋、修辭／句型與文意理解。
3. 外加變體有完整 `architecture_mapping`，且不會把 transformed／extended 內容冒充 Baseline。
4. `LANGUAGE_CANDIDATE_COVERAGE.character_related_idioms` 中每個 retained 項目都回指 `final_idiom_section_refs`。

任何錯序、缺區段或成語 provenance 斷裂標記 `SLIDE_ARCHITECTURE_ORDER_FAIL` 或 `IDIOM_CHARACTER_COVERAGE_INCOMPLETE`，不得進入 `RENDER_READY`。

5. `PAGE_DETAIL_CONFIRMATION` 狀態為 `approved`，且每頁都有文字、來源、圖片細節與版面規格。
6. Slide Script、Render Request 與頁面母檔的文字、source refs、頁型、圖片／版面 revision 一致。

缺少逐頁細節、頁面母檔未核准或下游資料與母檔不一致，標記 `PAGE_DETAIL_CONFIRMATION_PENDING` 或 `PAGE_DETAIL_SOURCE_CONFLICT`，不得進入 `RENDER_READY`。

正式 Renderer 只接受 `RENDER_READY`。若仍屬 `PRE_LAYOUT`，不得標記正式渲染完成。

有語詞標記的 `RENDER_READY` request，`glyph_bbox`、`baseline_y`、`mark_bbox`、`text_layout_revision` 必須完整；否則 `RENDER_READY_ANCHOR_INCOMPLETE` → FAIL。

成語頁 `RENDER_READY` 前必須已有完整 `IDIOM_APPLICATION_PLAN` 並通過 `IDIOM_EXAMPLE_NATURALNESS_PASS`。

## Gate F｜Renderer / Regression
老師不應再手動搬字、調底線、重畫語詞範圍，也不應逐頁提醒「例句要加大」「圖要配合造句」「成語、解釋、例句不要擠在一起」。反覆出現代表 Renderer／Layout Contract 尚未完成。

代表頁有語詞標記時實測一次 reflow；有成語頁時至少驗證一次成語語意、例句自然度與情境圖一致性。

## 修復順序
Vocabulary：重新 locate → 重算 glyph bbox → mark bbox → 局部重畫。
Idiom：先核對成語語意 → 修正自然例句 → 定義人物／動作 → 配 primary visual → 平衡文字層級 → 必要時拆頁。
大底圖退化：回 Object Composition。

## Teacher Effort Gate
若教師仍需反覆提出「底線往左／往上」「字放大後線又跑掉」「造句怪怪的」「圖跟造句對不起來」「例句太小」「三段文字擠在一起」，不得 PASS。

## 核心金句
> 先有正確自然的例句，才有配合例句的圖。

> PRE_LAYOUT 是準備；RENDER_READY 才是可施工合約。
## 階段證據分工

PRE_LAYOUT 只驗證草稿結構；RENDER_READY 驗證核准文字、成語例句審閱與排版 anchors，尚未產生成品的視覺 checks 可為 null。任何已知 false 先修復，不得施工。
成品 Gate 必須以 Renderer launcher 的 --result 驗證回條；通用七項及適用成語／語詞六項 checks 全數通過，並綁定 request_sha256、asset_sha256 與 review_ref。Schema／hash 通過僅證明資料與證據一致，不取代實際語意、文字與成品審閱。
