# V-MAX Knowledge Lab Ordering Policy 1.1

## 定位

本政策定義閱讀課中獨立 Knowledge Lab 與 `STEP 2.5 語文輻射` 的排序、分組、教師確認與 AI 教學價值判讀原則。

Knowledge Lab 不是附錄，也不是把所有字詞逐項講完；它只處理需要獨立建立辨識、比較、語意或遷移關係的內容。

核心原則：

> 先忠實讀取教材已提供的知識項目，再由 AI 做「教學價值判讀」，最後由教師篩選、替換與補充深教範圍。

> 教材原有 ≠ 一定深教；AI 推薦 ≠ 已決定。

---

## A. 預設內容範圍

Knowledge Lab 原則上處理：

- 生字
- 形近字／字群
- 多音字
- 成語

語詞不列為固定 Knowledge Lab 項目。語詞跟著課文處理，而且只教教師選定或確認的重點語詞。

`STEP 2.5 語文輻射` 可把上述內容整理成：

- `CORE`：建議配合課文理解／生字辨析正式處理
- `FLEX`：可短處理、可依班級時間調整
- `BONUS`：學生自選挑戰／延伸，不要求全部完成
- `LOW_PRIORITY`：教學價值較低或疑似雞肋，可由教師刪除

這些層級屬 AI 判讀與教學調度，不是教材來源標籤。

---

## B. 教材優先與教師篩選流程

生成 Knowledge Lab 前，系統先從教材／結構化轉錄來源完整讀取：

- 本課生字清單
- 教材已列出的形近字／字形辨析
- 本課多音字
- 教材已列出的成語

接著必須將兩個層次分開呈現：

### B1. 教材原有
忠實列出來源，不因 AI 判斷而靜默刪除。

### B2. AI 教學價值判讀
對每一個「形近字群／多音字／成語／其他語文活動」提供：

- `recommendation_index`：1–5
- `recommendation_level`
- `reason`：一句簡短理由
- `suggested_action`：深教／短辨析／Bonus／低優先

最後才由教師決定保留、刪除、補充或調整層級。

---

## C. 推薦指數｜Recommendation Index

`STEP 2.5 語文輻射` 中，推薦指數為**必填欄位**，不得省略。

### 量尺

- `5｜強烈推薦`：與本課課文、學生高混淆點、考評或高遷移價值高度相關，值得正式深教。
- `4｜推薦`：有明確辨析／理解價值，適合核心或短辨析。
- `3｜可選`：有學習價值，但非本課必要，可依班級／時間處理。
- `2｜低優先`：來源雖有，但教學增益有限，適合 Bonus 或簡短帶過。
- `1｜疑似雞肋`：與本課理解、常見錯誤或遷移關聯弱，AI 應主動提醒教師可刪除。

### 指數判斷至少考慮

```yaml
recommendation_dimensions:
  text_relevance: 0-2
  confusion_risk: 0-2
  transfer_value: 0-2
  assessment_value: 0-1
  cognitive_cost: 0 to -2
  redundancy_penalty: 0 to -1
```

最終不需要把計分細節全部展示給教師；教師端只需看到 `1–5 + 一句理由`。

### 禁止

- 因教材有列就全部給 4–5。
- 因被分到 `CORE` 就不顯示推薦指數。
- 因被分到 `BONUS` 就不做價值判讀。
- 用推薦指數取代 Teacher Decision。

---

## D. STEP 2.5 必填輸出格式

```yaml
step_2_5_language_radiation:
  status: WAITING_CONFIRMATION

  shape_near_groups:
    - item: 泳／永／詠
      provenance: SOURCE_TEXTBOOK | TEACHER_ADDED | AI_SUGGESTED
      recommendation_index: 5
      recommendation_level: 強烈推薦
      suggested_action: CORE_DEEP_DIVE
      reason: 與本課生字直接相關，字形近、讀音與詞義皆具辨析價值。
      teacher_decision: PENDING

  polyphonic_characters:
    - character: 溜
      source_usages: []
      extension_usages: []
      recommendation_index: 5
      recommendation_level: 強烈推薦
      suggested_action: CORE
      reason: 課文直接出現，且不同讀音對應不同語意與使用情境。
      teacher_decision: PENDING

  idioms:
    - item: 耳目一新
      provenance: SOURCE_TEXTBOOK
      recommendation_index: 4
      recommendation_level: 推薦
      suggested_action: BONUS_HIGH
      reason: 語意生活化且可遷移到口語與寫作，但非理解本課童詩的必要條件。
      teacher_decision: PENDING
```

若同一回合採「核心＋Bonus 自選」呈現，仍必須在每一項旁邊保留推薦指數。

例如：

```text
核心｜泳／永／詠　★★★★★ 5/5｜強烈推薦
理由：本課生字直接相關，且三字形近、語意差異清楚。

Bonus｜鷹／應　★★★☆☆ 3/5｜可選
理由：可做短辨析，但學生實際混淆風險低於其他字群。
```

---

## E. 生字區

### 目的
讓教師與學生掌握本課完整生字範圍，再決定哪些字值得深入處理。

### 規則
- 來源教材的生字完整保留在資料層。
- 生成前先提供生字清單給教師看，不由 AI 私下刪減。
- 並非每個生字都需要深教。
- AI 必須依易錯性、形近關係、構字價值、課文重要性等提供推薦指數。
- 教師確認後，只有被選中的字進入形近字／字群／字形深究。
- 不強制一字一頁。

