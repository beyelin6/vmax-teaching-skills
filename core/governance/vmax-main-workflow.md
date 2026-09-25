# V-MAX Main Workflow 2.10

## 定位

本檔定義 V-MAX 教材製作的正式主流程、教師確認點與必要 policy 載入關係。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 等不得反向改寫此核心順序。

所有實跑必須遵循：
- `skills/vmax-golden-path-executor/SKILL.md`
- `V-MAX_MANIFEST.md`
- Google Drive 該課 Runtime State

Machine-readable workflow objects use the portable contracts in `core/schemas/vmax/`.

The teacher-facing workflow remains Phase／STEP／HOLD based; schemas do not replace the confirmation card. A status transition must follow `status-transition.schema.json`, and an upstream change must create a `revision-event` before any downstream recalculation.

---

## A. Canonical Policy Wiring

### Teacher Review / HOLD
- `core/ui/teacher-review-view-contract.md`
- `core/governance/hold-teacher-interface-policy.md`

### SOURCE / STEP 1
- `core/governance/source-library-policy.md`
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`
- `core/schemas/vmax/source-ingestion-record.schema.json`

### STEP 2.5
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`

### STEP 2.6
- `core/director/idiom-expression-visualization-policy.md`

### Lesson / Knowledge / Slide
- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`
- `core/director/language-knowledge-placement-policy.md`
- `core/ui/text-ui-system-2.md`
- `core/character/character-system-2.md`
- `core/visual/lesson-visual-map.md`

### Delivery
- `core/governance/cloud-checkpoint-policy.md`
- `skills/presentation-engine/SKILL.md`
- `core/presentation/page-family-construction-contracts.md`
- `core/presentation/classroom-image-slide-policy.md`
- `core/renderer/image-first-hybrid-renderer.md`
- `skills/vmax-image-renderer/SKILL.md`
- `core/quality/visual-drift-detector.md`
- `core/quality/quality-gate-2.md`
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`

### Regression
- `tests/workflow-hold-regression-cases.md`
- `tests/character-teaching-regression-cases.md`
- `tests/worksheet-regression-cases.md`

---

## B. Golden Path

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

若無需處理成語：STEP 2.6 明確記錄 `N/A_NO_IDIOM`，仍須停在 HOLD 2.6；教師確認後才進 Teacher Intent Lock，不得默默跳過。

---

## C. Single-stage Advance

```text
HOLD 1 確認 → STEP 2 → HOLD 2
HOLD 2 確認 → STEP 2.5 → HOLD 2.5
HOLD 2.5 確認 → STEP 2.6 → HOLD 2.6
HOLD 2.6 確認 → Teacher Intent Lock
```

一次確認只走一站。違反：`RUNAWAY_WORKFLOW / SKIPPED_HOLD / STAGE_LEAP`。

---

## D. STEP 1｜教材定錨

只回答「教材裡有什麼」，不決定角色、畫風、頁數。

必須包含：
- 課文與結構
- 完整正式生字
- 認讀字 status
- 教材語詞／成語／語文活動
- provenance / gaps

### 認讀字固定檢查

必須交叉核對：
1. 課文頁下方小字生字標示
2. 課文後方獨立生字表／生字教學頁

無方格只作線索，不等於認讀字。兩處衝突 → `SOURCE_CONFLICT`。

只有完整性條件 PASS 才進 HOLD 1；必要來源仍缺漏時回報 `STEP1_INCOMPLETE`，不得要求核准或前進。

完成後 HOLD 1。

---

## E. STEP 2｜AI 教學價值判讀

STEP 2 先建立 `CANDIDATE_INVENTORY`：完整列出教材中可供判讀的教學候選，保留原文、來源證據與 AI 分析。候選物件不得寫入教師決定。

AI 主動提出：
- 哪些文本值得深讀／朗讀／推論／比較／聯想／遷移
- 哪些可短帶／Bonus／降權
- 理由
- 哪些地方要保留學生發現空間

完成後 HOLD 2。

HOLD 2 只確認教學價值判讀與候選範圍，不等於確認正式教學清單；正式選教另由 `APPROVED_TEACHING_SELECTION` 保存。

---

