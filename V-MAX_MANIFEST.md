# V-MAX Manifest 2.2

## 角色

本檔是 V-MAX 的正式模組索引與版本裁決表。任何 AI 不得自行猜測哪一份檔案較新、哪個舊名稱仍可執行。

---

## Current Canonical Files

```yaml
vmax_manifest_version: 2.2
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
  current_version: 1.9
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
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
  current_version: 1.5
knowledge_lab_ordering:
  path: core/director/knowledge-lab-ordering-policy.md
  current_version: 1.8
character_deep_teaching_focus:
  path: core/director/character-deep-teaching-focus-policy.md
  current_version: 1.1
polyphonic_source_policy:
  path: core/director/polyphonic-source-policy.md
  current_version: 1.0
character_group_visual_comparison:
  path: skills/character-group-visual-comparison/SKILL.md
  current_version: 1.0
character_teaching_regression:
  path: tests/character-teaching-regression-cases.md
  current_version: 1.0
lesson_visual_map:
  path: core/visual/lesson-visual-map.md
  current_version: 1.1
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
  current_version: 1.0
postlesson_short_writing_worksheet:
  path: skills/postlesson-short-writing-worksheet/SKILL.md
  current_version: 1.0
worksheet_regression:
  path: tests/worksheet-regression-cases.md
  current_version: 1.0
lesson_package_delivery:
  path: skills/lesson-package-delivery/SKILL.md
  current_version: 1.1
renderer_contract: core/renderer/image-first-hybrid-renderer.md
adapters:
  chatgpt: adapters/chatgpt.md
  codex: adapters/codex.md
  gemini: adapters/gemini.md
  notebooklm: adapters/notebooklm.md
  canva_renderer: adapters/canva.md
```

---

## Runtime Authority

GitHub 保存 Runtime schema 與規則；每一課的即時 Runtime State 以 Google Drive 為正式權威。

正式讀取順序：

```text
runtime/lesson-state.md
→ Google Drive V-MAX_Runtime_Index
→ 對應課程 V-MAX_State_{冊別}_{課次}_{課名}
```

