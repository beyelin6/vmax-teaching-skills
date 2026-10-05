# V-MAX Manifest 3.10.4

## Current Canonical Files

```yaml
vmax_manifest_version: 3.10.4
bootstrap: V-MAX_BOOTSTRAP.md
claude_launcher: { path: launchers/vmax-teaching-skills-claude/SKILL.md, current_version: "1.0" }
antigravity_launcher: { path: launchers/vmax-teaching-skills-antigravity/SKILL.md, current_version: "1.0" }
antigravity_adapter: { path: adapters/antigravity.md, current_version: "1.2" }
course_orchestrator: { path: skills/vmax-course-orchestrator/SKILL.md, current_version: "0.6.1" }
character_group_comparison: { path: skills/character-group-visual-comparison/SKILL.md, current_version: "1.5.1" }
font_safety: { path: skills/traditional-chinese-font-safety/SKILL.md, current_version: "1.2.3" }
lesson_delivery: { path: skills/lesson-package-delivery/SKILL.md, current_version: "1.6.1" }
portable_runtime_policy: { path: core/governance/portable-runtime-policy.md, current_version: "1.1" }
claude_adapter: { path: adapters/claude.md, current_version: "1.1" }
knowledge_lab_ordering: { path: core/director/knowledge-lab-ordering-policy.md, current_version: "1.10" }
lesson_knowledge_builder: { path: skills/chinese-lesson-knowledge-builder/SKILL.md, current_version: "0.3.5" }
learning_module_builder: { path: skills/learning-module-builder/SKILL.md, current_version: "0.2.1" }
teaching_strategy_builder: { path: skills/teaching-strategy-builder/SKILL.md, current_version: "0.2.1" }
role_recommender: { path: skills/role-recommender/SKILL.md, current_version: "0.2.1" }
style_recommender: { path: skills/style-recommender/SKILL.md, current_version: "0.2.1" }
prestudy_worksheet: { path: skills/prestudy-worksheet/SKILL.md, current_version: "1.6.1" }
short_writing_worksheet: { path: skills/postlesson-short-writing-worksheet/SKILL.md, current_version: "1.4.1" }
chinese_visual_presentation_workflow: { path: core/governance/chinese-visual-presentation-workflow.md, current_version: "1.3" }
teacher_review_view: { path: core/ui/teacher-review-view-contract.md, current_version: "1.3" }
representative_page_selection: { path: schemas/representative-page-selection-profile.md, current_version: 1.1 }
session_director: { path: core/director/session-director.md, current_version: "1.5" }
contextual_enrichment_policy: { path: core/director/contextual-enrichment-policy.md, current_version: "1.2" }
pedagogy_method_integration: { path: core/pedagogy/pedagogy-method-integration.md, current_version: "1.2" }
bootstrap_policy: { path: V-MAX_BOOTSTRAP.md, current_version: "1.8.1" }
lesson_master_preflight: { path: core/governance/lesson-master-preflight.md, current_version: 1.1 }
runtime_contract: runtime/lesson-state.md
runtime_contract_version: 2.6
working_handoff_area_policy: { path: core/governance/working-handoff-area-policy.md, current_version: "1.4" }
hold_teacher_interface_policy: { path: core/governance/hold-teacher-interface-policy.md, current_version: "2.0" }
recognition_only_character_policy: { path: core/governance/recognition-only-character-policy.md, current_version: 1.3 }
step1_source_anchor_policy: { path: core/governance/step1-source-anchor-policy.md, current_version: "1.10" }
chinese_textbook_transcriber: { path: skills/chinese-textbook-transcriber/SKILL.md, current_version: "0.4.6" }
presentation_preconstruction_policy: { path: core/governance/presentation-preconstruction-policy.md, current_version: "1.5" }
idiom_expression_policy: { path: core/director/idiom-expression-visualization-policy.md, current_version: "1.2" }
chatgpt_adapter: { path: adapters/chatgpt.md, current_version: "1.14" }
front_door: { path: skills/vmax-teaching-skills/SKILL.md, current_version: "1.9.1" }
chatgpt_work_launcher: { path: chatgpt-work/vmax-teaching-skills/SKILL.md, current_version: "2.1" }
main_workflow: { path: core/governance/vmax-main-workflow.md, current_version: "3.2" }
cloud_checkpoint_policy: { path: core/governance/cloud-checkpoint-policy.md, current_version: 1.2 }
executor: { path: skills/vmax-golden-path-executor/SKILL.md, current_version: "3.1.1" }
continuation_state_gate: { path: core/governance/continuation-state-gate.md, current_version: "1.9" }
google_drive_lesson_archive: { path: skills/google-drive-lesson-archive/SKILL.md, current_version: 1.1.1 }
lesson_presentation_execution_rules: { path: core/governance/lesson-presentation-execution-rules.md, current_version: "1.9" }
text_layer_construction_policy: { path: core/presentation/text-layer-construction-policy.md, current_version: 1.6 }
classroom_language_page_rules: { path: skills/presentation-engine/references/classroom-language-page-rules.md, current_version: 1.9 }
lesson_architecture_profile: { path: schemas/lesson-architecture-profile.md, current_version: 1.2 }
page_detail_confirmation_profile: { path: schemas/page-detail-confirmation-profile.md, current_version: "1.5" }
batch_construction_lock: { path: core/governance/batch-construction-lock.md, current_version: "1.5" }
paragraph_text_page_policy: { path: core/presentation/paragraph-text-page-policy.md, current_version: 1.1 }
character_library_writeback_policy: { path: core/character/character-library-writeback-policy.md, current_version: "1.1" }
slide_script_schema: { path: core/schemas/vmax/slide-script.schema.json, contract_version: object-composition-glyph-anchor-idiom-layout-v4-paragraph-placement }
render_request_schema: { path: skills/vmax-image-renderer/references/render-request-schema.md, current_version: 2.3 }
render_request_json_schema: { path: core/schemas/vmax/render-request.schema.json, contract_version: 1 }
renderer_contract: { path: core/renderer/image-first-hybrid-renderer.md, current_version: 2.1 }
presentation_engine: { path: skills/presentation-engine/SKILL.md, current_version: "0.13.0" }
image_renderer: { path: skills/vmax-image-renderer/SKILL.md, current_version: "2.10.1" }
quality_gate: { path: core/quality/quality-gate-2.md, current_version: 3.6 }
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
Front Door 1.9.1 依 Portable Runtime Policy 按階段載入；快照不變且原文仍在時重用。完整包支援 BUNDLED，完整 checkout 支援 REPOSITORY，輕量入口使用 REMOTE／可信 LKG。真正施工才載入適用 Renderer／QA／schema，VP1 不載視覺鏈，VP3 不提前要求 VP4 資產。

## Downstream Alignment
Execution Rules 1.9 / Presentation Engine 0.12.1 / Renderer Contract 2.1 / Image Renderer 2.10.1 / Quality Gate 3.5 / Visual Drift 1.2 / Text Layer 1.6 / Classroom Language 1.9 / Paragraph Text Page 1.1 / Render Request 2.3 / Slide Script object-composition-glyph-anchor-idiom-layout-v4-paragraph-placement / Main Workflow 3.2 / Front Door 1.9.1 / ChatGPT Work Launcher 2.1。

## Lesson Architecture and Variants

每課先建立 `schemas/lesson-architecture-profile.md` 的 Baseline 教學骨架，再依教師選擇建立平板、四學公開課、議題融入或自訂變體。變體可以改寫教學活動與呈現方式，但必須逐項回指 Baseline 的學習結果；不得靜默遺失教師指定內容。

## Canonical Golden Path

國語視覺簡報預設依 `core/governance/chinese-visual-presentation-workflow.md`：

```text
VP1_COURSE_REVIEW｜完整課程內容（來源＋語文＋四層次閱讀，集中審核）
→ VP2_DESIGN_REVIEW｜課程調整與視覺方案（集中審核）
→ VP3_PAGE_PLAN_REVIEW｜完整逐頁文字與配置（存 Drive，集中審核）
→ VP4_CHARACTER_REVIEW｜角色視覺定稿／沿用與資產綁定
→ VP5_REPRESENTATIVE_REVIEW｜代表頁組審核，逐類記錄
→ VP5_BATCH_REVIEW｜一次一批製作與審核，核准後才下一批
→ VP_COMPLETE｜品質、交付與歸檔
```

完整課程內容包含四層次閱讀策略與提問；預習單／短文單在內容核准後分支製作。SOURCE／STEP 2／2.5／2.6、Lesson Map、Coverage 為大階段內部工作，不另開小步 HOLD。DETAILED_LESSON 保留細分任務規則。

## Runtime Authority
GitHub 保存規格；每課即時 Runtime State 以 Google Drive 為權威。不得以模型記憶或舊對話取代最新 Runtime State。

## 核心金句
> 底線跟著字走；成語圖跟著正確例句走；只有 RENDER_READY 才能正式施工。

## 國語簡報施工前確認與成語雙軌

共用規則版本 1.5：`core/governance/presentation-preconstruction-policy.md` 是施工前確認、續作、已核准項目保留、批次大小及局部修正的詳細規則唯一來源。語文規劃與每次施工續作強制載入；「逐頁施工稿 → 停等確認 → 代表頁逐類驗證 → 小批次／逐批確認」不可跳過。每個正式生字的延伸成語判讀未完成即 `VOCABULARY_IDIOM_COVERAGE_INCOMPLETE`，不得施工。課文既有成語與生字補充成語為兩份必查清單；單課結果只存 Drive。

## STEP 1 完整擷取與階段邊界

Source Anchor Policy 1.10 是完整擷取與集中審核的 canonical：同 stage 的搜尋、逐頁／旁欄查核和存檔連續完成；必要缺口未解不得請求全文核准。Continuation State Gate 1.7 依目前階段套用前置條件，明確指定課次不被別課 active index 阻擋。教材多音字補充在 STEP 1 擷取，延伸選教與視覺鎖定依後段流程處理。

## ChatGPT Launcher 階段載入

Launcher 1.9 / Bootstrap 1.7.0 / ChatGPT Adapter 1.12：先按同一 GitHub commit 讀取規格並同步當課 Runtime，再顯示 LOAD 回條及開始分析。SOURCE 0／STEP 1 不預載視覺施工規則；空的 next_allowed_stage 不阻擋階段內擷取。平台能力留在 adapter，施工流程由共用政策提供。Plugin 版本取自 VERSION，不以 Launcher 版本代填。

## 來源續作與核准保留

Executor 3.0 / Source Anchor 1.10 / Recognition-only 1.3 / HOLD Interface 2.0 / Continuation State Gate 1.7：同步不另設 HOLD；正式認讀字與比較／多音字活動先分類再比對；續作沿用已核准來源、決定與頁面，只因教師要求或新證據修補受影響項目，不反覆重跑未變內容。ChatGPT Work Launcher 2.1 依 main 按需載入本次修正。
