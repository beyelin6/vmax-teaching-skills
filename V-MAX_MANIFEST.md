# V-MAX Manifest 3.8.21

## Current Canonical Files

```yaml
vmax_manifest_version: 3.8.21
bootstrap: V-MAX_BOOTSTRAP.md
session_director: { path: core/director/session-director.md, current_version: 1.3 }
contextual_enrichment_policy: { path: core/director/contextual-enrichment-policy.md, current_version: 1.1 }
pedagogy_method_integration: { path: core/pedagogy/pedagogy-method-integration.md, current_version: 1.1 }
bootstrap_policy: { path: V-MAX_BOOTSTRAP.md, current_version: 1.6.2 }
lesson_master_preflight: { path: core/governance/lesson-master-preflight.md, current_version: 1.1 }
runtime_contract: runtime/lesson-state.md
runtime_contract_version: 2.4
working_handoff_area_policy: { path: core/governance/working-handoff-area-policy.md, current_version: 1.2 }
hold_teacher_interface_policy: { path: core/governance/hold-teacher-interface-policy.md, current_version: 1.7 }
recognition_only_character_policy: { path: core/governance/recognition-only-character-policy.md, current_version: 1.3 }
step1_source_anchor_policy: { path: core/governance/step1-source-anchor-policy.md, current_version: 1.9 }
chinese_textbook_transcriber: { path: skills/chinese-textbook-transcriber/SKILL.md, current_version: 0.4.4 }
presentation_preconstruction_policy: { path: core/governance/presentation-preconstruction-policy.md, current_version: 1.1 }
idiom_expression_policy: { path: core/director/idiom-expression-visualization-policy.md, current_version: 1.1 }
chatgpt_adapter: { path: adapters/chatgpt.md, current_version: 1.8 }
front_door: { path: skills/vmax-teaching-skills/SKILL.md, current_version: 1.6 }
chatgpt_work_launcher: { path: chatgpt-work/vmax-teaching-skills/SKILL.md, current_version: 1.7 }
main_workflow: { path: core/governance/vmax-main-workflow.md, current_version: "2.12" }
cloud_checkpoint_policy: { path: core/governance/cloud-checkpoint-policy.md, current_version: 1.1 }
executor: { path: skills/vmax-golden-path-executor/SKILL.md, current_version: 2.7 }
continuation_state_gate: { path: core/governance/continuation-state-gate.md, current_version: 1.5 }
google_drive_lesson_archive: { path: skills/google-drive-lesson-archive/SKILL.md, current_version: 1.1 }
lesson_presentation_execution_rules: { path: core/governance/lesson-presentation-execution-rules.md, current_version: 1.8 }
text_layer_construction_policy: { path: core/presentation/text-layer-construction-policy.md, current_version: 1.5 }
classroom_language_page_rules: { path: skills/presentation-engine/references/classroom-language-page-rules.md, current_version: 1.7 }
lesson_architecture_profile: { path: schemas/lesson-architecture-profile.md, current_version: 1.0 }
page_detail_confirmation_profile: { path: schemas/page-detail-confirmation-profile.md, current_version: 1.1 }
batch_construction_lock: { path: core/governance/batch-construction-lock.md, current_version: 1.3 }
paragraph_text_page_policy: { path: core/presentation/paragraph-text-page-policy.md, current_version: 1.0 }
character_library_writeback_policy: { path: core/character/character-library-writeback-policy.md, current_version: 1.0 }
slide_script_schema: { path: core/schemas/vmax/slide-script.schema.json, contract_version: object-composition-glyph-anchor-idiom-layout-v4-paragraph-placement }
render_request_schema: { path: skills/vmax-image-renderer/references/render-request-schema.md, current_version: 2.3 }
render_request_json_schema: { path: core/schemas/vmax/render-request.schema.json, contract_version: 1 }
renderer_contract: { path: core/renderer/image-first-hybrid-renderer.md, current_version: 2.0 }
presentation_engine: { path: skills/presentation-engine/SKILL.md, current_version: 0.10.15 }
image_renderer: { path: skills/vmax-image-renderer/SKILL.md, current_version: 2.4 }
quality_gate: { path: core/quality/quality-gate-2.md, current_version: 3.4 }
visual_drift_detector: { path: core/quality/visual-drift-detector.md, current_version: 1.2 }
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
Render Request 正式區分 `PRE_LAYOUT` 與 `RENDER_READY`。只有 `RENDER_READY` 可進正式 Renderer。資料尚未量測或 page-family required plan 缺失，不得假裝 ready。施工前不要求成品視覺 PASS；成品交付須驗證綁定 request／asset SHA-256 的 QA 回條。

## Presentation Load Chain
Front Door 1.6 在簡報／視覺 stage 強制載入 Execution Rules、Presentation Engine、Classroom Language Rules、Paragraph Text Page、Canvas、Text Layer、Font Safety、Renderer Contract、Image Renderer、Render Request Schema、Quality Gate 與 Slide Script Schema，避免跨 AI 漏讀 canonical。GitHub refresh 暫時失敗時，可信 LKG 以實際版本載入並標記 `GITHUB_REFRESH_PENDING`；沒有 LKG 才 `BOOTSTRAP_BLOCKED`。

## Downstream Alignment
Execution Rules 1.8 / Presentation Engine 0.10.15 / Renderer Contract 2.0 / Image Renderer 2.4 / Quality Gate 3.4 / Visual Drift 1.2 / Text Layer 1.5 / Classroom Language 1.7 / Paragraph Text Page 1.0 / Render Request 2.3 / Slide Script object-composition-glyph-anchor-idiom-layout-v4-paragraph-placement / Main Workflow 2.12 / Front Door 1.6 / ChatGPT Work Launcher 1.7。

## Lesson Architecture and Variants

每課先建立 `schemas/lesson-architecture-profile.md` 的 Baseline 教學骨架，再依教師選擇建立平板、四學公開課、議題融入或自訂變體。變體可以改寫教學活動與呈現方式，但必須逐項回指 Baseline 的學習結果；不得靜默遺失教師指定內容。

## Canonical Golden Path
`SOURCE 0 → STEP 1 → HOLD 1 → STEP 2 → HOLD 2 → STEP 2.5 → HOLD 2.5 → STEP 2.6 → HOLD 2.6 → Teacher Intent Lock → Lesson Map → Session Map → Visual Strategy → Character/Cast → Knowledge Lab → Visual Grammar → Page-family/Teaching-function Draft → Style Matrix HOLD → Character/Canvas Lock → Page Ledger Confirmation → PAGE_DETAIL_CONFIRMATION (Object Composition + Character + Key Line + Vocabulary/Idiom Plans) → Teacher HOLD → Representative Selection/Validation → Per-family Teacher HOLD → Small-batch Renderer → Per-batch Teacher HOLD → Asset Verification → Quality Gate → Delivery → Archive Verification`

## Runtime Authority
GitHub 保存規格；每課即時 Runtime State 以 Google Drive 為權威。不得以模型記憶或舊對話取代最新 Runtime State。

## 核心金句
> 底線跟著字走；成語圖跟著正確例句走；只有 RENDER_READY 才能正式施工。

## 國語簡報施工前確認與成語雙軌

共用規則版本 1.1：`core/governance/presentation-preconstruction-policy.md`。語文規劃與每次施工續作強制載入；「逐頁施工稿 → 停等確認 → 代表頁逐類驗證 → 小批次／逐批確認」不可跳過。每個正式生字的延伸成語判讀未完成即 `VOCABULARY_IDIOM_COVERAGE_INCOMPLETE`，不得施工。課文既有成語與生字補充成語為兩份必查清單；單課結果只存 Drive。

## STEP 1 完整擷取與階段邊界

Source Anchor Policy 1.9 是完整擷取與集中審核的 canonical：同 stage 的搜尋、逐頁／旁欄查核和存檔連續完成；必要缺口未解不得請求全文核准。Continuation State Gate 1.5 依目前階段套用前置條件，明確指定課次不被別課 active index 阻擋。教材多音字補充在 STEP 1 擷取，延伸選教與視覺鎖定依後段流程處理。

## ChatGPT Launcher 階段載入

Launcher 1.7 / Bootstrap 1.6.2 / ChatGPT Adapter 1.8：先同步當課 Runtime，再載入目前階段模組。SOURCE 0／STEP 1 不預載視覺施工規則；空的 next_allowed_stage 不阻擋階段內擷取。視覺呈現與局部修訂要求保留在 adapter，依 Runtime 階段執行。Plugin 版本取自 VERSION，不以 Launcher 版本代填。

## 來源續作與核准保留

Executor 2.7 / Source Anchor 1.9 / Recognition-only 1.3 / HOLD Interface 1.7 / Continuation State Gate 1.5：同步不另設 HOLD；正式認讀字與比較／多音字活動先分類再比對；核准來源僅因具體新證據修補受影響項目，不反覆重跑未變內容。Launcher 維持 1.7，從 main 按需載入本次修正。
