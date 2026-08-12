# V-MAX v1 Integration Regression Cases 1.1-draft

## Purpose
驗證 v1 新增的 LKB Routing、Teaching Skill Selection、Experience Orchestration、Lesson Budget、Typography 與既有 Character / Scenario / Style canonical 能否共存，不產生第二套權威或流程逆轉。

---

## R1｜LKB Single Authority
Given：Official Knowledge 已在 HOLD 1 確認，`chinese-lesson-knowledge-builder` 建立 LKB。

Expect：
- LKB Builder 負責結構、節點、source trace、版本與驗證。
- Routing policy 只標 PREVIEW / SHORT_READ / CORE / PLUS / EXTENSION / TEACHER_ONLY 與 spiral route。
- 不得產生第二份不同 source truth 的 LKB。

Fail：`DUPLICATE_LKB_AUTHORITY / SOURCE_TRUTH_FORK`

---

## R2｜LKB Approval Gate
Given：LKB status = `READY_FOR_REVIEW`。
Expect：STEP 2 不合法；必須先 `approved_lkb`。
Fail：`UNAPPROVED_LKB_DOWNSTREAM / STAGE_LEAP`

---

## R3｜Lesson 9 Expository Text：技能先於工具
Input：平行介紹多國；荷蘭段需理解低窪、堤防、風車、木鞋與「所以／為了」。

Expect：
- 可選 COMPARE / INFER / STRUCTURE / TRANSFER。
- SCALE、CAUSE ARROW、COMPARE VIEW 只能是 visual tools。
- Text Anchor 保留原文；RETURN 視需要啟動。
- 「堤／提／題」可 PREVIEW → CORE_REINFORCE。

Fail：`VISUAL_TOOL_AS_TEACHING_GOAL / TEXT_ANCHOR_LOST / ROUTING_ERASES_CORE_REINFORCEMENT`

---

## R4｜Lesson 11 Script：文本世界優先
Input：劇本；角色、臺詞、舞臺提示；問題→嘗試→結果循環。

Expect：
- Teaching skills 可選 STAGE / PROBLEM_LOOP。
- 可推薦 Scenario = `SOURCE_WORLD`，不硬加 RPG / 偵探。
- Character System 決定 Text Character / Guide；課文人物足夠時可 TEXT_CHARACTER_LED / Guide OFF。
- 舞臺提示不得被 Guide 對話取代。

Fail：`CONTEXT_WRAPPER_OVERREACH / CHARACTER_SYSTEM_BYPASS / GUIDE_CHARACTER_DECORATIVE`

---

## R5｜Lesson 12 Story：不要複製 Lesson 9 技能
Input：故事主旨為感恩與回饋；角色行動證據重要。

Expect：STORY_ARC / CHARACTER_EVIDENCE / TRANSFER；不因系統有 SCALE / STAGE 就自動啟動。

Fail：`SKILL_TEMPLATE_OVERUSE / VISUAL_TOOL_AS_TEACHING_GOAL`

---

## R6｜Experience Layer Authority
Expect：
- Scenario → Scenario Wrapper Registry / Selector。
- Character topology / cast / DNA → Character System + Scenario Character Bridge。
- Style family → Style Recipe Families。
- Experience Layer 只 orchestration refs、Lesson Skin、Learner Role、Surprise Signature、跨教材 identity。

Fail：`EXPERIENCE_AUTHORITY_DUPLICATION / CHARACTER_SYSTEM_BYPASS / SCENARIO_REGISTRY_BYPASS / STYLE_RECIPE_BYPASS`

---

## R7｜Source World / OFF Are Legal
文本世界足夠時可 `SOURCE_WORLD`；外加 Wrapper 無增益時可 `OFF`。兩者不視為缺功能。

Fail：`CONTEXT_WRAPPER_OVERREACH`

---

## R8｜Guide Character Minimum Presence
形近字同框辨析、文本高潮、直接證據觀察頁，Guide 預設 OFF，除非有清楚 pedagogical purpose。

Fail：`GUIDE_CHARACTER_DECORATIVE`

