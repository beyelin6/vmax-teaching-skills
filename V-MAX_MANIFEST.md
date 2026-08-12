# V-MAX Manifest 4.7-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

```yaml
vmax_manifest_version: 4.7-draft
bootstrap: V-MAX_BOOTSTRAP.md

runtime_contract:
  path: runtime/lesson-state.md
  current_version: 2.7-draft
runtime_migration_template:
  path: runtime/templates/runtime-state-migration-2.7.md
  current_version: 2.7-template
runtime_legacy_migration_template:
  path: runtime/templates/runtime-state-migration-2.5.md
  current_version: 2.5-template
runtime_migration_resume_policy:
  path: core/governance/runtime-migration-resume-policy.md
  current_version: 1.0-draft
  authority: EVIDENCE_AWARE_RESUME
runtime_storage:
  provider: GOOGLE_DRIVE
  root_folder_name: 00_Runtime_State
  root_folder_id: 1AOjYwALGVNWu99b-SnjBUSALEDrlReMt
  index_title: V-MAX_Runtime_Index_v12
  index_document_id: 1LWpukiDfA8DaC3ZKVrJx3VEU0GO9XbqO6caqmnD-9N4
  previous_index_title: V-MAX_Runtime_Index_v11
  previous_index_document_id: 1Q1CQpSBtxpeD7tiocI2dbdskCclb_Ff9qr1XhMvFjlA
  active_runtime_title: V-MAX_State_四上_第一課_水陸小高手_13
  active_runtime_document_id: 1D5bKaFNInGctynN988VxGSwMoVDV7S90xYf2PleUHAk
  active_runtime_version: 13
  active_runtime_stage: STYLE_RECIPE

main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.6-draft
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.8-draft
hold_policy:
  path: core/governance/hold-teacher-interface-policy.md
  current_version: 1.5-draft

production_mode_policy:
  path: core/governance/production-mode-policy.md
  current_version: 1.0-draft
  modes:
    - SINGLE_LESSON_BUILD
    - BATCH_PREP_BUILD

upgrade_lifecycle_policy:
  path: core/governance/lesson-upgrade-lifecycle-policy.md
  current_version: 1.0-draft
  authority: NON_DESTRUCTIVE_VERSIONING_AND_ROLLBACK
  review_cadence_months: 24
  never_overwrite: true
  file_version_format: _vNN

lesson_knowledge_builder:
  path: skills/chinese-lesson-knowledge-builder/SKILL.md
  current_version: 0.3.0
  authority: LKB_STRUCTURE_SOURCE_TRACE_VERSIONING
lesson_knowledge_schema: schemas/lesson-knowledge-book.md
lesson_knowledge_routing:
  path: core/knowledge/lesson-knowledge-base-policy.md
  current_version: 1.1-draft
  authority: DOWNSTREAM_ROUTING_AND_SPIRAL_ONLY

teaching_skill_selection:
  path: core/pedagogy/teaching-skill-selection-policy.md
  current_version: 1.1-draft
lesson_budget:
  path: core/governance/lesson-budget-policy.md
  current_version: 1.1-draft

experience_layer:
  path: core/experience/vmax-experience-layer.md
  current_version: 1.4-draft
  authority: ORCHESTRATION_ONLY
scenario_wrapper_teacher_lock: core/governance/scenario-wrapper-teacher-lock.md
scenario_wrapper_registry: core/visual/scenario-wrapper-registry.md
scenario_wrapper_selector: core/visual/scenario-wrapper-language-arts-selector.md
scenario_character_bridge: core/character/scenario-character-bridge.md
character_system: core/character/character-system-2.md
bee_teacher_role:
  path: libraries/roles/bee-teacher/role.md
  current_version: 0.2.0
  signature_ownership: EXCLUSIVE_TO_ROLE-BEE-001
style_recipe_families: core/visual/style-recipe-families.md
extension_layer: core/extension/extension-layer-policy.md

google_drive_asset_authority:
  path: core/governance/google-drive-asset-authority-policy.md
  current_version: 1.0-draft
  authority: PERSISTENT_ASSET_AND_WORKSPACE_BOUNDARY
  shared_visual_asset_library:
    title: 00_V-MAX_角色與視覺資產庫
    folder_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
  book_dna_root:
    title: 02_整冊Book_DNA
    folder_id: 1XXaBuiiB0l0D0-cn7i5IiE-VhX9vm0iZ

lesson_package_delivery:
  path: skills/lesson-package-delivery/SKILL.md
  current_version: 1.4-draft
google_drive_lesson_archive:
  path: skills/google-drive-lesson-archive/SKILL.md
  current_version: 1.2-draft

typography_bridge:
  path: vmax-typography-bridge/SKILL.md
  current_version: 1.1-draft
renderer_contract: core/renderer/image-first-hybrid-renderer.md

character_group_visual_comparison: skills/character-group-visual-comparison/SKILL.md
text_embedded_language_policy: core/pedagogy/text-embedded-language-teaching-policy.md
text_embedded_language_skill: skills/text-embedded-language-teaching/SKILL.md
lesson_visual_map: core/visual/lesson-visual-map.md
prestudy_worksheet: skills/prestudy-worksheet/SKILL.md
postlesson_short_writing_worksheet: skills/postlesson-short-writing-worksheet/SKILL.md

regression:
  workflow_hold:
    path: tests/workflow-hold-regression-cases.md
    current_version: 1.9-draft
    contract_status: PASS
  integration:
    path: tests/vmax-v1-integration-regression-cases.md
    current_version: 1.3-draft
    contract_status: PASS
  migration_resume:
    path: tests/runtime-migration-resume-regression-cases.md
    current_version: 1.0-draft
    contract_status: PASS
  preseal_report:
    path: tests/vmax-v1-preseal-regression-report.md
    current_version: 1.0-draft
    status: TECHNICAL_PRESEAL_PASS
  live_runtime_gate_a_transition:
    path: tests/vmax-v1-live-runtime-gate-a-transition-report.md
    status: PASS_TO_GATE_A
  live_runtime_scenario_transition:
    path: tests/vmax-v1-live-runtime-scenario-transition-report.md
    status: PASS_TO_SCENARIO_LOCK
  live_runtime_character_transition:
    path: tests/vmax-v1-live-runtime-character-transition-report.md
    status: PASS_TO_CHARACTER_LOCK
  live_runtime_character_lock_and_dna:
    path: tests/vmax-v1-live-runtime-character-lock-and-dna-report.md
    status: PASS_TO_CHARACTER_DNA
  live_runtime_learner_role_book_dna:
    path: tests/vmax-v1-live-runtime-learner-role-book-dna-report.md
    status: PASS_TO_BOOK_DNA_CONFIRMATION
  live_runtime_book_dna_surprise_signature:
    path: tests/vmax-v1-live-runtime-book-dna-surprise-signature-report.md
    status: PASS_TO_SURPRISE_SIGNATURE_CONFIRMATION
  live_runtime_surprise_extension_knowledge_lab:
    path: tests/vmax-v1-live-runtime-surprise-extension-knowledge-lab-report.md
    status: PASS_TO_VISUAL_GRAMMAR_SLIDE_ARCHITECTURE
  live_runtime_visual_grammar_budget_ledger:
    path: tests/vmax-v1-live-runtime-visual-grammar-budget-ledger-report.md
    status: PASS_TO_STORYBOARD
  live_runtime_storyboard:
    path: tests/vmax-v1-live-runtime-storyboard-report.md
    current_version: 1.0-draft
    status: PASS_TO_STYLE_RECIPE
  static_contract: PASS
  three_lesson_tabletop: PASS_RECHECKED_UNDER_PRODUCTION_MODE_SPLIT
  asset_persistence_regression: PASS_LIVE_DRIVE
  production_mode_regression:
    status: PASS
    single: PASS_LIVE_DRIVE_DERIVATIVE_LINEAGE
    batch: PASS_LIVE_DRIVE_SAFE_CHECKPOINT
  rollback_versioning_regression: PASS_LIVE_DRIVE
  live_runtime_read_audit: PASS_WITH_MIGRATION_COMPLETED_AND_RESUMED
  live_runtime_rerun:
    status: PASS_TO_STYLE_RECIPE
    runtime_version: 13
    current_stage: STYLE_RECIPE

system_architecture:
  path: core/governance/vmax-system-architecture.md
  current_version: 1.3-draft
  status: TECHNICAL_PRESEAL_PASS_STORYBOARD_COMPLETE

compatibility_helpers:
  vmax_course_orchestrator:
    path: skills/vmax-course-orchestrator/SKILL.md
    current_version: 0.5.0-compat
  vmax_decision_engine:
    path: skills/vmax-decision-engine/SKILL.md
    current_version: 0.2.0-compat
  role_recommender:
    path: skills/role-recommender/SKILL.md
    current_version: 0.2.0-compat
  style_recommender:
    path: skills/style-recommender/SKILL.md
    current_version: 0.2.0-compat
  presentation_engine:
    path: skills/presentation-engine/SKILL.md
    current_version: 0.2.0-compat
```

