---
name: vmax-image-renderer
description: 將核准 Render Request 實際渲染為教學圖片；採 Object Composition First、Verified Text 與 glyph-anchored Vocabulary Marking。
---

# V-MAX Image Renderer

版本：2.1

## Request Contract Gate

直接呼叫本技能也必須先讀取 `references/render-request-schema.md`、`core/schemas/vmax/render-request.schema.json` 與 Quality Gate。正式施工前執行：

```sh
python "<目前 Renderer 技能絕對路徑>/scripts/validate_presentation.py" "<request.json 絕對路徑>" --kind render-request --require-ready
```

收到完整 Slide Script 時以預設 kind 驗證並加 `--require-ready`，同時檢查上下游 Plan 相等。執行環境須有 jsonschema；驗證器無法執行或非零退出碼 → `PRE_RENDER_RULE_BLOCKED`，不得宣稱通過。PRE_LAYOUT 只可進排版準備。

批次製作另必須先執行 `scripts/validate_batch_lock.py`，同時提供 Slide Script、已核准 PAGE_DETAIL_CONFIRMATION 與已確認 Style Selection Profile：

```sh
python "<Renderer 技能絕對路徑>/scripts/validate_batch_lock.py" --slide-script "<Slide Script 絕對路徑>" --page-detail "<PAGE_DETAIL_CONFIRMATION 絕對路徑>" --style-selection "<Style Selection Profile 絕對路徑>" --role-selection "<Role Selection Profile 絕對路徑>"
```

這個檢查會驗證整份母檔 hash、每頁 page hash、頁序、page family、來源回指、風格核心、已確認角色與 Registry writeback、課文完整性、相鄰語詞與教室投影字級證據、Render Request 綁定；非零退出碼 → `BATCH_CONSTRUCTION_LOCK_FAIL`，不得啟動任何批次 Renderer。缺欄位不得套用上一頁、平台預設或通用模板。

成語頁必須傳入完整 idiom_application_plan；施工前取得例句語法、用法、適齡生活語境審閱結果與 review_ref。證據不可由預設 true 代填；Schema 通過不代表語意審閱通過。沿用核准例句，圖跟例句人物與動作走。來源未提供時標示缺口或使用已核准補充，不得冒充教材原文。

交付前逐頁執行六項成語 gates（文字、層級、例句可讀性、自然度、圖文匹配、物件構圖），保留實際成品檢查證據；任一失敗不得 RENDER_VERIFIED。

施工前不要求尚未產生的圖文匹配結果；成品階段必須以 `--kind render-request --result RESULT` 驗證綁定請求 hash 與實際檔案 hash 的結果回條。正式文字以 layer_id/text/source_ref 原樣傳遞；空文字只允許明確 textless 的無字頁。資料格式、環境與草稿→排版→施工→QA 命令以 `references/render-request-schema.md` 為唯一詳細操作說明。

## PRE_RENDER_RULE_COMPLIANCE_CHECK

核對 Runtime State、Execution Rules、Layout Brief、Slide Script、Source/assets、Object/Character/Key Line plans，以及適用時的 `VOCAB_MARK_PLAN`、`text_layout_revision`、anchor metadata。檢查大底圖退化、Vocabulary collision/anchor/reflow、閱讀安全區、角色、答案與密度。任一 blocker → `PRE_RENDER_RULE_BLOCKED`。

## Object Composition First

正式文字／注音先占位，再配置場景、小插圖、角色、道具、標記與金句。不得使用無字大底圖→找空位→搬字流程。核准的場景交疊不是碰撞。

## Glyph-anchored Vocabulary Marking

每個語詞標記是獨立 annotation layer。**禁止以人工估算座標或上一次 render 的底線位置直接重用。**

執行流程：
1. 完成 Verified Text 最終排版並取得 `text_layout_revision`。
2. 以 `term_text + occurrence_index` 精確定位指定 occurrence。
3. 取得 `line_id`、`start_char_index`、`end_char_index`。
4. 從實際文字層量測 `glyph_bbox` 與 `baseline_y`。
5. 由 glyph bbox 計算 `mark_bbox`。
6. 生成 `UNDERLINE_HIGHLIGHT`。
7. 執行 anchor/reflow/alignment/span/layer/color QA。