---

## R9｜Cross-material Visual Identity
同課 PRESTUDY / SHORT_READ / TEACHING_SLIDE：Character identity、Scenario/Source World、Lesson Skin、Style family DNA、Typography Lock 一致；版型密度可不同。

Fail：`VISUAL_IDENTITY_DRIFT / MATERIAL_FAMILY_DRIFT`

---

## R10｜Lesson Budget Two-stage Model
Slide Architecture 前只可 Budget Draft；完成後才 Budget Final / Page Ledger，每頁必須 learning_gain。

Fail：`PAGE_COUNT_BEFORE_ARCHITECTURE / PAGE_WITHOUT_LEARNING_GAIN`

---

## R11｜Two Questions One Cognitive Scene
Pass：「從哪一句找到證據？」→「所以你推論什麼？」
Fail：「找因果」＋「寫不相關成語」。

Fail code：`UNRELATED_DUAL_QUESTION / ONE_QUESTION_ONE_SLIDE_TEMPLATE`

---

## R12｜Typography Image-first + QA
Expect：
- 允許整合式繁中 typography。
- 課文、生字、形近字、多音字、注音、目標字、關鍵句／臺詞 = P0。
- 局部錯字優先局部修復／overlay。
- 教學字形不可藝術化到無法辨識。

Fail：`P0_TEXT_UNVERIFIED / TEACHING_GLYPH_DISTORTED / FULL_REGEN_FOR_LOCAL_TEXT_ERROR`

---

## R13｜Extension Rebalance
「本課＋平板＋國際教育」必須回答自然接點、增益、角色／情境影響、時間、取代項、CORE/PLUS。無自然增益可 LIGHT / PLUS / OFF。

Fail：`EXTENSION_FOR_NOVELTY / BUDGET_NOT_REBALANCED`

---

## R14｜Teacher Command Semantics
Gate C confirmed 後：
- `繼續` → 依已鎖 Storyboard 製作
- `下一頁` → 下一 cognitive scene，不重畫目前頁
- `換一個版本` → 同內容重設計
- `重畫` → 重生目前視覺
- `鎖定` → downstream invariant

Fail：`COMMAND_SEMANTIC_DRIFT / REDRAW_ON_NEXT_PAGE`

---

## R15｜No Surprise Gimmick
找不到教學／投入／記憶增益時，`surprise_signature.status = OFF` 合法。

Fail：`SURPRISE_FORCED / SURPRISE_NO_LEARNING_VALUE`

---

## R16｜Scenario Lock Before Character
Given：Gate A confirmed，進 Experience。

Expect：
```text
Scenario Decision / Candidates
→ SCENARIO LOCK
→ Character Topology / Cast Candidates
```

即使選 `SOURCE_WORLD` 或 `OFF`，也先確認舞台決策，再推薦卡司。

Fail：`SCENARIO_LOCK_SKIPPED / SCENARIO_CHARACTER_COUPLED_SELECTION`

---

## R17｜Character Lock Before DNA
Given：Scenario locked。

Expect：
```text
Character Topology / Cast Candidates
→ CHARACTER LOCK
→ Character DNA / per-shot presence
```

禁止先生成正式角色 DNA 或大量角色圖，再請教師決定角色。

Fail：`CHARACTER_LOCK_SKIPPED`

---

## R18｜Three Production Gates Do Not Delete Existing Locks
Expect：
- Gate A/B/C 是大型 production decisions。
- HOLD / LKB Review / Scenario Lock / Character Lock 仍依相依關係存在。
- 不因追求「只剩三個 Gate」而破壞 source truth 或 Scenario→Character ordering。

Fail：`LOCK_COLLAPSE_FOR_SIMPLICITY / STAGE_DEPENDENCY_BROKEN`

---

## PASS Condition
v1 integration pass 至少需：
- R1–R18 全部無架構衝突。
- Main Workflow / Executor / Runtime / Manifest 對 Golden Path 與 lock ordering 一致。
- 專門 canonical authority boundary 一致。
- 新 policy 不重造舊系統。
