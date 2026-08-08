# V-MAX Manifest 1.6

## 角色

本檔是 V-MAX 的正式模組索引與版本裁決表。任何 AI 不得自行猜測哪一份檔案較新、哪個舊名稱仍可執行。

---

## Current Canonical Files

```yaml
vmax_manifest_version: 1.6
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
  current_version: 1.2
recognition_only_character_policy:
  path: core/governance/recognition-only-character-policy.md
  current_version: 1.0
hold_policy: core/governance/hold-teacher-interface-policy.md
workflow_test_freeze: core/governance/workflow-test-freeze.md
knowledge_lab_ordering:
  path: core/director/knowledge-lab-ordering-policy.md
  current_version: 1.8
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

認讀字／只認不寫／無方格字採 **Source-driven Presence Detection**：

- `PRESENT`：來源有列，完整保留，與正式生字分開。
- `N/A_SOURCE_NOT_PRESENT`：來源沒有，明確留下 N/A，不生成認讀字模組。
- `UNCERTAIN_SOURCE_LABEL`：來源標示不清，保留原標籤進 HOLD 1，不自行改判。

重要邊界：
- 不以「一二三年級常見、四上目前未見」直接寫成永久年級規則。
- 年級經驗只能提醒 AI 注意檢查，不能取代來源真值。
- 偏旁識字活動不得誤判成認讀字。

權威規則：`core/governance/recognition-only-character-policy.md`。

---

## Grade 3–4 Character Teaching Resolution

以三、四年級教材為預設時：

- 教材正式生字完整保留。
- 深教預設聚焦 `SHAPE_NEAR` 與 `POLYPHONIC`。
- 一般生字維持基本識寫／形音義，不預設每字同規格深教。
- 非形近／非多音字若有特殊構形、語義、評量或文本理解價值，可由 AI 提出例外深教建議。
- 認讀字若來源 PRESENT，屬識讀層，不因身分自動套用正式生字書寫深教規格。

權威規則：`core/director/knowledge-lab-ordering-policy.md`。

---

## Idiom Expression Resolution

- STEP 2.5：教學價值、保留範圍、CORE/FLEX/BONUS。
- STEP 2.6：生活例句、理解重點、單圖／前後對照／漫畫／同框比較／文字優先、是否獨立成頁。

權威規則：`core/director/idiom-expression-visualization-policy.md`。

不得進入視覺風格階段後只剩成語名稱而遺失例句與表達意圖。

---

## Worksheet Resolution

### Pre-study Worksheet

權威技能：`skills/prestudy-worksheet/SKILL.md`

固定精神：
- A4 橫式任務探索單。
- 課前探索＋學後複習雙用途。
- 三、四年級語文預習聚焦高價值形近字／多音字。
- 左／上短任務、右側較大閱讀理解區、下方開放思考區為預設 Layout Grammar；不得機械套版。
- 學生版無答案。

### Post-lesson Short Writing Worksheet

權威技能：`skills/postlesson-short-writing-worksheet/SKILL.md`

固定精神：
- A4 橫式圖像化寫作任務單。
- 素材／畫面啟動 → Bonus 工具箱 → 正式創作。
- Bonus 語詞、四字語詞／成語、句型、修辭皆為可選，不要求全部使用。
- 正式創作區為最大面積。
- 可依本課 Teacher Intent 寫短文、童詩或彈性創作。

預習單與短文單可共享同一課的視覺家族，但任務功能不得混同。

正式交付時必須通過：`tests/worksheet-regression-cases.md`。

---

## Deprecated / Legacy Flow Aliases

下列名稱只可作歷史參考：

- `STEP 3｜教學細節與教材配置確認`
- `STEP 3｜課程結構與簡報模組配置`
- `STEP 4｜引導角色 × 視覺風格選擇`
- 任何 `STEP 2 → STEP 3 → STEP 4` 的舊版直線流程
- 任何省略 STEP 2.5 / STEP 2.6 / Teacher Intent / Lesson Map / Session Map 後直接進角色、風格、頁數、逐頁腳本的流程

遇到上述內容標記：`LEGACY_FLOW_ALIAS`。

---

## Version Resolution

若 module 文件內版本與本 Manifest 不一致：

1. 先重新 fetch 該檔最新內容。
2. 若 Repository 最新檔案已升版但 Manifest 尚未更新，標記 `MANIFEST_STALE`。
3. 不得以舊 Manifest 覆蓋已明確更新的 canonical file；需先修正 Manifest。
4. 若無法確認，停止高風險流程，不自行猜測。

---

## Adapter Boundary

Adapter 只能描述平台差異，不得改寫 Source Truth、Teacher Intent、Golden Path、Lesson Map、Session Map、Knowledge selection、Worksheet learning function 或 Visual Grammar 的認知目的。

若平台沒有直接 Connector / API 或無法驗證寫入，必須標記 `*_HANDOFF_READY` 或 `*_BLOCKED`，不得宣稱已匯入、已生成或已建立。

---

## 核心金句

> Manifest 決定現在誰是權威；模型不靠記憶猜版本。

> GitHub 管系統，Drive 管每一課；兩者職責不要混在一起。

> 認讀字看來源，不看年級猜；有才保留，沒有也要留下 N/A。

> 三、四年級生字完整保留、深教聚焦；成語先決定教不教，再決定怎麼看懂。

> 預習單先帶孩子進文本；短文單再把本課語文工具變成孩子自己的作品。
