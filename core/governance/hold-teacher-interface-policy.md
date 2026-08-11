# V-MAX HOLD Teacher Interface Policy 1.3-draft

## 定位
本規則定義 V-MAX 所有需要教師確認的 Source Gate、HOLD、LKB Review 與 Production Gate 的共同教師介面。

核心原則：

> HOLD 是給老師做決策的，不是給系統展示資料結構的。

> AI 要把判斷做重，把老師的操作做輕。

> 一次確認，只往前走一個合法決策層。

---

## A. Confirmation Types

### 1. Source Truth Gate
- STEP 1 → HOLD 1
- 確認 Official Knowledge / Source Anchor 是否可用
- HOLD 1 confirmed 後才允許 LKB Assembly

### 2. LKB Review
- Chinese Lesson Knowledge Builder 完成 `ready_for_lkb_review` 後啟動
- 只確認整合、去重、來源追溯、Teacher Knowledge 分流是否正確
- 不新增新的 Learning Expansion / Teaching Strategy / Style / Scenario
- confirmed 後狀態為 `approved_lkb`

### 3. Mandatory Teaching HOLD
- STEP 2 → HOLD 2
- STEP 2.5 → HOLD 2.5
- STEP 2.6 → HOLD 2.6

### 4. Production Gates
- Gate A：Teaching Direction Lock
- Gate B：Experience + Storyboard Lock
- Gate C：Representative Visual Validation

Production Gate 是大型設計決策鎖，不是每張投影片重新確認。

---

## B. Teacher Interface First

任何 `WAITING_CONFIRMATION` 都必須先顯示 Teacher Confirmation Card，再保留 machine payload。

確認卡至少回答：
- 現在確認什麼？
- 依據哪些來源／規則？
- AI 建議是什麼？
- 為什麼？
- 教師可改哪些例外？
- 最省力的確認方式是什麼？
- 確認後唯一下一個決策層是什麼？

禁止只丟 JSON / YAML / schema 當教師 UI。

---

## C. Recommendation-first

預設互動：

```text
AI 完成分析與推薦
→ 用人類語言說明理由、取捨與風險
→ 教師只改例外
→ 停在當前確認點
```

可用短命令：`好 / 可以 / 繼續 / R / 短句例外修改`。

短命令不代表可以跨過兩個以上需要教師決策的層級。

---

## D. Single-stage Advance

合法鏈：

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
```

規則：
- HOLD 1 confirmed：執行 LKB Assembly，停在 LKB REVIEW。
- LKB REVIEW confirmed：標記 `approved_lkb`，執行 STEP 2，停在 HOLD 2。
- HOLD 2 confirmed：執行 STEP 2.5，停在 HOLD 2.5。
- HOLD 2.5 confirmed：執行 STEP 2.6，停在 HOLD 2.6。
- HOLD 2.6 confirmed：才進 Teacher Intent Lock。

違反：`RUNAWAY_WORKFLOW / SKIPPED_HOLD / STAGE_LEAP`。

---

## E. Production Gate Semantics

### Gate A｜Teaching Direction Lock
確認：
- 本課真正要學什麼
- 核心 Teaching Skills
- MUST / SHOULD / COULD
- 刻意不做什麼
- Lesson Budget Draft

Gate A 不確認精確頁數。

### Gate B｜Experience + Storyboard Lock
確認：
- Source World / Scenario ref
- Character topology / cast / DNA refs
- Learner Role
- Lesson Skin / Style Recipe ref
- Surprise Signature
- Storyboard
- Lesson Budget Final / Page Ledger

### Gate C｜Representative Visual Validation
確認 1–2 張代表頁：
- 畫面世界與角色
- Typography / Text integration
- 投影可讀性
- 視覺密度
- 教學重點是否一眼可見

Gate C confirmed 後，Full Renderer 可批次進行；不得每頁再問同一層級的「可以嗎」。

---

## F. Teacher Command Resolution

- `好 / 可以 / 繼續`：只確認當前 Source/HOLD/Review/Gate，依合法 transition 前進。
- production phase 且 Gate C confirmed 後：`繼續` = 依已鎖 Storyboard 繼續製作。
- `下一頁` = 下一認知場景，不重畫目前頁。
- `換一個版本` = 重設計同內容。
- `重畫` = 重生目前視覺。
- `鎖定` = 寫入 downstream invariant。
- `回前面` = 回指定 decision point 並重開受影響 downstream。

---

## G. Wrong Next-stage Pointer Guard

每個確認卡最後的 next step 必須與 `vmax-main-workflow.md` 一致。

正確例：
- HOLD 1 → LKB ASSEMBLY → LKB REVIEW
- LKB REVIEW → STEP 2 → HOLD 2
- HOLD 2 → STEP 2.5 → HOLD 2.5
- HOLD 2.5 → STEP 2.6 → HOLD 2.6
- HOLD 2.6 → Teacher Intent Lock

錯誤例：
- HOLD 1 直接指向頁數／角色／風格
- HOLD 2 直接指向 Slide Architecture
- Gate A 直接宣告精確頁數
- Gate B 未看代表頁就直接 Full Renderer

錯誤碼：`WRONG_NEXT_STAGE_POINTER`。

---

## H. LKB Review Boundary

LKB Review 不是要求老師重讀全部教材；AI 應主動摘要：
- 來源是否齊全
- 重複內容怎麼合併
- 有哪些 source conflict / gap
- Official / Teacher Knowledge 有無混線
- 哪些項目尚未核准

教師只需要確認例外。

若 LKB Review 被當成新的教學設計會議，標記 `LKB_REVIEW_SCOPE_OVERREACH`。

---

## I. Teacher Effort Quality

FAIL 指標：
- 老師替 AI 補大量遺漏
- 老師被迫看大段 machine payload 才能判斷
- 每頁重新確認相同已鎖設計
- AI 先鎖頁數再讓老師接受
- 角色／風格／Scenario 在早期來源 HOLD 被提前決定

錯誤碼：`TEACHER_EFFORT_FAIL / MISSING_INTERFACE`。

---

## J. TEST_FREEZE Compatibility

在 `TEST_FREEZE` 中，若確認點沒有依本 policy 顯示或 transition 錯誤：
- 記錄 failure code
- 停在原 stage
- 不自行修改 Core

只有教師明確要求修正規則／GitHub 時才寫回。

---

## 核心金句

> 資料結構給系統讀；確認卡給老師做決策。

> 前段一次確認只走一層；後段一旦鎖定，就不要把老師困在逐頁批准裡。
