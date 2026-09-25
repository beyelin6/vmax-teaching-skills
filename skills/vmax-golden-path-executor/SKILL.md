---
name: vmax-golden-path-executor
description: Execute the V-MAX canonical workflow and approval gates from locked lesson sources through rendering and delivery. Use when producing a complete lesson package by the standard golden path.
---

# V-MAX Golden Path Executor

The executor must create or resume the lesson's `00_施工中_接續區` at task start. After every stage or HOLD, save the stage record in its designated subfolder and update `00_CURRENT_目前進度.md` before continuing. Follow `core/governance/working-handoff-area-policy.md`; no stage may exist only in chat.

版本：2.3

## 目的

本技能是 V-MAX 國語教材工作流的執行控制器。它不重新定義教學設計，而是確保每次實跑只依 `core/governance/vmax-main-workflow.md` 與 Manifest 指定的 canonical rules 前進。

核心原則：

> 一次確認，只前進一個合法階段。

> 執行器必須載入當前階段所有已登記的必要政策，不能只讀舊的單一 Knowledge Lab 規則。

---

## A. 啟動必讀

每次開始或續跑一課，依序讀：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. Google Drive 對應課程 Runtime State
4. `core/governance/vmax-main-workflow.md`
5. `core/governance/hold-teacher-interface-policy.md`
6. `core/governance/continuation-state-gate.md`
7. `core/ui/teacher-review-view-contract.md`
8. `core/schemas/vmax/README.md`
9. `core/presentation/canvas-lock-policy.md`（進入簡報／視覺 stage 時）
10. `core/presentation/text-layer-construction-policy.md`（進入簡報／視覺 stage 時）
11. 當前 stage 的 canonical policies / skills

若舊技能、舊腳本、舊對話與 Manifest 衝突，一律以 Manifest 最新 canonical files 與 Drive Runtime State 為準。

Machine payloads for Source Master, Candidate Inventory, Approved Teaching Selection, HOLD, Revision, Status Transition, and Slide Script MUST conform to the matching schema in `core/schemas/vmax/`. Schema validation does not replace the teacher-facing confirmation card.

### A1. Resume / Continuation State Gate

續作簡報、修圖或生圖前，除 Runtime State 外，必須載入當課 `core/governance/lesson-presentation-execution-rules.md`（若存在），並遵循其優先順序與衝突處理。最新教師確認的 Lesson Execution Rules 高於歷史腳本、Render Request、代表頁與渲染結果，但不得高於官方教材事實。

每個 Render Request 前必須先通過 `PRE_RENDER_RULE_COMPLIANCE_CHECK`；未通過不得呼叫 Renderer。

教師討論結果必須依 `LESSON_LOCAL`、`REUSABLE_PATTERN`、`GLOBAL_SKILL_RULE` 分層保存。單課規則只更新當課 Execution Rules；只有跨課驗證後才可 promotion 到共用技能，並同步版本與 Manifest，不得因單課施工決策直接改寫全域規則。

在合法序列之前，必須先依 `core/governance/continuation-state-gate.md` 完成 State Sync Receipt。未確認 Runtime revision、目前 HOLD、教師最新決定、當前 stage 已應存在的上游版本與適用視覺基準、當前工作項目前，不得執行任何分析、設計、渲染或批次。

若「聊天記憶／本地候選／Drive Runtime／GitHub Manifest」出現差異，標記 `CONTINUATION_STATE_BLOCKED`，列出差異與下游影響，等待教師決定；不得自行選邊。

---

## B. 合法前進序列

```text
SOURCE 0｜Google Drive Source Library 尋源
→ STEP 1｜教材定錨
→ HOLD 1
→ STEP 2｜AI 教學價值判讀／Teacher Intent 候選
→ HOLD 2
→ STEP 2.5｜語文輻射分析與教師選擇
→ HOLD 2.5
→ STEP 2.6｜成語表達與視覺化確認
→ HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map
→ 補充內容／學習框架候選
→ Session Map
→ Lesson Visual Map Strategy
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ 頁型與教學功能草案（不展開逐頁施工細節）
→ 風格庫 3–5 組候選／主風格＋頁型混搭方案
→ HOLD｜教師選擇主風格與頁型混搭規則
→ 鎖定 Style Selection Profile／Style Matrix
→ 鎖定角色與畫布
→ 頁數估算／頁數帳本確認 HOLD
→ PAGE_DETAIL_CONFIRMATION｜逐頁可施工細節稿
→ HOLD｜等待教師確認逐頁施工稿
→ 代表頁選擇檔驗證（只從 PAGE_DETAIL_CONFIRMATION 挑選）
→ 代表頁驗證／逐類教師確認 HOLD
→ 全量 Renderer（小批次，每批教師確認 HOLD）
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery Gate
→ Google Drive 歸檔與驗證
```

