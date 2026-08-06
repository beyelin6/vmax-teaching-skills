# VQS Validation Report Schema

版本：1.0.0

```yaml
vqs_report:
  course_id: ""
  lesson_title: ""
  package_type: baseline | patch | classroom_variant
  package_version: ""
  source_lkb_version: ""
  generated_at: ""
  validator: ""
  overall_status: pass | conditional_pass | needs_revision

sections:
  curriculum_fidelity:
    status: pending
    blocking_issues: []
    notes: []
  knowledge_traceability:
    status: pending
    blocking_issues: []
    notes: []
  pedagogy:
    status: pending
    blocking_issues: []
    notes: []
  visual_readability:
    status: pending
    blocking_issues: []
    notes: []
  teacher_student_separation:
    status: pending
    blocking_issues: []
    notes: []
  digital_interaction:
    status: pending
    blocking_issues: []
    notes: []
  notebooklm_outputs:
    status: pending
    blocking_issues: []
    notes: []
  versioning_and_manifest:
    status: pending
    blocking_issues: []
    notes: []

required_checks:
  lesson_text_exact: false
  characters_complete: false
  recognition_characters_complete: false
  vocabulary_complete: false
  official_idioms_complete: false
  official_rhetoric_and_patterns_complete: false
  no_cross_lesson_contamination: false
  no_unapproved_extensions_in_official_layer: false
  no_student_answer_leak: false
  teaching_flow_approved: false
  role_approved: false
  style_approved: false
  tablet_fallback_present: false
  output_manifest_traceable: false
  no_unreplaced_variables: false
  no_duplicate_slide_root: false
  no_critical_overflow: false

optional_deliverables:
  tablet_activity:
    status: generated | not_generated | not_applicable
    reason: ""
  worksheet:
    status: generated | not_generated | not_applicable
    reason: ""
  exit_ticket:
    status: generated | not_generated | not_applicable
    reason: ""

blocking_summary: []
revision_actions: []
teacher_review:
  status: pending
  reviewed_by: null
  reviewed_at: null
  decision: null
```

## 判定規則

- 任一 `blocking_issues` 非空，整體狀態不得為 `pass`。
- 任一必要檢查為 `false`，整體狀態必須為 `needs_revision`，除非該項經明確判定為不適用。
- `conditional_pass` 只允許用於非阻斷性缺口，例如選配成果尚未生成。
- Baseline Package 必須在教師完成 Final Review 後，才能由 `pass` 轉為 `baseline_completed`。
