---
name: presentation-engine
description: 將核准教材與教學策略轉換為 Slide Script 與 Render Request；採 Object Composition First，語詞標記以最終 Verified Text glyph anchor 精準對位。
---

# Presentation Engine

版本：0.10.6

`SLIDE_SCRIPT` 是逐頁簡報唯一內容主檔。教材、教學策略、角色與視覺只使用已核准來源。

## PAGE_PLAN

每頁至少包含 page purpose、student visible text、source refs、page family/style、character policy、`OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`、canvas lock、density；有語詞標記時另含 `VOCAB_MARK_PLAN`。

一般頁預設 `OBJECT_SCENE`，禁止簡化成文字區＋一張底圖。完整場景吃滿畫布、文字只能搬移 → `MONOLITHIC_BACKGROUND_REGRESSION`。

## VOCAB_MARK_PLAN

每個指定語詞記錄：`term_text`、`source_ref`、`term_color_id`、`mark_mode`、`occurrence_index`、`line_id`、`start_char_index`、`end_char_index`、`glyph_bbox`、`baseline_y`、`mark_bbox`、`text_layout_revision`、`include_punctuation`、`layer_order`、clearance/stroke ratios、paired definition ref。

### Text Anchor Contract

Presentation Engine 不得在 PAGE_PLAN 階段猜最終底線 x/y。PAGE_PLAN 先指定 `term_text`、來源與 occurrence；實際 glyph anchor 必須等 Verified Text 完成最終排版後才建立。

固定流程：
`排版正式課文 → 產生 text_layout_revision → 精確定位 term occurrence → 取得 char indices / line / glyph bbox / baseline → 計算 mark bbox → 建立 Render Request`。

同詞多次出現必須指定 `occurrence_index`。任何字型、字級、字距、行距、欄寬、換行、文字位置或內容變更，都使舊 anchor 失效；Render Request 必須重新計算，不得沿用舊 mark bbox。

若找不到唯一正確 occurrence → `VOCAB_ANCHOR_FAIL`，不得猜位置。
若文字 reflow 後仍引用舊 anchor → `STALE_VOCAB_MARK_ANCHOR`。

## Vocabulary Visual Grammar

- 語詞定位 → `UNDERLINE_HIGHLIGHT`
- 整句／金句 → `BACKGROUND_HIGHLIGHT`

Underline 位於主要字框下方，淨距約字高 8–12%，筆刷厚度約 10–16%，只涵蓋指定語詞，標點預設排除，文字在上標記在下，不侵入注音。標記是獨立 annotation object，不烘焙進 AI 場景。

標記錯位時只修標記，不移動正確課文。

## CHARACTER / KEY LINE / OBJECT COMPOSITION

角色有教學或敘事功能，可依核准 overlap 融入場景。金句來源須區分教材、教師補充、AI 過場。正式文字／注音在視覺生成前先取得安全區，小插圖與角色盡量維持獨立物件。

## Representative Construction

代表頁需實際驗證物件位置、閱讀動線、角色交疊與 protected zones。本課有課文語詞標記時，至少一張代表頁必須實測：
- 正確 occurrence anchor
- 文字 reflow 後 anchor 重算
- underline alignment/span/layer
- term color consistency

## SLIDE_SCRIPT / Render Request

Slide Script 鎖定正式文字、來源、object/character/key-line plans；有語詞標記時記錄 `vocab_mark_plan`、`term_color_map`、`text_layout_revision`。

Render Request 有語詞標記時必須帶入 anchor metadata 與以下 acceptance checks：
- `VOCAB_ANCHOR_PASS`
- `VOCAB_REFLOW_PASS`
- `VOCAB_MARK_ALIGNMENT_PASS`
- `VOCAB_MARK_SPAN_PASS`
- `VOCAB_MARK_LAYER_PASS`
- `TERM_COLOR_CONSISTENCY_PASS`

未取得最終 glyph bbox 前，不得把估算座標寫成已核准 mark bbox。

## Verified Teaching Text

課文、注音、生字、形近字、多音字、成語、題目與正式例句不得由圖片模型自由生成。文字是構圖物件，先排版再產生依附於它的標記。

## 代表頁與批次

代表頁覆蓋實際 page families。教師核准後才進小批次 Renderer；任何 anchor、文字、Object Composition blocker 立即停批。

## 核心金句

> 底線跟著字走，不是字跟著底線走。

> 語詞標記的位置來自最終文字字框，不來自肉眼猜座標。