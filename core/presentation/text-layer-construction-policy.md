# V-MAX Text Layer Construction Policy 1.5

## 定位

本政策定義國語圖片式簡報的文字層施工方式。文字必須可精準校對，也必須和插圖、角色、物件、標記與閱讀動線共同形成教材畫面。

核心原則：

> 文字不是貼在圖片上的內容；文字是畫面中的教學物件。

> 依附文字的語詞標記必須綁定最終文字字框；底線跟著字走，不是字跟著底線走。

## 課文頁插圖最高原則

> **課文頁插圖只有一個最高原則：幫助理解課文。**

所有畫風、角色、場景、道具、構圖與裝飾選擇，都必須能說明它如何幫助學生理解當頁課文、段落、句子或關鍵詞；若不能提出這個對應，插圖不得使用。美感、豐富度、滿版效果與模型生成結果都不能凌駕課文理解與閱讀可讀性。

課文插圖不限定為單張靜態圖片；可採分格漫畫、日式漫畫風、連續鏡格、前後對照或事件流程畫面。只要每格都有課文理解功能、閱讀順序清楚，且不壓縮正文與語詞的投影可讀性，即屬合規的 Object Composition。

## 1. 三種視覺基準

### 正向基準：整合式路線／總覽頁
- 文字、人物、事件與路線共同形成閱讀順序。
- 插圖直接說明事件關係。
- 不依賴四欄、等尺寸卡片或固定左右欄。

### 可接受基準：情境主圖＋語詞標籤
- 一個連續主場景承載主要理解焦點。
- 語詞、感官圖示與短解釋靠近對應物件。
- 文字容器可以是手繪紙條、筆刷、標籤、泡泡或自然留白。

### 負向基準：分割式打字版
- 課文區與圖片區硬切、彼此不作用。
- 正文像逐行打字貼在背景。
- 圖片排成平均矩形格或卡片牆。
- 語詞解釋過小、脫離原文。

出現上述特徵 → `TYPED_TEXT_LAYOUT_FAIL`。

## 2. 文字元件施工

### 2.0 頁型分流

- `TEXT_READING_PAGE`：課文原文是閱讀主體，使用可控連續文字層；可以加局部語詞標記、圈選與提示，但不得破壞連續閱讀。
- `IMAGE_COMPOSED_PAGE`：語詞、句型、修辭、文意、形近字、多音字、成語、總覽與遷移等頁，使用 Verified Raster Text Components 與視覺物件共同合成。
- 只有 `IMAGE_COMPOSED_PAGE` 退化成普通浮動文字框、逐行打字、不透明白底文字框時才標記 `TYPED_TEXT_LAYOUT_FAIL`；不得誤判課文閱讀頁的正式文字層。

### 2.1 Verified Teaching Text

課文、語詞、注音、成語、句型、修辭、題目與提示先成為 Verified Teaching Text，再進文字渲染。圖片模型不得生成正式教材文字。

固定施工順序：

```text
Verified Teaching Text 確認
→ 選定並驗證實際字型
→ 完成最終文字排版
→ 建立 text_layout_revision
→ 校對字形、斷行、行距與大小
→ 建立需要的文字錨定標記
→ 與視覺物件共同合成
→ 扁平化與 QA
```

文字元件至少保存：

```yaml
text_component:
  component_id:
  exact_text:
  source_ref:
  visibility: STUDENT | TEACHER | QA
  font_role:
  font_file:
  font_size_pt:
  line_height:
  position:
  z_order:
  text_layout_revision:
  proof_status: UNCHECKED | PROOFED | EMBEDDED | VERIFIED
  repair_scope: LOCAL_COMPONENT_ONLY
```

字型選擇不在本檔硬綁單一 family；正式字型由 `skills/traditional-chinese-font-safety/SKILL.md` 的 font role、實際可取得字型、glyph coverage、臺灣字形與 fallback QA 決定。

### 2.2 Font Change = Reflow

下列任一改變都屬 text reflow：
- font family / font file
- 字級、字距、行距
- 欄寬、換行
- 文字 x/y 位置
- 文字內容

發生 reflow 時：
1. 更新 `text_layout_revision`。
2. 所有依附文字的舊 `glyph_bbox`、`baseline_y`、`mark_bbox` 全部 invalid。
3. 所有語詞標記、底線、圈選與精準文字 anchor 必須重新計算。
4. 不得把舊標記拖到新文字附近充當完成。

