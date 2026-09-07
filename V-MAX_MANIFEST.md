# V-MAX Manifest 3.8.6

## Current Canonical Files

```yaml
vmax_manifest_version: 3.8.6
bootstrap: V-MAX_BOOTSTRAP.md
runtime_contract: runtime/lesson-state.md
front_door: { path: skills/vmax-teaching-skills/SKILL.md, current_version: 1.2 }
main_workflow: { path: core/governance/vmax-main-workflow.md, current_version: 2.6 }
executor: { path: skills/vmax-golden-path-executor/SKILL.md, current_version: 2.0 }
lesson_presentation_execution_rules: { path: core/governance/lesson-presentation-execution-rules.md, current_version: 1.5 }
polyphonic_source_policy: { path: core/director/polyphonic-source-policy.md, current_version: 1.3 }
character_system: { path: core/character/character-system-2.md, current_version: 2.2 }
classroom_image_slide_policy: { path: core/presentation/classroom-image-slide-policy.md, current_version: 1.4 }
canvas_lock_policy: { path: core/presentation/canvas-lock-policy.md, current_version: 1.0 }
text_layer_construction_policy: { path: core/presentation/text-layer-construction-policy.md, current_version: 1.1 }
renderer_contract: { path: core/renderer/image-first-hybrid-renderer.md, current_version: 2.0 }
presentation_engine: { path: skills/presentation-engine/SKILL.md, current_version: 0.10.6 }
image_renderer: { path: skills/vmax-image-renderer/SKILL.md, current_version: 2.0 }
quality_gate: { path: core/quality/quality-gate-2.md, current_version: 2.8 }
```

## Object Composition Resolution

一般國語圖片式簡報採 `OBJECT_SCENE`：正式文字先占位，再配置場景、小插圖、角色、道具、標記與金句。完整大底圖＋反覆搬字 → `MONOLITHIC_BACKGROUND_REGRESSION`。

## Glyph-anchored Vocabulary Marking Resolution

語詞定位使用 `UNDERLINE_HIGHLIGHT`；整句／金句才使用核准 `BACKGROUND_HIGHLIGHT`。

每個語詞標記必須綁定**最終 Verified Text**：

```text
term_text + occurrence_index
→ line / char indices
→ glyph_bbox + baseline_y
→ mark_bbox
→ underline
```

不得用人工估算 x/y 或舊 render 座標定位。

任何字型、字級、字距、行距、欄寬、換行、文字位置或內容改變，皆更新 `text_layout_revision`；舊 glyph／mark anchors 全部失效並重新計算。

正式 failures：
- `VOCAB_HIGHLIGHT_COLLISION`
- `VOCAB_ANCHOR_FAIL`
- `STALE_VOCAB_MARK_ANCHOR`

正式 passes：
- `VOCAB_ANCHOR_PASS`
- `VOCAB_REFLOW_PASS`
- `VOCAB_MARK_ALIGNMENT_PASS`
- `VOCAB_MARK_SPAN_PASS`
- `VOCAB_MARK_LAYER_PASS`
- `TERM_COLOR_CONSISTENCY_PASS`

因此「食宿的線跑到學生可以」「女學堂的線跑到蔡阿信」不再視為可接受的小偏移，而是 `VOCAB_ANCHOR_FAIL`，不得交付。

下游一致版本：Execution Rules 1.5 / Presentation Engine 0.10.6 / Renderer Contract 2.0 / Image Renderer 2.0 / Quality Gate 2.8。

## Canonical Golden Path

```text
SOURCE 0 → STEP 1 → HOLD 1 → STEP 2 → HOLD 2 → STEP 2.5 → HOLD 2.5 → STEP 2.6 → HOLD 2.6
→ Teacher Intent Lock → Lesson Map → Supplement / Framework Decision → Session Map
→ Lesson Visual Map Strategy → Scenario Wrapper → Character Topology / Cast → Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Page-by-page Object Scene Composition + Character + Key Line + Vocabulary Mark + Scene Overlap Plan
→ Page-family Style Matrix / Style Recipe → HOLD
→ Page Estimate / Ledger → Representative Validation → Full Renderer
→ Actual Asset Verification → Quality Gate → Lesson Learning → Package Delivery → Google Drive Archive Verification
```

## Runtime Authority

GitHub 保存規格；每課即時 Runtime State 以 Google Drive 為權威。不得以模型記憶、舊對話或舊簡報取代最新 Runtime State。

## Version Resolution

版本不一致時重新 fetch；新 canonical 已升版而 Manifest 未更新 → `MANIFEST_STALE`；不得以舊 Manifest 覆蓋新 canonical。

## 核心金句

> 底線跟著字走，不是字跟著底線走。

> 字一換行，舊底線座標就作廢。