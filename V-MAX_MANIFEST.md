# V-MAX Manifest 3.8.8

## Current Canonical Files

```yaml
vmax_manifest_version: 3.8.8
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
classroom_language_page_rules: { path: skills/presentation-engine/references/classroom-language-page-rules.md, current_version: 1.4 }
slide_script_schema: { path: core/schemas/vmax/slide-script.schema.json, contract_version: object-composition-glyph-anchor-v1 }
render_request_schema: { path: skills/vmax-image-renderer/references/render-request-schema.md, current_version: 2.0 }
renderer_contract: { path: core/renderer/image-first-hybrid-renderer.md, current_version: 2.0 }
presentation_engine: { path: skills/presentation-engine/SKILL.md, current_version: 0.10.6 }
image_renderer: { path: skills/vmax-image-renderer/SKILL.md, current_version: 2.0 }
quality_gate: { path: core/quality/quality-gate-2.md, current_version: 2.9 }
```

## Object Composition Resolution

一般國語圖片式簡報採 `OBJECT_SCENE`：正式文字先占位，再配置場景、小插圖、角色、道具、標記與金句。完整大底圖＋反覆搬字 → `MONOLITHIC_BACKGROUND_REGRESSION`。`image_layout_plan` 只保留作 legacy compatibility summary；不得取代 `OBJECT_COMPOSITION_PLAN`。

## Glyph-anchored Vocabulary Marking Resolution

語詞定位使用 `UNDERLINE_HIGHLIGHT`；整句／金句才使用核准 `BACKGROUND_HIGHLIGHT`。每個語詞標記必須綁定最終 Verified Text：`term_text + occurrence_index → line/char indices → glyph_bbox + baseline_y → mark_bbox → underline`。任何文字 reflow 都使舊 anchor 失效並重新計算。

## Idiom Page Layout Resolution

成語頁不再允許固定「成語／解釋／例句」三個同等卡片或三欄講義。預設層級為：

`大成語 → 短解釋 → 大字例句＋情境圖`

插圖優先支援**例句中的實際用法／引申義**，而不是只畫成語字面。每頁建立 `idiom_application_plan`，讓成語、學生可懂解釋、例句、人物、動作與情境可追溯。

正式成語 passes：
- `IDIOM_TEXT_PASS`
- `IDIOM_HIERARCHY_PASS`
- `IDIOM_EXAMPLE_READABILITY_PASS`
- `IDIOM_EXAMPLE_VISUAL_MATCH_PASS`
- `IDIOM_OBJECT_COMPOSITION_PASS`

正式 failures：
- `IDIOM_LITERAL_IMAGE`
- `IDIOM_EXAMPLE_VISUAL_MISMATCH`

一頁兩成語只有在同一故事線、前後事件、對照或共享場景有可見關係時成立；否則拆頁。角色若參與例句，應融入情境，不作角落裝飾。

## Schema Alignment Resolution

`slide-script.schema.json` 正式接受並要求 `object_composition_plan`、`character_plan`、`key_line_plan`，適用時接受 `vocab_mark_plan` 與 `text_layout_revision`。`render-request-schema.md` v2.0 同步傳遞 Object Composition、Character、Key Line、Vocabulary Mark、glyph anchor 與 acceptance checks。

## Font Safety Resolution

國語頁規則不硬綁單一字型 family。字型選擇以 `traditional-chinese-font-safety` 的 font role、可取得字型、臺灣字形、glyph coverage、Bopomofo coverage 與 fallback QA 為執行依據。字型 fallback / family change = text reflow。

## Downstream Alignment

一致版本：Execution Rules 1.5 / Presentation Engine 0.10.6 / Renderer Contract 2.0 / Image Renderer 2.0 / Quality Gate 2.9 / Text Layer Construction Policy 1.2 / Classroom Language Page Rules 1.4 / Render Request Schema 2.0 / Slide Script Schema object-composition-glyph-anchor-v1。

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

> 成語頁的圖要讓學生看懂例句裡為什麼能用這個成語。