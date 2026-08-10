# V-MAX Manifest 2.9

## 角色

本檔是 V-MAX 的正式模組索引與版本裁決表。任何 AI 不得自行猜測哪一份檔案較新、哪個舊名稱仍可執行。

---

## Current Canonical Files

```yaml
vmax_manifest_version: 2.9
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
  current_version: 1.1
postlesson_short_writing_worksheet:
  path: skills/postlesson-short-writing-worksheet/SKILL.md
  current_version: 1.1
worksheet_regression:
  path: tests/worksheet-regression-cases.md
  current_version: 1.1
lesson_package_delivery:
  path: skills/lesson-package-delivery/SKILL.md
  current_version: 1.4
google_drive_lesson_archive:
  path: skills/google-drive-lesson-archive/SKILL.md
  current_version: 1.1
renderer_contract:
  path: core/renderer/image-first-hybrid-renderer.md
  current_version: 1.2
infographic_pdf_output:
  path: core/export/infographic-pdf-output-contract.md
  current_version: 1.1
infographic_pdf_regression:
  path: tests/infographic-pdf-regression-cases.md
  current_version: 1.1
quality_gate:
  path: core/quality/quality-gate-2.md
  current_version: 2.4
adapters:
  chatgpt: adapters/chatgpt.md
  codex: adapters/codex.md
  gemini: adapters/gemini.md
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

權威：`core/export/infographic-pdf-output-contract.md` v1.1、`core/renderer/image-first-hybrid-renderer.md` v1.2、`core/quality/quality-gate-2.md` v2.4。

---

## Idiom Expression Resolution

STEP 2.5 決定教學價值／保留；STEP 2.6 決定生活例句、理解重點、視覺表達與是否獨立成頁。

---

## Worksheet Resolution

### Pre-study Worksheet
權威：`skills/prestudy-worksheet/SKILL.md` v1.1。

### Post-lesson Short Writing Worksheet
權威：`skills/postlesson-short-writing-worksheet/SKILL.md` v1.1。

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
- AI 提出易錯字候選，或因易錯／特殊構形自行建立單字詳解
- 把教師指定的單字混淆焦點擴張成百科式單字頁
- 形近補充字因多音被 AI 拉入多音字單元
- 無方格直接等於認讀字
- 語詞／句型／修辭沒有原文證據
- 已選整課圖像心智地圖卻在大綱消失
- Drive 舊五類資料夾結構
- A4 學習單靠縮字到 12 pt 以下塞內容
- 把可修改的圖片式 PPT 當成預設正式成品
- 只輸出單頁圖片卻未組裝、重渲染與驗證最終 PDF
- Visual Grammar 只存在 metadata，未落實成學生可見 Gold Pattern
- 固定左文右圖／大白框／資料卡連發
- 圖片移除後完全不影響理解卻仍宣稱為圖像式教學頁

---

## 核心金句

> Manifest 決定現在誰是權威；Executor 必須真的載入，而不是只靠模型記得。

> 形近字用字群教，多音字用語境教；老師可以依班級需要指定「孩子容易搞錯的字」額外提醒，其餘不另提深教。

> 學習單寧可少放內容，也不要讓學生真正印出來看到的字小於 12 pt。

> 內容正確只是底線；Gold Page 要把理解變成學生眼睛能直接看到的教學事件。
