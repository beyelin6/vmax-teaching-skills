# V-MAX Golden Path Executor

版本：1.5-draft

## 目的
本技能是 V-MAX 國語教材工作流執行控制器。它不重新定義教學設計，只依 Main Workflow、Manifest 與 Google Drive Runtime State 執行合法下一步。

> 一次確認，只前進一個合法決策層；Gate C 後依已鎖 Storyboard 批次執行，不逐頁重問。

## A. 啟動必讀
1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. Google Drive 對應課程 Runtime State
4. `core/governance/vmax-main-workflow.md`
5. `core/governance/hold-teacher-interface-policy.md`
6. 當前 stage canonical policies / skills

## B. 合法前進序列

```text
SOURCE 0
→ STEP 1 Official Knowledge
→ HOLD 1 Source Truth Confirm
→ LKB ASSEMBLY
→ LKB REVIEW / approved_lkb
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
→ Teaching Skill Selection Lock
→ Lesson Budget Draft
→ GATE A Teaching Direction Lock
→ Scenario Decision / Candidates
→ SCENARIO LOCK
→ Character Topology / Cast Candidates
→ CHARACTER LOCK
→ Character DNA / Learner Role / Book DNA / Lesson Skin / Surprise Signature
→ Extension Check
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Lesson Budget Final / Page Ledger
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

無成語：`N/A_NO_IDIOM`。無外掛：`EXTENSION_OFF`。Scenario mode 可 `SOURCE_WORLD / REGISTRY_WRAPPER / OFF`。

## C. Transition Guard
- HOLD 1 confirmed → 建 LKB → 停 LKB REVIEW。
- LKB REVIEW confirmed → STEP 2 → 停 HOLD 2。
- HOLD 2 confirmed → STEP 2.5 → 停 HOLD 2.5。
- HOLD 2.5 confirmed → STEP 2.6 → 停 HOLD 2.6。
- HOLD 2.6 confirmed → Teacher Intent Lock。
- Gate A confirmed → 產生 Scenario Decision/Candidates → 停 SCENARIO LOCK。
- SCENARIO LOCK confirmed → 產生 Character Topology/Cast Candidates → 停 CHARACTER LOCK。
- CHARACTER LOCK confirmed → 建立 Character DNA / Learner Role 等 Experience 後續。
- Gate C confirmed → Full Renderer 可批次執行。

違反：`FLYING_TRAIN / SKIPPED_DECISION_LAYER / STAGE_LEAP / SCENARIO_LOCK_SKIPPED / CHARACTER_LOCK_SKIPPED`。

## D. STEP 1 / LKB Guard
STEP 1 必載入 Source Anchor / Recognition policy。HOLD 1 後才執行 `chinese-lesson-knowledge-builder`；LKB 未 `approved_lkb` 不得進 STEP 2。

Routing policy 只處理 approved LKB 的 PREVIEW / SHORT_READ / CORE / PLUS / EXTENSION / TEACHER_ONLY 與 spiral，不得建第二套 LKB。

## E. Teaching Direction Guard
必載入：
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`

Teaching Skill Selection Lock 必須在 Gate A 前；Lesson Budget Draft 只鎖時間、MUST/SHOULD/COULD、核心認知任務，不鎖精確頁數。

## F. STEP 2.5 / 2.6 Guard
AI 主動生字深教只有 `SHAPE_NEAR / POLYPHONIC`；預習做過仍可正式課堂 `CORE_REINFORCE`。成語需保留 student-friendly meaning、生活例句、understanding goal、visual expression。

## G. Text Anchor Guard
語詞、句型、修辭與重要閱讀教學必須保留原文證據。RETURN 只在必要時啟動。

## H. Experience Authority + Lock Guard
Gate A 後必載入：
- `core/experience/vmax-experience-layer.md`
- `core/governance/scenario-wrapper-teacher-lock.md`
- `core/visual/scenario-wrapper-registry.md`
- `core/visual/scenario-wrapper-language-arts-selector.md`
- `core/character/scenario-character-bridge.md`
- `core/character/character-system-2.md`
- `core/visual/style-recipe-families.md`

硬順序：

`Scenario Decision → SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK → Character DNA`

禁止在 Scenario 未鎖前偷偷建卡司；禁止在 Character 未鎖前生成正式 DNA／大量視覺。

Experience 只 orchestration：Scenario/Character/Style 規則由各自 canonical 管理。

## I. Extension Guard
新增 DIGITAL / CROSS / THEME / PROJECT / REAL_WORLD / CUSTOM 必須重算 Budget，先問「取代什麼」。

## J. Budget / Storyboard Guard
- Budget Draft：Gate A 前。
- Budget Final / Page Ledger：Slide Architecture 後。
- 一頁 = 一個 cognitive scene。
- 同頁可兩個有層次問題。
- 每頁必填 learning_gain。

## K. Typography / Renderer Guard
允許圖文一體繁中生成；正式輸出前跑 Text QA。P0：課文、生字、形近字、多音字、注音、目標字、關鍵句／臺詞。局部錯誤先局部修。

## L. LVM Guard
已選 Lesson Visual Map 必須保留到大綱、Slide Architecture、Page Ledger、Renderer。

## M. Teacher Command Language
- `繼續／好／可以`：依目前合法 decision layer 前進；Gate C 後直接工作。
- `下一頁`：下一 cognitive scene，不重畫目前頁。
- `換一個版本`：同內容重設計。
- `重畫`：重生目前視覺。
- `鎖定`：寫 downstream invariant。
- `回前面`：回指定決策點，重開受影響 downstream。

## N. Delivery / Drive Guard
固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

只有上傳後再次驗證可查到，才可 Archive PASS。

## O. Anti-duplication / Legacy Guard
禁止第二套 LKB、Experience 自建 Character/Scenario/Style、未鎖舞台先選卡司、一題一頁、從視覺工具反推教學、圖片中文字未 QA、舊五類 Drive 結構。

## 核心金句
> 前段不飛站；Experience 先鎖舞台再鎖卡司；Gate C 後不要逐頁重新問。
