---
name: vmax-education-document-design
description: Design, redesign, beautify, review, and produce elementary-school educational documents, worksheets, teaching materials, parent/class handbooks, and teaching slides. Use when the task requires teaching-aware information design, source fidelity, page planning, answer-space protection, controllable Traditional Chinese text, page-by-page production, teacher confirmation, or visual QA.
---

# V-MAX Education Document Design

Use this skill as the workflow controller for elementary-school educational document design. It is not a fixed template system.

## Core objective

Turn source content into an educational artifact that is correct, usable, readable, writable, teachable, printable/projectable, and visually coherent.

Priority when rules conflict:

1. Source fidelity and content correctness
2. Actual use function
3. Text clarity and safety
4. Information structure and reading order
5. Layout suitability
6. Visual consistency and aesthetics
7. Decoration

> Source → function → structure → Page Blueprint → layout → text → visual design → page production → teacher confirmation → QA → output.

Never start with a pretty image and then try to fit the text into it.

## Load references progressively

Read `references/core-design-spec.md` when the task involves page structure, layout, font-size safety, answer space, image/text integration, resolution, multi-page workflow, or QA.

Read `references/visual-typography-spec.md` when the task involves visual style, color language, typography, Chinese glyph style, title/body pairing, hand-drawn styling, or cross-page font consistency.

Do not copy examples or reference layouts mechanically. References provide judgment rules, not templates.

## Example routing

Use examples selectively. Do not load every example for every task.

Read `references/example-routing.md` when:
- the user asks for a redesign, beautification, visual direction, or representative page;
- a page repeatedly fails because of layout, density, image/text integration, or template-like appearance;
- you need to choose which Golden or Negative Example is relevant.

Golden Examples are **case evidence**, not templates. Extract the design logic that matches the current artifact's function, density, audience, and medium. Never copy a page's exact grid, palette, character position, card count, or title arrangement simply because it worked in the example.

Negative Examples are **failure-pattern references**. Use them to identify what to avoid and why. A negative example does not create a universal ban unless the underlying functional problem also exists in the current task.

Routing order:
1. Match artifact type and use context.
2. Match functional problem or design objective.
3. Match density and medium.
4. Prefer the smallest relevant set: normally 1 Golden Example and, when useful, 1 Negative Example.
5. If no example is a strong match, rely on K01/K02 rules rather than forcing an analogy.

## 1. Diagnose the task

Identify internally:
- artifact type: teaching-display / worksheet-writing / mixed / information-handbook / teacher-document
- audience and grade
- purpose and use context
- source format and required content
- size, orientation, page count, print/projection needs
- writing/answer requirements
- information density
- existing confirmed style, character, page plan, or approved pages

Do not ask again for information already available from the source or confirmed decisions.

If example guidance would materially improve the design, route to the closest matching example before selecting the visual system. Do not let the example override the source, Page Blueprint, or current user instruction.

Ask only when a missing answer materially changes content, function, size, page count, or a major visual direction.

## 2. Protect the source

Treat provided files and text as authoritative source material.

Do not invent, silently rewrite, omit, or alter questions, lesson text, names, dates, numbers, rules, contact information, or required fields.

If the source appears wrong or contradictory, identify the issue and ask before changing it.

For redesign/beautification tasks, beautification is not rewriting.

## 3. Build a Page Blueprint for multi-page work

Before producing a multi-page or high-density artifact, inventory the content and define P1, P2, P3…

For each page determine internally:
- purpose
- must-keep content
- primary/secondary information
- layout family
- density
- text strategy
- illustration strategy
- answer-space needs
- relationship to adjacent pages

Once confirmed, the Page Blueprint is a content contract. Do not silently redistribute or remove content later.

If the user explicitly asks to produce a specific page and the source, Blueprint, and visual system are already known, produce it directly.

## 4. Select layout from content relationships

Choose layout only after determining reading order and function.

Do not default to Bento, equal cards, 2×2 grids, fixed left-text/right-image, identical title placement, or repeated slide templates.

Use cards only for genuinely independent or parallel information. Keep continuous reading continuous.

Allow asymmetry and variable block sizes while maintaining invisible alignment and clear reading order.

> Let the frame fit the content, not the content fit the frame.

## 5. Protect educational usability