### PAGE_DETAIL_CONFIRMATION

`Slide Architecture`、教師選定的 `Style Selection Profile`／`Style Matrix`、角色、畫布與頁數帳本鎖定後，Executor 才能把前一步的版面配置初稿轉成正式 `PAGE_DETAIL_CONFIRMATION`（依 `schemas/page-detail-confirmation-profile.md`）。正式母檔必須先建立全課唯一的 `page_number_system` 與 `section_marker_system`，由代表頁實測、教師確認後鎖定各自 hash；後續頁面只能沿用，不得每頁重新決定。母檔另必須列出學生可見文字、source refs、圖片細節、角色／物件／動作、禁止誤畫、閱讀順序、文字與圖片區、留白、protected zones、字體角色與互動，並逐頁帶入核准的 `style_variant_id`、`layout_id`、`layout_contract` 與 hash。每個出場角色必須帶入 `base_character_id`、`core_dna_ref`、`approved_asset_id`、`asset_version`、`allowed_variations` 與 `prohibited_drift`；角色未出場也要明確記錄。教師確認前標記 `PAGE_DETAIL_CONFIRMATION_PENDING`，不得建立正式 Slide Script、代表頁或 Renderer；確認後才可挑選代表頁；各實際啟用頁型均經教師確認後，才可小批次製作。任何頁面變更都必須更新該頁 revision，不得只修改 prompt 或 Render Request。

風格 HOLD 必須先完成：依課文提出 3–5 組風格庫候選／混搭方案，顯示主風格、頁型變體與限制，等待教師選擇。`selected_style_id` 未被教師確認前保持空值；不得由 Executor、Presentation Engine、Renderer 或平台預設直接選風格。風格選定後，建立風格 hash 與 `BATCH_CONSTRUCTION_LOCK`，後續頁面只能沿用該主風格及已核准頁型變體。

若教師確認的是本課新角色，必須先依 `core/character/character-library-writeback-policy.md` 完成 Registry writeback，預設 `LESSON_ONLY`，再進入風格、逐頁版面與批次製作；沒有 `registry_ref`、DNA、核准資產與 hash 時標記 `CHARACTER_REGISTRY_WRITEBACK_REQUIRED`。

### SLIDE_ARCHITECTURE_LOCK

進入 `Visual Grammar / Slide Architecture` 前，Executor 必須建立並寫入 Slide Script 的 `SLIDE_ARCHITECTURE_LOCK`。預設順序為：

`opening → overview → visual_mind_map → paragraph_learning(text_and_context → vocabulary_explanation → rhetoric_or_sentence_pattern → meaning_comprehension) → character_comparison → idiom_learning → textbook_language_activity → summary_transfer`

頁數、模板或外加變體不得靜默重排此順序。若教師確認了變體，必須另存 `architecture_mapping`，逐項標記 `preserved`、`transformed`、`extended` 或 `omitted` 及理由；變體可以改變教學呈現，但不得遺失任何教師指定的學習結果。

若本課無需處理成語，STEP 2.6 明確記錄 `N/A_NO_IDIOM`，仍須停在 HOLD 2.6；教師確認後才進 Teacher Intent Lock。

---

## C. Confirmation Transition Guard

教師只輸入「確認／好／可以／OK／沿用」時，只等於：

`confirm_current_hold = true`

執行器必須：
1. 關閉當前 HOLD。
2. 先回寫教師決定與 State revision。
3. 重新同步 Runtime State 與主流程，取得唯一合法下一步。
4. 只執行該下一步。
5. 若下一步有 HOLD，完成後立即停住。
6. 不得順便執行再下一步。

違反：`FLYING_TRAIN / SKIPPED_DECISION_LAYER`。

---

## D. Teacher Review View Guard

任何 stage／HOLD 先保存完整 Machine Payload，再依 `core/ui/teacher-review-view-contract.md` 顯示教師審核卡。預設不得展開 raw JSON／YAML。

審核卡必須顯示：結論、教材證據、知識層、缺口、AI 理由、本次唯一決定、唯一下一步。重要項目標示 `[教材明載] / [教師補充] / [AI 延伸] / [待核對]`。

