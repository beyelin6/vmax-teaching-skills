# V-MAX Lesson Budget / Page Ledger Policy 1.0-draft

## 定位

本政策把既有 `Page Estimate / Page Ledger` 升級成真正的課程預算控制。頁數不是起點，而是 Teacher Intent、Lesson Map、Session Map、Knowledge Lab、Teaching Skill 與 Slide Architecture 完成後的結果。

核心：

> 不是問「這課還能做多少」，而是問「有限課堂時間裡，哪些理解最值得留下」。

> 一頁 = 一個完整認知場景；可有兩個有層次問題，不採一題一頁。

---

## 1. 啟動時機

Lesson Budget 不得在 STEP 1 / STEP 2 / STEP 2.5 / STEP 2.6 先鎖死。

合法順序至少為：

```text
Teacher Intent Lock
→ Lesson Map
→ Session Map
→ Teaching Skill Selection
→ Experience Decision
→ Knowledge Lab / Slide Architecture
→ Lesson Budget / Page Ledger
```

若前段尚未成立就宣告完整總頁數，標記 `PREMATURE_PAGE_LOCK`。

---

## 2. 教學優先級

所有候選內容至少標：

- `MUST`：不懂就等於沒有真正讀懂本課
- `SHOULD`：值得深化，但不是整課主軸
- `COULD`：有趣或有價值，可轉 PLUS / EXTENSION

Lesson Budget 優先保障 MUST，再配置 SHOULD；COULD 不得擠掉 MUST。

---

## 3. 預算單位

Lesson Budget 不是只看頁數，而是同時看：
- 可用課堂時間
- 核心認知任務數
- 語文焦點數
- 討論深度
- 輸出／遷移任務
- 視覺場景切換成本

一節課可優先抓：
- 2–3 個核心閱讀任務
- 1 個主要語文焦點
- 1 個遷移／收束

此為建議，不是固定模板。

---

## 4. Page Density Rule

### 4.1 一頁 = 一個完整認知場景
同一頁可以有兩個問題，只要兩題都服務同一個理解場景，且形成層次，例如：

```text
先觀察／找證據
→ 再解釋／推論
```

### 4.2 不應合併
若學生認知任務已切換，例如：
- 閱讀理解 → 創作遷移
- 找證據 → 新的語文技能
- 情節理解 → 跨領域研究

原則上應分頁或分場景。

### 4.3 禁止
- 機械式一題一頁。
- 為省頁數把兩個不同認知任務硬塞同頁。

---

## 5. Stop Rule

每新增一頁，系統必須回答：

> 這張新增了什麼學生理解？

若答案只是：
- 更漂亮
- 再舉一個類似例子
- 再複習一次
- 這個知識也很有趣
- 只是為了角色轉場

則預設：
- 不新增；或
- 合併進現有頁；或
- 降為 `PLUS`。

---

## 6. CORE / PLUS

正式簡報可在同一套中標記：
- `CORE`：正常教學一定跑
- `PLUS`：時間足夠才跑

PLUS 不得破壞 CORE 的連續性；跳過 PLUS 後，課程仍能完整成立。

---

## 7. 字群／多音字密度

沿用 `skills/character-group-visual-comparison/SKILL.md`：
- 主要字群原則一群一頁。
- 簡單兩字群可一頁放兩組。
- 多音字同理。

此規則屬認知負荷判斷，不得機械套用。

---

## 8. Extension Budget

加入 DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM 外掛時，必須先問：

> 它取代什麼？

新增 Extension 後需重算：
- time_budget
- core_task_count
- page_count
- student_output_load

若會擠掉 MUST，系統應主動警告教師。

---

## 9. Experience Budget

Guide Character、Context Wrapper、Surprise Signature 不得自動增加獨立頁。

只有當情境轉場本身具有：
- 必要導航功能
- 認知準備功能
- 關鍵情節揭曉
- 明確學習增益

才可占頁。

否則應融入原教學頁。

---

## 10. Page Ledger 最低欄位

```yaml
page_ledger:
  lesson_time_budget_minutes:
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

`learning_gain` 不得留空；留空代表該頁沒有合法存在理由。

---

## 11. Merge / Cut Check

完成 Page Ledger 後固定跑：

### Merge Check
- 有沒有兩頁其實是同一認知場景？
- 有沒有兩個短問題可在一頁完成？
- 有沒有純轉場頁可融入下一頁？

### Cut Check
- 若時間少 10 分鐘，先砍哪幾頁？
- 砍掉 PLUS 後，核心教學是否仍完整？
- 是否有 COULD 偷偷變成 CORE？

---

## 12. Quality Gate

FAIL：
- Slide Architecture 前就鎖完整頁數。
- 一題一頁造成頁數爆炸。
- 每新增頁無法說明 learning_gain。
- PLUS 被拿掉後課程斷裂。
- Extension 只增加、不替換。
- 為角色、裝飾、驚喜無限制加頁。
- 兩個不同認知任務為省頁數硬塞同頁。

Failure codes：
`PREMATURE_PAGE_LOCK / PAGE_GAIN_MISSING / ONE_QUESTION_ONE_PAGE_DRIFT / LESSON_BUDGET_OVERFLOW / PLUS_DEPENDENCY_FAIL / EXTENSION_BUDGET_FAIL / PAGE_MERGE_MISSED / PAGE_OVERMERGE`

---

## 核心金句

> 頁數是教學決策的結果，不是起點。

> 能在一個完整認知場景裡教完，就不要拆；需要學生換腦袋，就不要硬塞。

> V-MAX 不只要會增加好內容，也要會停止。
