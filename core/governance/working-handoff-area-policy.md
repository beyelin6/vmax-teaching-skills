# Working Handoff Area Policy

Version: 1.1

## Purpose

Intermediate confirmation records, trial renders, layout drafts, revision logs, and continuation notes must be kept in one lesson-specific working area until the lesson package is complete. This area is the handoff source for ChatGPT, Codex, Antigravity, and other V-MAX adapters.

## Placement with the existing lesson folders

Do not replace the existing six output folders (`01_教材整理` through `06_延伸教材`). Add one working folder beside them:

```text
03_分課教學簡報與教材/
└─ 03_第三課_我的籃球夢/
   ├─ 00_施工中_接續區/
   │  ├─ 00_CURRENT_目前進度.md
   │  ├─ 01_內容分析/
   │  ├─ 02_教師確認/
   │  ├─ 03_版面配置/
   │  ├─ 04_代表頁試做/
   │  ├─ 05_修正紀錄/
   │  └─ 99_歷史版本/
   ├─ 01_教材整理/
   ├─ 02_逐頁腳本/
   ├─ 03_NotebookLM/
   ├─ 04_角色視覺/
   ├─ 05_簡報成品/
   └─ 06_延伸教材/
```

The six numbered folders remain the canonical output structure. The `00_施工中_接續區` is only for unfinished work and must not be used as a final deliverable location.

## Current pointer and naming

`00_CURRENT_目前進度.md` is the single current pointer. It records the active stage, latest teacher decision, latest file for each artifact type, blocked items, and next permitted action.

Use:

```text
{lesson_id}__{artifact}__v{NN}__{STATUS}.{ext}
```

Allowed statuses: `DRAFT`, `TEACHER_REVIEW`, `LOCKED`, `APPROVED`, `SUPERSEDED`. Superseded files stay in `99_歷史版本`; an old draft must never be the unlabelled current file.

## Continuation read order

Every resume or cross-platform handoff reads:

```text
Runtime State
→ 00_施工中_接續區/00_CURRENT_目前進度.md
→ Lesson Execution Rules
→ latest teacher confirmation
→ latest layout brief / style matrix
→ current Slide Script or worksheet plan
→ approved artifacts and visual assets
→ 99_歷史版本 only for audit
```

If the current pointer, lesson ID, or latest confirmation cannot be verified, stop with `WORKING_HANDOFF_BLOCKED`; do not infer the next action from conversation memory.

## Incremental filing rule

The working area is created at the start of every presentation task, not at the end. After each stage, the executor must save the discussion result before moving to the next stage and update `00_CURRENT_目前進度.md`.

| Stage output | Working folder |
|---|---|
| content analysis, candidate inventory, source decisions | `01_內容分析/` |
| teacher choices, execution rules, violation checklist, holds | `02_教師確認/` |
| style recommendation, page-family matrix, layout brief | `03_版面配置/` |
| representative-page plan and trial render | `04_代表頁試做/` |
| revision requests, QA results, decision history | `05_修正紀錄/` |
| replaced or superseded files | `99_歷史版本/` |

No stage may exist only in chat. If a stage produces no file, the current pointer must explicitly record `NO_FILE_REQUIRED` and the reason. A handoff is not complete until the pointer and the latest stage file are both saved and readable.

## Current pointer minimum fields

Every `00_CURRENT_目前進度.md` must contain:

```yaml
lesson_id: G4_L03
active_stage: TEACHER_REVIEW
latest_decision_file: 02_教師確認/...
latest_layout_file: 03_版面配置/...
latest_trial_file: 04_代表頁試做/...
blocked_items: []
next_allowed_action: ...
last_updated: YYYY-MM-DD
```

## Completion

When the lesson package is approved, publish final artifacts into the existing six canonical folders. Retain the working records in:

```text
98_已完成施工紀錄/{lesson_id}_{lesson_name}/
```

The Artifact Registry links final artifacts to their working records through `derived_from` and `source_artifact_refs`. A new semester or course uses a new lesson-specific folder and its own current pointer.
