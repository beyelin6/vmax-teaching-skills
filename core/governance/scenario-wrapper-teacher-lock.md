# V-MAX Scenario Wrapper Teacher Lock 1.0

## Status

`CONFIRMED_AND_LOCKED`

Teacher confirmation: 2026-08-08

This file records four system-level decisions confirmed by the teacher. They override AI preference, historical defaults, renderer convenience, and legacy style-library behavior.

---

## LOCK-01｜Wrapper Families are evolvable core

The current 12 Wrapper Families are the working core, not a permanent closed list.

Rules:
- Prefer adding a Variant to an existing Family.
- Propose a new Family only when core student action, world logic, and pacing are materially different.
- AI may propose a new Family but may not promote it into core without teacher confirmation.

---

## LOCK-02｜Teacher confirmation point

Scenario Wrapper selection happens after Lesson Map and instructional-value judgment, and before Character Topology and visual style.

```text
Source Anchor
→ Lesson Map
→ AI Enrichment / Instructional Value Judgment
→ Scenario Wrapper Candidates (1–3, OFF allowed)
→ TEACHER CONFIRM / LOCK
→ Character Topology
→ Character Registry Retrieval
→ Visual Grammar
→ Style Recipe
→ Renderer
```

Once locked for a lesson, downstream systems may not silently replace the Wrapper.

---

## LOCK-03｜Student character reveal is optional

Teacher-facing design may reveal the selected character before class.
Student-facing reveal may happen through:
- preview worksheet easter egg,
- opening slide,
- formal reveal page,
- immediate appearance,
- or no reveal mechanic.

Do not turn character guessing into a required recurring ritual.

---

## LOCK-04｜Teacher owns promotion authority

Lesson learning may record evidence for Wrapper, Variant, Character, and visual strategy reuse.

AI may recommend:
- KEEP
- LIMIT
- RETIRE
- PROMOTE

But only the teacher may approve promotion to `REUSABLE_CONFIRMED`.

Single-use popularity, visual attractiveness, or engagement is not sufficient for automatic promotion.
Teaching benefit and repeatable fit must also be considered.

---

## Non-negotiable precedence

```text
Teacher Intent / Teacher Lock
> Confirmed Lesson Design
> Director Recommendation
> Registry Prior
> Historical Success
> Renderer Convenience
```

If any downstream tool conflicts with these locks, the downstream output must be revised rather than changing the lock silently.
