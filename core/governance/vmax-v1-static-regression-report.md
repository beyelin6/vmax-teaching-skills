# V-MAX v1 Static Contract Regression Report

Status: `STATIC_CONTRACT_PASS`

Next required status: `THREE_LESSON_TABLETOP_PENDING`

Live status: `END_TO_END_RUNTIME_RERUN_PENDING`

## 1. Scope

本報告只驗證 GitHub 上的 canonical contract 是否互相一致，不宣告 Google Drive Runtime 已實際完整重跑，也不宣告 v1 已封版。

對照版本：
- Main Workflow `2.4-draft`
- Golden Path Executor `1.6-draft`
- Runtime State Contract `2.5-draft`
- Manifest `3.1-draft`
- Experience Layer `1.3-draft`
- System Architecture `1.3-draft`
- Teaching Skill Selection `1.1-draft`
- Lesson Budget `1.1-draft`

---

## 2. Static Contract Checks

### S1｜One LKB Authority — PASS

Expectation:
- `chinese-lesson-knowledge-builder` owns LKB structure, source trace, node/version/validation.
- `lesson-knowledge-base-policy.md` owns downstream routing / spiral only.

Result: PASS.

No second LKB structure is allowed in Main Workflow, Executor, Runtime, Experience or compatibility helpers.

---

### S2｜Source Truth Before LKB / Approved LKB Before STEP 2 — PASS

Expected order:

```text
STEP 1
→ HOLD 1 Source Truth Confirm
→ LKB ASSEMBLY
→ LKB REVIEW
→ approved_lkb
→ STEP 2
```

Main Workflow / Executor / Runtime / Manifest are aligned.

Result: PASS.

---

### S3｜Teaching Skill Before Budget Draft — PASS

Expected order:

```text
learning difficulty
→ Teaching Skill Selection Lock
→ Lesson Budget Draft
→ Gate A
```

Budget Draft does not require or declare exact slide count.

Result: PASS.

---

### S4｜Budget Draft vs Budget Final — PASS

Expected:
- Draft before Gate A = time + MUST/SHOULD/COULD + cognitive tasks.
- Final / Page Ledger after Slide Architecture = actual pages + learning_gain.

Result: PASS.

No exact page count is required before Slide Architecture.

---

### S5｜Scenario Lock Before Character — PASS

Expected:

```text
Gate A
→ Scenario Decision / Candidates
→ SCENARIO LOCK
→ Character Topology / Cast Candidates
```

`SOURCE_WORLD` and `OFF` remain legal Scenario decisions; they still require the Scenario decision to be confirmed before Character selection.

Result: PASS.

---

### S6｜Character Lock Before Character DNA — PASS

Expected:

```text
Character Topology / Cast Candidates
→ CHARACTER LOCK
→ Character DNA / per-shot presence
```

Result: PASS.

Role Recommender was migrated to a helper that cannot bypass this dependency.

---

### S7｜Experience Does Not Rebuild Canonical Subsystems — PASS

Authority boundaries:
- Scenario = Registry / Selector / Teacher Lock
- Character = Character System / Scenario Character Bridge
- Style = Style Recipe Families
- Typography = Typography Bridge
- Experience = orchestration only

Result: PASS.

---

### S8｜Style Recipe Before Lesson Skin Final — PASS AFTER FIX

Conflict found during static audit:
- Earlier draft allowed `Lesson Skin` to appear in Experience Completion before the canonical Style Recipe was selected.
- This contradicted the definition of Lesson Skin as the lesson-specific concretization of a Style Recipe.

Fix applied:

```text
Visual Grammar / Slide Architecture
→ Page Ledger / Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative Visual
→ Gate C
```

Result after fix: PASS.

Failure now guarded as:
`LESSON_SKIN_BEFORE_STYLE_RECIPE / VISUAL_IDENTITY_INCOMPLETE_AT_GATE_B`.

---

### S9｜Gate B vs Gate C Responsibilities — PASS

Gate B locks a describable design contract:
- Scenario / Character refs
- Learner Role / Book DNA
- Style Recipe / Lesson Skin
- Typography direction
- Storyboard / Page Ledger