---

## Canonical Production Resolution

### SINGLE_LESSON_BUILD

```text
Shared Front Path
→ Character Lock
→ Character DNA / Learner Role / Book DNA / Surprise Signature
→ Extension Check（若有）
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
→ Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative / Gate C
→ Formal Slides
→ Renderer Script / NotebookLM adapter assets
→ Prestudy / Short Read
→ Question Bank / Kahoot / Other Outputs
→ Delivery
```

所有 derivatives 讀同一 `FINAL_LOCKED Lesson Visual Identity Pack`。

### BATCH_PREP_BUILD

```text
Shared Front Path
→ Character Lock
→ VISUAL SEED LOCK
→ Identity Pack = SEED_LOCKED
→ PRESTUDY / SHORT_READ
→ BATCH_PREP_CHECKPOINT_COMPLETE
→ STOP / NEXT LESSON
```

`lesson_skin_seed != Lesson Skin Final`。

---

## Migration Resume Resolution

一般新課完整遵守 mandatory HOLD 鏈。Legacy migration 只有在 `migration_status: REVIEWED` 且節點有 `MIGRATED_CONFIRMED + evidence` 時才可 carry forward；新版新增 lock 不得由舊 evidence 自動升格。

第一課 live chain：
- `_03`：migration review → LKB REVIEW
- `_04`：LKB 核准；evidence-aware resume 後重跑 Teaching Skill Selection / Budget Draft → Gate A
- `_05`：Gate A 核准 → Scenario Decision → SCENARIO LOCK
- `_06`：Scenario A → Character Topology / candidates → CHARACTER LOCK
- `_07`：Character A `SINGLE_GUIDE＋小澄主播` → Character DNA
- `_08`：Learner Role A `動作觀察員` / Final Transfer `水陸小詩人` → BOOK_DNA_CONFIRMATION
- `_09`：Book DNA A `自由手繪探險手帳` → SURPRISE_SIGNATURE_CONFIRMATION
- `_10`：Surprise A `文字變成慢動作軌跡` ＋ Extension `基礎包＋Kahoot` 鎖定；Knowledge Lab 完成 → `VISUAL_GRAMMAR_SLIDE_ARCHITECTURE`
- `_11`：Visual Grammar / Slide Architecture 完成，43 cognitive scenes → `LESSON_BUDGET_FINAL_PAGE_LEDGER`
- `_12`：Lesson Budget Final + Page Ledger 完成，43 cognitive scenes 合法收斂為 38 physical slides / 280 min → `STORYBOARD`
- `_13`：38 張 Storyboard v01 完成，逐頁目的／教師與學生動作／構圖／Reveal／Text Anchor 均落地 → `STYLE_RECIPE`

