# V-MAX Runtime 2.7 Migration Template

Use when a legacy Google Drive Runtime State predates Runtime Contract 2.7.

> Never overwrite the legacy state. Create a new runtime version and preserve the old file as historical evidence.

```yaml
runtime_schema_version: 2.7-draft
storage: GOOGLE_DRIVE
lesson_id:
workflow_version: 2.6-draft
manifest_version: 3.8-draft
executor_version: 1.8-draft
runtime_version:
production_mode: SINGLE_LESSON_BUILD | BATCH_PREP_BUILD
test_mode: TEST_FREEZE
migration:
  migrated_from_runtime_version:
  migrated_from_document_id:
  migration_status: REVIEW_REQUIRED | REVIEWED
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
  current_stage: MIGRATION_REVIEW | LKB_REVIEW | ...
  last_completed_stage: LEGACY_STATE_IMPORTED
  teacher_confirmation_status: WAITING_CONFIRMATION
  next_allowed_stage: []
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
      role_refs: []
      character_asset_refs: []
      legacy_evidence_ref:
    character_lock:
    learner_role:
    book_dna_ref:
    surprise_signature:
    visual_seed:
      status: NOT_REQUIRED | PROPOSED | SEED_LOCKED
      style_family_seed_ref:
      style_reference_asset_ref:
      lesson_skin_seed:
      typography_base_ref:
      drive_identity_pack_ref:
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
    identity_pack_status: PROPOSED | SEED_LOCKED | FINAL_LOCKED
    identity_pack_drive_ref:
    style_recipe_ref:
    lesson_skin_final:
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
  batch_prep_checkpoint:
    status: NOT_APPLICABLE | IN_PROGRESS | COMPLETE
  renderer_status: BLOCKED_UNTIL_GATE_C
  text_qa_status: NOT_RUN
  typography_qa_status: NOT_RUN
  quality_gate_status: NOT_RUN

persistence:
  shared_visual_asset_root_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
  last_persistence_checkpoint:
  approved_assets_persisted: false
  usable_wip_persisted: false
  drive_refs_verified: false
  active_assets: {}
  version_lineage:
    package_version:
    parent_package_ref:
    change_class: PATCH | REFRESH | REBASE
    reviewed_at:
    next_review_due:
    inherited_refs: []
    upgraded_refs: []
    retired_refs: []
    change_summary: []

runtime_rules:
  source_truth_must_precede_lkb_build: true
  approved_lkb_required_for_step2: true
  scenario_lock_required_before_character_topology: true
  character_lock_required_before_visual_seed_or_character_dna: true
  batch_requires_visual_seed_before_cross_material_generation: true
  style_recipe_required_before_lesson_skin_final: true
  visual_identity_final_required_before_gate_b: true
  approved_or_usable_wip_must_persist_to_drive: true
  saved_assets_must_not_be_overwritten: true
  formal_refs_must_pin_explicit_version: true
  newest_asset_is_not_automatically_active: true
  rollback_changes_active_ref_only: true
  mandatory_hold_single_stage_advance: true
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
3. New v1 locks absent from the old schema must be `NEEDS_REVIEW`, not silently confirmed.
4. Find the earliest uncertain dependency and rerun from there.
5. Do not resume FULL_RENDERER merely because the legacy state once allowed it.
6. Missing approved Drive visual assets block visual production even if an old textual character selection was confirmed.
7. Legacy style selection may be migration evidence, but cannot silently become a new `FINAL_LOCKED` Identity Pack if the current Style Recipe → Lesson Skin → Typography → Gate B sequence was not followed.
8. New runtime and every migration WIP are separate versions; never overwrite the legacy state.
9. Update Runtime Index only after the new state has been created, verified, and intentionally activated.