Gate C validates 1–2 actual representative pages.

Gate C confirmed → batch Renderer; no per-page repetition of the same art-direction approval.

Result: PASS.

---

### S10｜Teaching Skills Do Not Become Visual Tools — PASS

Teaching Skill Selection keeps COMPARE / INFER / STRUCTURE / STAGE / PROBLEM_LOOP / STORY_ARC / CHARACTER_EVIDENCE / TRANSFER / RETURN separate from ZOOM / SCALE / TIMELINE / Compare View / Cause Arrow and similar visual tools.

Result: PASS.

---

### S11｜Text Anchor / RETURN Boundary — PASS

Important reading instruction requires a Text Anchor.
RETURN remains conditional rather than mandatory on every page.

Result: PASS.

---

### S12｜Spiral Learning / Preview Reinforcement — PASS

Routing permits:
`PREVIEW → CORE_REINFORCE → RECOGNIZE → APPLY / TRANSFER`.

Preview exposure does not erase a high-value shape-similar or polyphonic focus from classroom teaching.

Result: PASS.

---

### S13｜Image-first Chinese Text + QA — PASS

Contract permits AI-generated integrated Traditional Chinese typography while requiring final Text / Typography QA.

P0 high-risk instructional text remains protected; local text errors prefer local repair instead of full-page regeneration.

Result: PASS.

---

### S14｜Compatibility Helpers Cannot Revive Parallel Workflow — PASS

Migrated helpers:
- Course Orchestrator → project version / patch / variant router
- Decision Engine → teaching-direction helper
- Role Recommender → character candidate helper after Scenario Lock
- Style Recommender → Style Recipe candidate helper
- Presentation Engine → locked-output mapping helper

Legacy 10-gate workflow file is now compatibility reference only.

Result: PASS.

---

### S15｜Runtime Is Progress Authority, GitHub Is Rule Authority — PASS

GitHub keeps schemas/policies; Google Drive Runtime keeps each lesson's actual state.

Legacy project-status or model memory cannot override Runtime.

Result: PASS at contract level.

Actual Drive Runtime behavior still requires a live rerun.

---

## 3. Static Golden Path Alignment

The following order is consistent across the canonical contract set:

```text
SOURCE 0
→ STEP 1
→ HOLD 1
→ LKB ASSEMBLY
→ LKB REVIEW
→ STEP 2 / HOLD 2
→ STEP 2.5 / HOLD 2.5
→ STEP 2.6 / HOLD 2.6
→ Teacher Intent
→ Lesson / Session / LVM
→ Teaching Skill Lock
→ Budget Draft
→ Gate A
→ Scenario / Scenario Lock
→ Character / Character Lock
→ Experience Completion
→ Extension
→ Knowledge Lab
→ Slide Architecture
→ Budget Final / Page Ledger
→ Storyboard
→ Style Recipe / Lesson Skin / Typography
→ Gate B
→ Representative Visual
→ Gate C
→ Renderer
→ Text / Typography QA
→ Quality / Delivery / Archive
```

Result: `STATIC_CONTRACT_PASS`.

---

## 4. What This Report Does NOT Prove

This report does not prove:
- Google Drive Runtime documents already contain the new 2.5 state shape.
- A real lesson can traverse every HOLD / Lock / Gate without interface friction.
- Renderer and Text QA have been exercised on a new full lesson under this exact contract.
- NotebookLM Visual / Audio Source Pack design is complete.

Therefore V-MAX v1 must remain `draft`.

---

## 5. Next Required Regression

1. Three-lesson tabletop rerun: Lessons 9 / 11 / 12.
2. Confirm different genres choose different minimum skill sets.
3. Verify Scenario / Character locks and two-stage Budget behavior in all three.
4. Then perform at least one live/runtime rerun using Google Drive Runtime.

Final sealing condition:

`STATIC_CONTRACT_PASS + THREE_LESSON_TABLETOP_PASS + LIVE_RUNTIME_RERUN_PASS + TEACHER_APPROVAL`
