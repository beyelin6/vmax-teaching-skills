# V-MAX v1 Integration Regression Cases 1.2-draft

## Purpose
驗證 LKB、Teaching Skill、Experience、Lesson Budget、Typography 與既有 Character / Scenario / Style canonical 能否共存，不產生第二套權威或流程逆轉。

---

## R1｜LKB Single Authority
LKB Builder 負責結構／node／source trace／版本；Routing Policy 只負責 PREVIEW / SHORT_READ / CORE / PLUS / EXTENSION / TEACHER_ONLY 與 spiral。

Fail：`DUPLICATE_LKB_AUTHORITY / SOURCE_TRUTH_FORK`

## R2｜LKB Approval Gate
`READY_FOR_REVIEW` 不得進 STEP 2；必須 `approved_lkb`。

Fail：`UNAPPROVED_LKB_DOWNSTREAM / STAGE_LEAP`

## R3｜Lesson 9 Expository Skill Fit
可選 COMPARE / INFER / STRUCTURE / TRANSFER；SCALE / CAUSE_ARROW / COMPARE_VIEW 只能是 visual tools；`堤／提／題` 可 PREVIEW→CORE_REINFORCE；Text Anchor 保留。

Fail：`VISUAL_TOOL_AS_TEACHING_GOAL / TEXT_ANCHOR_LOST / ROUTING_ERASES_CORE_REINFORCEMENT`

## R4｜Lesson 11 Script Skill Fit
可選 STAGE / PROBLEM_LOOP；SOURCE_WORLD 合法；Text Character 可主導；SCALE 只作 visual tool；舞臺提示不能被 Guide 對話取代。

Fail：`CONTEXT_WRAPPER_OVERREACH / CHARACTER_SYSTEM_BYPASS / GUIDE_CHARACTER_DECORATIVE`

## R5｜Lesson 12 Story Skill Fit
可選 STORY_ARC / CHARACTER_EVIDENCE / TRANSFER；GIVE↔RETURN 是 visual concept；不自動開 STAGE / SCALE。

Fail：`SKILL_TEMPLATE_OVERUSE / VISUAL_TOOL_AS_TEACHING_GOAL`

## R6｜Experience Authority
Scenario→Registry/Selector；Character→Character System/Bridge；Style→Style Recipe Families；Typography→Typography Bridge；Experience 只 orchestration。

Fail：`EXPERIENCE_AUTHORITY_DUPLICATION / CHARACTER_SYSTEM_BYPASS / SCENARIO_REGISTRY_BYPASS / STYLE_RECIPE_BYPASS`

## R7｜SOURCE_WORLD / OFF Legal
強文本世界可 SOURCE_WORLD；外加包裝無增益可 OFF。

Fail：`CONTEXT_WRAPPER_OVERREACH`

## R8｜Guide Minimum Presence
形近字同框、文本高潮、直接證據觀察頁，Guide 預設 OFF，除非有 pedagogical purpose。

Fail：`GUIDE_CHARACTER_DECORATIVE`

## R9｜Cross-material Identity
PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 共享 Character identity、Scenario/Source World、Style family DNA、Lesson Skin Final、Typography Lock；版型密度可不同。

Fail：`VISUAL_IDENTITY_DRIFT / MATERIAL_FAMILY_DRIFT`

## R10｜Lesson Budget Two-stage
Gate A 前只有 Budget Draft；Slide Architecture 後才 Budget Final / Page Ledger；每頁 learning_gain。

Fail：`PAGE_COUNT_BEFORE_ARCHITECTURE / PAGE_WITHOUT_LEARNING_GAIN`

## R11｜Two Questions One Cognitive Scene
同頁兩題須形成同一 cognitive scene，例如 evidence→inference。

Fail：`UNRELATED_DUAL_QUESTION / ONE_QUESTION_ONE_SLIDE_TEMPLATE`

## R12｜Typography Image-first + QA
整合式繁中 typography 合法；P0 逐字驗證；局部錯字優先局部修；Teaching Glyph 不可扭曲到不可辨識。

Fail：`P0_TEXT_UNVERIFIED / TEACHING_GLYPH_DISTORTED / FULL_REGEN_FOR_LOCAL_TEXT_ERROR`

## R13｜Extension Rebalance
Digital/Cross/Theme 外掛必須回答自然接點、增益、時間、取代項、CORE/PLUS；無增益可 OFF。

Fail：`EXTENSION_FOR_NOVELTY / BUDGET_NOT_REBALANCED`

## R14｜Teacher Command Semantics
Gate C 後 `繼續`=依 Storyboard 製作；`下一頁`=下一 cognitive scene；`換一個版本`=重設計；`重畫`=重生目前視覺；`鎖定`=downstream invariant。

Fail：`COMMAND_SEMANTIC_DRIFT / REDRAW_ON_NEXT_PAGE`

## R15｜No Surprise Gimmick
無教學／投入／記憶增益時 Surprise OFF 合法。

Fail：`SURPRISE_FORCED / SURPRISE_NO_LEARNING_VALUE`

## R16｜Scenario Lock Before Character
`Scenario Decision → SCENARIO LOCK → Character Topology/Cast`；SOURCE_WORLD / OFF 也先鎖舞台。

Fail：`SCENARIO_LOCK_SKIPPED / SCENARIO_CHARACTER_COUPLED_SELECTION`

## R17｜Character Lock Before DNA
`Topology/Cast → CHARACTER LOCK → Character DNA / per-shot presence`。

Fail：`CHARACTER_LOCK_SKIPPED`

## R18｜Three Production Gates Do Not Delete Dependency Locks
Gate A/B/C 不能刪掉 HOLD / LKB Review / Scenario Lock / Character Lock。

Fail：`LOCK_COLLAPSE_FOR_SIMPLICITY / STAGE_DEPENDENCY_BROKEN`

## R19｜Style Recipe Before Lesson Skin Final / Gate B

Expected order：

```text
Visual Grammar / Slide Architecture
→ Budget Final / Page Ledger
→ Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative Visual
→ Gate C
```

Gate B 鎖 describable visual direction；Gate C 看實際代表頁。

Fail：`LESSON_SKIN_BEFORE_STYLE_RECIPE / VISUAL_IDENTITY_INCOMPLETE_AT_GATE_B / GATE_C_BYPASSED`

---

## PASS Condition
- R1–R19 全部無架構衝突。
- Main Workflow / Executor / Runtime / Manifest 順序一致。
- 專門 canonical authority boundary 一致。
- 新 policy 不重造舊系統。