若 UI 未通過，標記 `RAW_SCHEMA_DUMP / TEACHER_INTERFACE_OVERLOAD / KNOWLEDGE_LAYER_MIXED`，停在原 stage。

## E. STEP 1 專用 Guard｜教材身分先讀對

STEP 1 必須載入：
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`
- `core/schemas/vmax/source-ingestion-record.schema.json`

認讀字必須做雙來源核對：
1. 課文頁下方的小字生字標示
2. 課文後方獨立生字表／生字教學頁

規則：
- 無方格只能是版面線索，不等於認讀字。
- 認讀字必須由教材生字系統明確區分。
- 兩處不一致 → `SOURCE_CONFLICT`，進 HOLD 1，不得靜默選一邊。
- 來源未列 → `N/A_SOURCE_NOT_PRESENT`。
- 未建立 `SOURCE_INGESTION_RECORD`、必要區塊未完成覆蓋記錄，或存在未命名 `UNCERTAIN` → `STEP1_INCOMPLETE`；不得直接組裝 Source Master。
- 完整正式生字、認讀字雙來源、教材詞語聯集、課文結構或 provenance 任一必要項未完成 → `STEP1_INCOMPLETE`；先完成可自行核對項目，再集中要求必要補來源；不開放完整 STEP 1 核准。
- STEP 1 不得鎖 Mode、教學主軸、固定詩節／段落迴圈、Scenario、角色、視覺或頁數。

---

## E2. STEP 2／STEP 2.5 Selection Object Guard

STEP 2 必須輸出符合 `core/schemas/vmax/candidate-inventory.schema.json` 的 `CANDIDATE_INVENTORY`。候選項目只保存教材內容、來源證據與 AI 分析，不保存教師選教決定。

STEP 2.5 完成教師確認後，才建立或更新符合 `core/schemas/vmax/approved-teaching-selection.schema.json` 的 `APPROVED_TEACHING_SELECTION`。只有其中 `confirmed_by_teacher: true` 的項目，才能供 Learning Modules、Teaching Strategy 或學生輸出使用。

若候選尚未進入 Approved Teaching Selection，保持 `AI_SUGGESTION`／`PENDING`／`HOLD`，列出受影響下游並停止，不得自行轉成 `MUST_TEACH`。

---

## F. STEP 2.5 專用 Guard｜生字／多音字不得再跑回舊規則

STEP 2.5 必須同時載入：
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`

### 生字深教唯一規則

STEP 2.5 不得把「教材成語清單」當成唯一語文候選來源。執行器必須分開保留：正式生字／認讀字、生字關聯詞／生字關聯成語、課文成語／四字詞語、多音字及其詞語。任何含有本課正式生字、形近字或多音字的詞語／成語，必須保留多重 provenance；成語數量上限只能影響獨立成頁推薦，不得刪除生字關聯記錄。

在進入 STEP 2.6 前，必須產生 `LANGUAGE_CANDIDATE_COVERAGE`，核對每一個正式生字是否已有關聯詞／關聯成語判讀，以及每個課文成語是否有保留／不保留理由。缺少任一對應時標記 `STEP2.5_COVERAGE_INCOMPLETE`，停留 STEP 2.5 補齊覆蓋；不得進入 HOLD 2.5，也不得將一般「確認」視為完成核准。覆蓋完整後才顯示 HOLD 2.5。

`LANGUAGE_CANDIDATE_COVERAGE` 必須保存 `character_related_idioms` 與每項的 `character_refs`、`source_refs`、`decision`。進入 Slide Script 前，所有 `decision: retained` 的生字相關成語必須各自出現在 `final_idiom_section_refs`；若缺少任一對應，標記 `IDIOM_CHARACTER_COVERAGE_INCOMPLETE`，不得進入 Renderer。

教材正式生字完整保留，但：

- AI 主動深教只有 `SHAPE_NEAR` 與 `POLYPHONIC`。
- 一般單字預設 `BASIC_LITERACY_ONLY`。
- 單一生字詳解只有教師明確指定後，才能成為 `TEACHER_ADDED_SINGLE_CHARACTER`。
- 「容易寫錯／字形複雜／字源有趣／評量重要／語義特殊」都不能成為 AI 自動建立單字頁的第三入口。
- AI 最多只能提示 `AI_SUGGESTION_SINGLE_CHARACTER`，不得自動成頁。

### 多音字合法來源

