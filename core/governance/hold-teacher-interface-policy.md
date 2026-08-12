# V-MAX HOLD Teacher Interface Policy 1.5-draft

## 定位
本規則定義 V-MAX 所有需要教師確認的 Source Gate、HOLD、LKB Review、Experience Micro Lock 與 Production Gate 的共同教師介面。

核心原則：
> AI 要把判斷做重，把老師的操作做輕。
>
> 一次確認，只往前走一個合法決策層。

---

## A. Confirmation Types

### Source / Knowledge
- HOLD 1：Source Truth Confirm
- LKB REVIEW：approved_lkb

### Mandatory Teaching HOLD
- HOLD 2：教學價值／學習難點
- HOLD 2.5：語文範圍
- HOLD 2.6：成語表達

### Experience Micro Locks
- `SCENARIO LOCK`：確認 SOURCE_WORLD / REGISTRY_WRAPPER / OFF 或特定 Wrapper；必須在 Character Topology 前。
- `CHARACTER LOCK`：確認 topology / cast；必須在正式 Character DNA 前。

### Production Gates
- Gate A：Teaching Direction + Lesson Budget Draft
- Gate B：Experience + Storyboard + Page Ledger + Visual Identity Direction
- Gate C：Representative Visual Validation

Micro Lock 保護依賴；Production Gate 保護大型設計決策。

---

## B. Teacher Interface First
任何 WAITING_CONFIRMATION 先顯示人類可讀 Confirmation Card，再保留 machine payload。

最低內容：現在確認什麼、來源／規則、AI 建議與理由、風險／取捨、可改例外、最省力確認方式、確認後唯一下一 decision layer。

---

## C. Recommendation-first
`AI 分析與少量候選 → 說明理由 → 教師只改例外 → 停當前確認點`。

`好 / 可以 / 繼續 / R` 只代表當前確認點，不代表跨站。

---

## D. Single-stage Advance

```text
HOLD 1 → LKB ASSEMBLY → LKB REVIEW
LKB REVIEW → STEP 2 → HOLD 2
HOLD 2 → STEP 2.5 → HOLD 2.5
HOLD 2.5 → STEP 2.6 → HOLD 2.6
HOLD 2.6 → Teacher Intent Lock
...
Gate A → Scenario Decision → SCENARIO LOCK
SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK
CHARACTER LOCK → Experience Completion / downstream architecture
...
Storyboard → Style Recipe / Lesson Skin / Typography → Gate B
Gate B → Representative Visual → Gate C
Gate C → Full Renderer
```

違反：`RUNAWAY_WORKFLOW / SKIPPED_HOLD / STAGE_LEAP / SCENARIO_LOCK_SKIPPED / CHARACTER_LOCK_SKIPPED`。

---

## E. Gate A｜Teaching Direction
確認：本課真正要學什麼、核心 Teaching Skills、MUST/SHOULD/COULD、刻意不做什麼、Lesson Budget Draft。

Gate A 不確認精確頁數，也不提前鎖 Scenario / Character / Style。

---

## F. Scenario Lock
Scenario Card 給 1–3 個真正不同候選；OFF 合法，原文世界強時可 SOURCE_WORLD。

說明：why fit、學生認知行動、風險、認知負荷。

Scenario confirmed 後 downstream 不得靜默換 Wrapper。

---

## G. Character Lock
只有 Scenario locked 後才出 Character Card。先 topology / role slots，再 cast；候選 1–3 組。

說明角色功能、自然性、Guide 是否可 OFF、是否搶文本主體。

Character confirmed 後才建立正式 DNA。

---

## H. Gate B｜Experience + Storyboard + Visual Identity
Gate B 前必須已完成：
- Visual Grammar / Slide Architecture
- Budget Final / Page Ledger
- Storyboard
- Style Recipe selection
- Lesson Skin Final
- Typography direction

Gate B 確認：
- 已鎖 Scenario / Character refs
- Learner Role / Book DNA
- Style Recipe / Lesson Skin Final
- Typography direction
- Surprise Signature
- Storyboard / Page Ledger

**Gate B 不要求教師看完整成品。**它鎖的是文字可說清楚的設計方向；下一階段才用 1–2 張代表頁驗證。

若教師要改 Scenario / Character，使用「回前面」重開對應 lock。

---

## I. Gate C｜Representative Visual
Gate B confirmed 後生成 1–2 張代表頁。Gate C 確認：畫面世界、角色、Typography / Text integration、投影可讀性、密度、教學重點。

Gate C confirmed 後 Full Renderer 批次執行，不逐頁重問同一決策。

---

## J. Teacher Command Resolution
- `好 / 可以 / 繼續`：確認當前 decision layer，依合法 transition 前進。
- Gate C 後 `繼續`：依已鎖 Storyboard 直接製作。
- `下一頁`：下一 cognitive scene，不重畫目前頁。
- `換一個版本`：重設計同內容。
- `重畫`：重生目前視覺。
- `鎖定`：寫 downstream invariant。
- `回前面`：回指定 point，重開受影響 downstream。

---

## K. Wrong Next-stage Pointer Guard
正確：
- HOLD 1 → LKB Assembly / Review
- LKB Review → STEP 2 / HOLD 2
- Gate A → Scenario Decision / Lock
- Scenario Lock → Character Topology / Lock
- Character Lock → Experience Completion
- Gate B → Representative Visual / Gate C
- Gate C → Full Renderer

錯誤：Gate B 前 Style / Lesson Skin 尚未成立；或 Gate B confirmed 後跳過 Representative 直接 Renderer。

錯誤碼：`WRONG_NEXT_STAGE_POINTER / VISUAL_IDENTITY_INCOMPLETE_AT_GATE_B`。

---

## L. Teacher Effort Quality
FAIL：老師替 AI 補大量遺漏、每頁重新確認同一設計、Scenario/Character 混問、早期來源 HOLD 提前決定風格／頁數、Gate B 又重新從零選舞台／卡司。

錯誤碼：`TEACHER_EFFORT_FAIL / MISSING_INTERFACE`。

---

## M. TEST_FREEZE Compatibility
測試中任何 UI 或 transition 錯誤：記錄 failure code、停原 stage、不自行改 Core。只有教師明確要求更新規則／GitHub 時才寫回。

---

## 核心金句
> 前段不飛站；Experience 先鎖舞台，再鎖卡司；Gate B 鎖設計語言，Gate C 看真實樣張。
