# V-MAX Main Workflow 2.4-draft

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
- `core/knowledge/lesson-knowledge-base-policy.md`（routing / spiral only）

### Teaching Direction
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`

### STEP 2.5 / 2.6
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `core/worksheet/prestudy-language-selection-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`
- `core/director/idiom-expression-visualization-policy.md`

### Text / Lesson Visual
- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`
- `core/visual/lesson-visual-map.md`

### Experience Canonical Stack
- `core/experience/vmax-experience-layer.md`（orchestration only）
- `core/governance/scenario-wrapper-teacher-lock.md`
- `core/visual/scenario-wrapper-registry.md`
- `core/visual/scenario-wrapper-language-arts-selector.md`
- `core/character/scenario-character-bridge.md`
- `core/character/character-system-2.md`
- `core/visual/style-recipe-families.md`
- `core/extension/extension-layer-policy.md`

### Typography / Renderer
- `vmax-typography-bridge/SKILL.md`
- `core/renderer/image-first-hybrid-renderer.md`

### Delivery / Regression
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`
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
→ Lesson Budget Draft
→ GATE A｜Teaching Direction Lock
→ Scenario Decision / Candidates
→ SCENARIO LOCK｜Teacher Confirm
→ Character Topology / Cast Candidates
→ CHARACTER LOCK｜Teacher Confirm
→ Character DNA / Learner Role / Book DNA / Surprise Signature
→ Extension Check（若有）
→ Knowledge Lab 正式編排
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
→ Storyboard
→ Style Recipe / Lesson Skin / Typography Lock
→ GATE B｜Experience + Storyboard + Visual Identity Lock
→ 代表頁驗證
→ GATE C｜Representative Visual Validation
→ 全量 Renderer
→ Text QA / Typography QA
→ Quality Gate
→ Lesson Learning
→ Lesson Package Delivery Gate
→ Google Drive 歸檔與驗證
```

若無成語：`N/A_NO_IDIOM`。
若無 Extension：`EXTENSION_OFF`。
Scenario 可選 `SOURCE_WORLD / REGISTRY_WRAPPER / OFF`，三者都需在 Character Topology 前完成 Scenario Lock。

---

## C. Confirmation Layers

### Source / Knowledge
- HOLD 1：Source Truth
- LKB REVIEW：approved_lkb

### Mandatory Teaching HOLD
- HOLD 2：教學價值／學習難點
- HOLD 2.5：語文範圍
- HOLD 2.6：成語表達

### Experience Micro Locks
- `SCENARIO LOCK`：先鎖舞台，再進 Character Topology。
- `CHARACTER LOCK`：鎖 topology / cast，之後才建立正式 Character DNA。

### 3 Production Gates
- Gate A：Teaching Direction + Budget Draft
- Gate B：Experience + Storyboard + **Style Recipe / Lesson Skin / Typography direction**
- Gate C：Representative Visual

Gate B 鎖的是可用語言描述與 token 定義的視覺方向；Gate C 才用實際代表頁驗證它是否真的成立。

Gate C confirmed 後批次 Renderer，不逐頁重問同一決策。

---

## D. Single-stage Advance

```text
HOLD 1 confirmed → LKB ASSEMBLY → LKB REVIEW
LKB REVIEW confirmed → STEP 2 → HOLD 2
HOLD 2 confirmed → STEP 2.5 → HOLD 2.5
HOLD 2.5 confirmed → STEP 2.6 → HOLD 2.6
HOLD 2.6 confirmed → Teacher Intent Lock
Gate A confirmed → Scenario Decision → SCENARIO LOCK
SCENARIO LOCK confirmed → Character Topology / Cast → CHARACTER LOCK
CHARACTER LOCK confirmed → Experience Completion → downstream architecture
Style / Lesson Skin / Typography prepared → Gate B
Gate B confirmed → Representative Visual → Gate C
```

一次確認只解鎖一個需要教師裁決的 decision layer。

---

## E. STEP 1 / LKB
STEP 1 只回答教材與來源裡有什麼。HOLD 1 後由 canonical LKB Builder 組裝；approved_lkb 後，Routing Policy 才決定 PREVIEW / SHORT_READ / CORE / PLUS / EXTENSION / TEACHER_ONLY 與 spiral。

