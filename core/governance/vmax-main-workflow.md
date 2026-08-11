# V-MAX Main Workflow 2.1-draft

## 定位

本檔定義 V-MAX 教材製作正式主流程、教師確認點與 canonical policy wiring。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 不得反向改寫此核心順序。

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
- `core/knowledge/lesson-knowledge-base-policy.md`

### STEP 2 / Teaching Direction
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

### Lesson / Experience / Extension
- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`
- `core/visual/lesson-visual-map.md`
- `core/experience/vmax-experience-layer.md`
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

---

## B. Golden Path

```text
SOURCE 0｜Google Drive Source Library 尋源
→ STEP 1｜教材定錨＋Lesson Knowledge Base 基底
→ HOLD 1
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
→ GATE A｜Teaching Direction Lock
→ Experience Decision
   Scenario Wrapper
   Character Topology / Guide Character
   Learner Role
   Book DNA / Lesson Skin / Surprise Signature
→ Extension Check（若有）
→ Knowledge Lab 正式編排
→ Teaching Skill Selection Lock
→ Visual Grammar / Slide Architecture
→ Lesson Budget / Page Ledger
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
若無 Extension：明確記錄 `EXTENSION_OFF`，不得硬加跨域或平板活動。

---

## C. Mandatory HOLD vs Production Gate

前段 HOLD 與後段 3 Gate 功能不同，不互相取代。

### Mandatory HOLD
HOLD 1 / 2 / 2.5 / 2.6 保護：來源真值、教學價值、語文範圍、成語表達。

```text
HOLD 1 確認 → STEP 2 → HOLD 2
HOLD 2 確認 → STEP 2.5 → HOLD 2.5
HOLD 2.5 確認 → STEP 2.6 → HOLD 2.6
HOLD 2.6 確認 → Teacher Intent Lock
```

一次確認只走一站。

### 3 Production Gates
- `GATE A｜Teaching Direction Lock`：確認整課要學什麼、技能、刻意不做什麼、Lesson Budget。
- `GATE B｜Experience + Storyboard Lock`：確認情境、引導角色、Learner Role、視覺世界、Storyboard、Page Ledger。
- `GATE C｜Representative Visual Validation`：確認 1–2 張代表頁的畫風、角色、文字融合、密度與投影可讀性；確認後可批次製作，不逐頁重問。

在 Mandatory HOLD 中「好／可以／繼續」仍只前進一站；在 GATE C 確認後的 production phase，「繼續」代表依已鎖設計直接往下製作。

---

## D. STEP 1｜教材定錨＋Knowledge Base

只回答教材裡有什麼與來源可確認的知識，不決定角色、畫風、頁數。

至少包含：
- 課文與結構
- 正式生字、認讀字 status
- 教材語詞／成語／語文活動
- 教冊重點、習作／評量連結
- 學生可能卡點與必要背景知識
- provenance / gaps / conflicts

所有後續輸出共用同一 LKB，不各自重猜重點。

---

## E. STEP 2｜AI 教學價值判讀

AI 主動提出：
- 哪些文本值得深讀／朗讀／推論／比較／聯想／遷移
- 學生真正可能卡在哪裡
- MUST / SHOULD / COULD
- 教學技能候選及理由
- 哪些可短帶／Bonus／降權
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

完成後 HOLD 2.5。

---

## G. STEP 2.6｜成語表達與視覺化

對保留成語決定 student-friendly meaning、生活例句、understanding goal、visual expression、independent page recommendation。成語插圖優先表達例句句意，不預設畫典故。

完成後 HOLD 2.6。

---

## H. Teacher Intent → Lesson / Session

Teacher Intent 採 `PROPOSED → CONFIRMED → LOCKED`。
Lesson Map 建整課理解旅程；Session Map 依內容密度自然切堂。不得固定段落頁數或固定每段五件套。

---

## I. Text Anchor / Text-Embedded Language

重要閱讀教學需保留 Text Anchor。語詞、句型、修辭：
- 語詞隨段落，附原文片段＋學生易懂意義。
- 句型帶課文原句，再抽結構與仿用。
- 修辭從原文發現效果，最後才命名。

RETURN 是可選技能，不是每頁固定流程。

---

## J. Experience Layer

在 Storyboard 前完成：
- Guide Character：必須有教學功能，不是裝飾吉祥物。
- Learner Role：有必要才啟用。
- Context Wrapper：`SOURCE_WORLD / LIGHT_WRAPPER / OFF`。
- Visual Identity：`BOOK DNA / LESSON SKIN / MATERIAL MODE`。
- Surprise Signature：每課原則 1 個主要驚喜，不為驚喜而驚喜。

同課預習單、短文單、正式簡報共享角色與 Visual Identity Lock，但依 Material Mode 調整密度。

---

## K. Extension Layer

老師可加 DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM。

模式：`LIGHT / THEME_MODE`。

新增 Extension 必須回答「它取代什麼？」並重算 Lesson Budget；不得無限加頁，也不得為跨域而跨域。

---

## L. Knowledge Lab → Slide Architecture → Lesson Budget

Knowledge Lab 讀取已確認內容，不得改寫 2.5／2.6／Teacher Intent。

教學技能先於視覺工具；Visual Grammar / Slide Architecture 先認知關係再決定畫面。

只有完成 Slide Architecture 後才可正式估頁數。

Lesson Budget / Page Ledger 必守：
- 一頁 = 一個完整認知場景
- 同頁可兩個有層次問題
- 每新增一頁必須說明新增的學生理解
- 只有漂亮、重複、額外例子、趣味知識時預設降為 PLUS

---

## M. Typography / Image-first Renderer

正式上課簡報採圖片式整體構圖優先＋文字正確性保護。

圖片引擎可直接生成繁中圖文構圖；正式教材經 Typography/Text QA。

P0 高風險逐字檢查：課文、生字、形近字、多音字、注音、學生辨識目標字、關鍵句／臺詞。

局部錯誤先局部修，不因一字錯誤整頁重畫；最終不把後製負擔轉給教師。

---

## N. Delivery / Drive Archive

Lesson Package 依 `skills/lesson-package-delivery/SKILL.md`；Drive 結構依 `skills/google-drive-lesson-archive/SKILL.md`，不得另維護第二套。

固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做先讀 Drive，再建立下一版本 `_01 / _02...`。只有實際上傳後再次驗證成功，才可 Archive PASS。

---

## O. Test Freeze

若教師說重跑／測試工作流：先依現行 canonical 規格執行，不自行改 Core。只有教師明確要求修改規則／更新 GitHub 時才寫回。

---

## P. Legacy / Failure

禁止：
- STEP 3 / STEP 4 舊流程復活
- AI 自動第三類單字深教
- 形近補充字被當多音字深教
- 無方格直接等於認讀字
- 語詞／句型／修辭脫離原文
- 已選 LVM 在後段消失
- 從視覺工具反推教學目的
- 每題一頁／每段固定模板
- 每課硬塞同一 Scenario／角色／Style
- 圖片中文字未經 QA 就交付
- Drive 回到舊五類結構

---

## 核心金句

> 先把教材讀對，再讓 AI 做有理由的推薦；老師只改例外，最後才變成簡報。

> 教學技能先於視覺工具；一頁是一個完整認知場景。

> 一致讓孩子有熟悉感；每課的驚喜讓孩子有期待感。
