# V-MAX Recognition-only Character Policy 1.0

## 定位

本政策定義「認讀字／只認不寫／無方格字」在 V-MAX 中的來源判定、資料保存與後續教學處理。

核心原則：

> 認讀字採來源驅動判定，不以年級預設有或沒有。

> 有就完整保留，沒有就明確標記 N/A；AI 不得因熟悉某年級而漏掉，也不得因系統有模組就自行補造。

---

## A. Source-driven Presence Detection

STEP 1 教材定錨時，必須獨立檢查來源是否存在：

- 認讀字
- 只認不寫
- 無方格字
- 教材以其他名稱標示但功能相同的 recognition-only characters

判定狀態：

```yaml
recognition_only_characters:
  status: PRESENT | N/A_SOURCE_NOT_PRESENT | UNCERTAIN_SOURCE_LABEL
  source_label:
  items: []
  provenance:
```

### PRESENT
來源明確列出認讀字時：
- 完整保留全部項目。
- 與正式「我會寫字／生字」分開記錄。
- 不得因沒有書寫方格而漏掉。

### N/A_SOURCE_NOT_PRESENT
來源沒有列出認讀字時：
- 明確記錄 `N/A_SOURCE_NOT_PRESENT`。
- 不建立虛構的認讀字清單。
- 不為了流程完整硬生一個認讀字教學模組。

### UNCERTAIN_SOURCE_LABEL
若教材標示方式不清楚：
- 保留來源截取／原文標籤。
- 進 HOLD 1 說明不確定處。
- 不自行把一般生字改判為認讀字。

---

## B. 年級不是 Source Truth

V-MAX 可保存教學經驗作為觀察，但不得把年級經驗改寫成來源硬規則。

例如：
- 一、二、三年級教材常可能出現認讀字，仍須逐課／逐冊依來源確認。
- 目前四上來源若未出現認讀字，該冊可標記 `N/A_SOURCE_NOT_PRESENT`。
- 未來四下、其他出版社、改版教材或其他年級仍必須重新讀來源，不沿用「四年級沒有認讀字」的假設。

核心：

> 年級經驗可以幫助 AI 注意檢查，不能代替教材來源做判定。

---

## C. 與正式生字的分工

認讀字與正式生字必須分開：

```text
正式生字／我會寫字
→ 需要識寫與教材規定的形音義處理

認讀字／只認不寫
→ 以辨識、讀音、語境理解為主
→ 不自動要求完整書寫教學
```

不得：
- 把認讀字混入正式生字數量後要求同規格書寫。
- 因認讀字不寫就從 Source Master 中刪掉。
- 把偏旁識字活動誤判成認讀字清單。

---

## D. Knowledge Lab 條件式處理

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

若某認讀字本身有高價值形近或多音關係，AI 可另提教學建議，但需標示這是 `AI_SUGGESTION`，不是因「認讀字身分」自動升級。

若 `N/A_SOURCE_NOT_PRESENT`：
- Knowledge Lab 記錄 N/A。
- 不生成認讀字頁面或活動。

---

## E. STEP 1 Teacher Card

HOLD 1 教師可讀卡需有一列：

```text
認讀字：
- 有：列出教材全部認讀字與來源標籤
- 無：本課來源未列認讀字（N/A）
- 不確定：列出教材原標籤與待確認點
```

不得因「沒有」就整欄消失，否則後續無法分辨是已檢查為無，還是 AI 漏讀。

---

## F. Regression Failures

以下任一情況為 FAIL：

- 來源有認讀字，但 STEP 1 沒有列出。
- 無方格認讀字被誤當成資料缺漏而刪除。
- 來源沒有認讀字，AI 卻自行補認讀字。
- 因過去經驗直接宣告某年級一定有／一定沒有認讀字。
- 偏旁識字活動被誤判為認讀字。
- `N/A_SOURCE_NOT_PRESENT` 後仍生成認讀字教學頁。

分類：

`RECOGNITION_CHAR_DROPPED / RECOGNITION_CHAR_HALLUCINATED / GRADE_ASSUMPTION_OVERRIDE / RECOGNITION_CHAR_MISCLASSIFIED`

---

## 核心金句

> 認讀字看教材，不看年級猜。

> 「沒有」也要留下已檢查的證據；N/A 不是漏掉。
