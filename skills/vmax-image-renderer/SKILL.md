---
name: vmax-image-renderer
description: 將核准 Render Request 實際渲染為教學圖片；採 Object Composition First、Verified Text 與 glyph-anchored Vocabulary Marking。
---

# V-MAX Image Renderer

版本：2.0

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

課文、注音、生字、形近字、多音字、成語、題目與正式定義不得由圖片模型自由生成。若 provider 無法量測最終文字 glyph bbox 或安全重算 anchor，標記 `RENDERER_CAPABILITY_BLOCKED`；不得以肉眼猜座標代替。

## Monolithic Background Regression

完整場景吃滿畫布、文字只能搬移或物件全烘焙成單一底圖 → `MONOLITHIC_BACKGROUND_REGRESSION`。回 Object Composition 重構。

## Representative / Batch

有語詞標記時，代表頁必須實測至少一次 reflow（例如字級／欄寬變動）後 anchor 自動失效並重新計算。全量採小批次，每批檢查文字、Object Composition、角色與 Vocabulary anchors。

## Completion

除一般文字／Object Composition／canvas／角色 gates 外，有語詞標記頁必須通過上述六項 Vocabulary gates。只有 `RENDER_VERIFIED` 可交付。

## 核心金句

> 食宿的底線只能從「食宿」兩字的最終字框算出來，不能因為它原本大概在第二行就畫在第二行某個位置。

> 字改了，anchor 就失效；重新算線，不搬字。