For student materials, answer space is core content, not leftover whitespace. Estimate expected response length and provide realistic writing, calculation, drawing, or composition space.

For parent documents, optimize scanability, grouping, and findability.

For teaching slides, prioritize projection readability, large text, and one clear teaching purpose per page rather than document-level density.

When content does not fit, reduce nonfunctional decoration, rebalance blocks, merge genuinely related information, adjust spacing, reselect the layout, or split the page before crossing safe text-size or answer-space limits.

## 6. Design text before illustration

Important Traditional Chinese text must remain controllable. Do not rely on image generation for titles, lesson text, questions, names, dates, numbers, phonetics, contact information, or other formal text.

Plan text region, size, line count, line spacing, alignment, and safety area before drawing containers or illustrations.

Use generated visuals for scenes, characters, objects, diagrams, textures, color blocks, borders, and decorative carriers; place formal text precisely afterward.

> Calculate the text first, then draw the container.

Controllable text must still feel integrated into the composition. Avoid generic PPT pasted-text appearance.

## 7. Apply the visual system

Use the visual/typography reference to choose an appropriate style language. Style and layout are separate decisions.

Keep cross-page system consistency through typography roles, colors, line language, illustration style, character specifications, title hierarchy, and page-number logic.

Allow composition, card count, image position, and text/image ratio to vary by page purpose.

> System consistent; layout varied.

If a representative page has been approved, lock its visual system for subsequent pages unless the user changes direction.

## 8. Produce multi-page image work one page at a time

For 2+ page PNG/JPG/image-style worksheets, handbooks, teaching materials, slides, or visual drafts:

> One page = one independent image.

Default workflow:
1. Produce only P1.
2. Run page QA.
3. Wait for review.
4. If the user says “下一頁”, lock the current page and produce only the next Blueprint page.

Never shrink multiple complete pages into one overview image as the formal deliverable. Never squeeze a multi-page plan into one page merely to finish in one generation.

“重做 P3” means only P3. “修改 P3 標題” means only that title and directly necessary dependent area.

Combine PDF/PPT or create an overview only after all pages are complete and the user requests it.

## 9. Respect modification scope

When the user identifies a local problem, fix that problem rather than redesigning unrelated approved content.

If the problem is structural and the page fundamentally fails, redesign that page instead of accumulating patches.

Generalize repeated feedback when appropriate, but do not turn a page-specific exception into a global rule without reason.

## 10. Teacher confirmation gates

Use only the necessary gates:

- Gate 1: overall direction, only when genuinely open
- Gate 2: Page Blueprint for multi-page/high-density work
- Gate 3: representative page / visual system; when useful, use one routed Golden Example as design evidence and one routed Negative Example as a failure check

After these are confirmed, use the loop:

> Produce → QA → teacher review → modify/pass → next page.

Do not ask for confirmation on every minor design decision.

## 11. QA before delivery

Check every page against three layers:

### Source QA
- no missing or invented information
- names, dates, numbers, Traditional Chinese, and source meaning correct
- Blueprint content fully represented

### Usability QA
- reading order clear
- real-size text readable
- answer space sufficient
- parent information findable
- projection/printing practical

### Visual/output QA
- one clear primary focus
- no overflow, clipping, drift, or image/text collision
- illustration supports rather than dominates content
- no excessive gridification or repeated template feel
- no obvious PPT pasted-text feel
- Chinese strokes and phonetics clear at final size
- output resolution suitable for the target medium
- no low-resolution upscale presented as true high resolution

For multi-page work also verify that approved pages remain unchanged and the visual system is consistent without making every page identical.

If a core QA item fails, fix it before presenting the page as complete.

## 12. Final decision test

Before completion ask internally:
- Is any source content missing or invented?
- Can the intended user actually use this page?
- Is the text clear at real output size?
- Is the layout caused by the content relationship rather than a favorite template?
- Is student writing space truly sufficient where required?
- Does the illustration help rather than compete?
- If decoration is removed, does the information structure still work?
- Does the work feel designed rather than typed onto a slide?
- For multi-page images, is each page still a full independent page?

A successful result preserves content and function, keeps formal Chinese clear, supports actual teaching/reading/writing, and achieves professional visual design without becoming template-driven.
