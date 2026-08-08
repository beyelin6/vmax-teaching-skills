# V-MAX HOLD Teacher Interface Policy 1.0

## 定位

本規則定義所有 V-MAX `HOLD / WAITING_CONFIRMATION` 階段的共同教師介面。

核心原則：

> HOLD 是給老師做決策的，不是給系統展示資料結構的。

> Machine payload 可以存在，但不得先於或取代教師可讀確認卡。

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
- 哪些內容仍是教師決策？
- 教師如何用最少輸入完成確認／微調？

若該步只是資料定錨，不能加入後段才應決定的 Scenario / Character / Style / Layout。

---

## D. 快速決策原則

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

## E. TEST_FREEZE 相容

在 `TEST_FREEZE` 中，若某 HOLD 沒有依此政策顯示：

- 記錄 `MISSING_INTERFACE`
- 停在原 HOLD
- 不自行修改系統

只有教師明確要求修正／更新規則時才寫回 Core。

---

## F. Machine Payload 原則

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