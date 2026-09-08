# V-MAX Manifest 3.8.9

## Current Canonical Files

```yaml
vmax_manifest_version: 3.8.9
bootstrap: V-MAX_BOOTSTRAP.md
runtime_contract: runtime/lesson-state.md
front_door: { path: skills/vmax-teaching-skills/SKILL.md, current_version: 1.3 }
main_workflow: { path: core/governance/vmax-main-workflow.md, current_version: 2.6 }
executor: { path: skills/vmax-golden-path-executor/SKILL.md, current_version: 2.0 }
lesson_presentation_execution_rules: { path: core/governance/lesson-presentation-execution-rules.md, current_version: 1.5 }
text_layer_construction_policy: { path: core/presentation/text-layer-construction-policy.md, current_version: 1.2 }
classroom_language_page_rules: { path: skills/presentation-engine/references/classroom-language-page-rules.md, current_version: 1.4 }
slide_script_schema: { path: core/schemas/vmax/slide-script.schema.json, contract_version: object-composition-glyph-anchor-idiom-v2 }
render_request_schema: { path: skills/vmax-image-renderer/references/render-request-schema.md, current_version: 2.1 }
renderer_contract: { path: core/renderer/image-first-hybrid-renderer.md, current_version: 2.0 }
presentation_engine: { path: skills/presentation-engine/SKILL.md, current_version: 0.10.7 }
image_renderer: { path: skills/vmax-image-renderer/SKILL.md, current_version: 2.0 }
quality_gate: { path: core/quality/quality-gate-2.md, current_version: 3.0 }
```

## Object Composition
一般國語圖片式簡報採 `OBJECT_SCENE`；正式文字先占位，再配置場景、小插圖、角色、道具、標記與金句。完整大底圖＋反覆搬字 → `MONOLITHIC_BACKGROUND_REGRESSION`。

## Vocabulary Anchor
語詞標記綁定最終 Verified Text；任何文字 reflow 都使舊 anchor 失效。`PRE_LAYOUT` 可尚未量測；有語詞標記的 `RENDER_READY` 必須已有完整 glyph bbox、baseline、mark bbox 與 text layout revision。

## Idiom Application Resolution
成語頁 `page_family = IDIOM` 時 `IDIOM_APPLICATION_PLAN` REQUIRED。正式依賴方向：

`核准成語語意 → 四年級可懂短解釋 → 自然正確例句 → 例句人物／動作／情境 → visual composition`

禁止先決定圖片再扭曲例句。成語頁必須通過 `IDIOM_TEXT_PASS`、`IDIOM_HIERARCHY_PASS`、`IDIOM_EXAMPLE_READABILITY_PASS`、`IDIOM_EXAMPLE_NATURALNESS_PASS`、`IDIOM_EXAMPLE_VISUAL_MATCH_PASS`、`IDIOM_OBJECT_COMPOSITION_PASS`。

## Render Readiness Resolution
Render Request 正式區分 `PRE_LAYOUT` 與 `RENDER_READY`。只有 `RENDER_READY` 可進正式 Renderer。資料尚未量測或 page-family required plan 缺失，不得假裝 ready。

## Presentation Load Chain
Front Door 1.3 在簡報／視覺 stage 強制載入 Execution Rules、Presentation Engine、Classroom Language Rules、Canvas、Text Layer、Font Safety、Renderer Contract、Image Renderer、Render Request Schema、Quality Gate 與 Slide Script Schema，避免跨 AI 漏讀 canonical。

## Downstream Alignment
Execution Rules 1.5 / Presentation Engine 0.10.7 / Renderer Contract 2.0 / Image Renderer 2.0 / Quality Gate 3.0 / Text Layer 1.2 / Classroom Language 1.4 / Render Request 2.1 / Slide Script object-composition-glyph-anchor-idiom-v2 / Front Door 1.3。

## Canonical Golden Path
`SOURCE 0 → STEP 1 → HOLD 1 → STEP 2 → HOLD 2 → STEP 2.5 → HOLD 2.5 → STEP 2.6 → HOLD 2.6 → Teacher Intent Lock → Lesson Map → Session Map → Visual Strategy → Character/Cast → Knowledge Lab → Visual Grammar → Page Object Composition + Character + Key Line + Vocabulary/Idiom Plans → Style Matrix HOLD → Page Ledger → Representative Validation → Full Renderer → Asset Verification → Quality Gate → Delivery → Archive Verification`

## Runtime Authority
GitHub 保存規格；每課即時 Runtime State 以 Google Drive 為權威。不得以模型記憶或舊對話取代最新 Runtime State。

## 核心金句
> 底線跟著字走；成語圖跟著正確例句走；只有 RENDER_READY 才能正式施工。