# V-MAX Lesson Learning 1.1

## 定位

每完成一課，V-MAX 不只產出教材，也要產出「這一課讓系統學會了什麼」。Lesson Learning 是每課結尾必跑的反思／回寫層。

核心原則：

> 每一課不只留下作品，也留下可被檢驗、可被教師批准的系統學習。

## 三類學習

```yaml
lesson_learning:
  lesson_specific: []
  global_rule_candidates: []
  one_off_exceptions: []
```

- `lesson_specific`：只適用本課，不自動外推。
- `global_rule_candidates`：可能值得跨課使用，但尚未成為全域規則。
- `one_off_exceptions`：本課特殊處理，避免被誤學成規則。

## 回寫範圍

應至少檢查：
- Teacher Intent 是否被完整保留
- Session Map 是否自然
- Lesson Visual Map 是否真的幫助學生快速建立整課理解
- Scenario Wrapper 是否真的增進理解
- Character 是否有功能且不搶戲
- Reading Strategy / Learning Framework 是否有效
- Knowledge Lab 的深教／短辨析判斷是否合適
- Visual Grammar 是否幫助理解
- Style / Renderer 是否有視覺漂移或中文字問題
- 學生投入訊號與理解證據
- 教師實際調整了什麼

## Lesson Visual Map Learning

若本課啟用 Lesson Visual Map，課後需分開檢查開課版與收束版：

```yaml
lesson_visual_map_learning:
  mode: OPEN | CLOSE | BOTH
  map_structure:
  quick_grasp_signal:
  helped_students_see_whole:
  helped_recall:
  spoiler_or_over_reveal_signal:
  overload_signal:
  visual_text_balance:
  teacher_adjustments: []
  reuse_recommendation: KEEP | MODIFY | LIMIT | RETIRE
```

判讀原則：
- 「學生喜歡看」與「學生因此更懂整課」分開記錄。
- OPEN 若太早暴露主旨、人物特質或答案，記為 `spoiler_or_over_reveal_signal`，不得升成成功模式。
- CLOSE 若變成密集文字表，記為 `overload_signal`。
- 某種 Visual Map 結構即使在本課有效，也只能先成為候選，不直接綁定某文體。

## 升級權

任何全域規則、Reusable Wrapper、Reusable Character、Class Preference、Reusable Visual Map Pattern 都不得由 AI 自動升級。

```yaml
promotion:
  status: LESSON_ONLY | CANDIDATE | TEACHER_CONFIRMED
  proposed_by: AI | TEACHER
  evidence: []
  teacher_decision: PENDING | ACCEPT | REJECT
```

只有教師可以把 `CANDIDATE` 升為 `TEACHER_CONFIRMED`。

## 核心金句

> 系統可以從課堂學習，但不能替老師決定什麼值得成為規則。
