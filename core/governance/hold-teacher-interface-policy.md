# V-MAX HOLD Teacher Interface Policy 1.1

## 定位

本規則定義所有 V-MAX `HOLD / WAITING_CONFIRMATION` 階段的共同教師介面。

核心原則：

> HOLD 是給老師做決策的，不是給系統展示資料結構的。

> Machine payload 可以存在，但不得先於或取代教師可讀確認卡。

> AI 要把判斷做重，把老師的操作做輕。

---

## A. 適用範圍

本規則適用所有需要教師確認的階段，包括但不限於：

- STEP 1 教材定錨
- AI 教學價值判讀
- STEP 2.5 語文輻射
- Teacher Intent Lock
- Lesson Map
- 補充內容／學習框架候選
- Session Map
- Lesson Visual Map Strategy
- Scenario Wrapper
- Character Topology / Cast
- Knowledge Lab Selection
- 代表頁驗證
- 正式輸出前 Quality Gate 需要教師決策之處

---

## B. 教師介面優先

當狀態為 `WAITING_CONFIRMATION` 時，輸出順序必須是：

1. `Teacher Confirmation Card`：人類可讀摘要／分析／推薦。
2. 明確標示目前 HOLD 與可做的教師決策。
3. 等教師確認或微調。
4. Machine JSON / YAML / schema 只在系統內保留，或教師明確要求時再顯示。

禁止：

- 只輸出 JSON / YAML / vocabulary[] / schema。
- 先貼大段 machine payload，再要求教師確認。
- 用 internal key（如 `mode`, `basicInfo`, `visualStructureRecommendation`）取代教師語言。
- 因為後續 NotebookLM / Renderer 需要結構化資料，就把結構化資料當 HOLD UI。

若違反上述規則，該 HOLD 狀態標記 `MISSING_INTERFACE`，不可直接往下一階段。

---

## C. 教師確認卡的最低要求

每張確認卡至少回答：

- 現在確認的是什麼？
- AI 根據哪些教材來源／既有規則判讀？
- AI 的建議或分析是什麼？
- **為什麼這樣建議？**
- 哪些內容仍是教師決策？
- 教師如何用最少輸入完成確認／微調？

若該步只是資料定錨，不能加入後段才應決定的 Scenario / Character / Style / Layout。

若該步是 AI 教學價值判讀，不能只給分類結果；必須有足以讓教師判斷的理由、取捨與風險。

---

## D. Recommendation-first｜推薦先完整，操作再簡化

教師端預設流程：

```text
AI 先分析與推薦
→ 說明理由與教學價值
→ 教師看得懂差異
→ 教師只改例外
```

不得反過來要求教師先選大量 A/B/C 選項，再由 AI 補理由。

### 可接受

- 「這組形近字 5/5，因為……；建議深教。」
- 「這個成語 2/5，和本課連結弱，建議 Bonus／可刪。」
- 「這一詩節最大的價值是聲音與畫面的交錯，不建議硬塞另一個句型頁。」
- 「這一段應保留推論空間，先找證據再揭示。」

### 不可接受

- 只有 `CORE / FLEX / BONUS`，沒有理由。
- 只有 `A/B/C/D/E`，沒有分析。
- 教師確認 STEP 1 後直接收到「52 頁帳本」。
- 把每一段都做成完全相同的五步模板，再請教師確認。

---

## E. 快速決策原則

AI 應先完整分析，再降低教師輸入成本。

可使用：

- `R`：其餘沿用 AI 推薦
- A/B/C/D/E：當該模組已定義決策代號時
- P1/P2/P3/PX/PE：預習單語文選擇
- 短句式例外修改

不得為了讓輸入變短而刪掉教師判斷所需的分析理由。

核心：

> 推薦要完整，操作要簡單。

---

## F. HOLD 不得跨階段

教師在某個 HOLD 說「確認／好／可以」時，只代表**當前決策被確認**，不代表 AI 可以跳過中間流程。

例如：

- HOLD 1 確認後，下一步應進 AI 教學價值判讀，而不是頁數帳本。
- STEP 2 / STEP 2.5 確認後，應進 Teacher Intent Lock / Lesson Map，而不是直接逐頁腳本。
- Session Map 尚未成立前，不得宣告完整教學版總頁數。

若跳過主流程中介階段，標記 `SKIPPED_DECISION_LAYER`。

---

## G. 教師主權的實際判定

好的 HOLD 應讓教師感覺自己在「導演」：

- AI 主動看懂教材與學生學習需要。
- AI 提出少量、有理由的判斷。
- 教師可以接受大部分，只改真正不同意的部分。
- 教師不用替 AI 補回它漏掉的教學亮點。

若教師主要工作變成：

- 幫 AI 找漏掉的內容
- 逐項替 AI 做初步分類
- 因 AI 已鎖頁數而被迫接受結構
- 反覆修正機械模板

則該 HOLD 雖形式上有確認點，仍視為 `TEACHER_EFFORT_FAIL`。

---

## H. TEST_FREEZE 相容

在 `TEST_FREEZE` 中，若某 HOLD 沒有依此政策顯示：

- 記錄 `MISSING_INTERFACE / SKIPPED_DECISION_LAYER / TEACHER_EFFORT_FAIL`
- 停在原 HOLD
- 不自行修改系統

只有教師明確要求修正／更新規則時才寫回 Core。

---

## I. Machine Payload 原則

Machine payload 是 downstream contract，不是 Teacher UI。

它可以用於：

- Source Master
- NotebookLM / Gemini / Renderer Adapter
- regression test
- programmatic processing

但教師確認階段預設不展示，除非：

1. 教師明確要求看 JSON/YAML；或
2. 正在做 schema/debug 測試。

---

## 核心金句

> 資料結構給系統讀；確認卡給老師做決策。

> HOLD 的價值是降低教師決策負擔，不是把內部資料格式丟給老師。

> AI 要把判斷做重，把老師的操作做輕。

> 教師確認的是方向與例外，不是替 AI 補完整套教學設計。