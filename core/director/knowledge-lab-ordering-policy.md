# V-MAX Knowledge Lab Ordering Policy 1.3

## 定位

本政策定義閱讀課中獨立 Knowledge Lab 與 `STEP 2.5 語文輻射` 的排序、分組、教師確認、AI 教學價值判讀，以及「課前預習單語文選擇」原則。

Knowledge Lab 不是附錄，也不是把所有字詞逐項講完；它只處理需要獨立建立辨識、比較、語意或遷移關係的內容。

核心原則：

> 先忠實讀取教材已提供的知識項目，再由 AI 做「教學價值判讀」，最後由教師篩選、替換與補充深教範圍。

> STEP 2.5 不只決定正式教學內容，也要同步決定哪些形近字／多音字值得先進入預習單。

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
- 同冊前課已確認的預習單形近字／多音字覆蓋紀錄

接著必須將三個層次分開呈現：

### B1. 教材原有
忠實列出來源，不因 AI 判斷而靜默刪除。

### B2. AI 教學價值判讀
對每一個「形近字群／多音字／成語／其他語文活動」提供：

- `recommendation_index`：1–5
- `recommendation_level`
- `reason`：一句具體理由
- `suggested_action`：深教／短辨析／Bonus／低優先

### B3. 預習單選擇判讀
對形近字群與多音字額外提供：

- `prestudy_recommendation`
- `volume_duplication_status`
- `volume_history`
- `prestudy_reason`

AI 必須主動判斷「值不值得先放進預習單」以及「同一冊是否已正式出現過」，不把查重工作交給教師。

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

最終不需要把計分細節全部展示給教師；教師端需看到 `1–5 + 具體理由`。

### 禁止

- 因教材有列就全部給 4–5。
- 因被分到 `CORE` 就不顯示推薦指數。
- 因被分到 `BONUS` 就不做價值判讀。
- 用推薦指數取代 Teacher Decision。

---

## D. 快速教師決策代號｜Decision Codes

為降低確認負擔，`STEP 2.5` 採「數字看 AI 推薦，字母回教師決策」的雙軌代號。

### 教學決策

- `A｜深教`
- `B｜短辨析`
- `C｜Bonus`
- `D｜刪除`
- `E｜調整`

### 預習單決策

- `P1｜預習核心`：正式放入預習單，學生需辨識／比較／書寫／圈選。
- `P2｜預習短看`：以小區塊快速辨識，不占主要書寫空間。
- `P3｜本課不放`：可留在簡報／Knowledge Lab，但不進預習單。
- `PX｜冊內已出現`：同字群／同多音辨析本冊前課已正式出現，預設不重複。
- `PE｜調整`：教師要新增、替換、改題型或例外重複。

### 快速回覆

若 AI 推薦都可接受：

```text
R
```

若只微調例外：

```text
R 2C/P2 5PE：補「坨」
```

代表：其他全部沿用；第 2 項教學改 Bonus、預習單改短看；第 5 項調整預習單內容。

---

## E. 同冊去重｜Volume-level Deduplication

完整細則以 `core/worksheet/prestudy-language-selection-policy.md` 為準。

### 核心規則

1. 同一字群在同一冊原則上只在預習單正式出現一次。
2. 字群比對採正規化，不因順序不同而視為不同群。
3. 後課若只是前課完整字群的子集合，視為已覆蓋，除非新增了重要比較關係。
4. 多音字以「字 + 讀音／語意對比」查重，不只看單一字。
5. `PX` 不等於永不再教；可在簡報、口頭、考前整理中快速喚回。
6. 前次若只有 `P2`，後課因教學價值升高可建議升成 `P1`，但需說明理由。
7. 只有教師確認的 `P1/P2` 才寫入本冊正式覆蓋紀錄；AI 候選不算。

---

## F. STEP 2.5 教師端顯示格式

形近字／多音字必須同時顯示「教學推薦」與「預習單推薦」。

```text
01｜泳／永／詠　★★★★★ 5/5｜強烈推薦
理由：本課生字直接相關，三字形近，且字義差異清楚。
教學建議：A 深教｜CORE
預習單：P1 預習核心
冊內紀錄：本冊尚未出現

02｜般／搬／船　★★☆☆☆ 2/5｜低優先
理由：教材雖有列，但本課實際混淆與遷移價值較低。
教學建議：D 刪除；若教師仍想保留，可改 C Bonus
預習單：P3 本課不放
冊內紀錄：—
```

若冊內重複：

```text
08｜永／詠　★★★★☆ 4/5｜推薦
理由：本課仍有辨析價值，但「泳／永／詠」已於第 1 課預習單正式出現。
教學建議：B 短辨析
預習單：PX 冊內已出現
冊內紀錄：第 1 課｜泳／永／詠
```

成語仍顯示詳細推薦與教學決策，但不強制納入此「冊級形近字／多音字預習單去重」規則。

---

## G. STEP 2.5 必填資料格式

```yaml
step_2_5_language_radiation:
  status: WAITING_CONFIRMATION
  volume_id:

  decision_legend:
    A: 深教
    B: 短辨析
    C: Bonus
    D: 刪除
    E: 調整
    P1: 預習核心
    P2: 預習短看
    P3: 本課不放
    PX: 冊內已出現
    PE: 預習單調整

  items:
    - id:
      category: SHAPE_NEAR | POLYPHONIC | IDIOM | OTHER
      item:
      provenance:
      recommendation_index:
      recommendation_level:
      ai_suggested_decision:
      reason:
      teacher_decision: PENDING
      prestudy:
        applicable: true | false
        ai_recommendation: P1 | P2 | P3 | PX
        volume_duplication_status: NEW | COVERED | PARTIAL_OVERLAP | NEW_RELATION
        volume_history: []
        reason:
        teacher_decision: PENDING
```

若形近字／多音字沒有 `prestudy` 判讀，STEP 2.5 視為 `INCOMPLETE`。

---

## H. AI 的責任

AI 不只提供候選，還必須主動做到：

- 比較本冊前課已確認的字群／多音字紀錄
- 判斷重複、部分重疊或新關係
- 根據預習單空間與教學價值選出 P1/P2/P3/PX
- 說明為什麼值得或不值得進預習單
- 優先避免同一冊重複占用預習單空間

教師的主要工作是看推薦後微調例外，不需要自己維護去重表。

---

## I. Director Engine 接軌

Director Engine 在完成段落閱讀 Acts 後：

1. 讀取教材原始生字／形近字／多音字／成語資料。
2. 讀取同冊 `Volume Language Coverage`。
3. 輸出 `STEP 2.5 語文輻射 Teacher Selection Card`。
4. 對所有候選產出推薦指數、詳細理由與教學建議。
5. 對形近字／多音字再產出預習單 P1/P2/P3/PX 建議與冊內查重紀錄。
6. 教師主要採 `R` 沿用，僅微調例外。
7. AI 依確認內容分 Knowledge Chunk，並同步輸出本課預習單語文項目。
8. 教師確認的 P1/P2 寫回本冊 Coverage Registry。
9. 才進入後續預習單版面與完整 Slide Architecture。

---

## 核心金句

> 教材告訴我們「有什麼」，AI 要告訴老師「值不值得教到什麼深度、值不值得先放進預習單」，最後仍由老師決定。

> 預習單不是每課重新塞一批字，而是一冊逐課長出來的語文學習地圖。
