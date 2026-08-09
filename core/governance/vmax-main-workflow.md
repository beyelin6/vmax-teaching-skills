# V-MAX Main Workflow 2.1

## 定位

本檔定義 V-MAX 教材製作的正式主流程、教師確認點與必要 policy 載入關係。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 等不得反向改寫此核心順序。

所有實跑必須遵循：
- `skills/vmax-golden-path-executor/SKILL.md`
- `V-MAX_MANIFEST.md`
- Google Drive 該課 Runtime State

---

## A. Canonical Policy Wiring

### SOURCE / STEP 1
- `core/governance/source-library-policy.md`
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`

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
- `core/visual/lesson-visual-map.md`

### Delivery
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
→ 頁數估算／頁數帳本
→ Style Recipe
→ 代表頁驗證
→ 全量圖文資訊圖表 Renderer
→ PDF 組裝與逐頁 Preflight
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery Gate
→ Google Drive 歸檔與驗證
```

若無需處理成語：STEP 2.6 明確記錄 `N/A_NO_IDIOM`，不得默默跳過。

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

完成後 HOLD 1。

---

## E. STEP 2｜AI 教學價值判讀

AI 主動提出：
- 哪些文本值得深讀／朗讀／推論／比較／聯想／遷移
- 哪些可短帶／Bonus／降權
- 理由
- 哪些地方要保留學生發現空間

完成後 HOLD 2。

---

## F. STEP 2.5｜語文輻射 Selection Gate

### 生字
- 正式生字完整保留。
- AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。
- 一般單字 `BASIC_LITERACY_ONLY`。
- `SHAPE_NEAR` 必須以兩字以上字群比較教學。
- 易錯字只有教師主動指定 `TEACHER_ADDED_WRITING_FOCUS`；AI 不列候選。
- 易錯、複雜、字源有趣、評量重要都不是 AI 自動第三入口。

### 多音字
合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：AI 只能從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`

形近補充字／比較字／認讀字／課文一般字不得被 AI 因本身多音而自動拉入。

### 形近字
先做真正辨析：共同／差異部件、字義、混淆點、辨認提示，再推薦。

### 成語
先判教學價值與保留範圍；後續 STEP 2.6 再決定例句與視覺表達。

### 預習單
`3–5 組` 只限制預習單主要練習區，不限制正式教學。

完成後 HOLD 2.5。

---

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

只有完成 Slide Architecture 後才可估頁數；頁數是結果，不是起點。

---

## L. Delivery / Drive Archive

Lesson Package 交付依 `skills/lesson-package-delivery/SKILL.md`。
Drive 結構依 `skills/google-drive-lesson-archive/SKILL.md`，不得另維護第二套。

正式課堂視覺成品預設依 `core/export/infographic-pdf-output-contract.md` 產生 16:9 圖文資訊圖表 PDF；PPTX 僅在教師明確要求時選配。

固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做先讀 Drive，再建立下一版本 `_01 / _02...`。

只有檔案實際上傳後再次 list/search 驗證成功，才可 Archive PASS。

---

## M. Test Freeze

若教師說重跑／測試工作流：先依現行規格執行，不自動修改 Core。只有教師明確要求修規則／更新技能／寫 GitHub 時才修改。

---

## N. Legacy / Failure

禁止：
- STEP 3 / STEP 4 舊流程復活
- AI 自動第三類單字深教
- 形近補充字被當多音字深教
- 無方格直接等於認讀字
- 語詞／句型／修辭脫離原文
- 已選 LVM 在簡報大綱消失
- Drive 回到舊五類結構

---

## 核心金句

> 先把教材讀對，再讓 AI 做有理由的推薦；老師只改例外，最後才變成簡報。

> 生字表 ≠ 生字教學清單；AI 主動只教形近字與多音字，單字詳解由老師指定。