沿用舊 anchor → `STALE_TEXT_ANCHOR`；若為語詞標記則使用 `STALE_VOCAB_MARK_ANCHOR`。

### 2.3 段落文字不可碎片化

- 課文閱讀頁自然段／完整語意單位維持連續文字。
- 不得每句切成獨立卡片、標籤或等距小框。
- 局部語詞標記是 annotation layer，不應把原文拆碎。
- 課文過長時拆連續閱讀頁，不縮字、不改寫、不打散。

### 2.3.1 課文頁文字層規範

- 課文以自然段為單位完整呈現；保留教材原文、標點、語氣詞、引號與段落順序，不刪節、不改寫、不自行濃縮。
- 課文頁不得自行增加「第一段」或摘要、結論、教師講解等解釋性標題；可保留必要的 `①`、`②` 等段落數字記號，但不得取代原文。
- 課文是獨立、可調整的連續文字物件。正文不可直接生成在圖片裡，插圖、正文、語詞標記與投影片序號必須分層保存。
- 課文頁文字區優先確保教室投影可讀性；中年級以大字級、寬鬆行距與安全留白為優先。放不下時先重排，仍無法容納才依完整句子拆成連續頁。

### 2.4 文字與畫面物件關係

文字可依附木牌、旗幟、書頁、紙條、筆刷、對話泡泡、場景招牌或自然留白。文字容器由當頁 Object Composition 決定，不先套固定矩形。

若文字拿掉後插圖與教學理解完全沒變化，檢查是否只是裝飾貼字；若插圖拿掉後文字仍只是普通講義，檢查是否缺少圖文共同構圖。

## 3. Vocabulary Marking Contract

### 3.1 視覺語法

- 語詞定位 → `UNDERLINE_HIGHLIGHT`
- 整句／金句 → 經核准的 `BACKGROUND_HIGHLIGHT`

語詞標記是獨立 annotation object，不是文字本身，也不是烘焙進 AI 圖片的背景色塊。`UNDERLINE_HIGHLIGHT` 為既有資料層的相容 mark mode；課文頁的實際視覺必須使用 `PALE_BRUSH_BEHIND_TEXT`，不得以單純線條取代筆刷。

### 3.1.1 段落語詞解釋規範

- 語詞在原文的實際出現處直接標示，anchor 必須對齊該 occurrence；課文外不存在的詞語不得硬加到原文。
- 筆刷採淡色螢光筆／手繪筆刷效果，位於文字後方，不遮字；高度接近文字高度，左右只略微超出詞語，不形成大色塊。
- 段落旁解釋只呈現「詞語：解釋」，保持簡潔、適合四年級理解；不得再加底線、重複筆刷、複雜卡片、框線或標籤。
- 詞語解釋必須在同頁下方、側邊或對應留白，緊跟所屬段落；拆頁時跟著所屬句子或段落，不另成脫離課文的清單頁。

### 3.2 Glyph Anchor

語詞標記固定流程：

```text
最終文字排版
→ text_layout_revision
→ term_text + occurrence_index
→ line_id + start/end char index
→ glyph_bbox + baseline_y
→ mark_bbox
→ UNDERLINE_HIGHLIGHT
```

不得用肉眼估計 x/y，也不得沿用上一版 render 的底線座標。

同詞多次出現時必須指定 `occurrence_index`。無法唯一定位 → `VOCAB_ANCHOR_FAIL`。

### 3.3 Vocabulary Mark Geometry

- 課文頁 `visual_style` 必須為 `PALE_BRUSH_BEHIND_TEXT`；淡色筆刷位於中文字主要字框後方，文字層保持在上方。
- 筆刷高度接近文字高度，左右只略微超出詞語，不形成大色塊。
- span 只涵蓋指定語詞；標點預設排除。
- 資料層可保留 `MARK_BELOW_TEXT` 表示文字覆蓋在標記之上，但不得把它渲染成單純線條。
- 不得侵入注音安全區。
- 同一 `term_color_id` 在原文與詞義標示一致。
- 手繪感只能改筆刷邊緣，不能破壞 anchor/span 準確度；若 occurrence 不存在，不得建立標記。

### 3.4 Vocabulary QA

有語詞標記時必須通過：
- `VOCAB_ANCHOR_PASS`
- `VOCAB_REFLOW_PASS`
- `VOCAB_MARK_ALIGNMENT_PASS`
- `VOCAB_MARK_SPAN_PASS`
- `VOCAB_MARK_LAYER_PASS`
- `TERM_COLOR_CONSISTENCY_PASS`

