# V-MAX System Architecture v1.2-draft

## 定位
V-MAX 是「教師課程設計與教材生成系統」，不是單純簡報生成器，也不是視覺特效庫。

本檔只描述跨模組架構、資料流與 authority boundary；專門規則一律由 Manifest 指定的 canonical files 管理。

> 架構檔負責看全局；專門 policy 負責做裁決。

---

## 1. System Flow

```text
SOURCE TRUTH
→ OFFICIAL KNOWLEDGE
→ LESSON KNOWLEDGE BOOK
→ CONTENT ROUTING / SPIRAL
→ TEACHING DIRECTION
→ EXPERIENCE ORCHESTRATION
   Scenario Decision → Scenario Lock
   Character Topology/Cast → Character Lock
→ EXTENSION CHECK
→ KNOWLEDGE LAB
→ VISUAL / SLIDE ARCHITECTURE
→ LESSON BUDGET FINAL / PAGE LEDGER
→ STORYBOARD
→ REPRESENTATIVE VISUAL
→ IMAGE-FIRST RENDERER
→ TEXT / TYPOGRAPHY QA
→ DELIVERY / ARCHIVE
```

Teacher Control 以 Source/HOLD/Review/Experience Lock/Production Gate 管理確認點。

---

## 2. Authority Map

### Source Truth
Canonical：source-library / step1-source-anchor / recognition-only-character policies。

### Lesson Knowledge Book
Canonical：
- `skills/chinese-lesson-knowledge-builder/SKILL.md`
- `schemas/lesson-knowledge-book.md`

負責 Official / Teacher Knowledge、節點、source trace、版本、驗證。

### Content Routing / Spiral
Canonical：`core/knowledge/lesson-knowledge-base-policy.md`。
只負責 approved LKB 的 PREVIEW / SHORT_READ / CORE / PLUS / EXTENSION / TEACHER_ONLY routing 與 spiral。

> LKB 只有一個 authority；Routing 不是第二本 LKB。

### Teaching Direction
Canonical：
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`
- 各語文／閱讀專門 policy

順序：`文本診斷 → 學習難點 → MUST/SHOULD/COULD → 最低必要 Teaching Skills → Lesson Budget Draft → Gate A`。

### Experience
Orchestrator：`core/experience/vmax-experience-layer.md`。

專門 canonical：
- Scenario lock → `core/governance/scenario-wrapper-teacher-lock.md`
- Scenario → Registry + Selector
- Character → Character System + Scenario Character Bridge
- Style → Style Recipe Families
- Typography → Typography Bridge

硬相依：

`Scenario Decision → SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK → Character DNA`

> Experience 是總導演，不再造角色庫、情境庫、風格庫；三個大 Gate 也不能刪掉既有依賴鎖。

### Extension
Canonical：`core/extension/extension-layer-policy.md`。
新增外掛先問「它取代什麼？」並重平衡 Lesson Budget。

### Visual / Scene Decision
Canonical：Lesson Visual Map、Visual Grammar、Visual Sequence、Director policies。
Teaching Skill 是學習目的；ZOOM / SCALE / TIMELINE / COMPARE VIEW / CAUSE ARROW 等只是 visual tools。

### Production
Canonical：Image-first Renderer + Typography Bridge。
圖片引擎可生成整合式繁中圖文構圖；正式輸出必經 Text / Typography QA。P0 教學文字逐字驗證，局部錯誤優先局部修復。

### Delivery / Runtime
Canonical：Lesson Package Delivery、Google Drive Archive、Runtime State。
GitHub 保存規則；Google Drive Runtime 保存每課現在真正跑到哪裡。

---

## 3. Golden Path
正式順序由 `core/governance/vmax-main-workflow.md` 唯一管理；本檔不維護第二份可執行流程。

摘要：

```text
STEP 1 / HOLD 1
→ LKB Assembly / LKB Review
→ STEP 2 / HOLD 2
→ STEP 2.5 / HOLD 2.5
→ STEP 2.6 / HOLD 2.6
→ Teacher Intent / Lesson / Session / LVM
→ Skill Lock + Budget Draft / Gate A
→ Scenario / Scenario Lock
→ Character / Character Lock
→ Experience Completion + Extension
→ Knowledge Lab / Slide Architecture
→ Budget Final + Page Ledger / Storyboard / Gate B
→ Style + Typography / Representative / Gate C
→ Renderer / QA / Delivery
```

若摘要與 Main Workflow 不一致，以 Main Workflow 為準。

---

## 4. Teacher Control
Canonical：HOLD Teacher Interface Policy + Golden Path Executor。

- Source/HOLD/LKB Review：single-stage advance。
- Scenario Lock：先鎖舞台。
- Character Lock：再鎖卡司。
- Gate A/B/C：大型方向與 production 鎖。
- Gate C confirmed 後：批次 production，不逐頁重問。

Command semantics：
- `繼續 / 好 / 可以`：目前合法 decision layer
- `下一頁`：下一 cognitive scene，不重畫目前頁
- `換一個版本`：同內容重設計
- `重畫`：重生目前視覺
- `鎖定`：downstream invariant
- `回前面`：重開指定點後受影響 downstream

---

## 5. Core Invariants

1. Source before design。
2. One LKB authority。
3. Teaching skills before visual tools。
4. Minimum necessary skill set。
5. Text Anchor 可追溯。
6. Spiral ≠ 重複同題。
7. Gate A 鎖 Budget Draft，不鎖精確頁數。
8. 一頁 = 一個完整 cognitive scene；同頁可兩個有層次問題。
9. Scenario 必須在 Character Topology 前鎖定。
10. Character 必須在正式 DNA 前鎖定。
11. 同課跨教材維持 Visual Identity continuity。
12. Conceptual accuracy before beauty。
13. Image-first with Text QA。
14. Teacher controls exceptions。

---

## 6. Book / Lesson / Material Identity

- `BOOK DNA`：整冊熟悉感。
- `LESSON SKIN`：本課在 canonical Style Recipe 上的具體化。
- `SURPRISE SIGNATURE`：0–1；有增益才開。
- `MATERIAL MODE`：PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 的密度與版面適配。

Lesson Skin 不是第二套 Style Library；Surprise 不是固定 gimmick。

---

## 7. NotebookLM Branch
NotebookLM 是主要輸出支線之一，但不阻塞 v1 收尾。

沿用：
- `adapters/notebooklm.md`
- `adapters/notebooklm/OUTPUT_CONTRACT.md`

未來可從 approved LKB 衍生 Visual Source Pack / Audio Source Pack；不得建立分叉 Source Truth。

狀態：`DEFERRED_NON_BLOCKING`。

---

## 8. Regression Requirement
v1 封版前至少通過：
- workflow HOLD regression
- character teaching regression
- worksheet regression
- v1 integration regression

重點：authority 唯一、stage 不飛站、Scenario→Character 依賴正確、Teaching Skill 不被 visual tool 取代、LKB / Text Anchor / Typography 保真、Teacher effort 下降。

---

## 核心金句

> LKB 只有一本；Experience 是總導演，不是第二套資料庫。

> 先鎖舞台，再選卡司；教學技能先於視覺工具。