不得回問已鎖定的 HOLD 2 / 2.5 / 2.6、Scenario A、Character A、Learner Role A、Book DNA A、Surprise A 或 Extension selection，除非教師明確 reopen 或上游變更使其失效。

---

## Upgrade / Rollback Resolution

所有 Drive 成品與可續跑半成品採 non-destructive versioning：

```text
{base}_v01.ext
{base}_v02.ext
{base}_v03.ext
```

硬規則：
- 不覆蓋舊檔。
- newest != active。
- Runtime 保存 explicit active refs。
- rollback 只切 active ref，不刪、不覆蓋、不重生。
- 約 24 個月可標 `REVIEW_DUE`，不得自動修改。
- shared character / style / Book DNA upgrade 必須明確 `KEEP_PINNED / UPGRADE / FORK / RETIRE_FROM_NEW_VERSION`。

---

## Drive / GitHub Authority Resolution

### GitHub
規則、技能、schema、Role stable spec、Style / Scenario / Character System、regression。

### Google Drive
所有實際成品、半成品、Runtime、核准角色長相、Style Reference、Book DNA evidence、Lesson Visual Identity Pack、NotebookLM 檔、預習單、短文單、題庫、簡報與 WIP。

### Character
- Bee signature 為 `ROLE-BEE-001` 專屬。
- 小澄只沿用 legacy boy visual lineage，不與「小樂」合併身份。
- isolated canonical face 仍須在 Gate B 前完成。

