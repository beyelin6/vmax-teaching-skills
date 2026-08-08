# V-MAX Recognition-only Character Policy 1.1

## 定位

本政策定義 V-MAX 對「認讀字」的教材身分判定、來源核對、資料保存與後續教學處理。

核心原則：

> 認讀字不是由 AI 依版面猜出來的，也不是「沒有方格的字」就自動算認讀字。

> 認讀字 = 教材在本課生字系統中，明確列為需要識讀、但不屬正式書寫生字的字。

> 課文下方小字與課文後方獨立生字表必須交叉核對；版面線索只能輔助辨識，不能單獨決定身分。

---

## A. 教材生字系統的雙來源核對

STEP 1 教材定錨時，至少檢查本課教材的兩個位置：

1. **課文頁下方的小字生字標示**
   - 這是課文閱讀時的生字提示來源。
   - 不得因字小、位於頁底、沒有書寫格而漏讀。

2. **課文後方獨立的生字表／生字教學頁**
   - 用來確認本課完整正式生字系統。
   - 需辨認教材是否區分正式書寫生字與認讀字。

正式流程：

```text
課文頁下方小字
↓
課後獨立生字表／生字教學頁
↓
雙來源交叉核對
↓
正式生字／認讀字身分判定
```

若兩處不一致，不得自行取其中一處當唯一真值；必須保留差異並進 HOLD 1。

---

## B. Recognition-only 正式定義

只有當教材本身在本課生字系統中，明確將某字列為「識讀要求、但非正式書寫生字」時，才判定為認讀字。

### 可以作為辨識線索，但不能單獨定義

下列現象只能當作 layout clue：

- 無書寫方格
- 字體較小
- 只出現在課文頁底
- 與正式生字分區排列
- 教材使用「認讀」「只認不寫」或其他功能相近標籤

其中「無方格」不是充分條件。

### 不得誤判為認讀字

以下都不能只因教材中出現，就被判為認讀字：

- 課文中出現但不在本課生字系統中的一般字
- 形近補充字／比較字
- AI 額外補充字
- 成語中的延伸字
- 偏旁識字活動中的示例字
- 沒有方格、但教材沒有把它列入本課認讀系統的字

---

## C. Source-driven Presence Detection

STEP 1 必須留下：

```yaml
recognition_only_characters:
  status: PRESENT | N/A_SOURCE_NOT_PRESENT | UNCERTAIN_SOURCE_LABEL | SOURCE_CONFLICT
  source_label:
  items: []
  textbook_footer_evidence: []
  posttext_character_table_evidence: []
  cross_check_status: MATCH | PARTIAL_MATCH | CONFLICT | NOT_APPLICABLE
  provenance:
```

### PRESENT
只有雙來源核對後，教材身分清楚時才成立。

- 完整保留全部認讀字。
- 與正式「我會寫字／正式生字」分開記錄。
- 不得因沒有方格而漏掉。

### N/A_SOURCE_NOT_PRESENT
兩個教材位置均未顯示認讀字身分時：

- 明確記錄 `N/A_SOURCE_NOT_PRESENT`。
- 不建立虛構認讀字清單。
- 不為了流程完整硬生認讀字模組。

### UNCERTAIN_SOURCE_LABEL
教材有特殊標示，但無法明確判定功能時：

- 保留原標籤與頁面位置。
- 進 HOLD 1。
- 不自行把一般生字改判為認讀字。

### SOURCE_CONFLICT
課文頁下方小字與課後獨立生字表對字的身分或清單不一致時：

- 完整保留兩邊證據。
- 標記 `SOURCE_CONFLICT`。
- 進 HOLD 1 讓教師確認。
- 不得靜默採其中一邊。

---

## D. 年級不是 Source Truth

V-MAX 可保存年級經驗，但不得將它改寫成來源硬規則。

- 某年級常見認讀字，只代表 AI 要記得檢查。
- 某冊目前未出現認讀字，不代表未來同年級、其他出版社或改版教材一定沒有。

核心：

> 年級經驗可以提醒檢查，不能代替教材生字系統做身分判定。

---

## E. 與正式生字的分工

```text
正式生字／我會寫字
→ 需要識寫與教材規定的形音義處理

認讀字
→ 以辨識、讀音、基本字義與課文語境理解為主
→ 不自動要求完整書寫教學
```

不得：
- 把認讀字混入正式生字數量後要求同規格書寫。
- 因認讀字不寫就從 Source Master 中刪掉。
- 把比較字／補充字／偏旁識字示例誤判為認讀字。

---

## F. Knowledge Lab 條件式處理

只有 `status: PRESENT` 時，Knowledge Lab 才處理認讀字。

預設教學目的：
- 字音辨識
- 基本字義／語境
- 必要的字形辨認線索
- 與課文閱讀直接相關的識讀

認讀字不自動進：
- 每字獨立深教頁
- 完整筆順／書寫練習
- 形近字深教
- 多音字深教

若 `N/A_SOURCE_NOT_PRESENT`：
- Knowledge Lab 記錄 N/A。
- 不生成認讀字頁面或活動。

若 `SOURCE_CONFLICT` 或 `UNCERTAIN_SOURCE_LABEL`：
- 不得進入正式認讀字教學生成。
- 先停在 HOLD 1 完成來源裁決。

---

## G. STEP 1 Teacher Card

HOLD 1 教師可讀卡需有一列：

```text
認讀字：
- 有：列出教材全部認讀字
- 無：本課教材生字系統未列認讀字（N/A）
- 不確定：列出教材原標籤與待確認點
- 來源衝突：列出「課文下方小字」與「課後生字表」的差異
```

並應簡要顯示：

```text
來源核對：課文頁下方小字 ✓／課後獨立生字表 ✓
```

不得因「沒有」就整欄消失，否則無法分辨已檢查為無，還是 AI 漏讀。

---

## H. Regression Failures

以下任一情況為 FAIL：

- 只讀課後生字表，漏掉課文下方小字。
- 只讀課文下方小字，未核對課後生字表。
- 把「無方格」直接當作認讀字定義。
- 來源有認讀字，但 STEP 1 沒有列出。
- 來源沒有認讀字，AI 卻自行補認讀字。
- 形近補充字／比較字被誤標為認讀字。
- 課文中一般字因未列在正式生字表就被誤標為認讀字。
- 兩個教材位置有衝突卻被靜默合併。
- `N/A_SOURCE_NOT_PRESENT` 後仍生成認讀字教學頁。

分類：

`RECOGNITION_CHAR_DROPPED / RECOGNITION_CHAR_HALLUCINATED / RECOGNITION_CHAR_MISCLASSIFIED / RECOGNITION_SOURCE_CROSSCHECK_MISSING / RECOGNITION_SOURCE_CONFLICT_IGNORED`

---

## 核心金句

> 認讀字看教材生字系統，不看方格猜。

> 課文下方小字與課後生字表都要看，兩邊核對後才定身分。

> 「沒有」也要留下已檢查的證據；N/A 不是漏掉。