## F. STEP 2.5｜語文輻射 Selection Gate

### 生字
- 正式生字完整保留。
- AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。
- 一般單字 `BASIC_LITERACY_ONLY`。
- 單一生字詳解只有教師指定 `TEACHER_ADDED_SINGLE_CHARACTER`。
- 易錯、複雜、字源有趣、評量重要都不是 AI 自動第三入口。

### 多音字
合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：AI 只能從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`

形近補充字／比較字／認讀字／課文一般字不得被 AI 因本身多音而自動拉入。

STEP 2.5 將教師對候選的 `MUST_TEACH／OPTIONAL／DO_NOT_TEACH／EXTENSION／HOLD` 決定寫入 `APPROVED_TEACHING_SELECTION`；每筆必須有教師確認事件。未寫入該物件前，只能稱為 AI 建議或 HOLD。

### 形近字
先做真正辨析：共同／差異部件、字義、混淆點、辨認提示，再推薦。

### 成語
先判教學價值與保留範圍；後續 STEP 2.6 再決定例句與視覺表達。

STEP 2.5 必須維持四份不可互相覆蓋的候選聯集：正式生字與認讀字身分、生字關聯詞／生字關聯成語、課文成語與四字詞語、多音字與讀音詞語。含有正式生字、形近字或多音字的詞語／成語，必須保留其關聯來源；不得因課文成語數量較多、成語頁數有限或去重而從生字關聯聯集中消失。若同一項同時屬於兩個聯集，保留一筆候選並保留多重 provenance。

STEP 2.5 結束前必須輸出 `LANGUAGE_CANDIDATE_COVERAGE`：列出各聯集的總數、保留數、未保留數與理由，並特別列出所有「生字 → 關聯詞／成語」對應。任一聯集未完成覆蓋，標記 `STEP2.5_COVERAGE_INCOMPLETE`，不得進入 HOLD 2.5。

### 預習單
`3–5 組` 只限制預習單主要練習區，不限制正式教學。

完成後 HOLD 2.5。

---

## Lesson Architecture Baseline 與外加變體

每課先建立並鎖定 `schemas/lesson-architecture-profile.md`：開頭導入 → 課文總說 → 圖像式心智圖 → 各段（課文／語詞解釋／修辭或句型／文意理解）→ 形近字 → 成語 → 教材語文活動 → 總結與學習遷移。

平板操作、四學公開課、議題融入與教師自訂模板都是 Baseline 的呈現變體。變體可以重組活動、媒介、互動、時間配置與頁面組織，但必須以 `architecture_mapping` 回指每一個 Baseline 學習結果，標記 `preserved`、`transformed`、`extended` 或經教師確認的 `omitted`。不得未標示地改寫 Official Knowledge，也不得靜默刪除教師指定的學習重點。

## G. STEP 2.6｜成語表達與視覺化

對保留成語決定：
- 學生可理解意思
- 生活例句＋provenance
- understanding_goal
- visual_expression
- independent_page_recommendation

成語插圖優先表達例句句意，不預設畫典故。

完成後 HOLD 2.6。

---

## H. Teacher Intent → Lesson / Session

Teacher Intent 採 `PROPOSED → CONFIRMED → LOCKED`。

Lesson Map 先建立整課理解旅程；Session Map 依內容密度自然切堂；不得固定段落頁數或固定每段五件套。

補充內容／框架可選，不強迫。

---

## I. Lesson Visual Map Strategy

判斷 `OPEN / CLOSE / BOTH / OFF`。

若教師已選定整課圖像心智地圖：
- 成為 downstream invariant。
- 簡報大綱必須明列。
- Slide Architecture、頁數估算、Renderer 不得靜默刪除。

---

## J. Text-Embedded Language

只要處理語詞／句型／修辭：
- 語詞隨段落，附原文片段＋學生易懂意義。
- 句型帶課文原句，再抽結構與仿用。
- 修辭從原文發現效果，最後才命名。
- 原文證據層不得在後段消失。

---

## K. Knowledge Lab → Slide Architecture

Knowledge Lab 讀取已確認的 2.5／2.6，不得改寫已鎖內容。

Visual Grammar / Slide Architecture 先認知關係再決定畫面。

簡報續作與生圖前必須讀取當課 `core/governance/lesson-presentation-execution-rules.md`。它承接教師已確認的課程局部視覺決策，優先於歷史腳本、Render Request、代表頁與渲染結果，但不得高於官方教材事實。

規則分為 `LESSON_LOCAL`、`REUSABLE_PATTERN` 與 `GLOBAL_SKILL_RULE`；單課施工決策不得直接污染全域技能，只有跨課驗證後才可 promotion。

完成 Slide Architecture 後，先建立頁型與教學功能草案供風格推薦，尚不展開逐頁施工細節。接著由 Style Recommender 產生 `working/style-recommendation.md`、`working/style-selection-profile.md` 與 `working/page-family-style-matrix.md`。

Style Recommender 必須依本課課文、教學策略、角色與頁面家族提出 3–5 組風格庫候選，也可提出主風格＋頁型混搭方案；這一步是教師選擇 HOLD，不是自動決策。`selected_style_id`、主風格、混搭頁型與限制未經教師確認前，不得建立 PAGE_DETAIL_CONFIRMATION、代表頁、正式 Slide Script 或啟動 Renderer。

風格、角色、畫布與頁數帳本確認後，才產生 `working/slide-page-layout-brief.md` 的逐頁可施工細節；與上述核准文件共同組成 `PAGE_DETAIL_CONFIRMATION`。每頁還必須明列：頁碼與區段、`page_family_contract_id`、完整 `page_specific_plan`、學生可見的每一段文字、來源回指、圖片目的／場景／人物／動作／必要物件／禁止誤畫、閱讀順序、文字區、圖片區、留白、protected zones、字體角色與互動方式。不得只寫抽象主題或一句圖片 prompt。

風格可混搭，但只能以頁面類型為單位管理：同一頁型必須使用同一 `style_variant`；不同頁型才可使用不同媒材。水彩、漫畫或其他畫風僅為示意，實際媒材、版型與構圖應依教材、教學功能與教師偏好推薦，不得硬編成固定答案。整課共用的字體、畫布、角色 DNA、章節標籤、留白與文字規則仍必須一致。

教師確認角色後，若是本課新角色，先完成 Character Registry writeback（預設 `LESSON_ONLY`）。教師確認主風格／頁型混搭規則後，才建立 Style Selection Profile 的 `CONFIRMED` 鎖；每個頁型變體同時鎖定 `layout_id`、`layout_contract` 與 hash。接著教師確認逐頁版面稿與頁型風格矩陣；在此之前狀態為 `PAGE_DETAIL_CONFIRMATION_PENDING`，不得建立正式 Slide Script、代表頁或啟動 Renderer。確認後才建立 `PAGE_DETAIL_CONFIRMATION_APPROVED` 與 `BATCH_CONSTRUCTION_LOCK`；Renderer 必須依核准母檔批次製作，不能自行補抓教材內容、決定風格或改變頁面排版意圖。

只有完成 Slide Architecture 後才可估頁數；頁數是結果，不是起點。

教師口述型圖像簡報必須依 `core/presentation/classroom-image-slide-policy.md`、`core/presentation/canvas-lock-policy.md` 與 `core/presentation/text-layer-construction-policy.md` 建立：先詢問教師選擇 `4:3` 或 `16:9`，選定後鎖定畫布；學生頁只放學生此刻需要看見的內容；教師講稿、答案與來源細節分流到教師層。若當課已有核准 Lesson Baseline／施工總表，進入逐頁腳本、生圖、修圖或排版前必讀，並以小節／Act 為單位先規劃頁組，再逐頁施工。

---

## L. Delivery / Drive Archive

代表頁驗證前，必須先建立並通過 `schemas/representative-page-selection-profile.md` 定義的選擇檔。選擇檔只能引用已核准 `PAGE_DETAIL_CONFIRMATION.pages`，不得另寫一份獨立 prompt 或自行補內容；每個選取頁都要保存 `page_detail_page_id`、PAGE_DETAIL 檔案 hash 與 `page_spec_sha256`。代表頁驗證必須覆蓋課文閱讀頁、一般圖片合成頁、高風險語文頁，以及本課啟用時的 Lesson Visual Map。每類逐一核准，未展示頁型不得因教師對另一張說「可以」而連帶通過。代表頁與批次頁交付檢查時，優先使用 ChatGPT 原生圖像生成／影像編輯直接顯示於工作區並保留可續編原圖；原生入口不可用時標記 `NATIVE_IMAGE_REVIEW_UNAVAILABLE`。

除課文閱讀頁外，學生可見頁預設為整頁圖片式合成；精準文字可控排字後扁平化，不得退化成背景圖＋文字框、卡片牆、逐行打字或大量半透明框。代表頁組全數通過後才可進全量 Renderer；全量以 4–8 頁小批次推進並逐批檢查 Visual Drift、Canvas Drift 與 Text Layer Drift。

Lesson Package 交付依 `skills/lesson-package-delivery/SKILL.md`。
Drive 結構依 `skills/google-drive-lesson-archive/SKILL.md`，不得另維護第二套。

固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做先讀 Drive，再建立下一版本 `_01 / _02...`。

每次教師確認或批次產生可供檢查的頁面後，先依 `core/governance/cloud-checkpoint-policy.md` 上傳確認快照並回讀驗證；`CLOUD_CHECKPOINT_UNVERIFIED` 時不得宣告可接續或進入下一個高風險施工階段。只有檔案實際上傳後再次 list/search 驗證成功，才可 Archive PASS。

---

## M. Test Freeze

若教師說重跑／測試工作流：先依現行規格執行，不自動修改 Core。只有教師明確要求修規則／更新技能／寫 GitHub 時才修改。

---

## N. Legacy / Failure

禁止：
- STEP 3 / STEP 4 / STEP 2.75 舊流程復活
- raw JSON／YAML 取代 Teacher Review View
- 教材、教師補充與 AI 延伸混層
- AI 自動第三類單字深教
- 形近補充字被當多音字深教
- 無方格直接等於認讀字
- 語詞／句型／修辭脫離原文
- 已選 LVM 在簡報大綱消失
- Drive 回到舊五類結構
- 代表頁未覆蓋所有實際頁型就進全量 Renderer
- 代表頁未由已核准 PAGE_DETAIL 挑選，或代表頁資料與 PAGE_DETAIL hash 不一致
- 非課文頁以背景圖＋文字框冒充整頁圖片式構圖
- 圖片模型錯字兩次後刪除必要頁，而非改走可控排字合成
- 將教師口述型簡報做成學生講義、學習單、書寫單、投影考卷或滿版資訊表
- 跳過已核准 Lesson Baseline，直接憑印象生圖或排版

---

## 核心金句

> 先把教材讀對，再讓 AI 做有理由的推薦；老師只改例外，最後才變成簡報。

> 生字表 ≠ 生字教學清單；AI 主動只教形近字與多音字，單字詳解由老師指定。

## 國語簡報施工前確認（GLOBAL_SKILL_RULE）

語文規劃、簡報施工或每次續作／下一步／確認前，必須載入 `core/governance/presentation-preconstruction-policy.md`。先讀最新 Drive Runtime；到 STEP 2.5 才檢核成語雙軌與每個正式生字的延伸成語覆蓋；缺漏為 `VOCABULARY_IDIOM_COVERAGE_INCOMPLETE`。風格、角色、畫布與頁數帳本鎖定後，建立逐頁施工稿並停等確認；核准後才選代表頁，逐類核准後才進每批最多 8 頁的小批次，每批完成必須停等教師確認。每個 stage／HOLD 都回寫並驗證 Runtime State 與 Runtime Index；不得以舊流程簡寫跳過這些關卡。

## STEP 1 整合擷取

SOURCE 0／STEP 1、重新製作或來源補漏時，必讀 `core/governance/step1-source-anchor-policy.md` 第 G 節。依既定清單完成所有可查頁區與類別，包含多音字旁欄補充；階段內持續處理，剩餘缺口集中詢問，完整後才交付一份審核稿並停在 HOLD 1。LKB、成語延伸選教、風格、角色、頁數及代表頁不作為 STEP 1 前置條件。
