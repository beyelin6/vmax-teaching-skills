# V-MAX Runtime State Contract 2.7-draft

## 定位
GitHub 保存 Runtime schema；Google Drive 保存每一課實際 Runtime State。不得把每次 HOLD 或 stage 前進變成 GitHub commit。

## Google Drive Runtime Root
- Folder name: `00_Runtime_State`
- Folder ID: `1AOjYwALGVNWu99b-SnjBUSALEDrlReMt`
- Index: `V-MAX_Runtime_Index`
- Index document ID: `1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ`

每課命名：`V-MAX_State_{冊別}_{課次}_{課名}`。

## 最低欄位

```yaml
runtime_schema_version: 2.7-draft
storage: GOOGLE_DRIVE
lesson_id:
workflow_version:
production_mode: SINGLE_LESSON_BUILD | BATCH_PREP_BUILD
lesson:
  grade_volume:
  lesson_number:
  title:
source:
  library_mode:
  source_status:
  source_file:
state:
  current_stage:
  last_completed_stage:
  teacher_confirmation_status:
  next_allowed_stage: []
  forbidden_next: []
locked_decisions:
  source_anchor:
  official_knowledge_status:
  lkb:
    status: NOT_BUILT | READY_FOR_REVIEW | APPROVED
    lkb_ref:
    validation_ref:
  lkb_routing:
  step2_teaching_value:
  step2_5_language_scope:
  step2_6_idiom_expression:
  teacher_intent:
  lesson_map:
  supplement_framework_decision:
  session_map:
  lesson_visual_map:
  teaching_skill_selection:
  lesson_budget_draft:
  gate_a_teaching_direction:
  experience:
    scenario:
      status: PROPOSED | LOCKED
      mode: SOURCE_WORLD | REGISTRY_WRAPPER | OFF
      wrapper_ref:
      selector_result_ref:
    scenario_lock:
    character:
      status: PROPOSED | LOCKED
      topology_ref:
      cast_ref:
      role_refs: []
      character_asset_refs: []
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
    status: OFF | LIGHT | THEME_MODE
    types: []
  slide_architecture:
  lesson_budget_final:
  page_ledger:
  storyboard:
  visual_identity:
    identity_pack_status: PROPOSED | SEED_LOCKED | FINAL_LOCKED
    identity_pack_drive_ref:
    style_recipe_ref:
    lesson_skin_final:
    typography_lock:
  gate_b_experience_storyboard_visual_identity:
  representative_visual:
  gate_c_representative_visual:
production:
  batch_prep_checkpoint:
    status: NOT_APPLICABLE | IN_PROGRESS | COMPLETE
    prestudy_ref:
    short_read_ref:
    drive_persistence_verified:
  renderer_status:
  text_qa_status:
  typography_qa_status:
  quality_gate_status:
persistence:
  shared_visual_asset_root_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
  last_persistence_checkpoint:
  approved_assets_persisted: true | false
  usable_wip_persisted: true | false
  drive_refs_verified: true | false
  active_assets:
    source_master_ref:
    lkb_export_ref:
    storyboard_ref:
    page_ledger_ref:
    renderer_script_ref:
    identity_pack_ref:
    teaching_slides_ref:
    prestudy_ref:
    short_read_ref:
    notebooklm_source_ref:
    notebooklm_visual_yaml_ref:
    question_bank_ref:
    character_asset_refs: []
    style_asset_ref:
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
language_focus:
  grade_3_4_character_deep_focus:
    - SHAPE_NEAR
    - POLYPHONIC
  source_characters_complete: true
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
  lesson_budget_has_draft_and_final: true
  model_memory_cannot_override_runtime: true
notes: []
```

---

## Shared Front State Chain

```text
STEP_1
→ HOLD_1_SOURCE_TRUTH
→ LKB_ASSEMBLY
→ LKB_REVIEW
→ STEP_2
→ HOLD_2
→ STEP_2_5
→ HOLD_2_5
→ STEP_2_6
→ HOLD_2_6
→ TEACHER_INTENT_LOCK
→ LESSON_MAP
→ SESSION_MAP
→ LVM
→ TEACHING_SKILL_SELECTION_LOCK
→ LESSON_BUDGET_DRAFT
→ GATE_A_TEACHING_DIRECTION
→ SCENARIO_DECISION
→ SCENARIO_LOCK
→ CHARACTER_TOPOLOGY_CAST
→ CHARACTER_LOCK
```

## SINGLE_LESSON_BUILD State Chain

