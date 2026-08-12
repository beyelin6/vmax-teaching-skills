# V-MAX HOLD Teacher Interface Policy 1.4-draft

## 定位
本規則定義 V-MAX 所有需要教師確認的 Source Gate、HOLD、LKB Review、Experience Micro Lock 與 Production Gate 的共同教師介面。

核心原則：

> HOLD 是給老師做決策的，不是給系統展示資料結構的。

> AI 要把判斷做重，把老師的操作做輕。

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
- `SCENARIO LOCK`：確認 SOURCE_WORLD / REGISTRY_WRAPPER / OFF 或特定 Wrapper；必須發生在 Character Topology 前。
- `CHARACTER LOCK`：確認 topology / cast；必須發生在正式 Character DNA 前。

### Production Gates
- Gate A：Teaching Direction Lock
- Gate B：Experience + Storyboard Lock
- Gate C：Representative Visual Validation

Micro Lock 保護先後依賴；Production Gate 保護大型設計決策。兩者不互相取代。

---

## B. Teacher Interface First
任何 `WAITING_CONFIRMATION` 必須先顯示人類可讀 Confirmation Card，再保留 machine payload。

最低內容：
- 現在確認什麼
- 依據哪些來源／規則
- AI 建議與理由
- 風險／取捨
- 教師可改哪些例外
- 最省力的確認方式
- 確認後唯一下一個 decision layer

禁止只丟 JSON / YAML / schema。

---

## C. Recommendation-first

```text
AI 完成分析與少量候選
→ 說明理由
→ 教師只改例外
→ 停在當前確認點
```

`好 / 可以 / 繼續 / R / 短句例外修改` 都只代表當前確認點，不代表跨站。

---

## D. Single-stage Advance

```text
HOLD 1
→ LKB ASSEMBLY
→ LKB REVIEW
→ STEP 2
→ HOLD 2
→ STEP 2.5
→ HOLD 2.5
→ STEP 2.6
→ HOLD 2.6
→ Teacher Intent Lock
...
→ Gate A
→ Scenario Decision
→ SCENARIO LOCK
→ Character Topology / Cast
→ CHARACTER LOCK
→ Experience Completion
```

規則：
- HOLD 1 confirmed → 執行 LKB Assembly，停 LKB REVIEW。
- LKB REVIEW confirmed → STEP 2，停 HOLD 2。
- HOLD 2 confirmed → STEP 2.5，停 HOLD 2.5。
- HOLD 2.5 confirmed → STEP 2.6，停 HOLD 2.6。
- HOLD 2.6 confirmed → Teacher Intent Lock。
- Gate A confirmed → Scenario candidates，停 SCENARIO LOCK。
- SCENARIO LOCK confirmed → Character candidates，停 CHARACTER LOCK。
- CHARACTER LOCK confirmed → 才建立 Character DNA 與後續 Experience。

違反：`RUNAWAY_WORKFLOW / SKIPPED_HOLD / STAGE_LEAP / SCENARIO_LOCK_SKIPPED / CHARACTER_LOCK_SKIPPED`。

---

## E. Gate A｜Teaching Direction
確認：本課真正要學什麼、核心 Teaching Skills、MUST/SHOULD/COULD、刻意不做什麼、Lesson Budget Draft。

Gate A 不確認精確頁數，也不提前替教師鎖 Scenario / Character。

---

## F. Scenario Lock
Scenario Card 應給 1–3 個真正有差異的候選，`OFF` 合法；若原文世界很強，可推薦 `SOURCE_WORLD`。

必須說明：
- 為什麼適合這篇文本／任務
- 學生會做什麼不同的認知行動
- 可能風險
- 是否會增加認知負荷

Scenario confirmed 後 downstream 不得靜默換 Wrapper。

---

## G. Character Lock
只有 Scenario locked 後才出 Character Card。

先確認 topology / role slots，再確認 cast；候選最多 1–3 組真正不同方案。

角色確認卡需說明：
- 角色功能
- 為何課文人物／既有角色／新角色較合適
- Guide 是否其實可 OFF
- 是否會搶走文本主體

Character confirmed 後才建立正式 Character DNA。

---

## H. Gate B｜Experience + Storyboard
確認：
- 已鎖 Scenario / Character refs
- Learner Role
- Lesson Skin / Visual Identity
- Surprise Signature
- Storyboard
- Lesson Budget Final / Page Ledger

Gate B 不重新要求 Scenario / Character 從零選一次；若教師要改，使用「回前面」重開對應 lock。

---

## I. Gate C｜Representative Visual
確認 1–2 張代表頁：畫面世界、角色、Typography / Text integration、投影可讀性、視覺密度、教學重點。

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
- HOLD 2 → STEP 2.5 / HOLD 2.5
- HOLD 2.5 → STEP 2.6 / HOLD 2.6
- Gate A → Scenario Decision / Lock
- Scenario Lock → Character Topology / Lock
- Character Lock → Experience Completion
- Gate B → Style / Typography / Representative
- Gate C → Full Renderer

錯誤碼：`WRONG_NEXT_STAGE_POINTER`。

---

## L. Teacher Effort Quality
FAIL：
- 老師替 AI 補大量遺漏
- 每頁重新確認相同已鎖設計
- Scenario 與 Character 一次混問，導致先後依賴失效
- 早期來源 HOLD 提前決定風格／角色／頁數
- Gate A 就丟精確頁數

錯誤碼：`TEACHER_EFFORT_FAIL / MISSING_INTERFACE`。

---

## M. TEST_FREEZE Compatibility
測試中任何確認點若 UI 或 transition 錯誤：記錄 failure code、停在原 stage、不自行修改 Core。只有教師明確要求更新規則／GitHub 時才寫回。

---

## 核心金句

> 前段不飛站；Experience 先鎖舞台，再鎖卡司。

> 後段一旦方向鎖定，不要把老師困在逐頁批准裡。
