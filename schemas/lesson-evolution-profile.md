# Lesson Evolution Profile

Lesson Evolution 用於彙整同一課跨年度、跨版本的教學演化，不取代逐次的 Teaching Memory。

## 定位

```text
Teaching Memory
每一次實際上課的紀錄
        ↓
Lesson Evolution
跨年度整理出的穩定趨勢與版本決策
```

## 建議檔名

`evolution/{lesson_id}_lesson-evolution.md`

## 標準格式

```yaml
lesson_evolution:
  lesson_id: ""
  lesson_title: ""
  current_baseline_version: ""
  first_built_at: ""
  last_reviewed_at: ""

source_memories: []

annual_history:
  - school_year: ""
    classes_used: []
    baseline_version: ""
    classroom_variants: []
    patch_ids: []
    additions: []
    revisions: []
    removals: []
    successful_patterns: []
    recurring_difficulties: []
    digital_findings: []
    teacher_decision: ""

stable_findings:
  consistently_effective_modules: []
  recurring_misconceptions: []
  recommended_time_allocation: []
  recommended_digital_activities: []
  recommended_fallbacks: []
  role_findings: []
  style_and_layout_findings: []

next_baseline_plan:
  rebuild_required: false
  target_version: null
  keep: []
  add: []
  revise: []
  remove: []
  unresolved_questions: []

confidence:
  evidence_count: 0
  confidence_level: low
```

## 彙整規則

- 單次課堂反應不得直接標記為「穩定發現」。
- 原則上至少兩次以上相同趨勢，才可提高為 recurring 或 consistently effective。
- 不同班級若反應相反，必須保留差異，不得強行合併。
- 教材改版時保留舊年度紀錄，但建立新的 Baseline 主版本。
- Lesson Evolution 只能提出修改建議，是否重建 Baseline 仍由教師決定。

## 版本建議

- 版面、錯字、小型修正：Patch version，例如 `1.0.1`
- 新增活動、平板互動或補強模組：Minor version，例如 `1.1.0`
- 官方教材、LKB 結構或整體教學架構重大改變：Major version，例如 `2.0.0`
