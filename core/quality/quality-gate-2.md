# V-MAX Quality Gate 2.9

## 定位

正式簡報交付前檢查教材真值、Object Composition、文字／注音、語詞標記、成語應用情境、角色與教師後製負擔。

## Gate A｜Teaching Integrity

教材與教師核准內容必須正確；一頁一主要焦點；學生頁不洩漏答案。教材真值錯誤 → FAIL。

## Gate B｜Object Composition

一般頁可追溯 Object/Character/Key Line plans；有語詞標記時可追溯 Vocabulary Mark Plan。正式文字先占位；小插圖、角色、標記有主次與 protected zones。

完整 AI 場景吃滿畫布、文字只能搬動、物件全烘焙 → `MONOLITHIC_BACKGROUND_REGRESSION` → FAIL。核准的場景 overlap 不算碰撞。

## Gate C｜Text & Vocabulary Marking

### Zero-tolerance Text

課文、生字、注音、多音字、形近字、成語、題目與需辨識文字零錯誤。

### Vocabulary Anchor Gate

每個指定語詞逐一核對：`term_text`／occurrence／char indices 正確；`glyph_bbox`／`baseline_y` 來自目前最終文字層；`mark_bbox` 由 glyph anchor 派生；`text_layout_revision` 與目前排版一致。任一不成立 → `VOCAB_ANCHOR_FAIL` → FAIL。

### Vocabulary Reflow Gate

字型、字級、字距、行距、欄寬、換行、文字位置或內容只要變更，即視為 reflow。必須建立新的 `text_layout_revision` 並重算 glyph／mark bbox。沿用舊 anchor → `STALE_VOCAB_MARK_ANCHOR` → FAIL。

### Vocabulary Visual Gate

語詞使用 `UNDERLINE_HIGHLIGHT`；整句／金句才使用核准 `BACKGROUND_HIGHLIGHT`。Underline 在主要字框下方，淨距約字高 8–12%，厚度約 10–16%，只涵蓋指定語詞，標點預設排除，文字在上標記在下，不遮注音，同一 term color ID 一致。

有語詞標記頁必須全部通過：`VOCAB_ANCHOR_PASS`、`VOCAB_REFLOW_PASS`、`VOCAB_MARK_ALIGNMENT_PASS`、`VOCAB_MARK_SPAN_PASS`、`VOCAB_MARK_LAYER_PASS`、`TERM_COLOR_CONSISTENCY_PASS`。

像「要求標食宿，線卻出現在學生可以下面」或「女學堂的線跑到蔡阿信附近」屬 anchor failure，直接 FAIL。

## Gate D｜Idiom Application & Layout

有成語教學頁時逐頁檢查：

1. 成語、解釋、例句逐字正確；例句語意自然、通順，且真正使用該成語。
2. 成語為主要文字焦點；短解釋次之；例句具有足夠投影字級與獨立閱讀空間。
3. 不得固定退化成「成語／解釋／例句」三個同等卡片、三欄表或密集文字團。
4. 情境圖必須支援**例句中的實際用法／引申義**，不是只畫成語字面拆解。
5. 圖中的人物、動作、關係或事件必須能回到例句；看圖應能幫學生理解「為什麼這句可以用這個成語」。
6. 角色若參與例句，必須融入情境，不作無功能角落裝飾。
7. 一頁兩成語只有在同一故事線、前後事件、對照或共享場景有可見關係時成立；否則拆頁。

必須通過：
- `IDIOM_TEXT_PASS`
- `IDIOM_HIERARCHY_PASS`
- `IDIOM_EXAMPLE_READABILITY_PASS`
- `IDIOM_EXAMPLE_VISUAL_MATCH_PASS`
- `IDIOM_OBJECT_COMPOSITION_PASS`

只畫字面意思 → `IDIOM_LITERAL_IMAGE` → FAIL。
圖與例句人物／動作／語意不一致 → `IDIOM_EXAMPLE_VISUAL_MISMATCH` → FAIL。

例如例句是「媽媽耳提面命地提醒我出門前要檢查用品」，插圖就應支援媽媽反覆叮嚀孩子的情境；只畫耳朵、嘴巴或無關人物，不得通過。

## Gate E｜Renderer / Regression

老師不應再手動搬字、調底線、重畫語詞範圍，也不應逐頁提醒「例句要加大」「圖要配合造句」「成語、解釋、例句不要擠在一起」。若這些問題反覆出現，Renderer／Layout Contract 尚未完成，Quality Gate 不得 PASS。

代表頁若有語詞標記，必須實際測一次 reflow 後自動重算 anchor；有成語頁時，代表頁至少驗證一次成語、例句與情境圖的語意一致性。

Visual Drift、角色 DNA、canvas、閱讀安全區與實際成品仍須通過既有 V-MAX gates。

## 修復順序

Vocabulary：`重新 locate occurrence → 重算 glyph bbox → 重算 mark bbox → 調 clearance/stroke → 局部重畫標記`。

Idiom：`先核對成語與例句語意 → 定義例句人物／動作 → 重配 primary visual → 重平衡成語／解釋／例句層級 → 必要時拆頁`。

大底圖退化：回 Object Composition。

## Teacher Effort Gate

若教師仍需反覆提出「底線往左／往上」「字放大後線又跑掉」「圖跟造句對不起來」「例句太小」「三段文字擠在一起」，表示系統尚未完成應自動處理的版面／語意工作，不得 PASS。

## 核心金句

> 對位不是看起來差不多；標記必須有證據證明它綁在正確的字上。

> 成語圖不是裝飾：圖要讓學生看懂例句裡為什麼能用這個成語。