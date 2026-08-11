# V-MAX Main Workflow 2.2-draft

## 定位

本檔定義 V-MAX 教材製作正式主流程、教師確認點與 canonical policy wiring。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 不得反向改寫此核心順序。

所有實跑必須遵循：
- `skills/vmax-golden-path-executor/SKILL.md`
- `V-MAX_MANIFEST.md`
- Google Drive 該課 Runtime State

---

## A. Canonical Policy Wiring

### SOURCE / Official Knowledge / LKB
- `core/governance/source-library-policy.md`
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`
- `skills/chinese-lesson-knowledge-builder/SKILL.md`
- `schemas/lesson-knowledge-book.md`
- `core/knowledge/lesson-knowledge-base-policy.md`（只負責 routing / spiral，不是 LKB 結構權威）

### Teaching Direction
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`

### STEP 2.5
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `core/worksheet/prestudy-language-selection-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`

### STEP 2.6
- `core/director/idiom-expression-visualization-policy.md`

### Text / Lesson Visual
- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`
- `core/visual/lesson-visual-map.md`

### Experience Canonical Stack
- `core/experience/vmax-experience-layer.md`（orchestration only）
- `core/visual/scenario-wrapper-registry.md`
- `core/visual/scenario-wrapper-language-arts-selector.md`
- `core/character/scenario-character-bridge.md`
- `core/character/character-system-2.md`
- `core/visual/style-recipe-families.md`
- `core/extension/extension-layer-policy.md`

### Typography / Renderer
- `vmax-typography-bridge/SKILL.md`
- `core/renderer/image-first-hybrid-renderer.md`

### Delivery
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`

### Regression
- `tests/workflow-hold-regression-cases.md`
- `tests/character-teaching-regression-cases.md`
- `tests/worksheet-regression-cases.md`
- `tests/vmax-v1-integration-regression-cases.md`

---

## B. Golden Path

```text
SOURCE 0｜Google Drive Source Library 尋源
→ STEP 1｜教材定錨 / Official Knowledge
→ HOLD 1｜Source Truth Confirm
→ LKB ASSEMBLY｜Chinese Lesson Knowledge Builder
→ LKB REVIEW｜approved_lkb
→ STEP 2｜AI 教學價值判讀／核心學習難點／技能候選
→ HOLD 2
→ STEP 2.5｜語文輻射分析與教師選擇
→ HOLD 2.5
→ STEP 2.6｜成語表達與視覺化確認
→ HOLD 2.6
→ Teacher Intent Lock
→ Lesson Map
→ Supplement / Framework Decision
→ Session Map
→ Lesson Visual Map Strategy
→ Teaching Skill Selection Lock
→ Lesson Budget Draft（MUST / SHOULD / COULD + time / cognitive tasks）
→ GATE A｜Teaching Direction Lock
→ Experience Decision
   Source World / Scenario Wrapper
   Character Topology / Cast / Guide presence
   Learner Role
   Book DNA / Lesson Skin / Surprise Signature
→ Extension Check（若有）
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
→ Storyboard
→ GATE B｜Experience + Storyboard Lock
→ Style Recipe / Typography Lock
→ 代表頁驗證
→ GATE C｜Representative Visual Validation
→ 全量 Renderer
→ Text QA / Typography QA
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery Gate
→ Google Drive 歸檔與驗證
```

若無需成語：STEP 2.6 明確記錄 `N/A_NO_IDIOM`。
若無 Extension：明確記錄 `EXTENSION_OFF`。
若無 Scenario Wrapper：Experience 記錄 `SOURCE_WORLD` 或 `SCENARIO_OFF`，不得硬加包裝。

---

## C. Source Gates / Mandatory HOLD / Production Gates

### Source Gate
`HOLD 1` 核准 Official Knowledge 後，才允許 Chinese Lesson Knowledge Builder 組裝 LKB。Builder 完成 `ready_for_lkb_review` 後必須取得 `approved_lkb`，才可進 STEP 2。

LKB Review 不允許新增來源外知識，只確認整合、去重、關聯、Teacher Knowledge 分流與 source trace。

### Mandatory HOLD
HOLD 2 / 2.5 / 2.6 保護：教學價值、語文範圍、成語表達。

```text
HOLD 1 確認 → LKB ASSEMBLY → LKB REVIEW
LKB REVIEW 確認 → STEP 2 → HOLD 2
HOLD 2 確認 → STEP 2.5 → HOLD 2.5
HOLD 2.5 確認 → STEP 2.6 → HOLD 2.6
HOLD 2.6 確認 → Teacher Intent Lock
```

一次確認只走一個合法決策層。

### 3 Production Gates
- `GATE A｜Teaching Direction Lock`：確認本課真正學什麼、核心技能、刻意不做什麼、Lesson Budget Draft。
- `GATE B｜Experience + Storyboard Lock`：確認 Scenario/Source World、角色拓撲、Learner Role、Visual Identity、Storyboard、Page Ledger。
- `GATE C｜Representative Visual Validation`：確認 1–2 張代表頁的 Style、角色、文字融合、密度與投影可讀性；確認後批次製作，不逐頁重問。

---

## D. STEP 1 / LKB

STEP 1 只回答「教材與來源裡有什麼」，不決定角色、畫風、頁數。

