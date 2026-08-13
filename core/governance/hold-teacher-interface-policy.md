# V-MAX HOLD Teacher Interface Policy 1.4

## 定位

本規則定義所有 V-MAX `HOLD / WAITING_CONFIRMATION` 階段的共同教師介面，並強制套用 `core/ui/teacher-review-view-contract.md`。

核心原則：

> HOLD 是給老師做決策的，不是給系統展示資料結構的。

> Machine payload 可以存在，但不得先於或取代教師可讀確認卡。

> AI 要把判斷做重，把老師的操作做輕。

> 一次確認，只往前走一關。

---

## A. 適用範圍

本規則適用所有需要教師確認的階段，包括但不限於：

- STEP 1 教材定錨 → HOLD 1
- STEP 2 AI 教學價值判讀 → HOLD 2
- STEP 2.5 語文輻射 → HOLD 2.5
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
3. 明確寫出「確認後唯一下一步」。
4. 等教師確認或微調。
5. Machine JSON / YAML / schema 只在系統內保留，或教師明確要求時再顯示。

禁止：

- 只輸出 JSON / YAML / vocabulary[] / schema。
- 顯示內部狀態欄位、空白程式碼框或未經教師要求的 Machine Payload。
- 先貼大段 machine payload，再要求教師確認。
- 用 internal key 取代教師語言。
- 因 downstream 需要結構化資料，就把結構化資料當 HOLD UI。
- 在 HOLD 結尾列出多個後續階段，暗示一次確認可連跑。

若違反上述規則，該 HOLD 狀態標記 `MISSING_INTERFACE`，不可直接往下一階段。若畫面以大段 raw JSON／YAML 為主，另標記 `RAW_SCHEMA_DUMP / TEACHER_INTERFACE_OVERLOAD`。

---

## C. 教師確認卡的最低要求

每張確認卡至少回答：

- 現在確認的是什麼？
- AI 根據哪些教材來源／既有規則判讀？
- AI 的建議或分析是什麼？
- **為什麼這樣建議？**
- 哪些內容仍是教師決策？
- 教師如何用最少輸入完成確認／微調？
- 確認後唯一會進哪一階段？

若該步只是資料定錨，不能加入後段才應決定的 Scenario / Character / Style / Layout，也不能先決定「每段都怎麼教」。

若該步是 AI 教學價值判讀，不能只給分類結果；必須有足以讓教師判斷的理由、取捨與風險，並在 `HOLD 2` 停下來。

---

## D. Recommendation-first｜推薦先完整，操作再簡化

教師端預設流程：

```text
AI 先分析與推薦
→ 說明理由與教學價值
→ 教師看得懂差異
→ 教師只改例外
→ 停在當前 HOLD
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
- STEP 2 做完後直接說「下一步進課程結構與簡報模組配置」。

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

## F. STEP 2.5 專用停等格式

STEP 2.5 的 Teacher Confirmation Card 只包含形近字、多音字、教材詞語／成語審核表、待確認項目與 AI 推薦理由。每個項目須顯示 `[教材已確認] / [教育部辭典已核對] / [AI 建議，待教師確認] / [尚待教材來源核對]` 中適用的狀態。

本階段最後固定停在：

`⏸ HOLD 2.5｜請回覆「確認」或指出修改項目；確認後唯一下一步為 STEP 2.6。`

不得在同一回覆展開各段／詩節教學，不得宣布進入其他階段。來源未完成或字形／讀音有疑點時停在 STEP 2.5，不得把項目標示為已鎖定。

## G. HOLD 不得跨階段｜Single-stage Advance

教師在某個 HOLD 說「確認／好／可以」時，只代表**當前決策被確認**，且只解鎖主流程中**緊接的一個正式階段**。

### 必守鏈條

```text
HOLD 1
→ STEP 2
→ HOLD 2
→ STEP 2.5
→ HOLD 2.5
→ STEP 2.6
→ HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map
```

因此：

- HOLD 1 確認後，只做 STEP 2，然後停在 HOLD 2。
- HOLD 2 確認後，只做 STEP 2.5，然後停在 HOLD 2.5。
- HOLD 2.5 確認後，只做 STEP 2.6，然後停在 HOLD 2.6。
- HOLD 2.6 確認後，才進 Teacher Intent Lock；不得直接開始 Slide Architecture。
- Session Map 尚未成立前，不得宣告完整教學版總頁數。

若一個「確認」後連續跑過兩個以上需教師介入的決策層，標記：

`RUNAWAY_WORKFLOW / SKIPPED_HOLD / STAGE_LEAP`

---

## H. 下一步指向驗證

每個 HOLD 最後一句「確認後下一步」必須和 `vmax-main-workflow.md` 完全一致。

例如：

- HOLD 1 下一步只能是 `STEP 2 AI 教學價值判讀`。
- HOLD 2 下一步只能是 `STEP 2.5 語文輻射分析與教師選擇`。
- HOLD 2.5 下一步只能是 `STEP 2.6 成語表達與視覺化確認`。
- HOLD 2.6 下一步只能是 `Teacher Intent Lock`。

若文字把下一步寫成「課程結構與簡報模組配置」「頁數規劃」「逐頁腳本」，但正式流程尚未到該階段，標記 `WRONG_NEXT_STAGE_POINTER`。

---

## I. 教師主權的實際判定

好的 HOLD 應讓教師感覺自己在「導演」：

- AI 主動看懂教材與學生學習需要。
- AI 提出少量、有理由的判斷。
- 教師可以接受大部分，只改真正不同意的部分。
- 教師不用替 AI 補回它漏掉的教學亮點。
- 教師有時間在關鍵轉折處真正做決策，而不是看系統連跑。

若教師主要工作變成：

- 幫 AI 找漏掉的內容
- 逐項替 AI 做初步分類
- 因 AI 已鎖頁數而被迫接受結構
- 反覆修正機械模板
- 追著已經飛過去的流程叫 AI 回頭

則該 HOLD 雖形式上有確認點，仍視為 `TEACHER_EFFORT_FAIL`。

---

## J. TEST_FREEZE 相容

在 `TEST_FREEZE` 中，若某 HOLD 沒有依此政策顯示：

- 記錄 `MISSING_INTERFACE / SKIPPED_DECISION_LAYER / TEACHER_EFFORT_FAIL / RUNAWAY_WORKFLOW / WRONG_NEXT_STAGE_POINTER`
- 停在原 HOLD
- 不自行修改系統

只有教師明確要求修正／更新規則時才寫回 Core。

---

## K. Machine Payload 原則

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

> 一次確認，只往前走一關；不要飛站。

> 教師確認的是方向與例外，不是替 AI 補完整套教學設計。