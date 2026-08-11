# V-MAX Manifest 2.6-draft

## 角色
本檔是 V-MAX 正式模組索引與版本裁決表。任何 AI 不得自行猜測哪份檔案較新、哪個舊名稱仍可執行。

---

## Current Canonical / Candidate Files

```yaml
vmax_manifest_version: 2.6-draft
bootstrap: V-MAX_BOOTSTRAP.md
runtime_contract:
  path: runtime/lesson-state.md
  current_version: 2.2-draft
runtime_storage:
  provider: GOOGLE_DRIVE
  root_folder_name: 00_Runtime_State
  root_folder_id: 1AOjYwALGVNWu99b-SnjBUSALEDrlReMt
  index_title: V-MAX_Runtime_Index
  index_document_id: 1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ
main_workflow:
  path: core/governance/vmax-main-workflow.md
  current_version: 2.1-draft
executor:
  path: skills/vmax-golden-path-executor/SKILL.md
  current_version: 1.3-draft

source_library_policy: core/governance/source-library-policy.md
step1_source_anchor:
  path: core/governance/step1-source-anchor-policy.md
  current_version: 1.3
recognition_only_character_policy:
  path: core/governance/recognition-only-character-policy.md
  current_version: 1.1
lesson_knowledge_base:
  path: core/knowledge/lesson-knowledge-base-policy.md
  current_version: 1.0-draft

hold_policy: core/governance/hold-teacher-interface-policy.md
workflow_test_freeze: core/governance/workflow-test-freeze.md
workflow_hold_regression:
  path: tests/workflow-hold-regression-cases.md
  current_version: 1.6

teaching_skill_selection:
  path: core/pedagogy/teaching-skill-selection-policy.md
  current_version: 1.0-draft
lesson_budget:
  path: core/governance/lesson-budget-policy.md
  current_version: 1.0-draft

knowledge_lab_ordering:
  path: core/director/knowledge-lab-ordering-policy.md
  current_version: 1.9
character_deep_teaching_focus:
  path: core/director/character-deep-teaching-focus-policy.md
  current_version: 1.1
polyphonic_source_policy:
  path: core/director/polyphonic-source-policy.md
  current_version: 1.0
prestudy_language_selection:
  path: core/worksheet/prestudy-language-selection-policy.md
  current_version: 1.1
character_group_visual_comparison:
  path: skills/character-group-visual-comparison/SKILL.md
  current_version: 1.1-draft
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

experience_layer:
  path: core/experience/vmax-experience-layer.md
  current_version: 1.0-draft
extension_layer:
  path: core/extension/extension-layer-policy.md
  current_version: 1.0-draft

typography_bridge:
  path: vmax-typography-bridge/SKILL.md
  current_version: 1.1-draft
renderer_contract:
  path: core/renderer/image-first-hybrid-renderer.md
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
  current_version: 1.3
google_drive_lesson_archive:
  path: skills/google-drive-lesson-archive/SKILL.md
  current_version: 1.0

system_architecture:
  path: core/governance/vmax-system-architecture.md
  current_version: 1.0-draft
  status: CANDIDATE_UNTIL_REGRESSION_PASS

adapters:
  chatgpt: adapters/chatgpt.md
  codex: adapters/codex.md
  gemini: adapters/gemini.md
  notebooklm: adapters/notebooklm.md
  canva_renderer: adapters/canva.md
```

---

## Runtime Authority
GitHub 保存規格；每一課即時 Runtime State 以 Google Drive 為權威。不得用模型記憶、舊對話或舊簡報取代 Drive 最新 State。

---

## Canonical Golden Path Candidate 2.1

```text
SOURCE 0
→ STEP 1 + Lesson Knowledge Base
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
→ GATE A Teaching Direction Lock
→ Experience Decision
→ Extension Check
→ Knowledge Lab
→ Teaching Skill Selection Lock
→ Visual Grammar / Slide Architecture
→ Lesson Budget / Page Ledger
→ Storyboard
→ GATE B Experience + Storyboard Lock
→ Style Recipe / Typography Lock
→ Representative Validation
→ GATE C Representative Visual Validation
→ Full Renderer
→ Text QA / Typography QA
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery
→ Google Drive Archive Verification
```

