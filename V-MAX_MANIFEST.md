# V-MAX Manifest 3.0

## 角色

本檔是 V-MAX 的正式模組索引與版本裁決表。任何 AI 不得自行猜測哪一份檔案較新、哪個舊名稱仍可執行。

---

## Current Canonical Files

```yaml
vmax_manifest_version: 3.0
universal_bootstrap: V-MAX_UNIVERSAL_BOOTSTRAP.md
bootstrap: V-MAX_BOOTSTRAP.md
runtime_contract: runtime/lesson-state.md
runtime_storage:
  provider: GOOGLE_DRIVE
  root_folder_name: 00_Runtime_State
  root_folder_id: 1AOjYwALGVNWu99b-SnjBUSALEDrlReMt
  index_title: V-MAX_Runtime_Index
  index_document_id: 1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ
main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.1
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.6
checkpoint_resume_executor:
  path: skills/vmax-checkpoint-resume/SKILL.md
  current_version: 1.1
modular_checkpoint_execution:
  path: core/governance/modular-checkpoint-execution-policy.md
  current_version: 1.0
skill_io_registry:
  path: core/governance/skill-io-registry.md
  current_version: 1.1
universal_skill_packaging:
  path: core/governance/universal-skill-packaging-standard.md
  current_version: 1.0
platform_capability_matrix:
  path: core/governance/platform-capability-matrix.md
  current_version: 1.0
skill_sync_policy:
  path: core/governance/skill-sync-policy.md
  current_version: 1.0
artifact_migration_policy:
  path: core/governance/artifact-migration-policy.md
  current_version: 1.0
platform_conformance_test:
  path: tests/platform-conformance/vmax-platform-conformance-test.md
  current_version: 1.0
google_drive_storage_architecture:
  path: core/governance/google-drive-storage-architecture.md
  current_version: 1.0
google_drive_portable_artifact_policy:
  path: core/governance/google-drive-portable-artifact-policy.md
  current_version: 1.1
source_library_policy: core/governance/source-library-policy.md
step1_source_anchor:
  path: core/governance/step1-source-anchor-policy.md
  current_version: 1.3
recognition_only_character_policy:
  path: core/governance/recognition-only-character-policy.md
  current_version: 1.1
hold_policy: core/governance/hold-teacher-interface-policy.md
workflow_test_freeze: core/governance/workflow-test-freeze.md
workflow_hold_regression:
  path: tests/workflow-hold-regression-cases.md
  current_version: 1.8
knowledge_lab_ordering:
  path: core/director/knowledge-lab-ordering-policy.md
  current_version: 2.1
character_deep_teaching_focus:
  path: core/director/character-deep-teaching-focus-policy.md
  current_version: 1.3
polyphonic_source_policy:
  path: core/director/polyphonic-source-policy.md
  current_version: 1.0
character_group_visual_comparison:
  path: skills/character-group-visual-comparison/SKILL.md
  current_version: 1.0
character_teaching_regression:
  path: tests/character-teaching-regression-cases.md
  current_version: 1.1
lesson_visual_map:
  path: core/visual/lesson-visual-map.md
  current_version: 1.1
gold_page_pattern:
  path: core/visual/gold-page-pattern-library.md
  current_version: 1.0
text_embedded_language_policy:
  path: core/pedagogy/text-embedded-language-teaching-policy.md
  current_version: 1.0
text_embedded_language_skill:
  path: skills/text-embedded-language-teaching/SKILL.md
  current_version: 1.0
idiom_expression_visualization:
  path: core/director/idiom-expression-visualization-policy.md
  current_version: 1.0
prestudy_language_selection:
  path: core/worksheet/prestudy-language-selection-policy.md
  current_version: 1.1
prestudy_worksheet:
  path: skills/prestudy-worksheet/SKILL.md
  current_version: 1.2
postlesson_short_writing_worksheet:
  path: skills/postlesson-short-writing-worksheet/SKILL.md
  current_version: 1.3
worksheet_regression:
  path: tests/worksheet-regression-cases.md
  current_version: 1.1
lesson_package_delivery:
  path: skills/lesson-package-delivery/SKILL.md
  current_version: 1.4
google_drive_lesson_archive:
  path: skills/google-drive-lesson-archive/SKILL.md
  current_version: 1.3
renderer_contract:
  path: core/renderer/image-first-hybrid-renderer.md
  current_version: 1.2
infographic_pdf_output:
  path: core/export/infographic-pdf-output-contract.md
  current_version: 1.2
infographic_pdf_regression:
  path: tests/infographic-pdf-regression-cases.md
  current_version: 1.1
quality_gate:
  path: core/quality/quality-gate-2.md
  current_version: 2.4
adapters:
  chatgpt: adapters/chatgpt.md
  claude: adapters/claude.md
  codex: adapters/codex.md
  gemini: adapters/gemini.md
  gemini_spark: adapters/gemini-spark.md
  notebooklm: adapters/notebooklm.md
  canva_renderer: adapters/canva.md
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

---

## Cross-platform Execution Resolution

所有相容執行器先經：

```text
V-MAX_UNIVERSAL_BOOTSTRAP
→ Capability Detection
→ Platform Adapter
→ V-MAX_BOOTSTRAP
→ FULL_GOLDEN_PATH | CHECKPOINT_RESUME
```

- ChatGPT、Claude、Codex、Gemini Spark 都是執行器，不是 canonical authority。
- 平台差異只由 Adapter 與 Capability Matrix 處理；不得複製一套平台專屬 Core。
- 已核准 artifact 可直接由 Checkpoint Resume 使用；不得因換平台重新轉錄／分析教材。
- 平台缺少 Drive、GitHub、image 或 code 能力時，必須誠實標記 fallback / blocked，不得偽稱已完成外部操作。
- 舊 artifact 優先依 Artifact Migration Policy 無損升級；不得只因 schema 版本較舊就整課重算。

權威：`V-MAX_UNIVERSAL_BOOTSTRAP.md`、`core/governance/platform-capability-matrix.md`、`core/governance/universal-skill-packaging-standard.md`、`core/governance/skill-sync-policy.md`、`core/governance/artifact-migration-policy.md`。

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
→ Visual Grammar
→ Gold Page Pattern
→ Slide Architecture / Visual Sequence
→ Page Estimate
→ Style Recipe
→ Representative Gold Page Validation
→ Full Renderer
→ PDF Assembly / Preflight
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery
→ Google Drive Archive Verification
```

