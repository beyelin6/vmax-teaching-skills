# V-MAX System Architecture v1.3-draft

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
→ STYLE RECIPE / LESSON SKIN / TYPOGRAPHY
→ GATE B DESIGN LOCK
→ REPRESENTATIVE VISUAL
→ GATE C VISUAL VALIDATION
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
Canonical：Teaching Skill Selection + Lesson Budget + 各語文／閱讀專門 policy。

順序：`文本診斷 → 學習難點 → MUST/SHOULD/COULD → 最低必要 Teaching Skills → Budget Draft → Gate A`。

### Experience
Orchestrator：`core/experience/vmax-experience-layer.md`。

專門 canonical：
- Scenario lock → Scenario Wrapper Teacher Lock
- Scenario → Registry + Selector
- Character → Character System + Scenario Character Bridge
- Style → Style Recipe Families
- Typography → Typography Bridge

硬相依：
`Scenario Decision → SCENARIO LOCK → Character Topology/Cast → CHARACTER LOCK → Character DNA`

視覺身份相依：
`Visual Grammar / Slide Architecture → Storyboard → Style Recipe → Lesson Skin Final → Typography → Gate B → Representative → Gate C`

> Experience 是總導演，不再造角色庫、情境庫、風格庫；Lesson Skin 也不是在 Style Recipe 前憑空決定。

### Extension
Canonical：Extension Layer。新增外掛先問「它取代什麼？」並重平衡 Budget。

### Visual / Scene Decision
Canonical：Lesson Visual Map、Visual Grammar、Visual Sequence、Director policies。
Teaching Skill 是學習目的；ZOOM / SCALE / TIMELINE / COMPARE VIEW / CAUSE ARROW 等只是 visual tools。

### Production
Canonical：Image-first Renderer + Typography Bridge。
圖片引擎可生成整合式繁中圖文；正式輸出必經 Text / Typography QA。P0 教學文字逐字驗證，局部錯誤優先局部修復。

### Delivery / Runtime
Canonical：Lesson Package Delivery、Google Drive Archive、Runtime State。
GitHub 保存規則；Google Drive Runtime 保存每課真正進度。

---

## 3. Golden Path
正式順序由 `core/governance/vmax-main-workflow.md` 唯一管理；本檔不維護第二份 executable workflow。

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
→ Budget Final + Page Ledger / Storyboard
→ Style Recipe / Lesson Skin / Typography / Gate B
→ Representative / Gate C
→ Renderer / QA / Delivery
```

若摘要與 Main Workflow 不一致，以 Main Workflow 為準。

---

## 4. Teacher Control
Canonical：HOLD Teacher Interface Policy + Golden Path Executor。

- Source/HOLD/LKB Review：single-stage advance。
- Scenario Lock：先鎖舞台。
- Character Lock：再鎖卡司。
- Gate A：教學方向與 Budget Draft。
- Gate B：Storyboard / Page Ledger / Visual Identity direction。
- Gate C：真實代表頁驗證。
- Gate C confirmed 後：批次 production，不逐頁重問。

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
11. Lesson Skin Final 必須在 Style Recipe 之後。
12. Gate B 前 Visual Identity direction 必須已成立。
13. 同課跨教材維持 Visual Identity continuity。
14. Conceptual accuracy before beauty。
15. Image-first with Text QA。
16. Teacher controls exceptions。

---

## 6. Book / Lesson / Material Identity

- `BOOK DNA`：整冊熟悉感，可較早確立。
- `LESSON SKIN`：Style Recipe 的本課具體化，待 Visual Grammar / Storyboard 後 final lock。
- `SURPRISE SIGNATURE`：0–1；有增益才開。
- `MATERIAL MODE`：PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 的密度與版面適配。

Lesson Skin 不是第二套 Style Library；Surprise 不是固定 gimmick。

---

## 7. NotebookLM Branch
NotebookLM 是主要輸出支線之一，但不阻塞 v1 收尾。沿用既有 adapter / output contract。

未來可從 approved LKB 衍生 Visual Source Pack / Audio Source Pack；不得建立分叉 Source Truth。

狀態：`DEFERRED_NON_BLOCKING`。

---

## 8. Regression Requirement
v1 封版前至少通過：
- workflow HOLD regression
- character teaching regression
- worksheet regression
- v1 integration regression
- three-lesson tabletop
- 至少一輪 live/runtime lesson rerun

重點：authority 唯一、stage 不飛站、Scenario→Character 正確、Lesson Skin→Style Recipe 正確、Teaching Skill 不被 visual tool 取代、LKB/Text Anchor/Typography 保真、Teacher effort 下降。

---

## 核心金句
> LKB 只有一本；先鎖舞台，再鎖卡司；先做認知架構，再讓 Style Recipe 長成 Lesson Skin。
