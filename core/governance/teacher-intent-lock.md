# V-MAX Teacher Intent Lock 1.0

## 定位

Teacher Intent Lock 用來保護教師已明確確認的教學意圖，避免後續 AI、Director、Character、Visual 或 Renderer 在未經允許下悄悄改寫。

核心原則：

> AI 可以提案，但不能把教師已鎖定的決策當成可自行優化的草稿。

## 狀態

```yaml
teacher_intent_state:
  PROPOSED
  CONFIRMED
  LOCKED
```

- `PROPOSED`：AI 或教師提出，尚未確認。
- `CONFIRMED`：教師已確認，可進入下一步設計；若需重大修改必須重新提示。
- `LOCKED`：正式鎖定。後續模組不得自行改變，只能提出 patch 建議並等待教師解鎖或重新確認。

## 可鎖定項目

```yaml
teacher_intent_lock:
  lesson_focus: []
  must_keep: []
  must_remove: []
  pedagogy_choices: []
  assessment_constraints: []
  scenario_wrapper:
  character_decisions:
  visual_constraints: []
  student_visible_rules: []
  teacher_note_rules: []
```

## 變更規則

若後續系統發現衝突、錯誤或更佳方案：
1. 不得直接改寫 LOCKED 項目。
2. 產生 `CHANGE_PROPOSAL`，說明原因、影響與替代方案。
3. 教師確認後才更新鎖定值。

```yaml
change_proposal:
  target:
  current_locked_value:
  proposed_change:
  reason:
  affected_modules: []
  teacher_decision: PENDING | ACCEPT | REJECT
```

## 優先序

Teacher Intent LOCKED > Teacher Intent CONFIRMED > Director Recommendation > Registry Prior > Renderer Capability。

平台限制不能凌駕 LOCKED Teacher Intent；若 Renderer 做不到，應降級呈現方式，而不是改變教學意圖。

## 核心金句

> 教師確認過的意圖不是提示詞素材，而是系統契約。
