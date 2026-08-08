# V-MAX Language Modes Integration 1.0

## 定位

Language Modes Integration 定義國語課中的「聽、說、讀、寫」四種語言能力如何從課文、教材活動與教師意圖中自然長出來，並彼此串聯，而不是把閱讀當核心、其他三項當附加活動。

核心原則：

> 聽、說、讀、寫不是四個獨立單元，而是學生理解、表達與遷移同一份語言經驗的四種方式。

> 先讀懂課文與教材，再判斷哪一種語言模式值得被加深；不為了湊滿四項而硬做四種活動。

---

## A. 系統位置

```text
Text DNA / Textbook Activities / Teacher Intent
        ↓
Language Modes Scan
        ↓
Listening / Speaking / Reading / Writing Opportunities
        ↓
Teacher Confirmation
        ↓
Session Director + Learning Framework Overlay
        ↓
Activity / Evidence of Learning / Slide Architecture
```

Language Modes Integration 屬於國語課核心能力層，不只是可有可無的政策 Overlay。

---

## B. 四大語言模式

### 1. Listening｜聽

不是只有「老師講、學生聽」。

可包含：
- 聽讀與朗讀辨識
- 聽出語氣、節奏、重音、停頓
- 聽故事或說明後抓重點
- 聽同儕表達並回應
- 聽取不同觀點後比較
- 聽指令完成任務
- 聽辨詞義、音義或語境差異
- 聽後摘要、提問、判斷、轉述

對童詩、韻文、對話文、演說、故事等，Listening 應優先檢查其節奏與聲音價值。

### 2. Speaking｜說

不是只有「回答老師問題」。

可包含：
- 完整句回答
- 口頭敘事
- 看圖說話
- 轉述
- 說明理由與文本證據
- 比較與辯證
- 小組討論
- 角色對話／訪談
- 朗讀表演
- 口頭發表
- 即席表達
- 同儕回饋

重點是讓學生從「會說答案」進到「能清楚組織、說明、回應與修正」。

### 3. Reading｜讀

Reading 與 Reading Strategy Registry、Reading Taxonomy 深度串接。

可包含：
- 字詞與句義理解
- 文本訊息擷取
- 推論與找證據
- 段落與篇章結構
- 主旨與觀點
- 圖文整合
- 多文本閱讀
- 閱讀監控
- 評估與批判
- 閱讀遷移

不得把閱讀理解縮成只有答題。

### 4. Writing｜寫

不是只有作文課才出現。

可包含：
- 詞語／句型仿寫
- 短句改寫
- 句子擴寫／縮寫
- 摘要
- 語句重組
- 描寫
- 仿作
- 續寫
- 觀點表達
- 回應文本
- 寫給真實讀者
- 筆記與整理
- 小型創作到完整作品

寫作可由課文語句、結構、修辭、節奏、觀點、題材自然延伸，不必每課都做完整作文。

---

## C. Language Modes Scan｜每課掃描

完成 Text DNA 與教材活動整理後，AI 應掃描：

```yaml
language_modes_scan:
  listening:
    textbook_basis: []
    text_affordance: []
    teacher_extension_candidates: []
    recommended_depth: OFF | LIGHT | CORE | DEEP

  speaking:
    textbook_basis: []
    text_affordance: []
    teacher_extension_candidates: []
    recommended_depth: OFF | LIGHT | CORE | DEEP

  reading:
    textbook_basis: []
    text_affordance: []
    teacher_extension_candidates: []
    recommended_depth: OFF | LIGHT | CORE | DEEP

  writing:
    textbook_basis: []
    text_affordance: []
    teacher_extension_candidates: []
    recommended_depth: OFF | LIGHT | CORE | DEEP
```

### `textbook_basis`
教材原有活動或明確要求。

### `text_affordance`
課文本身自然提供的語言學習機會。

### `teacher_extension_candidates`
AI 只提出少量、具理由的延伸候選，等待教師確認。

### `recommended_depth`
描述本課值得投入的程度，不是四項都必須相同。

---

## D. 不追求四項平均

禁止：
- 每課固定設計一個聽、一個說、一個讀、一個寫活動。
- 為了形式完整，硬把不適合的語言模式塞進課堂。
- 把四項做成互不相干的任務。

允許：
- 某課以閱讀＋口說為主。
- 某課以聽覺節奏＋朗讀表達為主。
- 某課由閱讀深究一路走到仿寫。
- 某課閱讀比重高，但只有一次短寫作遷移。

核心是「依課文可供性與教材設計深化」，不是平均配給。

---