禁止第二套 LKB。

---

## F. STEP 2 / Skill / Budget Draft
STEP 2 提出學生卡點、MUST/SHOULD/COULD、技能候選與理由。
Teaching Skill Selection Lock 必須在 Gate A 前完成。
Lesson Budget Draft 只控制時間與核心認知任務，不宣告精確頁數。

---

## G. STEP 2.5 / 2.6
AI 主動單字深教只有 `SHAPE_NEAR / POLYPHONIC`；一般單字不自動獨立深教。預習做過的高價值字群可 `CORE_REINFORCE`。

成語保留 student-friendly meaning、life example、understanding goal、visual expression、是否需要獨立場景。

---

## H. Text Anchor
重要閱讀教學保留 Text Anchor。語詞、句型、修辭需帶原文證據。RETURN 只在需要驗證或防理解漂移時啟動。

---

## I. Experience Ordering

必守：
`Scenario Candidates → SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK → Character DNA`

Scenario：由 Registry / Selector；可 SOURCE_WORLD / OFF。
Character：由 Character System + Bridge。
Learner Role：有任務價值才開；若 Wrapper 已帶 student_role，優先沿用。
Book DNA / Surprise Signature 可在 Experience Completion 先成立。

**Lesson Skin Final 不在 Character Lock 後提前鎖。**它必須等 Visual Grammar / Slide Architecture 與 Style Recipe 選擇後，和 Typography 一起在 Gate B 前形成。

---

## J. Extension
支援 DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM，模式 LIGHT / THEME_MODE。新增內容先問「它取代什麼？」並重平衡 Budget。

---

## K. Slide Architecture / Budget Final / Visual Identity
Knowledge Lab 讀取已確認 LKB、Teacher Intent、語文範圍、Skill Lock 與 Experience locks。

Visual Grammar / Slide Architecture 完成後：
1. 建立 Budget Final / Page Ledger。
2. 完成 Storyboard。
3. 由 Style Recipe Families 選 Primary / Secondary Family。
4. 將 Style Recipe 具體化為 Lesson Skin。
5. 套 Typography Lock。
6. 進 Gate B 一次確認 Storyboard + Page Ledger + Visual Identity direction。

Page rules：
- 一頁 = 一個完整 cognitive scene
- 同頁可兩個有層次問題
- 每頁有 learning_gain
- 純漂亮、重複、額外例子、趣味知識預設降 PLUS

---

## L. Gate B / Gate C
Gate B 確認：已鎖 Scenario / Character refs、Learner Role、Book DNA、Style Recipe / Lesson Skin、Typography direction、Storyboard、Page Ledger。

若教師要改 Scenario / Character，使用「回前面」重開對應 lock，不在 Gate B 偷偷改。

Gate B confirmed 後生成 1–2 張代表頁；Gate C 用實際畫面驗證 art direction。Gate C confirmed 後才批次 Renderer。

---

## M. Typography / Renderer
圖片引擎可直接生成整合式繁中圖文構圖；正式教材必經 Text / Typography QA。

P0：課文、生字、形近字、多音字、注音、目標字、關鍵句／臺詞。局部錯誤優先局部修，不把後製負擔轉教師。

---

## N. Delivery / Runtime
Drive 固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

只有實際上傳並再次驗證成功才 Archive PASS。

---

## O. Legacy / Failure
禁止：
- 第二套 LKB
- 未 Scenario Lock 就進 Character Topology
- 未 Character Lock 就正式建立角色 DNA／大量視覺
- Lesson Skin 在 Style Recipe 尚未選定前被當成 final lock
- Experience 重建 Character / Scenario / Style canonical
- 從 visual tool 反推 Teaching Skill
- 一題一頁／固定每段模板
- 圖片中文字未 QA
- 已選 LVM 後段消失
- Drive 舊五類結構

---

## 核心金句

> 先鎖舞台，再選卡司；先做認知架構，再把 Style Recipe 長成本課 Lesson Skin。

> Gate B 鎖設計語言，Gate C 用真實代表頁驗證。