無成語：`N/A_NO_IDIOM`。無外掛：`EXTENSION_OFF`。

---

## Teacher Control Resolution

### Mandatory HOLD
HOLD 1/2/2.5/2.6 採 single-stage advance，保護來源與教學範圍。

### Production Gates
- Gate A：Teaching Direction Lock
- Gate B：Experience + Storyboard Lock
- Gate C：Representative Visual Validation

Gate C confirmed 後可批次 Renderer；不得逐頁重新建立同一決策確認。

---

## Character Teaching Resolution

三、四年級：
- 正式生字完整保留。
- AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。
- 一般單字 `BASIC_LITERACY_ONLY`。
- 單一生字詳解只有教師指定。

多音字來源只有：TEXTBOOK／AI_RECOMMENDED_FROM_FORMAL_CHARACTER／TEACHER_ADDED。

形近字／多音字頁遵循 `character-group-visual-comparison` 1.1-draft：主要字群原則一群一頁；簡單兩字群可一頁兩組；預習做過仍可 CORE_REINFORCE。

---

## Text / Typography Resolution

重要閱讀教學保留 Text Anchor；RETURN 為可選技能，不是固定頁。

圖文一體生成允許 AI 圖片引擎產生繁中草稿文字，但正式輸出必須經 Typography/Text QA。

P0 逐字檢查：課文、生字、形近字、多音字、注音、學生辨識目標字、關鍵句／臺詞。

字形本身是教學內容時，Teaching Glyph Rule 優先於藝術化變形。

---

## Experience Resolution

同冊：Book DNA；同課：Lesson Skin；跨教材：Visual Identity Lock；不同用途：Material Mode。

Guide Character 必須有教學功能；Learner Role／Scenario 可 OFF。每課原則 1 個 Surprise Signature，但不得為驚喜而驚喜。

預習單、短文單、正式簡報共享同課角色、視覺世界與 Typography Lock，但依用途調整密度。

---

## Extension Resolution

支援 DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM，模式 LIGHT / THEME_MODE。

新增 Extension 必須重算 Lesson Budget，先問「它取代什麼？」；若牽強則降 PLUS 或不加入。

---

## Lesson Budget Resolution

頁數只能在 Slide Architecture 後正式成立。

- 一頁 = 一個完整認知場景
- 同頁可兩個有層次問題
- 新增頁必須有新增 learning_gain
- 漂亮／額外例子／重複／趣味知識預設不獨立成 CORE 頁

---

## Lesson Visual Map Resolution
教師選定 LVM 後成為 downstream invariant；大綱、Slide Architecture、Page Ledger、Renderer 不得靜默刪除。

---

## Worksheet Resolution
預習單與短文單維持既有 1.1 規則；A4 100% 實際列印時，所有學生需要閱讀、辨認、勾選或作答依據的文字不得低於 12 pt。

---

## Google Drive Lesson Archive Resolution
固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。
完整重做不覆蓋舊版；只有實際上傳並再次驗證成功才 Archive PASS。

---

## Draft / Version Resolution
本分支 2.6-draft 將新增 v1 policies 登記為 candidate canonical。只有完成必要 regression 且教師確認封版後，才移除 `draft` 並視為 main canonical。

若模組內版本與 Manifest 不一致：重新 fetch 最新檔；無法確認即停，不猜。

---

## Legacy / Conflict Rules
以下一律視為舊規則：
- STEP 3／STEP 4 舊主流程
- AI 自動第三類單字深教
- 無方格直接等於認讀字
- 語詞／句型／修辭沒有原文證據
- 從視覺工具反推教學目的
- 每題一頁／固定每段模板
- 每課強制相同 Scenario／角色／Style
- 已選 LVM 後段消失
- 圖片中文字未 QA 即交付
- Drive 舊五類結構
- A4 學習單縮到 12 pt 以下

---

## 核心金句
> Manifest 決定現在誰是權威；Executor 必須真的載入。

> 教學技能先於視覺工具；視覺融合優先，但正式文字必須校對到對。
