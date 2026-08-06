# V-MAX Project Status

```yaml
project:
  course_id: ""
  title: ""
  grade: ""
  semester: ""
  created_at: ""
  updated_at: ""

workflow:
  mode: full_lesson_build
  current_stage: project_initialized
  blocked: false
  blocked_reason: null
  next_skill: null
  selected_teaching_mode: null

version_control:
  baseline_version: null
  active_classroom_version: null
  source_lkb_version: null
  applied_patch_ids: []
  latest_patch_version: null

approvals:
  official_knowledge:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  lkb:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  learning_modules:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  learning_path_and_flow:
    status: pending
    approved_by: null
    approved_at: null
    decision_version: null
    learning_path_id: null
    teaching_flow_id: null
    teaching_mode: null
  teaching_strategy:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  digital_interaction:
    status: pending
    approved_by: null
    approved_at: null
    version: null
    mode: null
  role:
    status: pending
    approved_by: null
    approved_at: null
    role_id: null
  style:
    status: pending
    approved_by: null
    approved_at: null
    style_id: null
  output_profile:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  baseline_final_review:
    status: pending
    approved_by: null
    approved_at: null
  patch_scope:
    status: not_required
    approved_by: null
    approved_at: null
  patch_review:
    status: not_required
    approved_by: null
    approved_at: null
  patched_output_review:
    status: not_required
    approved_by: null
    approved_at: null
  variant_review:
    status: not_required
    approved_by: null
    approved_at: null
  variant_output_review:
    status: not_required
    approved_by: null
    approved_at: null

artifacts:
  official_knowledge: null
  teacher_knowledge: null
  source_map: null
  official_validation: null
  lkb: null
  lkb_validation: null
  learning_expansion: null
  decision_profile: null
  learning_path_profile: null
  teaching_flow_profile: null
  teaching_strategy: null
  tablet_interaction_profile: null
  role_selection: null
  style_selection: null
  output_profile: null
  baseline_output_manifest: null
  active_output_manifest: null

baseline:
  package_path: null
  presentation_path: null
  speaker_notes_path: null
  notebooklm_source_path: null
  worksheet_paths: []
  assessment_paths: []
  tablet_activity_paths: []

patches: []

classroom_variants: []

versions:
  official_knowledge: null
  lkb: null
  learning_modules: null
  decision_profile: null
  teaching_flow: null
  teaching_strategy: null
  digital_interaction: null
  role: null
  style: null
  output_profile: null

stale_artifacts: []
errors: []
history: []
```

## Patch 紀錄範例

```yaml
patches:
  - patch_id: PATCH-002
    title: 成語補強
    patch_type: add_on
    based_on_version: 1.0.0
    target_version: 1.1.0
    status: approved
    profile_path: patches/PATCH-002/patch-profile.md
    affected_layers:
      - learning_expansion
      - teaching_flow
      - presentation
```

## Classroom Variant 紀錄範例

```yaml
classroom_variants:
  - variant_id: VARIANT-2026-09-18-A
    title: 四年二班高互動版
    baseline_version: 1.0.0
    applied_patch_ids:
      - PATCH-002
    teaching_mode: high_interaction
    available_minutes: 40
    device_mode: one_device_per_student
    status: approved
    profile_path: variants/VARIANT-2026-09-18-A/variant-profile.md
```

## 狀態更新紀錄

每次狀態變更追加：

| 時間 | 工作模式 | 原狀態 | 新狀態 | 執行技能 | 原因或核准紀錄 |
|---|---|---|---|---|---|

## stale 標記範例

```yaml
stale_artifacts:
  - artifact: teaching_strategy
    reason: learning_path_changed
    marked_at: ""
  - artifact: presentation
    reason: digital_interaction_changed
    marked_at: ""
```
