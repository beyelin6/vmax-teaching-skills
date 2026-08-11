# V-MAX Golden Path Executor

版本：1.3-draft

## 目的
本技能是 V-MAX 國語教材工作流執行控制器。它不重新定義教學設計，只依 Main Workflow、Manifest 與 Google Drive Runtime State 執行合法下一步。

> 一次確認，只前進一個合法階段；進入已鎖 production phase 後，依 Gate 結果批次執行，不逐頁重問。

## A. 啟動必讀
1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. Google Drive 對應課程 Runtime State
4. `core/governance/vmax-main-workflow.md`
5. `core/governance/hold-teacher-interface-policy.md`
6. 當前 stage 的 canonical policies / skills

不得以舊對話、模型記憶或 legacy skill 覆蓋 Manifest 與 Runtime。

## B. 合法前進序列

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

無成語：`STEP 2.6 = N/A_NO_IDIOM`。
無外掛：`EXTENSION_OFF`。

## C. Confirmation Transition Guard
教師只說「確認／好／可以／OK／沿用」時：
- 若位於 HOLD 1/2/2.5/2.6，只確認當前 HOLD，執行唯一下一步後立刻停在下一 HOLD。
- 若位於 Gate A/B/C，只確認該 Gate 的鎖定內容；不得跨下一個 Gate。
- Gate C 確認後，Full Renderer 可依已鎖 Storyboard 批次前進，不逐頁再問「可以嗎」。

違反：`FLYING_TRAIN / SKIPPED_DECISION_LAYER / STAGE_LEAP`。

## D. STEP 1 Guard
必載入：
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`
- `core/knowledge/lesson-knowledge-base-policy.md`

先把來源讀對，再建立整課 LKB；不得在 STEP 1 決定 Scenario、Character、Style、頁數。

## E. STEP 2 Guard
必載入：
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`

AI 必須提出學習難點、MUST/SHOULD/COULD、技能候選與理由；不可只列活動名稱。

## F. STEP 2.5 Guard
必載入：
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `core/worksheet/prestudy-language-selection-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`

AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`；一般單字不自動獨立成頁。預習單 P3/PX 不代表正式課堂永遠不再出現。

## G. STEP 2.6 Guard
依 `core/director/idiom-expression-visualization-policy.md`，保留 student-friendly meaning、生活例句、understanding goal、visual expression、是否獨立成頁。

## H. Text Anchor / Language Guard
進 Lesson Map、Knowledge Lab、Slide Architecture 後，處理語詞／句型／修辭必載入：
- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`
- `core/pedagogy/teaching-skill-selection-policy.md`

原文證據層不得在後段消失；RETURN 只在有必要時啟動。

## I. Experience / Extension Guard
Gate A 後必載入：
- `core/experience/vmax-experience-layer.md`
- `core/extension/extension-layer-policy.md`

Guide Character／Learner Role／Scenario／Style 都須有教學理由。Extension 新增內容必重算 Lesson Budget，先問「取代什麼」。

## J. Lesson Budget / Storyboard Guard
必載入 `core/governance/lesson-budget-policy.md`。

- 一頁 = 一個完整認知場景
- 同頁可兩個有層次問題
- 每新增一頁必須有新增 learning_gain
- Page Estimate 只能在 Slide Architecture 後正式成立

## K. Typography / Renderer Guard
必載入：
- `vmax-typography-bridge/SKILL.md`
- `core/renderer/image-first-hybrid-renderer.md`

允許圖文一體生成；正式輸出前跑 Text QA。P0 高風險：課文、生字、形近字、多音字、注音、目標字、關鍵句／臺詞。局部錯字先局部修，不轉嫁教師。

## L. Lesson Visual Map Guard
若教師已選 LVM，簡報大綱、Slide Architecture、Page Ledger、Renderer 都必須保留；消失標記 `LVM_OUTLINE_DROPPED / LVM_DOWNSTREAM_DROPPED`。

## M. Teacher Command Language
- `繼續／好／可以`：依目前合法 stage 前進；production lock 後直接工作。
- `下一頁`：下一認知場景，不重畫目前頁。
- `換一個版本`：同內容重新設計。
- `重畫`：重生目前視覺。
- `鎖定`：寫入 downstream invariant。
- `回前面`：回指定決策點並重開受影響 downstream。

## N. Delivery / Drive Guard
交付必載入 Lesson Package 與 Drive Archive skill。固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做不覆蓋舊版。只有上傳後再次驗證可查到，才可 Archive PASS。

## O. Anti-template / Legacy Guard
禁止：固定每段頁數、每題一頁、所有生字同規格、從視覺工具反推教學、每課套同一角色／Scenario／Style、圖片中文字未 QA、舊五類 Drive 結構。

## 核心金句
> AI 做重判斷，老師只改例外；前段一次確認只走一站，後段設計鎖定後不要每頁重新問。
