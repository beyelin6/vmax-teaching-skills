# V-MAX v1 Live Runtime Storyboard Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
storyboard_generation: PASS
physical_slides_preserved: 38
session_distribution: [5, 5, 5, 7, 6, 5, 5]
page_ledger_drift: NONE
decorative_page_growth: NONE
source_text_reconstruction: FORBIDDEN_AND_RESPECTED
guide_overuse_check: PASS
bee_signature_isolation: PASS
typography_reopen_guard_p25: PRESERVED
runtime_transition: PASS_TO_STYLE_RECIPE
illegal_stage_jump_detected: false
lesson_skin_final_entered: false
typography_lock_entered: false
gate_b_entered: false
renderer_entered: false
```

## A. Drive Storyboard

- title: `L01_storyboard_v01`
- document id: `1ir8B4xVh4bCeOURIEagyfO-Y_KXdPy7uAXkRdBacmSw`
- folder: `02_逐頁腳本`
- status: `COMPLETE_READY_FOR_STYLE_RECIPE`

Storyboard covers P01–P38 and records for every physical slide:
- teaching purpose
- teacher move
- learner move
- composition
- text zone
- interaction / reveal state
- guide presence
- text anchor / source authority

## B. Storyboard invariants

- 38 physical slides remain unchanged from Page Ledger.
- Seven-session distribution remains `[5,5,5,7,6,5,5]`.
- No decorative transition slide was added.
- Question / Reveal remains a controlled overlay on the same base slide where specified.
- Slow-motion trace remains limited to learning-critical reading / comparison / recap pages.
- Character-group and idiom slides do not inherit unnecessary cinematic effects.

## C. Guide placement

Xiaocheng key moments are limited to:
`P01, P05, P07, P14, P22, P28, P33, P34, P38`.

Other pages may omit the Guide entirely.

## D. Text safety

High-risk official text is not reconstructed in the Storyboard. Exact source text remains deferred to the formal text layer and must read from:
- official PDF for source text / source sentence skeletons;
- approved LKB + official source refs for character groups, readings, zhuyin, and idioms.

`要言不煩` remains excluded from student-facing formal activities.

## E. Typography reopen guard

P25 keeps the approved dual-zone plan for `陀／駝 + 躍／耀` only conditionally.

If Typography Lock cannot preserve large, legible characters and necessary zhuyin, Page Ledger must reopen. Shrinking text to preserve 38 slides is forbidden.

## F. Runtime transition

New Drive runtime:
- `V-MAX_State_四上_第一課_水陸小高手_13`
- document id: `1D5bKaFNInGctynN988VxGSwMoVDV7S90xYf2PleUHAk`
- current stage: `STYLE_RECIPE`
- last completed stage: `STORYBOARD`

New Runtime Index:
- `V-MAX_Runtime_Index_v12`
- document id: `1LWpukiDfA8DaC3ZKVrJx3VEU0GO9XbqO6caqmnD-9N4`

Old Runtime `_12` and Index v11 remain preserved.

## G. Legal next step

`STYLE_RECIPE → LESSON_SKIN_FINAL → TYPOGRAPHY_LOCK → GATE_B`.

Renderer remains blocked until Gate C.

Result: `PASS_TO_STYLE_RECIPE`.
