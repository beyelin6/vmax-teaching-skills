# V-MAX Quality Gate 2.8

## 定位

正式簡報交付前檢查教材真值、Object Composition、文字／注音、語詞標記、角色與教師後製負擔。

## Gate A｜Teaching Integrity

教材與教師核准內容必須正確；一頁一主要焦點；學生頁不洩漏答案。教材真值錯誤 → FAIL。

## Gate B｜Object Composition

一般頁可追溯 Object/Character/Key Line plans；有語詞標記時可追溯 Vocabulary Mark Plan。正式文字先占位；小插圖、角色、標記有主次與 protected zones。

完整 AI 場景吃滿畫布、文字只能搬動、物件全烘焙 → `MONOLITHIC_BACKGROUND_REGRESSION` → FAIL。核准的場景 overlap 不算碰撞。

## Gate C｜Text & Vocabulary Marking

### Zero-tolerance Text

課文、生字、注音、多音字、形近字、成語、題目與需辨識文字零錯誤。

### Vocabulary Anchor Gate

每個指定語詞逐一核對：
1. `term_text` 與來源完全一致。
2. `occurrence_index` 指向正確一次出現；同詞多次時不得含糊。
3. `start_char_index`／`end_char_index` 對應正確字元。
4. `glyph_bbox`／`baseline_y` 來自**目前最終文字層**。
5. `mark_bbox` 由該 glyph anchor 派生，而非人工猜測座標。
6. `text_layout_revision` 與目前排版一致。

任一不成立 → `VOCAB_ANCHOR_FAIL` → FAIL。

### Vocabulary Reflow Gate

字型、字級、字距、行距、欄寬、換行、文字位置或內容只要變更，即視為 reflow。必須看到新的 `text_layout_revision`，並重新建立 glyph bbox、baseline 與 mark bbox。

文字已 reflow、底線仍沿用舊 anchor → `STALE_VOCAB_MARK_ANCHOR` → FAIL。

必須通過 `VOCAB_REFLOW_PASS`。

### Vocabulary Visual Gate

- 語詞 → `UNDERLINE_HIGHLIGHT`。
- 整句／金句 → 核准 `BACKGROUND_HIGHLIGHT`。
- Underline 在主要字框下方，淨距約字高 8–12%，厚度約 10–16%。
- 只涵蓋指定語詞，標點預設排除。
- 文字在上、標記在下；不遮注音。
- 同一 term color ID 在原文／詞義一致。
- 手繪感不得犧牲 anchor 精準度。

穿字、錯詞、多／少字、遮注音、標記偏到其他文字下方 → `VOCAB_HIGHLIGHT_COLLISION`。

### Required Vocabulary Passes

有語詞標記頁必須全部通過：
- `VOCAB_ANCHOR_PASS`
- `VOCAB_REFLOW_PASS`
- `VOCAB_MARK_ALIGNMENT_PASS`
- `VOCAB_MARK_SPAN_PASS`
- `VOCAB_MARK_LAYER_PASS`
- `TERM_COLOR_CONSISTENCY_PASS`

像「要求標食宿，線卻出現在學生可以下面」或「女學堂的線跑到蔡阿信附近」屬 anchor failure，不是微調問題，直接 FAIL。

## Gate D｜Renderer / Regression

老師不應再手動搬字、調底線、重畫語詞範圍。若標記錯位，Renderer 必須重新定位 occurrence／重算 glyph anchor，而不是搬課文。

代表頁若有語詞標記，必須實際測一次 reflow 後自動重算 anchor。未測不得代表全課放行。

Visual Drift、角色 DNA、canvas、閱讀安全區與實際成品仍須通過既有 V-MAX gates。

## 修復順序

Vocabulary：`重新 locate occurrence → 重算 glyph bbox → 重算 mark bbox → 調 clearance/stroke → 局部重畫標記`。

大底圖退化：回 Object Composition。

## Teacher Effort Gate

教師仍需逐頁說「食宿的線往左」「女學堂的線往上」「字放大後線又跑掉」即代表 Renderer 尚未完成，Quality Gate 不得 PASS。

## 核心金句

> 對位不是看起來差不多；標記必須有證據證明它綁在正確的字上。

> 文字 reflow 之後，所有舊底線座標都作廢。