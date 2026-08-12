# V-MAX v1 Live Runtime Typography Lock Report

status: PASS_TO_GATE_B_CHECKPOINT_WITH_CHARACTER_ASSET_BLOCKER
lesson: 四上第一課〈水陸小高手〉
runtime_target: 16
completed_at: 2026-08-12

## Evidence
- Typography Bridge: `vmax-typography-bridge/SKILL.md` v1.1-draft
- Character Group Visual Comparison: `skills/character-group-visual-comparison/SKILL.md` v1.1-draft
- Storyboard v01 Drive ref: `1ir8B4xVh4bCeOURIEagyfO-Y_KXdPy7uAXkRdBacmSw`
- Lesson Skin Final v01 Drive ref: `1tRRGkcnwH6QPn8G-EP2LjLR8_zK8HhH-bZQ2nR-r3sY`
- Typography Lock v01 Drive ref: `1ciZL5YcL6eCq7IUm7aNygsUvfwJjFDicwCajFfUhRu8`

## Locked Rules
- T01 standard sans is the truth layer for BODY / QUESTION / official source text / teaching glyph / zhuyin.
- H1 may use T04 hand-writing only when verified Traditional Chinese glyph coverage is safe; otherwise fallback T02.
- Teaching glyph hard floor: 72 pt.
- Zhuyin hard floor: 22 pt.
- Teaching slide body hard floor: 24 pt.
- A4 derivative body: 14 pt preferred, 12 pt hard floor.
- Image-generated Chinese text is draft visual text, never Source Truth.

## P25 Fit Test
Target: `陀／駝 + 躍／耀` on one physical slide.

Result: `PASS_KEEP_SINGLE_SLIDE`.

Conditions:
- two independent 50/50 zones;
- each zone contains only two target glyphs, zhuyin, one core example/context per glyph, and one discrimination cue;
- target glyph 80–88 pt preferred, never below 72 pt;
- zhuyin 24–26 pt preferred, never below 22 pt;
- no extra character illustration or decorative background;
- if actual font mapping violates floors or creates zone interference, reopen Page Ledger and split P25 rather than shrink text.

## Runtime Transition
- `_15`: `TYPOGRAPHY_LOCK`
- `_16`: `GATE_B_EXPERIENCE_STORYBOARD_VISUAL_IDENTITY`
- last completed: `TYPOGRAPHY_LOCK`
- renderer: `BLOCKED_UNTIL_GATE_C`

## Gate B Blocker
Visual Identity Pack cannot become `FINAL_LOCKED` yet because the selected guide character 小澄主播 still lacks an approved isolated canonical face asset. Gate B remains blocked until that prerequisite is resolved and persisted to Google Drive.

## Regression Result
- typography DNA <= 3: PASS
- teaching glyph equal scale: PASS
- source truth guard: PASS
- no shrink-to-fit: PASS
- P25 density: PASS_KEEP_SINGLE_SLIDE
- cross-material 12 pt A4 floor: PASS
- illegal Gate B completion: NOT PERFORMED
- renderer jump: NOT PERFORMED