只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：AI 只能從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`：教師可依班級困難指定加入

形近補充字、比較字、AI 補充字、課文一般字，不因本身多音而被 AI 自動拉進多音字單元。

### 學生可見字群頁

- 形近字：大字＋注音＋字義情境圖＋例詞＋哪裡像／哪裡不一樣＋辨認提示。
- 多音字：同一大字＋不同讀音＋語意／情境＋例詞／例句＋回到課文判斷。

完成後只顯示形近字、多音字、教材詞語／成語審核表與待確認項目。每個項目顯示來源狀態、教材證據、字形／讀音核對、AI 建議與理由、教師決定。

部首、偏旁、字形口訣逐字核對；多音字以課本生字欄／課文注音為本課第一來源，教育部《國語辭典簡編本》只作補充驗證，例詞必須逐詞查核。任何疑點停在 STEP 2.5。

教材已列的多音字讀音集合與列數不得由 AI 自行擴張；若 AI 發現教材未列的其他讀音，只能標為 `AI_SUGGESTED_READING`，完成權威來源驗證並列出受影響下游項目，等待教師確認後才能進入預習單、簡報或其他學生可見輸出。

完成後顯示 `HOLD 2.5`，等待教師確認；不得展開詩節教學或其他 stage。

---

## G. STEP 2.6 專用 Guard｜成語表達不可掉落

依 `core/director/idiom-expression-visualization-policy.md`。

對保留成語至少決定：
- 學生可理解的意思
- 生活例句與 provenance
- 理解重點
- 視覺表達關係
- 是否值得獨立成頁
- AI 理由

禁止只剩名稱／定義，禁止所有成語固定同一漫畫格數。

完成後顯示 `HOLD 2.6`。

---

## H. Text-Embedded Language Guard

進 Lesson Map、Knowledge Lab、Slide Architecture 後，只要處理語詞／句型／修辭，必須載入：

- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`

固定：
- 語詞隨段落，附原文＋學生易懂語意。
- 句型一定帶課文原句，再抽結構。
- 修辭先從原文發現效果，再命名。
- 原文證據層不得在 Renderer 階段消失。

---

## I. Lesson Visual Map Guard

依 `core/visual/lesson-visual-map.md`。

若教師已選定「整課圖像心智地圖」，它成為 downstream invariant：
- 簡報大綱必須明列。
- Slide Architecture 必須保留。
- 頁數估算不得省略。
- Renderer 不得靜默刪除。

若消失：`LVM_OUTLINE_DROPPED`。

---

## J. Delivery / Drive Guard

進入 Full Renderer 時必須載入：

- `core/renderer/image-first-hybrid-renderer.md`
- `skills/vmax-image-renderer/SKILL.md`

代表頁不是重新發想頁面；必須先依 `schemas/representative-page-selection-profile.md` 建立選擇檔，從已核准 `PAGE_DETAIL_CONFIRMATION.pages` 以 `page_detail_page_id` 挑選，並保存 PAGE_DETAIL 檔案 hash 與每頁 `page_spec_sha256`。代表頁製作前執行 `validate_representative_selection.py`，並把課級頁碼／區段標籤的實測結果與系統 hash 納入代表頁確認；教師確認後才可把該系統沿用到全量頁。缺欄、hash 不一致、未涵蓋實際頁型或出現 PAGE_DETAIL 沒有的內容時，標記 `REPRESENTATIVE_PAGE_SOURCE_CONFLICT`／`REPRESENTATIVE_PAGE_FAMILY_COVERAGE_INCOMPLETE`，不得施工。

代表頁與批次頁交付教師檢查時，優先使用 ChatGPT 原生圖像生成／影像編輯工具直接顯示在工作區，保留「編輯」入口與最新核准圖片引用；不得只交付 PNG 卡片、下載連結或檔案路徑。若當下平台無法提供原生入口，標記 `NATIVE_IMAGE_REVIEW_UNAVAILABLE` 並說明限制，再提供可直接預覽的替代結果。

Full Renderer 的前置條件不是「看過一張樣張」，而是跨頁型代表頁組均已核准：課文閱讀頁、一般圖片合成頁、高風險語文頁，以及本課啟用時的 Lesson Visual Map。教師的「可以」只核准本次實際展示的頁型；未展示頁型不得自動通過。

