# V-MAX Cross-AI Schema Package

This directory is the platform-neutral contract for V-MAX data objects.

The schemas are intended to be readable by Codex, ChatGPT, Gemini, Antigravity, Spark, and other tools that support JSON Schema Draft 2020-12.

Package baseline: `0.1.0`.

Package manifest: `package-manifest.yaml`.
Examples: `examples/`.
Migration policy: `migrations/README.md`.

## Rules

- Read this README before consuming a V-MAX object.
- Validate `object_type`, required fields, status, version, and provenance.
- Preserve `derived_from.direct_parent` and `derived_from.lineage`.
- Do not invent missing source text, teacher decisions, or schema meanings.
- An open HOLD blocks the dependent stage.
- Machine payload is a downstream contract; it is not a replacement for the teacher confirmation card.

## Schemas

- `source-master.schema.json`: source, text, markup, evidence, uncertainty, and lock state.
- `source-ingestion-record.schema.json`: page/region extraction log, complete captured text, coverage checks, and fingerprints.
- `candidate-inventory.schema.json`: complete textbook-grounded candidate inventory.
- `approved-teaching-selection.schema.json`: teacher-confirmed teaching scope.
- `hold-event.schema.json`: conflict and teacher-wait event.
- `revision-event.schema.json`: change impact and minimal rollback event.
- `status-transition.schema.json`: legal workflow transitions.
- `slide-script.schema.json`: page-by-page presentation source of truth.
- `output-manifest.schema.json`: downstream output inventory, version lineage, affected slides, platform status, and teacher confirmation state.
- `learning-module-profile.schema.json`: versioned learning extensions linked to approved selections and LKB.
- `teaching-strategy-profile.schema.json`: versioned teaching flow linked to approved selections, LKB, and Learning Modules.
- `role-selection-profile.schema.json`: approved base character, role function, and context variant reference.
- `style-selection-profile.schema.json`: approved style core and allowed page-family variants.

## Source layers

`OFFICIAL_TEXT`, `TEXTBOOK_MARKUP`, `PUBLISHER_TEACHER_RESOURCE`, `TEACHER_KNOWLEDGE`, `AI_SUGGESTION`, and `EXTENSION` are separate layers. They are not a single authority ranking. Field ownership determines precedence; same-field conflicts require a HOLD.

`SOURCE_INGESTION_RECORD` records what was scanned and captured from each source page. It is an evidence log, not a teaching decision. `coverage_check` may report `FOUND`, `NOT_FOUND`, `UNCERTAIN`, or `NOT_APPLICABLE`; `UNCERTAIN` does not permit an Agent to infer the missing content.

`CANDIDATE_INVENTORY` records what the source contains and what the AI recommends examining. It must not contain a teacher decision. `MUST_TEACH`, `OPTIONAL`, `DO_NOT_TEACH`, `EXTENSION`, and `HOLD` belong only in `APPROVED_TEACHING_SELECTION`, where `confirmed_by_teacher` is required.

`STATUS_TRANSITION` is a legal transition contract, not just an enum of labels. An unlisted from/to/actor combination is invalid; quality approval requires both a teacher confirmation reference and a QA summary.

## Legacy policy fields

Some older, policy-specific documents contain fields such as `teacher_decision`, `promotion.status`, or local `*_decision` values. Those fields remain available for the policy that defines them, but they are not the cross-AI approval source of truth. A decision that authorizes downstream V-MAX production must also be represented by the applicable `APPROVED_TEACHING_SELECTION`, confirmed companion profile, `HOLD_EVENT` resolution, or `STATUS_TRANSITION` object. If the old field and the portable object disagree, stop and create a HOLD; do not normalize the disagreement silently.