### Book DNA
Book DNA 保存整冊熟悉感；Lesson Skin 保存每課的新鮮感；Surprise Signature 保存每課特有的理解驚喜。Book DNA 不等於固定版型，也不包含 Bee signature。

---

## Live Runtime 13 Resolution

```yaml
title: V-MAX_State_四上_第一課_水陸小高手_13
document_id: 1D5bKaFNInGctynN988VxGSwMoVDV7S90xYf2PleUHAk
runtime_schema: 2.7-draft
workflow: 2.6-draft
manifest: 4.7-draft
executor: 1.8-draft
production_mode: SINGLE_LESSON_BUILD
current_stage: STYLE_RECIPE
last_completed_stage: STORYBOARD
renderer_status: BLOCKED_UNTIL_GATE_C
visual_seed_status: NOT_REQUIRED
```

Runtime Index v12 已 active 指向 `_13`；v11 與更早 Index、Runtime 全部保留。

目前已鎖：
- Gate A
- Scenario A：運動播報中心＋局部慢動作／特寫
- Character A：SINGLE_GUIDE＋小澄主播
- Learner Role A：動作觀察員
- Final Transfer：水陸小詩人
- Book DNA A：`ZH4A-HANDDRAWN-EXPLORER-01 / 自由手繪探險手帳`
- Surprise A：`L01-TEXT-TO-MOTION-TRACE / 文字變成慢動作軌跡`
- Extension：`基礎包＋Kahoot`

### Extension output queue
- PRESTUDY_WORKSHEET
- SHORT_READ_OR_SHORT_WRITING_WORKSHEET
- SUPPLEMENT_QUESTION_BANK
- KAHOOT_QUESTION_BANK

這四項是 formal deck 完成後的 derivatives，不新增七堂核心課時。平板互動、主題融合、跨域與 Project 目前 OFF。