HOLD 1 確認後，由 `chinese-lesson-knowledge-builder` 依 approved Official Knowledge 建立本課唯一 LKB。

`core/knowledge/lesson-knowledge-base-policy.md` 只在 `approved_lkb` 後負責 Content Routing 與 Spiral Learning；不得建立第二套 LKB。

---

## E. STEP 2｜AI 教學價值判讀

AI 主動提出：
- 哪些文本值得深讀／朗讀／推論／比較／聯想／遷移
- 學生真正可能卡在哪裡
- MUST / SHOULD / COULD
- 教學技能候選及理由
- 哪些可短帶／PLUS／降權
- 哪些地方要保留學生發現空間

完成後 HOLD 2。

---

## F. STEP 2.5｜語文輻射 Selection Gate

正式生字完整保留；AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。一般單字為 `BASIC_LITERACY_ONLY`，單字詳解只有教師指定。

多音字合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：只從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`

形近字先做部件、字義、混淆點、辨認提示再推薦。

預習單 `3–5 組` 只限制預習主要練習區，不限制正式教學。預習做過的高價值字群可在正式教材 `CORE_REINFORCE` 深化。

---

## G. STEP 2.6｜成語表達與視覺化

對保留成語決定 student-friendly meaning、生活例句、understanding goal、visual expression、independent page recommendation。成語插圖優先表達例句句意，不預設畫典故。

---

## H. Teaching Skill Selection / Gate A

`Teaching Skill Selection Lock` 必須在 Gate A 前完成，因 Gate A 要確認核心技能。

技能選擇遵守 Minimum Necessary Skill Set：每個技能都要能說出「解決哪個學習難點、拿掉少理解什麼」。

Lesson Budget 此時先做 Draft：以時間、MUST/SHOULD/COULD、核心認知任務為主，尚不宣告精確頁數。

---

## I. Text Anchor / Text-Embedded Language

重要閱讀教學保留 Text Anchor。語詞、句型、修辭需帶原文證據。RETURN 為可選技能，只在需要文本驗證或防止理解漂移時啟動。

---

## J. Experience Layer / Canonical Authority

Experience Layer 只 orchestrate：
- Scenario：由 Scenario Wrapper Registry / Selector 決定，或 SOURCE_WORLD / OFF。
- Character：由 Character System + Scenario Character Bridge 決定 topology、cast、DNA、出場功能。
- Learner Role：有任務價值才啟用；若 Wrapper 已內含 student_role，優先沿用。
- Style：由 Style Recipe Families 決定；Lesson Skin 只是本課具體化，不是第二套 Style Library。
- Surprise Signature：原則一課一個主要驚喜；無教學價值就 OFF。

同課預習單、短文單、正式簡報共享 Visual Identity references，但依 Material Mode 調整密度。

---

## K. Extension Layer

老師可加 DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM，模式 `LIGHT / THEME_MODE`。

新增 Extension 必須回答「它取代什麼？」並重算 Lesson Budget；不得無限加頁。

---

## L. Knowledge Lab → Slide Architecture → Lesson Budget Final

Knowledge Lab 讀取已確認 LKB、2.5／2.6、Teacher Intent、Skill Lock，不得重寫來源真值。

Visual Grammar / Slide Architecture 先認知關係再決定畫面。

只有完成 Slide Architecture 後才可形成 Lesson Budget Final / Page Ledger：
- 一頁 = 一個完整認知場景
- 同頁可兩個有層次問題
- 每新增一頁必須有 learning_gain
- 漂亮、重複、額外例子、趣味知識預設降 PLUS

---

## M. Typography / Image-first Renderer

正式上課簡報採圖片式整體構圖優先＋文字正確性保護。

圖片引擎可直接生成繁中圖文構圖；正式教材經 Typography/Text QA。

P0 高風險逐字檢查：課文、生字、形近字、多音字、注音、學生辨識目標字、關鍵句／臺詞。

局部錯誤先局部修，不因一字錯誤整頁重畫；最終不把後製負擔轉給教師。

---

## N. Delivery / Drive Archive

Lesson Package 依 `skills/lesson-package-delivery/SKILL.md`；Drive 結構依 `skills/google-drive-lesson-archive/SKILL.md`。

固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做先讀 Drive，再建立下一版本。只有實際上傳後再次驗證成功，才可 Archive PASS。

---

## O. Test Freeze

若教師說重跑／測試工作流：先依現行 canonical 規格執行，不自行改 Core。只有教師明確要求修改規則／更新 GitHub 時才寫回。

---

## P. Legacy / Failure

禁止：
- 兩套 LKB 權威並存
- STEP 3 / STEP 4 舊流程復活
- AI 自動第三類單字深教
- 形近補充字被當多音字深教
- 無方格直接等於認讀字
- 語詞／句型／修辭脫離原文
- 已選 LVM 在後段消失
- Experience 自行重定義 Character / Scenario / Style canonical
- 從視覺工具反推教學目的
- 每題一頁／每段固定模板
- 圖片中文字未經 QA 就交付
- Drive 回到舊五類結構

---

## 核心金句

> LKB 只有一本；教材可以很多種。

> 教學技能先於視覺工具；一頁是一個完整認知場景。

> Experience Layer 是總導演，不是再造角色庫、情境庫、風格庫。