若無成語：STEP 2.6 明確記錄 `N/A_NO_IDIOM`。

---

## Checkpoint Resume Resolution

Golden Path 定義完整課程如何形成；Checkpoint Resume 定義已形成資料如何重用。

- 已核准資料不重算。
- target skill 只讀自己真正需要的 checkpoint / artifact。
- 缺欄位只補缺欄位，不自行回到 SOURCE 0。
- Batch Mode 每課使用自己的 checkpoint；一課失敗不阻塞其他課。
- standalone skill 不得假裝推進 Golden Path `current_stage`。

權威：`core/governance/modular-checkpoint-execution-policy.md`、`core/governance/skill-io-registry.md`、`skills/vmax-checkpoint-resume/SKILL.md`。

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
- `SHAPE_NEAR` 必須以兩字以上的字群比較教學，不得退化成單字詳解。
- 容易搞錯的單字只由教師依班級需求主動指定 → `TEACHER_ADDED_WRITING_FOCUS`；AI 不列易錯字候選。
- 教師指定後只處理實際混淆焦點，例如易漏／多寫筆畫、部件位置與比例、局部字形看錯／寫錯、必要筆順或其他已觀察到的辨認／書寫混淆點；不得擴張成完整單字百科頁。
- 若真正需要的是形近字比較或多音語境，仍回到 `SHAPE_NEAR` / `POLYPHONIC`。
- 複雜／字源／評量／語義特殊皆不是 AI 第三入口。
- 其餘生字不特別提出深教，只留在基礎識寫層。

