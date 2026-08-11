# V-MAX Lesson Budget / Page Ledger Policy 1.1-draft

## 定位
Lesson Budget 分成兩個合法階段：

1. **Budget Draft**：在 Gate A 前控制課堂時間、MUST/SHOULD/COULD 與核心認知任務，尚不宣告精確頁數。
2. **Budget Final / Page Ledger**：Slide Architecture 完成後，才把認知場景轉成正式頁數與逐頁 learning_gain。

> 先控制要教多少，再決定要用幾頁。

> 一頁 = 一個完整認知場景；可有兩個有層次問題，不採一題一頁。

---

## 1. Phase A｜Lesson Budget Draft

### 啟動時機
至少需要：
- approved LKB
- STEP 2 教學價值判讀
- STEP 2.5 / 2.6 已確認範圍
- Teacher Intent / Lesson Map / Session Map
- Teaching Skill Selection Lock

此時 Experience / Slide Architecture 尚未完成也沒關係。

### Draft 只決定
- 可用課堂時間
- MUST / SHOULD / COULD
- 核心 reading / language / transfer tasks
- 每個 task 大致時間需求
- 哪些內容明確不做或降 PLUS

### Draft 不得決定
- 精確總頁數
- 每頁版型
- 每個轉場是否獨立成頁
- 因畫面漂亮而增加場景

若 Gate A 前宣告完整總頁數：`PAGE_COUNT_BEFORE_ARCHITECTURE`。

---

## 2. Phase B｜Budget Final / Page Ledger

### 啟動時機

```text
Gate A confirmed
→ Experience / Extension
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Budget Final / Page Ledger
```

只有此時才可把 cognitive scenes 映射成正式頁數。

---

## 3. Priority Model

- `MUST`：不懂就等於沒有真正讀懂本課
- `SHOULD`：值得深化，但不是整課主軸
- `COULD`：有趣或有價值，可轉 PLUS / EXTENSION

先保障 MUST，再配置 SHOULD；COULD 不得擠掉 MUST。

---

## 4. Budget Units

Lesson Budget 同時看：
- time budget
- 核心認知任務數
- 語文焦點數
- 討論深度
- 產出／遷移負荷
- 視覺場景切換成本

一節課可優先抓 2–3 個核心閱讀任務＋1 個主要語文焦點＋1 個遷移／收束；這是 heuristic，不是模板。

---

## 5. Page Density Rule

### 一頁 = 一個完整認知場景
同頁可以有兩個問題，只要形成同一理解的層次，例如：

`找證據 → 解釋 / 推論`

### 應分場景
若認知任務切換，例如：
- 閱讀理解 → 創作遷移
- 找證據 → 新語文技能
- 情節理解 → 跨域研究

### 禁止
- 一題一頁
- 為省頁數硬塞兩個無關任務

---

## 6. Stop Rule

每新增一頁都要回答：

> 這張新增了什麼學生理解？

若答案只是更漂亮、再一個相似例子、再複習一次、只是有趣、純角色轉場，預設：不新增／合併／降 PLUS。

---

## 7. CORE / PLUS

- `CORE`：正常教學一定跑
- `PLUS`：時間足夠才跑

跳過 PLUS 後，核心教學仍必須完整成立。

---

## 8. 字群／多音字密度

沿用 `skills/character-group-visual-comparison/SKILL.md`：
- 主要字群原則一群一頁
- 簡單兩字群可一頁兩組
- 多音字同理

這是認知負荷規則，不是死模板。

---

## 9. Extension Rebalance

加入 DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM 時，必須先問：

> 它取代什麼？

重算：time budget、core task count、student output load；若會擠掉 MUST，主動警告。

---

## 10. Experience Budget

Scenario、Guide、Learner Role、Surprise Signature 不得自動增加獨立頁。

只有當轉場／揭曉本身有導航、認知準備、關鍵情節或 learning_gain 時才可占頁；否則整合進既有 cognitive scene。

---

## 11. Page Ledger Schema

```yaml
page_ledger:
  lesson_time_budget_minutes:
  budget_draft_ref:
  core_tasks: []
  pages:
    - page_id:
      session:
      priority: MUST | SHOULD | COULD
      delivery: CORE | PLUS
      cognitive_scene:
      learning_gain:
      teaching_skill: []
      text_anchor:
      questions: []
      visual_need:
      experience_role:
      estimated_minutes:
      can_merge: true | false
      can_cut: true | false
      cut_consequence:
  totals:
    core_pages:
    plus_pages:
    estimated_minutes:
```

`learning_gain` 不得留空。

---

## 12. Merge / Cut Check

### Merge
- 兩頁是否其實同一 cognitive scene？
- 兩個短問題是否可同頁完成？
- 純轉場是否可融入下一頁？

### Cut
- 若少 10 分鐘先砍什麼？
- 砍 PLUS 後 CORE 是否完整？
- COULD 是否偷偷變 CORE？

---

## 13. Quality Gate

FAIL：
- Gate A 前鎖精確頁數
- Slide Architecture 前形成 Final Page Ledger
- 一題一頁
- learning_gain 留空
- PLUS 移除後課程斷裂
- Extension 只增加、不替換
- 角色／裝飾／驚喜無限加頁

Failure codes：
`PAGE_COUNT_BEFORE_ARCHITECTURE / PAGE_GAIN_MISSING / ONE_QUESTION_ONE_PAGE_DRIFT / LESSON_BUDGET_OVERFLOW / PLUS_DEPENDENCY_FAIL / EXTENSION_BUDGET_FAIL / PAGE_MERGE_MISSED / PAGE_OVERMERGE`

---

## 核心金句

> Gate A 鎖的是教學預算，不是投影片數。

> 頁數是 Slide Architecture 的結果，不是教學設計的起點。