簡報畫布必須先詢問教師選擇 `4:3` 或 `16:9`，再建立並鎖定 `canvas_lock`；不得由 Renderer、平台預設或舊對話自行選邊。除課文閱讀頁外，學生可見頁預設為整頁圖片式合成，正式文字採 `VERIFIED_RASTER_TEXT_LAYERS`。禁止背景圖＋文字框、卡片牆、大量半透明框或純文字骨架。Full Renderer 前必須完成代表頁組：課文欣賞、難詞、句型／修辭、文意理解、形近字、多音字、成語／四字詞語、總結遷移等實際啟用頁型；每類均需教師確認，且每頁先載入當課角色定錨。全量必須以 4–8 頁小批次推進並逐批檢查；任一批發生 `COMPOSITION_REGRESSION`、`TYPED_TEXT_LAYOUT_FAIL`、`TEXT_OBJECT_DETACHED` 或角色／風格漂移即停止，不得做完整套後才回頭驗收。

對每個必要圖片建立 Render Request，探測當前平台實際工具並執行。prompt、Renderer Script、Visual YAML 或 `IMAGE_HANDOFF_READY` 不等於圖片完成；只有實際資產通過重檢並標記 `RENDER_VERIFIED` 才能進入 Quality Gate。工具不可用時保留 handoff 並回報阻塞，不得跳過圖片需求。

交付必須同時載入：
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`

Google Drive 固定根目錄為 Manifest 指定的 `V-MAX 教材庫`。

每課版本資料夾固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做不覆蓋舊版，依 Drive 實際現況建立 `_01 / _02 / _03...`。

每次教師確認、代表頁核准／退回、批次產生檢查頁或批次停止後，必須依 `core/governance/cloud-checkpoint-policy.md` 立即上傳確認快照；快照包含確認檔、頁面、hash、原生圖像回條與目前狀態。上傳後必須再次 list/search 驗證並回寫 Runtime State；`CLOUD_CHECKPOINT_UNVERIFIED` 或 `RUNTIME_WRITE_BLOCKED` 時不得宣告可接續，也不得進行下一個高風險施工階段。只有實際上傳後再次 list/search 驗證成功，才可宣告 Archive PASS。

---

## K. Anti-template / Legacy Guard

以下視為錯誤：
- STEP 3／STEP 4／STEP 2.75 舊流程名稱復活
- raw JSON／YAML 直接作為教師確認畫面
- STEP 1 來源未完整就要求核准
- 教材明載、教師補充與 AI 延伸未標記或混寫
- 每段固定相同頁數／步驟
- 所有生字固定同規格頁
- AI 自動增加第三類單字深教入口
- 形近補充字被拉去做多音字
- 認讀字只靠「無方格」判定
- 已選定整課圖像心智地圖卻在大綱消失
- Drive 仍使用舊五類資料夾結構
- 一張代表頁通過就直接全量生成
- 非課文頁退化成背景圖＋文字框、卡片牆或大量半透明框
- 圖片模型文字錯誤兩次後直接刪頁，而非改走可控排字合成

---

## 核心金句

> AI 做重判斷，老師只改例外；一次確認只走一站。

> 生字表 ≠ 生字教學清單；AI 主動只教形近字與多音字，單字詳解由老師指定。

> 規格寫了不算載入；Executor 必須真的把當前 canonical policy 帶進實跑。

## 國語簡報施工前確認（GLOBAL_SKILL_RULE）

語文規劃、簡報施工或每次續作／下一步／確認前，必須載入 `core/governance/presentation-preconstruction-policy.md`。先讀最新 Drive Runtime；到 STEP 2.5 才檢核成語雙軌與每個正式生字的延伸成語覆蓋；缺漏為 `VOCABULARY_IDIOM_COVERAGE_INCOMPLETE`。風格、角色、畫布與頁數帳本鎖定後，建立逐頁施工稿並停等確認；核准後才選代表頁，逐類核准後才進每批最多 8 頁的小批次，每批完成必須停等教師確認。每個 stage／HOLD 都回寫並驗證 Runtime State 與 Runtime Index；不得以舊流程簡寫跳過這些關卡。

## STEP 1 整合擷取

SOURCE 0／STEP 1、重新製作或來源補漏時，必讀 `core/governance/step1-source-anchor-policy.md` 第 G 節。依既定清單完成所有可查頁區與類別，包含多音字旁欄補充；階段內持續處理，剩餘缺口集中詢問，完整後才交付一份審核稿並停在 HOLD 1。LKB、成語延伸選教、風格、角色、頁數及代表頁不作為 STEP 1 前置條件。
