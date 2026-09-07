# V-MAX Image-first Hybrid Renderer 2.0

## 定位

V-MAX 圖片式簡報採 **Object Composition First + Verified Text**。背景只是底層物件；正式文字先取得閱讀空間，再配置角色、場景、小插圖、道具與標記。

## Object Composition

一般頁預設 `OBJECT_SCENE`，不得先做不可拆大底圖再找空位搬字。完整場景吃滿畫布、物件全部烘焙、修改主要變成搬字 → `MONOLITHIC_BACKGROUND_REGRESSION`，必須回物件構圖。

核准 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP`／planned overlaps 不算碰撞；只有未規劃或遮核心閱讀／視覺證據才是 `IMAGE_COLLISION`。

## Verified Teaching Text

課文、注音、生字、語詞、成語、題目等來自核准來源。圖片模型不得自由生成教學關鍵中文。`TEXT_READING_PAGE` 使用可控連續文字；其他圖片式頁使用 Verified Raster Text Components。

## Vocabulary Marking Rendering Contract

語詞定位預設 `UNDERLINE_HIGHLIGHT`；整句／金句才用核准的 `BACKGROUND_HIGHLIGHT`。語詞標記是獨立 annotation object。

### Glyph Anchor Pipeline

Renderer **不得依肉眼或舊 x/y 座標猜底線位置**。固定流程：

`final text layout → text_layout_revision → locate(term_text, occurrence_index) → line_id + start/end char index → glyph_bbox + baseline_y → calculate mark_bbox → render underline → QA`

要求：
- 同詞多次出現，以 `occurrence_index` 精確指定。
- 找不到唯一 occurrence 時停止，`VOCAB_ANCHOR_FAIL`；不得挑看起來最接近的位置。
- `glyph_bbox` 必須由最終文字層實際量測。
- `mark_bbox` 是 glyph anchor 的派生值，不是獨立永久座標。
- 字型、字級、字距、行距、欄寬、換行、文字位置或內容改變時，`text_layout_revision` 必須更新。
- revision 改變後，所有舊 glyph bbox／baseline／mark bbox 立即 invalid，強制重新定位與計算。
- 沿用舊 anchor → `STALE_VOCAB_MARK_ANCHOR`。

### Underline Geometry

- 標記位於中文字主要字框下方。
- 淨距約字高 8–12%。
- 筆刷厚度約字高 10–16%。
- span 只涵蓋指定語詞，標點預設排除。
- `MARK_BELOW_TEXT`，不得遮注音。
- 同一 `term_color_id` 在原文與詞義區一致。
- 可有自然手繪感，但不能犧牲 anchor 精準度。

### Vocabulary QA

必須通過：
- `VOCAB_ANCHOR_PASS`：term occurrence 與 glyph bbox 正確。
- `VOCAB_REFLOW_PASS`：當前 anchor 對應當前 text layout revision。
- `VOCAB_MARK_ALIGNMENT_PASS`：襯在字下，不穿字。
- `VOCAB_MARK_SPAN_PASS`：起訖字元正確。
- `VOCAB_MARK_LAYER_PASS`：文字／注音層級安全。
- `TERM_COLOR_CONSISTENCY_PASS`。

以下任一 FAIL：`VOCAB_HIGHLIGHT_COLLISION`、`VOCAB_ANCHOR_FAIL`、`STALE_VOCAB_MARK_ANCHOR`。

修復順序：重新 locate occurrence → 重算 glyph bbox → 重算 mark bbox → 調 clearance/stroke → 局部重建標記。**若文字正確，不得搬文字追底線。**

## Reference Composition / Canvas

先完成 canvas lock。Reference Composition 是物件關係藍圖，不是大底圖草稿。小插圖內容允許時採自然輪廓、去背、局部淡出或遮罩。

## 代表頁 Gate

全量前驗證課文閱讀頁、一般 Object Scene、高風險語文頁；有語詞標記時至少一張代表頁必須實測：同詞 occurrence、glyph anchor、以及一次文字 reflow 後的自動重算。

## Completion Gate

至少通過文字 proof/readability、Object Composition、protected zones、planned overlap、monolithic background；有語詞標記時再通過六項 Vocabulary QA。只有 `RENDER_VERIFIED` 可交付。

## 核心金句

> 底線的位置是文字排版的函數，不是另一組手工座標。

> 字一換行，底線就重新算；底線錯了，不能搬字來配合它。