---

## F. 形近字／字群區

### 目的
針對教師選定的重點生字，建立真正有價值的同場比較與字族關係。

### 核心觀念
教材原有形近字是「基準候選」，不是必教清單。教材有時提供的比較字可能關係較弱、實際辨析價值不高，或不足以形成學生容易記憶的字群；此時教師可以直接刪減、替換或補充更有教學價值的字群。

### 規則
- 每一組形近字都必須有 `recommendation_index 1–5` 與一句理由。
- 形近字／字群深究的入口是「教師選中的生字」，不是 AI 對所有生字自動輻射。
- 優先讀取教材已提供的形近字／字形辨析資料，完整呈現在教師確認介面中。
- 教材原有形近字不得因 AI 判斷而靜默刪除，但可由教師選擇不教。
- 教師可保留、刪除、替換或補充字群。
- 教師補充的字群可以成為最終主要教學組。
- AI 建議未經教師確認，不得進入最終教學腳本。
- 同一比較群盡量同頁／同場呈現，建立 Comparison Field。

### 來源標記
- `SOURCE_TEXTBOOK`
- `TEACHER_ADDED`
- `AI_SUGGESTED`

### 禁止
- 因教材有列就自動全部深教。
- AI 未經確認自行增加大量字族。
- 把來源與 AI 判讀混在同一欄。
- 為了頁數或視覺豐富硬做比較。

---

## G. 多音字區

### 目的
完整建立教材所列多音字的「讀音 × 語意 × 情境」關係。

### 規則
- 每個多音字必須有推薦指數；教材直接出現且讀音／語意辨析重要者通常為 4–5，但仍須依實際文本判斷。
- 多音字通常數量不多，教材已列者原則上全部保留。
- 不只列讀音，每個讀音都連到教材詞語或清楚可理解的使用情境。
- 若教材來源只教特定讀音與用法，以來源資料為主，不擅自擴充冷僻讀音。
- 教師可依學生程度補充或刪減。

---

## H. 成語區

### 目的
以教材原始來源為底，再依教師需要補充，讓學生看懂語意、辨識使用情境並遷移。

### 規則
- 每個成語都必須提供推薦指數與一句理由，即使它最終屬 Bonus。
- 推薦指數重點看：與課文語意連結、生活／寫作遷移、學生理解門檻、與其他成語是否重複。
- 先完整讀取教材／轉錄來源已列出的成語候選。
- 不由 AI 取代教材來源另造一套核心成語。
- 教師可依班級、課文重點、寫作遷移或既有學習狀況刪減或增加補充成語。
- 單一情境即可理解時，可用一張主情境圖。
- 有誤會、轉折、前後差異、因果時，優先使用 Sequential Narrative。
- 不預設每個成語都需要典故。

---

## I. 分組邏輯優先於頁數

Knowledge Lab 不以「教材列了幾個項目」直接等同頁數，而以教師確認後的教學範圍與認知關係決定。

`CORE / FLEX / BONUS / LOW_PRIORITY` 必須由推薦指數與 Teacher Intent 共同決定，不可只靠 AI 自動分類。

---

## J. 權限原則

### Source First
教材／轉錄來源決定「有哪些原始候選」。

### AI Judges Value
AI 必須提供：
- recommendation_index
- recommendation_level
- suggested_action
- one-line reason

### Teacher Selects & Curates
教師決定：
- 哪些生字深入
- 哪些形近字保留／替換／補充
- 哪些成語保留／補充
- CORE／FLEX／BONUS 是否調整

### AI Organizes
AI 負責將教師確認後的內容建立比較、情境與視覺關係。

AI 不得把「推薦」偷偷變成「已決定」。

---

## K. Director Engine 接軌

Director Engine 在完成段落閱讀 Acts 後：

1. 讀取教材原始生字／形近字／多音字／成語資料。
2. 輸出 `STEP 2.5 語文輻射 Teacher Selection Card`。
3. **先對所有候選產出推薦指數與一句理由。**
4. 教師選定需深教／短辨析／Bonus／刪除內容。
5. AI 依教師確認內容分 Knowledge Chunk。
6. 決定 Knowledge Lab 是否集中出現，或穿插在閱讀後的自然位置。
7. 最後才決定 Shot 數與版面。

若 `STEP 2.5` 沒有推薦指數，視為 `INCOMPLETE`，不得進入下一個 HOLD。

---

## L. Teacher Selection Card 必填格式

```yaml
teacher_selection_card:
  shape_near_groups:
    - item:
      provenance:
      recommendation_index:
      recommendation_level:
      suggested_action:
      reason:
      teacher_decision: PENDING

  polyphonic_characters:
    - item:
      recommendation_index:
      recommendation_level:
      suggested_action:
      reason:
      teacher_decision: PENDING

  idioms:
    - item:
      provenance:
      recommendation_index:
      recommendation_level:
      suggested_action:
      reason:
      teacher_decision: PENDING
```

此卡片是確認介面，不是教師必須逐欄填寫的表單。教師端應優先呈現簡潔的：

`項目｜推薦指數｜AI 判讀｜教師決策`

---

## 核心金句

> 教材告訴我們「有什麼」，AI 要告訴老師「值不值得教到什麼深度」，最後仍由老師決定。

> 推薦指數的目的不是替老師打分，而是讓老師不用自己重新判讀整份教材。