權威：`character-deep-teaching-focus-policy.md` v1.3、`knowledge-lab-ordering-policy.md` v2.1。

### Polyphonic Source
合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：AI 只從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`

形近補充字、比較字、認讀字、課文一般字不因本身多音而由 AI 自動升級。

---

## Character Group Visual Resolution

形近字／多音字學生可見頁遵循 `skills/character-group-visual-comparison/SKILL.md`。

- 形近字：以字群同框比較，大字＋注音＋字義情境圖＋例詞＋像／不像＋辨認提示。
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

LVM 不得退化為矩形＋箭頭流程圖；需以能承載真實文本關係的整課世界、路徑、場景或結構視覺呈現。

權威：`core/visual/lesson-visual-map.md` v1.1、`core/visual/gold-page-pattern-library.md` v1.0。

---

## Gold Page Pattern Resolution

Visual Grammar 與 Renderer 之間新增正式 canonical layer：`Gold Page Pattern`。

- Visual Grammar：決定學生要看懂哪一種認知關係。
- Gold Page Pattern：決定這個關係在學生眼前如何發生。
- Layout / Style Recipe：只能在 Pattern 之後決定。

正式 Pattern：
`WORLD_MAP / DUAL_WORLD_COMPARE / SEQUENCE_DISCOVERY / COGNITIVE_METAPHOR / CHARACTER_MEANING_FIELD / SENSORY_TRANSLATION / EVIDENCE_DISCOVERY / CHOICE_PATH`。

代表頁必須先通過 Gold Page Gate，才可進全量 Renderer。

以下不得 PASS：
`TEMPLATE_CARD_DRIFT / LEFT_TEXT_RIGHT_IMAGE_DRIFT / VISUAL_EVIDENCE_MISSING / DISCOVERY_PREEMPTED / GOLD_PATTERN_DROPPED`。

權威：`core/visual/gold-page-pattern-library.md` v1.0。

---

## Final Teaching Visual Output Resolution

- 正式課堂視覺成品預設為 16:9 圖文資訊圖表 PDF。
- 每頁是完整圖文構圖，但必須先由 Visual Grammar → Gold Page Pattern 決定理解方式，不得固定套版。
- 可修改性保留在 Source Master、Renderer Script、Visual YAML、Character Assets 與單頁圖檔。
- 不製作「圖片塞進可修改 PPT」作為預設交付；PPTX 只有教師明確要求才產生。
- 最終 PDF 必須逐頁渲染回 PNG，完成 Gold Pattern、文字、注音、頁序、裁切、清晰度與答案外洩檢查。
- PDF 以 `BALANCED_SCREEN_PRINT_SAFE` 為預設；A4 列印教材維持 300 dpi，不以降 DPI 換取檔案大小。

權威：`core/export/infographic-pdf-output-contract.md` v1.2、`core/renderer/image-first-hybrid-renderer.md` v1.2、`core/quality/quality-gate-2.md` v2.4。

---

## Idiom Expression Resolution

STEP 2.5 決定教學價值／保留；STEP 2.6 決定生活例句、理解重點、視覺表達與是否獨立成頁。

---

## Worksheet Resolution

### Pre-study Worksheet
權威：`skills/prestudy-worksheet/SKILL.md` v1.2。

內容層只負責題目、語文焦點、閱讀任務、Teacher Key 與 `PRESTUDY_WORKSHEET_SOURCE`；A／B 雙版本視覺 Renderer 在 PR #3 收斂後由 Registry 接續，不得反向改寫已核准內容。

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

預習單與短文單可共享視覺家族，但功能必須分開：
- 預習單：探索／理解／預備
- 短文單：素材啟動／語文 Bonus／創作遷移

正式交付必須通過 `tests/worksheet-regression-cases.md` v1.1；若 `WORKSHEET_FONT_TOO_SMALL` 或 `WORKSHEET_EXPORT_SCALE_FAIL`，不得交付為 PASS。

---

## Google Drive Storage Resolution

Drive 不再以「所有成果都塞進每課六類」作為唯一模型。正式採分層架構：

```text
V-MAX 教材庫
├─ 00_系統與數據管理
├─ 主體架構
└─ 學科教學資源
   └─ 冊別
      ├─ 冊別共用來源／鎖定主檔
      ├─ Batch Artifact（跨課系列教材）
      └─ 分課 Lesson Package