不得用 GitHub 範例狀態、模型記憶或舊對話取代 Drive 中該課最新 State。

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
→ STEP 2.6 Idiom Expression & Visualization
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
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery
→ Google Drive Archive Verification
```

若本課無需處理成語，STEP 2.6 必須明確記錄 `N/A_NO_IDIOM`，不得默默跳過。

---

## Recognition-only Character Resolution

正式定義：

> 認讀字 = 教材在本課生字系統中明確列為需要識讀、但不屬正式書寫生字的字。

判定必須完成教材雙來源核對：

1. 課文頁下方的小字生字標示
2. 課文後方獨立生字表／生字教學頁

兩者交叉核對後，才可判定正式生字／認讀字身分。

重要邊界：
- 「無方格」只能是版面線索，不能單獨作為認讀字定義。
- 課文一般字、形近補充字、比較字、AI 補充字、偏旁識字示例不得因此被判為認讀字。
- 兩個教材位置不一致時，標記 `SOURCE_CONFLICT`，不得靜默採其中一邊。
- 來源未列認讀字時，明確記錄 `N/A_SOURCE_NOT_PRESENT`。

權威規則：
- `core/governance/recognition-only-character-policy.md` v1.1
- `core/governance/step1-source-anchor-policy.md` v1.3
- `tests/workflow-hold-regression-cases.md` v1.5

---

## Grade 3–4 Character Teaching Resolution

以三、四年級教材為預設時：

- 教材正式生字全部完整保留。
- **AI 主動深教只有兩類入口：`SHAPE_NEAR`、`POLYPHONIC`。**
- 一般生字標記為 `BASIC_LITERACY_ONLY`，不預設獨立成頁。
- **單一生字詳解只有教師明確指定才可建立**，標記 `TEACHER_ADDED_SINGLE_CHARACTER`。
- 容易寫錯、字形複雜、字源有趣、評量重要或語義特殊，都不是 AI 自動建立單字深教頁的合法理由。
- AI 可提醒某字可能需要額外處理，但只能標 `AI_SUGGESTION_SINGLE_CHARACTER`；教師確認後才可升級。

權威規則：
- `core/director/character-deep-teaching-focus-policy.md` v1.1
- `tests/character-teaching-regression-cases.md`

若 `knowledge-lab-ordering-policy.md` 或舊文件仍含「AI 可因特殊構形／語義／易錯而自行例外深教單字」的舊表述，視為 deprecated conflict，以本節與 `character-deep-teaching-focus-policy.md` v1.1 的較窄規則為準。

### Polyphonic Source Resolution

多音字合法來源只有三種：

1. `TEXTBOOK_POLYPHONIC`：教材明列，必須保留。
2. `AI_RECOMMENDED_POLYPHONIC`：教材未明列時，AI 只能從本課正式生字中推薦，且必須有明確教學價值。
3. `TEACHER_ADDED_POLYPHONIC`：教師可因班級反覆誤讀、語境判斷困難或影響課文理解而指定加入，即使該字不是本課正式生字。

形近補充字、比較字、AI 補充字，不因本身具有多音而自動升級。

權威規則：`core/director/polyphonic-source-policy.md`。

### Character Group Visual Resolution

當形近字／字群或多音字已被確認值得深教時，學生可見頁面遵循：

`skills/character-group-visual-comparison/SKILL.md`

核心呈現：
- 形近字／字群：大字＋注音＋字義情境圖＋例詞＋哪裡像／哪裡不一樣＋辨認提示。
- 多音字：同一大字＋不同讀音＋不同語意／情境＋例詞／例句＋回到課文判斷。

---

## Lesson Visual Map Resolution

權威規則：`core/visual/lesson-visual-map.md`

若教師已選定整課圖像心智地圖，該項成為 downstream invariant；簡報大綱、Slide Architecture、頁數估算與 Renderer 不得靜默刪除。

---

## Text-Embedded Language Resolution

權威政策：`core/pedagogy/text-embedded-language-teaching-policy.md`

執行摘要：`skills/text-embedded-language-teaching/SKILL.md`

核心規則：
- 語詞隨段落：保留原文片段、重點語詞與學生易懂的語意。
- 句型帶原文：先有課文原句，再找結構、看懂作用、進行仿說／仿寫。
- 修辭從文本發現：先讀原文、觀察特點與效果，最後才命名。
- 原文是語文教學的共同證據層，不得在後段消失。

---

## Idiom Expression Resolution

- STEP 2.5：教學價值、保留範圍、CORE/FLEX/BONUS。
- STEP 2.6：生活例句、理解重點、視覺表達方式與是否獨立成頁。

權威規則：`core/director/idiom-expression-visualization-policy.md`。

---

## Worksheet Resolution

### Pre-study Worksheet
權威技能：`skills/prestudy-worksheet/SKILL.md`

### Post-lesson Short Writing Worksheet
權威技能：`skills/postlesson-short-writing-worksheet/SKILL.md`

預習單與短文單可共享同一課的視覺家族，但任務功能不得混同。

正式交付時必須通過：`tests/worksheet-regression-cases.md`。

---

## Deprecated / Legacy Flow Aliases

下列名稱只可作歷史參考：

- `STEP 3｜教學細節與教材配置確認`
- `STEP 3｜課程結構與簡報模組配置`
- `STEP 4｜引導角色 × 視覺風格選擇`
- 任何省略 STEP 2.5 / STEP 2.6 / Teacher Intent / Lesson Map / Session Map 後直接進角色、風格、頁數、逐頁腳本的流程

遇到上述內容標記：`LEGACY_FLOW_ALIAS`。

---

## Version Resolution

若某 module 文件內版本與本 Manifest 不一致：

1. 先重新 fetch 該檔最新內容。
2. 若 Repository 最新檔案已升版但 Manifest 尚未更新，標記 `MANIFEST_STALE`。
3. 不得以舊 Manifest 覆蓋已明確更新的 canonical file；需先修正 Manifest。
4. 若無法確認，停止高風險流程，不自行猜測。

---

## Adapter Boundary

Adapter 只能描述平台差異，不得改寫 Source Truth、Teacher Intent、Golden Path、Lesson Map、Session Map、Knowledge selection、Character Deep Teaching scope、Polyphonic Source identity、Recognition-only source identity、Lesson Visual Map invariant、Text-Embedded Language evidence layer 或 Visual Grammar 的認知目的。

---

## 核心金句

> 認讀字看教材生字系統，不看方格猜。

> 課文下方小字與課後生字表都要看，兩邊核對後才定身分。

> 生字表 ≠ 生字教學清單。

> AI 主動教形近字與多音字；單一生字詳解由老師指定。

> 多音字先看身分，再看讀音：教材明列保留；AI 只從正式生字推薦；老師可以因班級真實困難指定加入。

> 語詞隨文理解；句型回到原句；修辭從文本發現。
