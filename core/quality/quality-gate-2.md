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
7. 每個出場角色都有相同且已核准的 `base_character_id`、`core_dna_ref`、`approved_asset_id` 與 `asset_version`；只使用 `allowed_variations`。

缺少逐頁細節、頁面母檔未核准、下游資料與母檔不一致或角色定錨缺失，標記 `PAGE_DETAIL_CONFIRMATION_PENDING`、`PAGE_DETAIL_SOURCE_CONFLICT` 或 `CHARACTER_ANCHOR_MISSING`，不得進入 `RENDER_READY`。若成品出現臉型、髮型、服裝識別、比例或年齡感漂移，標記 `CHARACTER_IDENTITY_DRIFT`，停止該批次。

正式 Renderer 只接受 `RENDER_READY`。若仍屬 `PRE_LAYOUT`，不得標記正式渲染完成。

有語詞標記的 `RENDER_READY` request，`glyph_bbox`、`baseline_y`、`mark_bbox`、`text_layout_revision` 必須完整；否則 `RENDER_READY_ANCHOR_INCOMPLETE` → FAIL。

成語頁 `RENDER_READY` 前必須已有完整 `IDIOM_APPLICATION_PLAN` 並通過 `IDIOM_EXAMPLE_NATURALNESS_PASS`。

## Gate E1｜Batch Construction Lock

批次製作逐頁核對 `core/governance/batch-construction-lock.md`：

1. PAGE_DETAIL_CONFIRMATION 為 `approved`，且整份檔案 hash 與 `BATCH_CONSTRUCTION_LOCK` 相同。
2. 每個 page detail page object 都有 `page_spec_sha256`，並與 Slide Script、Render Request 的 page hash 相同。
3. 頁面數量、`page_id`、sequence、page family、來源回指與角色錨點一對一相符。
4. 沒有未宣告頁、靜默補頁、刪頁、重排、換模板或沿用上一頁資料。
5. 每 5–8 頁小批次開始前重新驗證，批次結束後完成逐頁回讀與 drift check。
6. Style Selection Profile 已由教師確認，所有頁面與 Render Request 的 `style_core_id` 都等於選定主風格；頁型變體只能來自已核准的 `page_variants`。
7. 課文閱讀頁的 `text_coverage` 顯示完整原文，且 `vocabulary_coverage.placement` 為相鄰版位；語詞解釋不得脫離課文另成清單頁。
8. 新角色的 Role Selection Profile 已完成 Registry writeback，`reuse_level` 至少為 `LESSON_ONLY`，並有可回讀的 registry hash；不得自動升級為跨課可重用角色。
9. 課文正文與段落語詞通過教室投影等效字級檢查：正文目標 36–40 pt、硬下限 32 pt；語詞目標 30–34 pt、硬下限 28 pt，且有最終文字層實測證據。
10. `page_number_system` 與 `section_marker_system` 已鎖定；每頁的設計感數字符號仍可回指正式頁序與 `section_id`，不得以裝飾記號取代機讀序號。

任一項失敗標記 `BATCH_CONSTRUCTION_LOCK_FAIL`、`STYLE_SELECTION_REQUIRED`、`STYLE_SELECTION_HASH_MISMATCH`、`STYLE_DRIFT`、`CHARACTER_REGISTRY_WRITEBACK_REQUIRED`、`CHARACTER_REGISTRY_HASH_MISMATCH`、`PAGE_DETAIL_HASH_MISMATCH`、`PAGE_SPEC_HASH_MISMATCH`、`PAGE_ORDER_DRIFT`、`PAGE_FAMILY_DRIFT`、`LAYOUT_SPEC_DRIFT`、`PARAGRAPH_TEXT_INCOMPLETE`、`PARAGRAPH_VOCABULARY_DROPPED`、`PARAGRAPH_VOCABULARY_DETACHED`、`CLASSROOM_FONT_SIZE_UNVERIFIED`、`CLASSROOM_FONT_TOO_SMALL`、`UNDECLARED_PAGE` 或 `RENDER_REQUEST_UNBOUND`，整批停止，不得進入 `RENDER_READY`。

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