若 occurrence 不唯一或找不到 → `VOCAB_ANCHOR_FAIL`，不得猜。

### Reflow Invalidation

下列任何變更均視為 text reflow：字型、字級、字距、行距、欄寬、換行、文字 x/y、文字內容。

發生 reflow：
- 更新 `text_layout_revision`。
- invalid 所有舊 `glyph_bbox`、`baseline_y`、`mark_bbox`。
- 強制重新 locate、measure、calculate、render。

若 revision 已改變但 anchor 未重算 → `STALE_VOCAB_MARK_ANCHOR` → FAIL。

### Underline Geometry

字下淨距約字高 8–12%；筆刷厚度約 10–16%；span 只含指定語詞，標點預設排除；文字在上、標記在下；不得遮注音。同一 term color ID 跨原文／詞義一致。手繪感只能作用於筆刷邊緣，不能改變 anchor/span 的準確性。

整句／金句才可用核准 `BACKGROUND_HIGHLIGHT`。

## Vocabulary Completion Gate

逐詞必須通過：
- `VOCAB_ANCHOR_PASS`
- `VOCAB_REFLOW_PASS`
- `VOCAB_MARK_ALIGNMENT_PASS`
- `VOCAB_MARK_SPAN_PASS`
- `VOCAB_MARK_LAYER_PASS`
- `TERM_COLOR_CONSISTENCY_PASS`

`VOCAB_HIGHLIGHT_COLLISION`、`VOCAB_ANCHOR_FAIL`、`STALE_VOCAB_MARK_ANCHOR` 任一存在，不得 `RENDER_VERIFIED`。

修復標記：先重新定位 occurrence，再重算 bbox，最後調 clearance/stroke。文字正確時禁止搬文字追底線。

## Verified Text / Provider

課文、注音、生字、形近字、多音字、成語、題目與正式定義不得由圖片模型自由生成。只有當頁含語詞標記或其他精準文字 anchor 時，才要求最終文字 glyph bbox 量測與安全重算能力；若缺少，標記 `RENDERER_CAPABILITY_BLOCKED`，不得以肉眼猜座標代替。無此類 anchor 的頁面不因缺少量測 API 而阻擋，仍須通過文字、字型與其他適用 QA。

每次選擇 provider 或施工正式文字前，必須載入 `references/provider-routing.md` 與 `references/verified-text-overlay.md`。圖片生成可與文字 renderer 分工；平台只匯入既有合成資產時，依 provider routing 的 reflow 規則保留或重算 anchor。

## Monolithic Background Regression

完整場景吃滿畫布、文字只能搬移或物件全烘焙成單一底圖 → `MONOLITHIC_BACKGROUND_REGRESSION`。回 Object Composition 重構。

## Representative / Batch

全量採 5–8 頁小批次；每批開始前重新執行 `validate_batch_lock.py`，每批結束後回讀 page_id、sequence、文字層、Object Composition、角色、來源、風格與產物 hash。發現 `PAGE_DETAIL_HASH_MISMATCH`、`PAGE_SPEC_HASH_MISMATCH`、`PAGE_ORDER_DRIFT`、`PAGE_FAMILY_DRIFT`、`STYLE_DRIFT`、`LAYOUT_SPEC_DRIFT`、`RENDER_REQUEST_UNBOUND` 或角色／風格漂移，立即停止整批，不得先完成全套再回頭修。

有語詞標記時，代表頁必須實測至少一次 reflow（例如字級／欄寬變動）後 anchor 自動失效並重新計算。代表頁通過不代表其他頁通過；每頁仍需依自己的 locked page detail 與產物 QA 驗證。

## Completion

除一般文字／Object Composition／canvas／角色 gates 外，有語詞標記頁必須通過上述六項 Vocabulary gates。只有 `RENDER_VERIFIED` 可交付。

## 核心金句

> 食宿的底線只能從「食宿」兩字的最終字框算出來，不能因為它原本大概在第二行就畫在第二行某個位置。

> 字改了，anchor 就失效；重新算線，不搬字。