## E. 四項整合鏈

優先設計可自然串聯的學習鏈，而不是四個分離活動。

例：

```text
聽：聽兩種朗讀版本
  ↓
讀：找出造成節奏差異的詞句
  ↓
說：說明哪一種讀法更符合詩意，並指出證據
  ↓
寫：仿照節奏寫一小節
```

又例如：

```text
讀：找人物行動證據
  ↓
說：小組推論人物想法
  ↓
聽：聽別組觀點與證據
  ↓
寫：寫一句「我認為……因為……」
```

同一學習行動可同時服務多個語言模式。

---

## F. 與課文文體的關係

### 童詩／韻文
優先檢查：聽覺節奏、朗讀、意象口說、短詩仿寫。

### 故事／記敘文
優先檢查：聽故事重點、口頭轉述、事件結構、人物推論、續寫／改寫。

### 說明文
優先檢查：聽取資訊、口頭說明、結構閱讀、摘要、圖表轉述與說明寫作。

### 議論／觀點文本
優先檢查：聆聽立場、口頭論證、觀點證據閱讀、理由寫作與回應。

### 應用文／生活文本
優先檢查：情境聆聽、功能性口語、實用閱讀、真實任務寫作。

以上只是提示，不得取代對實際課文的分析。

---

## G. 與教材語文活動的關係

教材原有的語文活動必須先保留並辨識其主要 Language Mode。

例如：
- 朗讀 → Listening + Speaking
- 認識詞語 → Reading，必要時連 Speaking / Writing
- 句型練習 → Reading → Writing
- 口語表達 → Speaking + Listening
- 童詩仿作 → Reading → Writing，亦可加 Speaking 分享

AI 可提出深化方式，但不得把教師未確認的延伸冒充成教材原有要求。

---

## H. 與 Reading Strategy Registry 的關係

Reading Strategy 是「如何讀懂」；Language Modes 是「用什麼語言行動學習與表達」。

例如：
- 推論策略 + Speaking → 口頭說出推論與證據
- 摘要策略 + Writing → 寫一句核心摘要
- 視覺化策略 + Speaking → 說出腦中畫面
- 監控理解 + Listening → 聽到不懂處主動提出澄清問題

兩者可組合，不互相取代。

---

## I. 與 Discussion Protocol / ORID 的關係

ORID、六何法等決定討論與提問的進程；Language Modes 決定學生正在進行聽、說、讀、寫中的哪些語言行動。

例如 ORID：
- O：讀文本、聽同儕整理客觀訊息
- R：口頭表達感受
- I：閱讀證據後口頭推論
- D：寫下決定／遷移想法

不要求每次都完整跑四階段。

---

## J. 與數位／四學／PBL 的關係

數位工具與教學法可放大語言模式，但不是替代語言學習。

例如：
- 平板錄音 → Speaking + Listening 自我檢核
- 共編文件 → Reading + Writing + Collaborative Learning
- 四學 → 可安排個人閱讀、組內口說、組間聆聽、教師導學
- PBL → 真實資料閱讀、訪談聆聽、提案口說、成果寫作

每次使用都要回答：學生的語言能力因此多長了什麼？

---

## K. Evidence of Learning｜學習證據

四項能力都應盡量留下可觀察證據，但不一定是紙筆測驗。

Listening 可觀察：
- 是否抓到重點
- 是否能回應他人
- 是否聽出語氣／訊息差異

Speaking 可觀察：
- 是否表達完整
- 是否有條理
- 是否能提出證據
- 是否能回應與修正

Reading 可觀察：
- 是否找得到證據
- 是否能推論／整合／評估
- 是否能監控理解

Writing 可觀察：
- 是否能把學到的語言工具遷移到自己的句子或作品
- 是否能依目的組織內容
- 是否能修正與改寫

---

## L. Quality Gate

每課檢查：
- 是否只重閱讀而忽略其他語言模式？
- 聽與說是否真的由學生進行，而不是只有老師講、學生答？
- 寫作是否由課文語言或結構自然延伸？
- 四項是否有自然串聯，而不是各做一個活動湊數？
- 教材原有活動是否被完整辨識？
- 教師補充與 AI 建議是否清楚標來源？
- 是否有一種模式被硬塞進不適合的文本？
- 活動是否真的增加理解與表達，而不是只增加流程？

---

## 核心金句

> 國語課不是只有把課文讀懂，而是讓孩子能聽懂、說清楚、讀深入、寫出自己的語言。

> 聽說讀寫不是四個勾選框，而是同一段語言學習旅程的四種移動方式。
