# V-MAX Runtime 2.5 Migration Template

Use when a legacy Google Drive Runtime State predates Runtime Contract 2.5.

> Never overwrite the legacy state. Create a new runtime version and preserve the old file as historical evidence.

```yaml
runtime_schema_version: 2.5-draft
storage: GOOGLE_DRIVE
lesson_id:
workflow_version: 2.4-draft
manifest_version: 3.2-draft
executor_version: 1.6-draft
runtime_version:
test_mode: TEST_FREEZE
migration:
  migrated_from_runtime_version:
  migrated_from_document_id:
  migration_status: REVIEW_REQUIRED
  migration_notes: []

lesson:
  grade_volume:
  lesson_number:
  title:

source:
  library_mode: GOOGLE_DRIVE_SOURCE_LIBRARY
  source_status:
  source_file:
  source_file_id:
  source_anchor_status:

state:
  current_stage: MIGRATION_REVIEW
  last_completed_stage: LEGACY_STATE_IMPORTED
  teacher_confirmation_status: WAITING_CONFIRMATION
  next_allowed_stage:
    - MIGRATION_REVIEW
  forbidden_next:
    - FULL_RENDERER

locked_decisions:
  source_anchor:
    status: MIGRATED_CONFIRMED | NEEDS_REVIEW
    legacy_evidence_ref:
  official_knowledge_status:
  lkb:
    status: NOT_BUILT | READY_FOR_REVIEW | APPROVED | MIGRATION_REVIEW_REQUIRED
    lkb_ref:
    validation_ref:
    legacy_evidence_ref:
  lkb_routing:
  step2_teaching_value:
    status: MIGRATED_CONFIRMED | NEEDS_REVIEW | NOT_RUN
  step2_5_language_scope:
    status: MIGRATED_CONFIRMED | NEEDS_REVIEW | NOT_RUN
  step2_6_idiom_expression:
    status: MIGRATED_CONFIRMED | NEEDS_REVIEW | NOT_RUN
  teacher_intent:
    status: MIGRATED_CONFIRMED | NEEDS_REVIEW | NOT_RUN
  lesson_map:
  supplement_framework_decision:
  session_map:
  lesson_visual_map:
  teaching_skill_selection:
    status: NEEDS_REVIEW | NOT_RUN
  lesson_budget_draft:
    status: NEEDS_REVIEW | NOT_RUN
  gate_a_teaching_direction:
    status: NEEDS_REVIEW | NOT_RUN
  experience:
    scenario:
      status: PROPOSED | LOCKED | MIGRATION_REVIEW_REQUIRED
      mode: SOURCE_WORLD | REGISTRY_WRAPPER | OFF
      wrapper_ref:
      legacy_evidence_ref:
    scenario_lock:
    character:
      status: PROPOSED | LOCKED | MIGRATION_REVIEW_REQUIRED
      topology_ref:
      cast_ref:
      character_dna_refs: []
      legacy_evidence_ref:
    character_lock:
    learner_role:
    book_dna_ref:
    surprise_signature:
  extension:
    status: OFF | LIGHT | THEME_MODE | NEEDS_REVIEW
    types: []
  slide_architecture:
    status: NEEDS_REVIEW | NOT_RUN
  lesson_budget_final:
    status: NEEDS_REVIEW | NOT_RUN
  page_ledger:
    status: NEEDS_REVIEW | NOT_RUN
  storyboard:
    status: NEEDS_REVIEW | NOT_RUN
  visual_identity:
    style_recipe_ref:
    lesson_skin:
    typography_lock:
    status: NEEDS_REVIEW | PROPOSED | LOCKED
    legacy_style_ref:
  gate_b_experience_storyboard_visual_identity:
    status: NEEDS_REVIEW | NOT_RUN
  representative_visual:
    status: NEEDS_REVIEW | NOT_RUN
  gate_c_representative_visual:
    status: NEEDS_REVIEW | NOT_RUN

production:
  renderer_status: BLOCKED_UNTIL_GATE_C
  text_qa_status: NOT_RUN
  typography_qa_status: NOT_RUN
  quality_gate_status: NOT_RUN

runtime_rules:
  source_truth_must_precede_lkb_build: true
  approved_lkb_required_for_step2: true
  scenario_lock_required_before_character_topology: true
  character_lock_required_before_character_dna: true
  style_recipe_required_before_lesson_skin_final: true
  visual_identity_required_before_gate_b: true
  gate_c_allows_batch_renderer: true
  model_memory_cannot_override_runtime: true

migration_review:
  explicitly_confirmed_legacy_fields: []
  inferred_fields_requiring_review: []
  stale_inner_statuses_ignored: []
  recommended_reopen_point:
  rationale:
```

## Migration rules

1. Only top-level legacy state plus explicitly confirmed decision records can be migrated as evidence.
2. Historical inner `PROPOSED_WAITING_CONFIRMATION` sections do not override the latest top-level state.
3. New v1 locks absent from the old schema must be `NEEDS_REVIEW`, not silently `confirmed`.
4. Find the earliest uncertain dependency and rerun from there.
5. Do not resume FULL_RENDERER merely because the legacy state once allowed it.
6. After successful migration review, update Google Drive Runtime Index to point to the new version only when the new state is intentionally activated.