### Drive refs
- Surprise v02 locked: `11P7ZsbcY9e8YKSsZDK8SU9S1WbukvOrY_tds2MXCmfs`
- Extension Check v01: `1-uOq9Zoj_bFFB37pkocRPadGH-4rs4RZzAaWhzQbYMs`
- Derivative Output Plan v01: `1gfJYGOO2Wl16_QIpffIvNgMiOmpIk0t8aXhMzOwwP8Y`
- Knowledge Lab v01: `1fcAwJbcqfYS2nsO7ZohGL2ByqVFSGdDhq35ebF8iyjE`
- Visual Grammar / Slide Architecture v01: `1PqHde5c0Hacah0eVQZK_c3dhXJFsx26LWr5cXLnT1c0`
- Lesson Budget Final v01: `1gzSLZLyVW-QYUKgd_Il0mO0M9LDGOaK17vw8QZC8gJA`
- Page Ledger v01: `1YALLfUv2HmxNwxi_bUjl-LGQxYO8s5rdcI2KfIzsmhg`
- Storyboard v01: `1ir8B4xVh4bCeOURIEagyfO-Y_KXdPy7uAXkRdBacmSw`

### Final core budget

```yaml
sessions: 7
minutes_per_session: 40
total_core_minutes: 280
cognitive_scenes: 43
physical_slides: 38
physical_slide_distribution: [5, 5, 5, 7, 6, 5, 5]
```

43 → 38 是 5 組合法的同頁認知合併，不是刪除教學內容：Question / Reveal、Compare / Conclusion、兩個簡單 2 字組雙區，以及 Transfer planning。

Storyboard v01 沒有增加任何裝飾頁；小澄只在 P01、P05、P07、P14、P22、P28、P33、P34、P38 九個 key moments 出現。

P25 `陀／駝 + 躍／耀` 只有在 Typography Lock 能維持大字辨識時成立；若不成立，必須 reopen Page Ledger，不得縮字硬塞。

---

## Save-on-Approval Rule

```text
任何 APPROVED / LOCKED / USABLE_WIP
→ SAVE AS NEW VERSION TO GOOGLE DRIVE
→ VERIFY DRIVE REFERENCE
→ UPDATE ACTIVE REF ONLY AFTER APPROVAL
→ 才可跨平台／跨天續跑
```

---

## Pre-seal Status

```yaml
technical_preseal: PASS
static_contract: PASS
asset_persistence: PASS
single_mode: PASS
batch_mode: PASS
rollback: PASS
migration_resume_guard: PASS
surprise_signature_teacher_confirmation: PASS_A
extension_check_teacher_confirmation: PASS_BASIC_PLUS_KAHOOT
extension_budget_guard: PASS_NO_CORE_TIME_ADDED
knowledge_lab_live: PASS_COMPLETE
visual_grammar_slide_architecture_live: PASS_COMPLETE
lesson_budget_final_live: PASS_280_MINUTES
page_ledger_live: PASS_38_PHYSICAL_SLIDES
storyboard_live: PASS_38_SLIDES_NO_DRIFT
live_runtime_transition: PASS_TO_STYLE_RECIPE
remaining:
  - STYLE_RECIPE
  - LESSON_SKIN_FINAL
  - TYPOGRAPHY_LOCK
  - ISOLATED_CANONICAL_FACE_ASSET_REQUIRED_BEFORE_GATE_B
  - GATE_B_AND_GATE_C
  - TEACHER_FINAL_V1_SEAL_APPROVAL
v1_sealed: false
```

NotebookLM Visual / Audio Source Pack 的更深設計仍為 `DEFERRED_NON_BLOCKING`；NotebookLM adapter output 不得成為視覺 Source of Truth。

---

## 核心金句

> GitHub 保存方法；Google Drive 保存工作。

> Migration 不讓老師重做已做過的決定，也不讓舊 evidence 冒充新 lock。

> 單課模式先完成正式簡報母體；derivatives 後製但共享同一 Identity Pack。

> 新版是新增，不是取代；Drive 留版本，Runtime 決定今天用哪一版。

> Bee signature 只屬於 Bee 老師。

> Book DNA 保存熟悉感；Lesson Skin 保存新鮮感；Surprise Signature 讓理解本身產生期待。

> 第一課目前合法進入 Style Recipe；Lesson Skin Final／Typography／Gate B／Renderer 仍不得飛站。