```

- 系統文件、Runtime 與轉錄數據進 `00_系統與數據管理`。
- 跨課角色／視覺／可重用資產可進「主體架構」。
- 第一至六課預習單、短文單等跨課系列可集中為冊別 Batch Artifact；不必重複塞進每課 `06_延伸教材`。
- 單課 Golden Path / Lesson Package 仍可使用六類：`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。
- GitHub 管規則；Drive 管教師跨裝置需要續作、查找與交付的 portable artifact。
- 只有實際上傳並再次 list/search 驗證成功，才可 Archive PASS。

權威：`core/governance/google-drive-storage-architecture.md`、`core/governance/google-drive-portable-artifact-policy.md`、`skills/google-drive-lesson-archive/SKILL.md` v1.3。

---

## Platform Conformance Resolution

正式宣稱跨平台 PASS 前，必須使用 `tests/platform-conformance/vmax-platform-conformance-test.md` 驗證至少 C-01～C-09。

- Renderer 可以有平台差異；Canonical Decision 不可以有平台差異。
- 沒有實際四平台測試資料時，只能標記 `PACKAGE_STRUCTURE_READY / PLATFORM_RUNTIME_NOT_YET_FULLY_TESTED`，不得標記 `FULLY_VERIFIED_CROSS_PLATFORM`。

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
- AI 提出易錯字候選，或因易錯／特殊構形自行建立單字詳解
- 把教師指定的單字混淆焦點擴張成百科式單字頁
- 形近補充字因多音被 AI 拉入多音字單元
- 無方格直接等於認讀字
- 語詞／句型／修辭沒有原文證據
- 已選整課圖像心智地圖卻在大綱消失
- Drive 舊五類資料夾結構
- 把「每課六類」誤當成跨課 Batch Artifact 也必須重複存放的唯一模型
- A4 學習單靠縮字到 12 pt 以下塞內容
- A4 正式列印教材靠降 DPI 瘦身
- 把可修改的圖片式 PPT 當成預設正式成品
- 只輸出單頁圖片卻未組裝、重渲染與驗證最終 PDF
- Visual Grammar 只存在 metadata，未落實成學生可見 Gold Pattern
- 固定左文右圖／大白框／資料卡連發
- 圖片移除後完全不影響理解卻仍宣稱為圖像式教學頁
- 平台內 Skill 副本反向覆蓋 GitHub canonical
- 因換 ChatGPT／Claude／Codex／Gemini Spark 而重算已核准教材

---

## 核心金句

> Manifest 決定現在誰是權威；Executor 必須真的載入，而不是只靠模型記得。

> Golden Path 定義完整課程如何形成；Checkpoint Resume 定義已形成資料如何重用。

> 形近字用字群教，多音字用語境教；老師可以依班級需要指定「孩子容易搞錯的字」額外提醒，其餘不另提深教。

> 學習單寧可少放內容，也不要讓學生真正印出來看到的字小於 12 pt。

> V-MAX 不屬於任何一個 AI；平台只是不同執行器，Canonical Decision 不得漂移。

> 內容正確只是底線；Gold Page 要把理解變成學生眼睛能直接看到的教學事件。