```text
CHARACTER_LOCK
→ EXPERIENCE_COMPLETION
→ EXTENSION_CHECK
→ KNOWLEDGE_LAB
→ SLIDE_ARCHITECTURE
→ LESSON_BUDGET_FINAL_PAGE_LEDGER
→ STORYBOARD
→ STYLE_RECIPE
→ LESSON_SKIN_FINAL
→ TYPOGRAPHY_LOCK
→ GATE_B_EXPERIENCE_STORYBOARD_VISUAL_IDENTITY
→ REPRESENTATIVE_VISUAL
→ GATE_C_REPRESENTATIVE_VISUAL
→ FULL_RENDERER
→ TEXT_TYPOGRAPHY_QA
→ QUALITY_GATE
→ OUTPUT_DERIVATIVES
→ DELIVERY
```

## BATCH_PREP_BUILD State Chain

```text
CHARACTER_LOCK
→ CHARACTER_ASSET_REFERENCE_VERIFICATION
→ VISUAL_SEED_PROPOSAL
→ VISUAL_SEED_LOCK
→ IDENTITY_PACK_SEED_PERSIST
→ PRESTUDY_PRODUCTION
→ PRESTUDY_PERSIST_VERIFY
→ SHORT_READ_PRODUCTION
→ SHORT_READ_PERSIST_VERIFY
→ BATCH_PREP_CHECKPOINT_COMPLETE
```

Batch checkpoint 完成後可 STOP / NEXT LESSON。

### Batch Resume to Slides

```text
BATCH_PREP_CHECKPOINT_COMPLETE
→ LOAD_IDENTITY_SEED
→ KNOWLEDGE_LAB
→ SLIDE_ARCHITECTURE
→ PAGE_LEDGER / STORYBOARD
→ STYLE_RECIPE_FINALIZATION
→ LESSON_SKIN_FINAL
→ TYPOGRAPHY_LOCK
→ GATE_B
→ REPRESENTATIVE / GATE_C
→ RENDERER
```

---

## Visual Identity State Rule

```yaml
PROPOSED:
  can_generate: none_or_preview_samples
SEED_LOCKED:
  can_generate:
    - PRESTUDY
    - SHORT_READ
  cannot_claim:
    - LESSON_SKIN_FINAL
    - GATE_B_COMPLETE
FINAL_LOCKED:
  can_generate:
    - TEACHING_SLIDE
    - EXTENSION
    - platform_adapters
```

`lesson_skin_seed` 不是 `lesson_skin_final`。

---

## Persistence / Version Rule
任何 `APPROVED / LOCKED / USABLE_WIP` 產生後，必須另存新 Drive file version，不能覆蓋既有檔案。

正式引用必須 pin `_vNN` 或等價明確 asset version；禁止 `latest`。

建立新版後，只有教師確認或合法 Gate / Lock 通過才更新 `persistence.active_assets`。

因此 rollback 只需要：

```text
active_ref: v03
→ rollback
→ active_ref: v02
```

舊檔不變，新檔也不刪。

若即將因額度、平台或時間中斷：
- WIP 另存新版本
- 更新 `last_persistence_checkpoint`
- 驗證 Drive ref
- 才結束本輪

---

## Refresh / Rebase Rule
約每 24 個月可將課程標為 `REVIEW_DUE`，但不自動修改。

### PATCH
同一 package 內新 file version。

### REFRESH
同一 source baseline 下重新備課，建立新 Lesson Package folder，保留 parent package ref。

### REBASE
來源教材改版，建立新 Source Baseline，重新跑 Source Truth / LKB。

共享角色或 Style 有新版時，不自動升級歷史課；必須明確記錄 KEEP_PINNED / UPGRADE / FORK / RETIRE_FROM_NEW_VERSION。

---

## Reopen Rule
- Scenario reopen → Character / Visual Seed / Storyboard / Visual Identity downstream 重評。
- Character reopen → asset refs / Visual Seed / Storyboard / Visual Identity downstream 重評。
- Visual Seed reopen → 先前 PRESTUDY / SHORT_READ 標 `NEEDS_VISUAL_SYNC_REVIEW`。
- Storyboard / Visual Grammar 大改 → Style Recipe / Lesson Skin Final / Gate B downstream 重評。
- Style Recipe 改 → Lesson Skin Final / Typography / Gate B / Representative downstream 重評。
- LKB node 變更 → 只重開引用該 node 的 outputs。

---

## 核心金句
> Drive 每一版都留著；Runtime 只決定現在採用哪一版。

> 新版不是覆蓋舊版，回退也不是重做舊版。
