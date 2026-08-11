# V-MAX Golden Path Executor

版本：1.4-draft

## 目的
本技能是 V-MAX 國語教材工作流執行控制器。它不重新定義教學設計，只依 Main Workflow、Manifest 與 Google Drive Runtime State 執行合法下一步。

> 一次確認，只前進一個合法決策層；進入已鎖 production phase 後，依 Gate 結果批次執行，不逐頁重問。

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
→ Experience Decision
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

無成語：`STEP 2.6 = N/A_NO_IDIOM`。
無外掛：`EXTENSION_OFF`。
無 Scenario：`SOURCE_WORLD` 或 `SCENARIO_OFF`。

## C. Confirmation Transition Guard
教師只說「確認／好／可以／OK／沿用」時：
- HOLD 1：只確認 Source Truth，接著執行 LKB Assembly，停在 LKB REVIEW。
- LKB REVIEW：只確認 `approved_lkb`，接著執行 STEP 2，停在 HOLD 2。
- HOLD 2/2.5/2.6：只確認當前 HOLD，執行唯一下一步並停在下一決策點。
- Gate A/B/C：只確認該 Gate 的鎖定內容，不跨下一 Gate。
- Gate C confirmed 後，Full Renderer 可依已鎖 Storyboard 批次前進，不逐頁重問。

違反：`FLYING_TRAIN / SKIPPED_DECISION_LAYER / STAGE_LEAP`。

## D. STEP 1 / LKB Guard
STEP 1 必載入：
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`

HOLD 1 confirmed 後才載入：
- `skills/chinese-lesson-knowledge-builder/SKILL.md`
- `schemas/lesson-knowledge-book.md`

Builder 完成 `ready_for_lkb_review` 後必停；只有 `approved_lkb` 才可進 STEP 2。

`core/knowledge/lesson-knowledge-base-policy.md` 只負責 approved LKB 的 routing / spiral；不得建立第二套 LKB。

## E. STEP 2 / Gate A Guard
STEP 2 與 Teaching Direction 必載入：
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`

AI 必須提出學習難點、MUST/SHOULD/COULD、技能候選與理由。

`Teaching Skill Selection Lock` 必須發生在 Gate A 前。Gate A 確認的是核心技能與 Lesson Budget Draft，不是精確頁數。

## F. STEP 2.5 Guard
必載入：
- `core/director/knowledge-lab-ordering-policy.md`
- `core/director/character-deep-teaching-focus-policy.md`
- `core/director/polyphonic-source-policy.md`
- `core/worksheet/prestudy-language-selection-policy.md`
- `skills/character-group-visual-comparison/SKILL.md`

AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`；預習做過仍可正式課堂 `CORE_REINFORCE`。

## G. STEP 2.6 Guard
依 `core/director/idiom-expression-visualization-policy.md`，保留 student-friendly meaning、生活例句、understanding goal、visual expression、是否獨立成頁。

## H. Text Anchor / Language Guard
進 Lesson Map、Knowledge Lab、Slide Architecture 後，處理語詞／句型／修辭必載入：
- `core/pedagogy/text-embedded-language-teaching-policy.md`
- `skills/text-embedded-language-teaching/SKILL.md`
- `core/pedagogy/teaching-skill-selection-policy.md`

原文證據層不得消失；RETURN 只在必要時啟動。

## I. Experience Authority Guard
Gate A 後必載入：
- `core/experience/vmax-experience-layer.md`
- `core/visual/scenario-wrapper-registry.md`
- `core/visual/scenario-wrapper-language-arts-selector.md`
- `core/character/scenario-character-bridge.md`
- `core/character/character-system-2.md`
- `core/visual/style-recipe-families.md`
- `core/extension/extension-layer-policy.md`

權威順序：
- Scenario 由 Registry / Selector 決定。
- Character topology / cast / DNA 由 Character System + Bridge 決定。
- Style family 由 Style Recipe Families 決定。
- Experience Layer 只 orchestration，不得重建上述規則。

若 Source World 已足夠，可 `SOURCE_WORLD`；若角色無教學價值可 `NO_GUIDE / OFF`。

## J. Lesson Budget / Storyboard Guard
Lesson Budget 分兩段：
- Gate A 前：Budget Draft，只定 MUST/SHOULD/COULD、時間與核心認知任務。
- Slide Architecture 後：Budget Final / Page Ledger，才定頁數與逐頁 learning_gain。

一頁可有兩個同一認知場景的層次問題；每新增一頁必須有 learning_gain。

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
固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。

完整重做不覆蓋舊版。只有上傳後再次驗證可查到，才可 Archive PASS。

## O. Anti-duplication / Legacy Guard
禁止：
- 第二套 LKB authority
- Experience 自建 Character / Scenario / Style 規則
- 固定每段頁數、每題一頁
- 從視覺工具反推教學
- 圖片中文字未 QA
- 舊五類 Drive 結構

## 核心金句
> LKB 只有一本；Experience 只負責編排，不重造專門系統。

> 前段一次確認只走一層；Gate C 後依已鎖設計批次完成。
