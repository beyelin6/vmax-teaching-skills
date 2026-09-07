# V-MAX Manifest 3.8.7

## Current Canonical Files

```yaml
vmax_manifest_version: 3.8.7
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
text_layer_construction_policy: { path: core/presentation/text-layer-construction-policy.md, current_version: 1.2 }
classroom_language_page_rules: { path: skills/presentation-engine/references/classroom-language-page-rules.md, current_version: 1.3 }
slide_script_schema: { path: core/schemas/vmax/slide-script.schema.json, contract_version: object-composition-glyph-anchor-v1 }
render_request_schema: { path: skills/vmax-image-renderer/references/render-request-schema.md, current_version: 2.0 }
renderer_contract: { path: core/renderer/image-first-hybrid-renderer.md, current_version: 2.0 }
presentation_engine: { path: skills/presentation-engine/SKILL.md, current_version: 0.10.6 }
image_renderer: { path: skills/vmax-image-renderer/SKILL.md, current_version: 2.0 }
quality_gate: { path: core/quality/quality-gate-2.md, current_version: 2.8 }
```

## Object Composition Resolution

一般國語圖片式簡報採 `OBJECT_SCENE`：正式文字先占位，再配置場景、小插圖、角色、道具、標記與金句。完整大底圖＋反覆搬字 → `MONOLITHIC_BACKGROUND_REGRESSION`。

`image_layout_plan` 只保留作 legacy compatibility summary；不得取代 `OBJECT_COMPOSITION_PLAN`。

## Glyph-anchored Vocabulary Marking Resolution

語詞定位使用 `UNDERLINE_HIGHLIGHT`；整句／金句才使用核准 `BACKGROUND_HIGHLIGHT`。

每個語詞標記必須綁定最終 Verified Text：

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

## Schema Alignment Resolution

`slide-script.schema.json` 現在正式接受並要求簡報頁的：
- `object_composition_plan`
- `character_plan`
- `key_line_plan`
- 適用時 `vocab_mark_plan`
- 適用時 `text_layout_revision`

因此 machine-readable validation 不得再因 `additionalProperties: false` 拒絕新版欄位。

`render-request-schema.md` v2.0 同步傳遞 Object Composition、Character、Key Line、Vocabulary Mark、glyph anchor、text layout revision 與六項 Vocabulary acceptance checks；不得在下游遺失。

## Font Safety Resolution

國語頁規則不再硬綁單一字型 family。字型選擇以 `traditional-chinese-font-safety` 的 font role、可取得字型、臺灣字形、glyph coverage、Bopomofo coverage 與 fallback QA 為唯一執行依據。

**字型 fallback / family change = text reflow**。任何 reflow 都使舊語詞 anchor 失效，必須重新量測 glyph bbox 並重算 mark bbox。

## Downstream Alignment

一致版本：
- Execution Rules 1.5
- Presentation Engine 0.10.6
- Renderer Contract 2.0
- Image Renderer 2.0
- Quality Gate 2.8
- Text Layer Construction Policy 1.2
- Classroom Language Page Rules 1.3
- Render Request Schema 2.0
- Slide Script Schema: object-composition-glyph-anchor-v1

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

> 字型是排版幾何的一部分；字型一換，舊 anchor 就作廢。