# Presentation Canvas 16:9 Migration

## Scope

This migration applies only to presentation outputs and visual slide assets. It does not change worksheet, prestudy worksheet, postlesson writing worksheet, or other non-presentation Output Profiles.

## New contract

- Presentation canvas: `16:9`
- Orientation: `LANDSCAPE`
- `STYLE_SELECTION_PROFILE.style_core.page_ratio` must be `16:9`.
- Slide Render Requests must use `output_spec.aspect_ratio: 16:9` with width greater than height.

## Migration behavior

- Existing 16:9 presentation records remain valid without recalculation.
- Existing presentation records with another ratio are preserved as historical versions and marked for teacher review before reuse.
- Do not resize or regenerate historical assets automatically.
- If a record mixes presentation and worksheet outputs, split the outputs by their existing Output Profiles before migrating.
- If the intended scope or source ratio is unclear, create a HOLD listing affected slides and wait for teacher decision.
