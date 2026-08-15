# V-MAX Manifest 3.6

## 角色

本檔是 V-MAX 的正式模組索引與版本裁決表。任何 AI 不得自行猜測哪一份檔案較新、哪個舊名稱仍可執行。

---

## Current Canonical Files

```yaml
vmax_manifest_version: 3.6
bootstrap: V-MAX_BOOTSTRAP.md
runtime_contract: runtime/lesson-state.md
front_door:
  path: skills/vmax-teaching-skills/SKILL.md
  current_version: 1.0
runtime_storage:
  provider: GOOGLE_DRIVE
  root_folder_name: 00_Runtime_State
  location_authority: runtime/lesson-state.md
  root_folder_id: 1AOjYwALGVNWu99b-SnjBUSALEDrlReMt
  index_title: V-MAX_Runtime_Index
  index_document_id: 1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ
main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.3
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.6
course_orchestrator:
  path: skills/vmax-course-orchestrator/SKILL.md
  current_version: 0.5.0
source_library_policy: core/governance/source-library-policy.md
lesson_master_preflight:
  path: core/governance/lesson-master-preflight.md
  current_version: 1.0
task_knowledge_requirement_registry:
  path: core/governance/task-knowledge-requirement-registry.md
  current_version: 1.0
step1_source_anchor:
  path: core/governance/step1-source-anchor-policy.md
  current_version: 1.4
recognition_only_character_policy:
  path: core/governance/recognition-only-character-policy.md
  current_version: 1.1
hold_policy:
  path: core/governance/hold-teacher-interface-policy.md
  current_version: 1.4
teacher_review_view:
  path: core/ui/teacher-review-view-contract.md
  current_version: 1.1
workflow_test_freeze: core/governance/workflow-test-freeze.md
workflow_hold_regression:
  path: tests/workflow-hold-regression-cases.md
  current_version: 1.9
knowledge_lab_ordering:
  path: core/director/knowledge-lab-ordering-policy.md
  current_version: 1.9
character_deep_teaching_focus:
  path: core/director/character-deep-teaching-focus-policy.md
  current_version: 1.1
polyphonic_source_policy:
  path: core/director/polyphonic-source-policy.md
  current_version: 1.1
character_group_visual_comparison:
  path: skills/character-group-visual-comparison/SKILL.md
  current_version: 1.1
character_teaching_regression:
  path: tests/character-teaching-regression-cases.md
  current_version: 1.1
lesson_visual_map:
  path: core/visual/lesson-visual-map.md
  current_version: 1.1
text_embedded_language_policy:
  path: core/pedagogy/text-embedded-language-teaching-policy.md
  current_version: 1.0
text_embedded_language_skill:
  path: skills/text-embedded-language-teaching/SKILL.md
  current_version: 1.0
language_knowledge_placement:
  path: core/director/language-knowledge-placement-policy.md
  current_version: 1.1
text_ui_system:
  path: core/ui/text-ui-system-2.md
  current_version: 2.1
character_system:
  path: core/character/character-system-2.md
  current_version: 2.2
classroom_image_slide_policy:
  path: core/presentation/classroom-image-slide-policy.md
  current_version: 1.1
idiom_expression_visualization:
  path: core/director/idiom-expression-visualization-policy.md
  current_version: 1.0
prestudy_language_selection:
  path: core/worksheet/prestudy-language-selection-policy.md
  current_version: 1.1
prestudy_worksheet:
  path: skills/prestudy-worksheet/SKILL.md
  current_version: 1.3
postlesson_short_writing_worksheet:
  path: skills/postlesson-short-writing-worksheet/SKILL.md
  current_version: 1.3
worksheet_regression:
  path: tests/worksheet-regression-cases.md
  current_version: 1.2
lesson_package_delivery:
  path: skills/lesson-package-delivery/SKILL.md
  current_version: 1.5
google_drive_lesson_archive:
  path: skills/google-drive-lesson-archive/SKILL.md
  current_version: 1.0
renderer_contract:
  path: core/renderer/image-first-hybrid-renderer.md
  current_version: 1.5
presentation_engine:
  path: skills/presentation-engine/SKILL.md
  current_version: 0.3.0
image_renderer:
  path: skills/vmax-image-renderer/SKILL.md
  current_version: 1.2
  request_schema: skills/vmax-image-renderer/references/render-request-schema.md
visual_drift_detector:
  path: core/quality/visual-drift-detector.md
  current_version: 1.1
quality_gate:
  path: core/quality/quality-gate-2.md
  current_version: 2.5
typography_bridge:
  path: skills/vmax-typography-bridge/SKILL.md
  current_version: 1.1
vqs_quality_validator:
  path: skills/vqs-quality-validator/SKILL.md
  current_version: 0.2.0
adapters:
  chatgpt: adapters/chatgpt.md
  codex: adapters/codex.md
  gemini: adapters/gemini.md
  notebooklm: adapters/notebooklm.md
  canva_renderer: adapters/canva.md
gemini_source_analysis:
  contract: adapters/gemini/source-analysis-contract.md
  report_schema: schemas/gemini-source-analysis-report.md
  lesson_master_index_schema: schemas/lesson-master-index.md
  lkb_patch_schema: schemas/lkb-patch.md
  task_requirement_registry: core/governance/task-knowledge-requirement-registry.md
  regression: tests/gemini-source-analysis-regression-cases.md
  adapter_version: 2.5
```

