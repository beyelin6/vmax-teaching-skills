# V-MAX Quality Gate 2.7

## 定位

正式簡報交付前檢查教材真值、觀看路徑、Object Composition、文字／注音、語詞標記、角色、Visual Drift 與教師後製負擔。

核心問題：投影片是否真正共同構圖？學生是否能清楚辨認「哪幾個字是指定語詞」，而不是被穿字色塊或錯位底線干擾？

## Gate A｜Teaching Integrity

教材、語詞、句型、修辭、生字、形近字、多音字、成語符合核准來源與教師選擇；一頁一主要焦點；學生頁不洩漏答案。教材真值錯誤 → FAIL。

## Gate B｜Visual Understanding & Object Composition

一般圖片式頁可追溯 `OBJECT_COMPOSITION_PLAN`、`CHARACTER_PLAN`、`KEY_LINE_PLAN`；有語詞標記時可追溯 `VOCAB_MARK_PLAN`。

正式文字／注音先取得空間；主視覺、小插圖、角色、標記有主次；protected zones 完整；適合時使用自然輪廓而非全數硬矩形。

### Monolithic Background Regression

完整 AI 場景吃滿畫布、文字只能在縫隙搬動、所有物件烘焙成單一底圖、修改主要變成上下左右挪字 → `MONOLITHIC_BACKGROUND_REGRESSION`，一般頁 FAIL。回 Object Composition 重構。

### Planned Overlap

核准 `SCENE_INTEGRATED`／`FOREGROUND_OVERLAP`／planned overlaps 不算碰撞。未規劃或遮住臉、關鍵動作、核心教材證據、課文／注音閱讀區才是 `IMAGE_COLLISION`。

## Gate C｜Text Accuracy, Readability & Vocabulary Marking

### C1. Zero-Tolerance Core Text
課文、生字、注音、多音字、形近字、成語正式內容、題目與所有需朗讀／辨識文字零錯誤。

### C2. Readability
不縮字硬塞；後排可讀；注音不被圖像或標記侵入；課文保持連續閱讀秩序。

### C3. Vocabulary Marking Gate

指定語詞預設 `UNDERLINE_HIGHLIGHT`，整句／金句才使用核准的 `BACKGROUND_HIGHLIGHT`。

逐一檢查：
- **Alignment**：筆刷位於中文字主要字框下方，保留約字高 8–12% 淨距；不可穿過主要筆畫。
- **Stroke**：厚度約字高 10–16%，可有自然手繪感，但不可高到成為字後色塊。
- **Span**：只涵蓋指定語詞，無多字／少字／錯詞；標點預設不納入。
- **Layer**：文字在上、標記在下；不得遮注音。
- **Color**：同一 `term_color_id` 在原文與詞語解釋一致。
- **Hierarchy**：語詞字下標記與整句背景筆刷視覺層級明確不同。

任一失敗 → `VOCAB_HIGHLIGHT_COLLISION` → REVISE；若造成語詞範圍誤判、遮字／注音或標錯詞 → FAIL。

修正原則：若正式文字位置正確，只修標記物件，不得搬課文來遷就底線。

必須通過：
- `VOCAB_MARK_ALIGNMENT_PASS`
- `VOCAB_MARK_SPAN_PASS`
- `VOCAB_MARK_LAYER_PASS`
- `TERM_COLOR_CONSISTENCY_PASS`

### C4. Typed Text / Strange Character
非課文頁只是打字浮在背景 → `TYPED_TEXT_LAYOUT_FAIL`。逐頁掃描假字、錯字、亂碼、錯誤注音與字形異常。

## Gate D｜Renderer, Character & Regression

老師不應再自行搬字、排圖、重打核心文字或調語詞底線。角色有功能且 canonical DNA 一致。代表頁需覆蓋實際 page families；本課有語詞標記時，至少一張代表頁必須實際通過 Vocabulary Marking Gate。

Visual Drift 檢查 WORLD / STYLE / PALETTE / CHARACTER / TYPOGRAPHY / UI / COMPOSITION / PEDAGOGICAL_VISUAL / LVM drift。任何 unresolved blocker → FAIL。

若有 Approved Visual Benchmark，另檢查留白、文字密度、局部插畫比例、角色干擾度、模板感、大底圖退化，以及語詞標記是否與核准教材視覺語法一致。

## Page Risk

- R1：封面、情境、意象、情緒停格。
- R2：段落原句＋情境、語詞、句型／修辭、成語、Lesson Visual Map。
- R3：生字、注音、形近字、多音字、正式定義、評量。

課文語詞標記因可能改變學生對語詞範圍的判讀，至少按 R2 檢查；涉及注音／字形辨識時提升至 R3。

## 修復順序

1. 局部標記／文字／物件修復
2. 局部圖片修補
3. 小區域重做
4. 最後才整頁重構

`VOCAB_HIGHLIGHT_COLLISION`：先修標記，不搬正確文字。
`MONOLITHIC_BACKGROUND_REGRESSION`：直接回 Object Composition，不繼續搬字。

## Teacher Effort Gate

若教師仍需逐頁調底線高低、重畫語詞範圍、搬字避色塊、統一角色或修大量中文字，Renderer 尚未完成。

## 核心金句

> 語詞標記的任務是讓孩子一眼看出語詞範圍；不能反過來妨礙孩子看字。

> 字對了但畫線穿字、標錯範圍，一樣不是完成品。