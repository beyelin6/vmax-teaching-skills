# V-MAX Live Runtime Compatibility Audit

Status: `LIVE_RUNTIME_READ_AUDIT_PASS_WITH_MIGRATION_REQUIRED`

Write status: `NO_DRIVE_MUTATION_PERFORMED`

## 1. Live objects inspected

Google Drive Runtime Index:
- title: `V-MAX_Runtime_Index`
- registry version: `1.0`
- active lesson: `zh-4a-l01-water-land-athletes`
- active state: `V-MAX_State_四上_第一課_水陸小高手_02`
- active runtime version: `02`

Active state top metadata:
- `runtime_schema_version: 2.1`
- `workflow_version: 2.0`
- `manifest_version: 2.5`
- `executor_version: 1.2`
- `test_mode: TEST_FREEZE`

Current canonical GitHub contract:
- Runtime `2.5-draft`
- Main Workflow `2.4-draft`
- Manifest `3.2-draft`
- Executor `1.6-draft`

Conclusion: live Drive state predates the v1 integration changes and requires migration or fresh rerun before it can claim canonical compliance.

---

## 2. Active state observed

Top-level state reports:

```yaml
current_stage: HOLD_REPRESENTATIVE_VALIDATION
last_completed_stage: REPRESENTATIVE_VALIDATION_SAMPLES
teacher_confirmation_status: WAITING_CONFIRMATION
next_allowed_stage:
  - FULL_RENDERER
```

Existing locked decisions include:
- source anchor confirmed
- step2 teaching value confirmed
- step2.5 language scope confirmed
- step2.6 idiom expression confirmed
- teacher intent confirmed
- lesson map confirmed
- supplement framework confirmed
- session map confirmed
- lesson visual map strategy confirmed
- scenario confirmed
- character confirmed
- knowledge lab confirmed
- visual style confirmed

Therefore the old runtime contains meaningful validated history and must not be overwritten.

---

## 3. Compatibility problem

The same Google Doc also contains historical stage sections whose local `status` values still say forms such as `PROPOSED_WAITING_CONFIRMATION`, even though the top-level state has advanced much further.

This indicates the old state file functions partly as:
- current state snapshot
- append-only decision/history log

The new Runtime 2.5 contract expects a clearer normalized current-state structure with explicit fields for:
- approved LKB
- Teaching Skill Selection Lock
- Lesson Budget Draft
- Gate A
- Scenario Lock
- Character Lock
- Lesson Budget Final / Page Ledger
- Storyboard
- Style Recipe / Lesson Skin / Typography Lock
- Gate B
- Representative Visual / Gate C
- Text / Typography QA

If an executor reads old inner historical statuses as current truth, stage resolution may become ambiguous.

Risk codes:
- `RUNTIME_SCHEMA_DRIFT`
- `STALE_INNER_STATUS_AMBIGUITY`
- `MISSING_NEW_GATE_FIELDS`
- `LEGACY_STATE_FALSE_CONTINUATION`

---

## 4. Migration rule

Do NOT mutate `_02` in place.

Recommended migration:

```text
V-MAX_State_四上_第一課_水陸小高手_02
→ preserve as historical runtime
→ create _03 migration/rerun state
→ map only explicitly confirmed old locks
→ mark unavailable new fields as MIGRATION_REVIEW_REQUIRED
→ run canonical review from earliest uncertain dependency
```

### Safe mappings
Old explicit confirmed fields can map to references such as:
- source_anchor → confirmed
- teacher_intent → confirmed
- lesson_map / session_map / LVM → confirmed references
- old scenario confirmed → Scenario historical selection reference
- old character confirmed → Character historical selection reference
- old visual_style confirmed → historical style reference

### Must NOT be silently inferred as confirmed
Because old schema did not contain the new contract explicitly, do not automatically mark as confirmed:
- `approved_lkb`
- Teaching Skill Selection Lock under current policy
- Lesson Budget Draft under current policy
- Gate A under current semantics
- Scenario Lock under current teacher-lock semantics
- Character Lock under current topology/cast semantics
- Budget Final / Page Ledger under current learning_gain rule
- Gate B with current Visual Identity semantics
- Gate C with current representative-page semantics

Old evidence can be used to accelerate review, but confirmation must be explicit or tagged `MIGRATION_INFERRED_NEEDS_REVIEW`.

---

## 5. Recommended live rerun strategy

For the first real v1 runtime regression, use the active Lesson 1 because:
- source file and prior state already exist
- old confirmed work gives comparison evidence
- TEST_FREEZE history is available
- migration can be non-destructive

Suggested `_03` flow:

1. Create new Runtime 2.5 state with `test_mode: TEST_FREEZE`.
2. Reference `_02` as `migrated_from_runtime_version: 02`.
3. Preserve source truth references.
4. Re-establish `approved_lkb` under current canonical LKB contract.
5. Rerun Teaching Skill Selection + Budget Draft → Gate A.
6. Rerun Scenario decision / Scenario Lock.
7. Rerun Character topology/cast / Character Lock.
8. Continue through Slide Architecture / Page Ledger / Style / Gate B / Representative / Gate C.
9. Stop before destructive/full Renderer if the purpose is workflow validation only.
10. Mark `LIVE_RUNTIME_RERUN_PASS` only if state transitions and teacher-interface pointers are coherent.

---

## 6. Why not resume directly at FULL_RENDERER

Although `_02` says `next_allowed_stage: FULL_RENDERER`, that next step belonged to the older workflow semantics.

Current v1 changed:
- LKB approval requirement
- Teaching Skill / Budget sequence
- Scenario / Character micro-locks
- Gate B visual identity semantics
- Lesson Skin timing

Therefore directly rendering would test the old pipeline, not the new v1 pipeline.

---

## 7. Verdict

```yaml
live_runtime_read_audit:
  runtime_index_read: PASS
  active_state_read: PASS
  schema_version_match: FAIL_EXPECTED_LEGACY
  destructive_write: NOT_PERFORMED
  migration_required: true
  live_runtime_rerun: PENDING
```

This is not a v1 runtime failure. It is a migration requirement caused by the active lesson state predating the new canonical contract.

## Core sentence

> 舊 Runtime 要保留成歷史證據；v1 的第一次 live test 應建立新版本重跑，而不是假裝舊 state 已經符合新 schema。