---

## Runtime Authority

GitHub 保存規格；每一課即時 Runtime State 以 Google Drive 為權威。

```text
runtime/lesson-state.md
→ Google Drive V-MAX_Runtime_Index
→ V-MAX_State_{冊別}_{課次}_{課名}
```

不得以模型記憶、舊對話、舊簡報取代 Drive 最新 State。

固定 Drive ID 只允許出現在 Manifest、`runtime/lesson-state.md` 與 `skills/google-drive-lesson-archive/SKILL.md` 三個治理位置；一般內容技能必須引用治理文件，不得複製 ID。此 repository 若公開發布前要移除個人位置，應在這三個位置同步參數化。

---

## Repository Hygiene

正式 repository 只保存跨課可重用規格、技能、schema、library、平台 adapter 與回歸測試。

禁止加入：
- `runtime/lessons/` 或任何單課即時 Runtime State；正式狀態只在 Google Drive。
- 根目錄 `lessons/` 下的特定課程成品或單課鎖定檔。
- `docs/legacy/`、migration audit、legacy resource 等只供歷史追溯的檔案。

歷史內容由 Git commit、tag 與 release 保存，不得留在可安裝套件中影響模型選路。現行架構參考文件可以保留在 `docs/`，但不能覆寫 Manifest canonical files。

---

## Canonical Golden Path

```text
SOURCE 0
→ STEP 1
→ HOLD 1
→ STEP 2
→ HOLD 2
→ STEP 2.5
→ HOLD 2.5
→ STEP 2.6
→ HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map
→ Supplement / Framework Decision
→ Session Map
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Page Estimate
→ Style Recipe
→ Representative Validation
→ Full Renderer
→ Actual Asset Verification
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery
→ Google Drive Archive Verification
```

若無成語：STEP 2.6 明確記錄 `N/A_NO_IDIOM`。

---

## Teacher Review View Resolution

所有 HOLD 與教師審核畫面以 `core/ui/teacher-review-view-contract.md` 為權威：完整 Machine Payload 留在母檔，對話預設顯示人類可讀的結論、證據、知識層、缺口、本次唯一決定與唯一下一步。

- raw JSON／YAML 不得作為主要 UI。
- STEP 1 必要來源未完成時標記 `STEP1_INCOMPLETE`，不得要求核准。
- 重要項目標記 `[教材明載] / [教師補充] / [AI 延伸] / [待核對]`。
- 前段只允許 STEP 1、STEP 2、STEP 2.5、STEP 2.6 與各自 HOLD；`STEP 2.75` 為非法別名。

---

## Recognition-only Character Resolution

認讀字 = 教材在本課生字系統中明確列為需要識讀、但不屬正式書寫生字的字。

固定雙來源核對：
1. 課文頁下方小字生字標示
2. 課文後方獨立生字表／生字教學頁

- 無方格只作線索，不等於認讀字。
- 兩處不一致 → `SOURCE_CONFLICT`。
- 來源無 → `N/A_SOURCE_NOT_PRESENT`。

權威：`recognition-only-character-policy.md` v1.1、`step1-source-anchor-policy.md` v1.3。

---

## Grade 3–4 Character Teaching Resolution

- 正式生字完整保留。
- **AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。**
- 一般單字 = `BASIC_LITERACY_ONLY`。
- 單一生字詳解只有教師指定 → `TEACHER_ADDED_SINGLE_CHARACTER`。
- AI 只能提示 `AI_SUGGESTION_SINGLE_CHARACTER`，不得自動成頁。
- 易錯／複雜／字源／評量／語義特殊皆不是 AI 第三入口。

權威：`character-deep-teaching-focus-policy.md` v1.1、`knowledge-lab-ordering-policy.md` v1.9。

