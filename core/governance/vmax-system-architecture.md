# V-MAX System Architecture v1.1-draft

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

Teacher Control 以 Source/HOLD/Review/Gate 管理確認點。

---

## 2. Authority Map

### Source Truth
Canonical：
- `core/governance/source-library-policy.md`
- `core/governance/step1-source-anchor-policy.md`
- `core/governance/recognition-only-character-policy.md`

### Lesson Knowledge Book
Canonical：
- `skills/chinese-lesson-knowledge-builder/SKILL.md`
- `schemas/lesson-knowledge-book.md`

負責：Official / Teacher Knowledge、節點、source trace、版本、驗證。

### Content Routing / Spiral
Canonical：
- `core/knowledge/lesson-knowledge-base-policy.md`

只負責 approved LKB 的 PREVIEW / SHORT_READ / CORE / PLUS / EXTENSION / TEACHER_ONLY routing，以及 spiral learning。

> LKB 只有一個 authority；Routing 不是第二本 LKB。

### Teaching Direction
Canonical：
- `core/pedagogy/teaching-skill-selection-policy.md`
- `core/governance/lesson-budget-policy.md`
- 各語文／閱讀專門 policy

核心順序：
`文本診斷 → 學習難點 → MUST/SHOULD/COULD → 最低必要 Teaching Skills → Lesson Budget Draft`

### Experience
Orchestrator：
- `core/experience/vmax-experience-layer.md`

專門 canonical：
- Scenario → `core/visual/scenario-wrapper-registry.md` + selector
- Character → `core/character/character-system-2.md` + scenario-character bridge
- Style → `core/visual/style-recipe-families.md`
- Typography → `vmax-typography-bridge/SKILL.md`

> Experience 是總導演，不再造角色庫、情境庫、風格庫。

### Extension
Canonical：
- `core/extension/extension-layer-policy.md`

新增外掛先問「它取代什麼？」並重新平衡 Lesson Budget。

### Visual / Scene Decision
Canonical 來源：
- `core/visual/lesson-visual-map.md`
- `core/visual/visual-grammar.md`
- `core/visual/visual-sequence.md`
- Director policies

Teaching Skill 是學習目的；ZOOM / SCALE / TIMELINE / COMPARE VIEW / CAUSE ARROW 等只是 visual tools。

### Production
Canonical：
- `core/renderer/image-first-hybrid-renderer.md`
- `vmax-typography-bridge/SKILL.md`

圖片引擎可生成整合式繁中圖文構圖；正式輸出必經 Text / Typography QA。P0 教學文字逐字驗證，局部錯誤優先局部修復。

### Delivery / Runtime
Canonical：
- `skills/lesson-package-delivery/SKILL.md`
- `skills/google-drive-lesson-archive/SKILL.md`
- `runtime/lesson-state.md`

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
→ Experience + Extension
→ Knowledge Lab / Slide Architecture
→ Budget Final + Page Ledger / Storyboard / Gate B
→ Style + Typography / Representative / Gate C
→ Renderer / QA / Delivery
```

若摘要與 Main Workflow 不一致，以 Main Workflow 為準。

---

## 4. Teacher Control

Canonical：
- `core/governance/hold-teacher-interface-policy.md`
- `skills/vmax-golden-path-executor/SKILL.md`

前段 Source/HOLD/Review 採 single-stage advance；Gate C confirmed 後，production 依已鎖 Storyboard 批次前進，不逐頁重問。

Teacher command semantics：
- `繼續 / 好 / 可以`：合法下一決策層；Gate C 後直接製作
- `下一頁`：下一認知場景，不重畫目前頁
- `換一個版本`：同內容重設計
- `重畫`：重生目前視覺
- `鎖定`：downstream invariant
- `回前面`：重開指定點之後受影響 downstream

---

## 5. Core Invariants

1. **Source before design**：先讀對教材，再做教學判斷。
2. **One LKB authority**：不得各輸出自己猜一套知識。
3. **Teaching skills before visual tools**。
4. **Minimum necessary skill set**：能不視覺化就不硬視覺化。
5. **Text Anchor**：重要閱讀教學能追回原句／原段。
6. **Spiral ≠ repetition**：再次出現必須深化認知任務。
7. **One cognitive scene per page**：不是一題一頁；同頁可兩個有層次問題。
8. **Budget before bloat**：新增內容先問 learning_gain 與「取代什麼」。
9. **Visual identity continuity**：同課跨教材共享身份 DNA，不共享死版型。
10. **Conceptual accuracy before beauty**。
11. **Image-first with QA**：視覺融合優先，正式文字正確性由 QA 兜底。
12. **Teacher controls exceptions**：AI 做重判斷，老師改例外。

---

## 6. Book / Lesson / Material Identity

- `BOOK DNA`：整冊熟悉感。
- `LESSON SKIN`：本課在 canonical Style Recipe 上的具體化。
- `SURPRISE SIGNATURE`：可選；有教學／投入／記憶價值才開。
- `MATERIAL MODE`：PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 的密度與版面適配。

不得把 Lesson Skin 當第二套 Style Library，也不得把每課驚喜變成固定 gimmick。

---

## 7. NotebookLM Branch

NotebookLM 是主要輸出支線之一，但 v1 收尾不要求完成新的 NotebookLM Source Pack 規格。

現階段沿用：
- `adapters/notebooklm.md`
- `adapters/notebooklm/OUTPUT_CONTRACT.md`

未來可從 approved LKB 衍生 Visual Source Pack / Audio Source Pack；不得建立與 LKB 分叉的新 Source Truth。

狀態：`DEFERRED_NON_BLOCKING`。

---

## 8. Regression Requirement

v1 封版前至少通過：
- workflow HOLD regression
- character teaching regression
- worksheet regression
- `tests/vmax-v1-integration-regression-cases.md`

測試重點不是「能不能產很多頁」，而是：
- authority 是否唯一
- stage 是否飛站
- 教學技能有沒有被視覺工具取代
- Experience 是否重造舊系統
- LKB / Text Anchor / Typography 是否一路保真
- Teacher effort 是否下降

---

## 核心金句

> LKB 只有一本；教材可以很多種。

> Experience 是總導演，不是第二套資料庫。

> 教學技能先於視覺工具；視覺融合優先，但正式文字必須校對到對。