穿字、標錯詞、跑到其他文字下方、遮注音 → `VOCAB_HIGHLIGHT_COLLISION`。

修正順序：重新定位 occurrence → 重算 glyph bbox → 重算 mark bbox → 調整 clearance/stroke → 局部重建標記。若正文正確，不得搬正文配合底線。

## 4. Object Composition 與插圖密度

渲染前使用 `OBJECT_COMPOSITION_PLAN`，不再以 `image_layout_plan` 作為主要施工契約。舊 `image_layout_plan` 僅可保留作兼容摘要。

Object Composition 至少區分：
- 文字／注音閱讀安全區
- 主場景物件
- supporting visual objects
- character objects
- annotation objects
- layer order
- planned overlaps
- protected zones

一般頁不得先生成完整大底圖再塞字。`MONOLITHIC_BACKGROUND_REGRESSION`、`IMAGE_DENSITY_OVERLOAD`、未核准 `IMAGE_COLLISION`、`VISUAL_BREATHING_FAIL` 均不得交付。

核准的 `SCENE_INTEGRATED`、`FOREGROUND_OVERLAP` 不因相切本身判碰撞。

## 5. 依頁型決定文字層

| 頁型 | 文字層策略 | 禁止退化 |
| --- | --- | --- |
| 課文總覽／路線圖 | 短句融入路線、旗幟、木牌與角色動線 | 固定四欄資訊卡 |
| 課文閱讀頁 | 連續原文主區＋局部理解插圖；指定語詞用 glyph-anchored 字下標記 | 每句一框、全文貼在背景上 |
| 語詞／感官頁 | 主場景＋物件錨定詞語／短解釋 | 語詞四格表、解釋卡片牆 |
| 文意理解頁 | 情境圖＋一個主問題＋少量視覺線索 | 考卷式題目框 |
| 句型／修辭頁 | 原句先出現，關鍵詞與視覺效果建立對應 | 名稱／定義／例句三欄 |
| 形近字／多音字頁 | 精準字形、注音與情境有可見關聯 | 圖片模型生成國字、平均四格 |
| 成語頁 | 先情境後成語，文字沿故事線出現 | 成語／解釋／例句固定三格 |

## 6. 密度與層級

- 一頁一個主要教學焦點。
- 一般情境頁最多約 3–4 個必要次要標籤；超過時優先刪減或拆頁。
- 課文閱讀頁正文是主體，投影等效字級以 36–40 pt 為目標。
- 語詞解釋靠近段落或對應情境，不縮成角落小字。
- 教師答案、講者備註、進度資訊留教師層。

### 6.1 投影片頁碼與段落記號規範

- 頁碼是整份簡報的實際投影片順序，例如 `P04`，放在整張投影片角落（通常右下角）；教材來源頁碼只放施工資料或備註，不放在學生畫面。
- 頁碼與段落記號可以有設計感，但必須分別回指 `sequence_index` 與 `section_id`，不能以圖案或顏色取代正式序號。
- 段落記號只作導覽輔助，不得新增課文標題、摘要或結論，也不得壓過正文安全區。

## 7. 文字層驗收

交付前至少通過：
1. `TEXT_PROOF_PASS`
2. `TEXT_OBJECT_RELATION_PASS`
3. `TEXT_DENSITY_PASS`
4. `TEXT_EMBEDDING_PASS`
5. `STUDENT_LAYER_PASS`
6. `OBJECT_COMPOSITION_PASS`
7. `TEXT_OBJECT_SEPARATION_PASS`
8. 適用時六項 Vocabulary Marking passes
9. Font Safety / glyph / Bopomofo QA

常用阻擋碼：
- `TYPED_TEXT_LAYOUT_FAIL`
- `TEXT_EMBEDDING_FAIL`
- `TEXT_OBJECT_SEPARATION_FAIL`
- `TEXT_OBJECT_DETACHED`
- `TEXT_DENSITY_OVERLOAD`
- `PARAGRAPH_FRAGMENTED`
- `ANSWER_LEAK`
- `TEACHER_LAYER_LEAK`
- `MONOLITHIC_BACKGROUND_REGRESSION`
- `VOCAB_HIGHLIGHT_COLLISION`
- `VOCAB_ANCHOR_FAIL`
- `STALE_VOCAB_MARK_ANCHOR`

## 核心金句

> 文字先排好，標記才知道要去哪裡。

> 字型一換、文字一 reflow，所有依附文字的舊標記都必須重新算。