### Polyphonic Source
合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：AI 只從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`

形近補充字、比較字、認讀字、課文一般字不因本身多音而由 AI 自動升級。

---

## Character Form and Pronunciation Resolution

- 課本生字欄、課文注音或教材辨音活動是本課讀音第一來源。
- 教育部辭典只作補充與驗證，不取代教材身分。
- 多音字例詞逐詞核對，不從單字讀音自行類推。
- 部首、偏旁、部件、字形口訣逐字核對；口訣預設為 AI 建議，教師確認前不得鎖定。
- 發現字形、讀音或例詞疑點時停在當前 STEP。

權威：`core/director/polyphonic-source-policy.md` v1.1、`skills/character-group-visual-comparison/SKILL.md` v1.1。

---

## Character Group Visual Resolution

形近字／多音字學生可見頁遵循 `skills/character-group-visual-comparison/SKILL.md`。

- 形近字：大字＋注音＋字義情境圖＋例詞＋像／不像＋辨認提示。
- 多音字：同一大字＋不同讀音＋語意／情境＋例詞／例句＋課文判斷。

---

## Text-Embedded Language Resolution

- 語詞隨段落：原文＋語詞＋學生易懂意義。
- 句型帶原文：課文原句 → 結構 → 仿用。
- 修辭從文本發現：原文 → 效果 → 命名。
- 原文證據層不可在 Renderer 消失。

權威：`text-embedded-language-teaching-policy.md`、`skills/text-embedded-language-teaching/SKILL.md`。

---

## Lesson Visual Map Resolution

若教師已選定整課圖像心智地圖，它成為 downstream invariant；簡報大綱、Slide Architecture、頁數估算、Renderer 都不得靜默刪除。

權威：`core/visual/lesson-visual-map.md` v1.1。

---

## Idiom Expression Resolution

STEP 2.5 決定教學價值／保留；STEP 2.6 決定生活例句、理解重點、視覺表達與是否獨立成頁。

---

## Worksheet Resolution

### Pre-study Worksheet
權威：`skills/prestudy-worksheet/SKILL.md` v1.3。

### Post-lesson Short Writing Worksheet
權威：`skills/postlesson-short-writing-worksheet/SKILL.md` v1.3。

兩份學習單共同硬規格：

> **A4 100% 實際列印時，所有學生需要閱讀、辨認、勾選或作答依據的文字不得低於 12 pt。**

建議層級：
- 正文／題幹／Bonus 項目：12–14 pt 以上
- 區塊標題：14–18 pt 以上
- 主標題：20 pt 以上

班級／座號／姓名、勾選項、提示語、角色台詞與必要圖說，只要需要學生辨讀，同樣受 12 pt 下限約束。

內容放不下時：`刪減 → 縮短 → 重排 → 必要時增加頁數`；**不得縮到 12 pt 以下**。

圖片／PDF 輸出必須以 A4 實際列印尺寸檢查等效字級，避免畫布縮放造成假 PASS。


共同交付規格：
- 先通過 Lesson Master Preflight 與任務 Coverage Diff；母檔不足時只增補核准 Patch。
- 正式 PNG 必須經 `vmax-image-renderer` 實際生成與重檢，狀態為 `RENDER_VERIFIED`。
- 形近字／多音字使用「短直式注音欄＋可寫二至三個國字的長造詞線」。
- 單課與合併檔名課次固定補零為兩位數，例如 `第07課`、`第07至12課`。
- 每批保留全部單課 PNG，並分設合併 PDF 的印刷版與分享版。
- 分享版壓縮後仍須重新渲染全部頁面；可見模糊或鋸齒即 FAIL。
- 短文單人物可依真實留白適度放大，但不得侵入題幹、工具箱或正式書寫線。
- 年級、學期、科目、出版社與課次由 Output Profile 參數化，不把 `四上` 寫成通用固定值。

預習單與短文單可共享視覺家族，但功能必須分開：
- 預習單：探索／理解／預備
- 短文單：素材啟動／語文 Bonus／創作遷移

正式交付必須通過 `tests/worksheet-regression-cases.md` v1.2；若 `WORKSHEET_FONT_TOO_SMALL` 或 `WORKSHEET_EXPORT_SCALE_FAIL`，不得交付為 PASS。

---

## Google Drive Lesson Archive Resolution

固定根目錄：
`V-MAX 教材庫` — folder_id `1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA`

每課版本固定六類：
```text
01_教材整理
02_逐頁腳本
03_NotebookLM
04_角色視覺
05_簡報成品
06_延伸教材
```

完整重做不覆蓋舊版，先讀 Drive 後建立 `_01 / _02 / _03...`。

Lesson Package 不得再維護舊五類歸檔結構；Archive Skill 是位置與版本的唯一權威。

只有實際上傳並再次 list/search 驗證成功，才可 Archive PASS。

---

## Version Resolution

若模組內版本與 Manifest 不一致：
1. 重新 fetch 最新檔。
2. Repo 最新已升版但 Manifest 未更新 → `MANIFEST_STALE`。
3. 不得以舊 Manifest 覆蓋新 canonical file。
4. 無法確認就停止高風險流程，不猜。

---

## Legacy / Conflict Rules

以下一律視為舊規則：
- STEP 3／STEP 4 舊主流程
- AI 因易錯／特殊構形自行建立單字詳解
- 形近補充字因多音被 AI 拉入多音字單元
- 無方格直接等於認讀字
- 語詞／句型／修辭沒有原文證據
- 已選整課圖像心智地圖卻在大綱消失
- Drive 舊五類資料夾結構
- A4 學習單靠縮字到 12 pt 以下塞內容

---

## 核心金句

> Manifest 決定現在誰是權威；Executor 必須真的載入，而不是只靠模型記得。

> 生字表 ≠ 生字教學清單；AI 主動只教形近字與多音字，單字詳解由老師指定。

> 學習單寧可少放內容，也不要讓學生真正印出來看到的字小於 12 pt。

> 教師口述型圖像簡報不是講義；學生頁只放此刻需要看見的內容，完整說明留給老師說。
