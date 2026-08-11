# V-MAX v1 Integration Regression Cases 1.0-draft

## Purpose
驗證 v1 新增的 LKB Routing、Teaching Skill Selection、Experience Orchestration、Lesson Budget、Typography 與既有 Character / Scenario / Style canonical 能否共存，不產生第二套權威或流程逆轉。

---

## R1｜LKB Single Authority

### Given
- Official Knowledge 已在 HOLD 1 確認。
- `chinese-lesson-knowledge-builder` 建立 LKB。

### Expect
- LKB Builder 負責結構、節點、source trace、版本與驗證。
- `lesson-knowledge-base-policy.md` 只標 PREVIEW / SHORT_READ / CORE / PLUS / EXTENSION / TEACHER_ONLY 與 spiral route。
- 不得產生第二份不同章節或不同 source truth 的 LKB。

### Fail
`DUPLICATE_LKB_AUTHORITY / SOURCE_TRUTH_FORK`

---

## R2｜LKB Approval Gate

### Given
LKB status = `READY_FOR_REVIEW`。

### Expect
STEP 2 不合法；必須先 `approved_lkb`。

### Fail
`UNAPPROVED_LKB_DOWNSTREAM / STAGE_LEAP`

---

## R3｜Lesson 9 Expository Text：技能先於工具

### Input characteristics
- 平行介紹多個國家。
- 荷蘭段需要理解低窪、堤防、風車、木鞋與「所以／為了」。

### Expect
- 可選 COMPARE / INFER / STRUCTURE / TRANSFER。
- SCALE、CAUSE ARROW、COMPARE VIEW 只能是 visual tools，不得被宣告為教學目標。
- Text Anchor 保留原文；RETURN 視需要啟動。
- 形近字「堤／提／題」可從 PREVIEW 進 CORE_REINFORCE。

### Fail
`VISUAL_TOOL_AS_TEACHING_GOAL / TEXT_ANCHOR_LOST / ROUTING_ERASES_CORE_REINFORCEMENT`

---

## R4｜Lesson 11 Script：Character / Scenario Canonical

### Input characteristics
劇本；核心閱讀包含角色、臺詞、舞臺提示，並有問題→嘗試→結果循環。

### Expect
- Teaching skills 可選 STAGE / PROBLEM_LOOP。
- Experience 若直接使用劇本世界，Scenario mode = `SOURCE_WORLD`，不必外加 RPG / 偵探 wrapper。
- Character System 決定 Text Character / Guide 是否需要；若課文人物足夠，可 `TEXT_CHARACTER_LED` 或 Guide OFF。
- `(不慌不忙)` 等舞臺提示不得被 Guide 對話取代。

### Fail
`SCENARIO_REGISTRY_BYPASS / CHARACTER_SYSTEM_BYPASS / GUIDE_CHARACTER_DECORATIVE`

---

## R5｜Lesson 12 Story：不要複製 Lesson 9 技能

### Input characteristics
故事主旨為感恩與回饋；角色行動證據重要。

### Expect
- 可選 STORY_ARC / CHARACTER_EVIDENCE / TRANSFER。
- 不因系統有 SCALE / STAGE 就自動啟動。
- Scene Decision 可用 GIVE↔RETURN 的互惠視覺，但它服務理解而非成為新教學技能。

### Fail
`SKILL_TEMPLATE_OVERUSE / VISUAL_TOOL_AS_TEACHING_GOAL`

---

## R6｜Experience Layer Authority

### Given
本課需要情境、角色與 Style。

### Expect
- Scenario → Scenario Wrapper Registry / Selector。
- Character topology / cast / DNA → Character System + Scenario Character Bridge。
- Style family → Style Recipe Families。
- Experience Layer 只保存 refs、Lesson Skin、Learner Role、Surprise Signature 與跨教材 identity。

### Fail
`EXPERIENCE_AUTHORITY_DUPLICATION / CHARACTER_SYSTEM_BYPASS / SCENARIO_REGISTRY_BYPASS / STYLE_RECIPE_BYPASS`

---

## R7｜Source World Beats Forced Wrapper

### Given
文本本身已有強烈故事／戲劇世界。

### Expect
- Experience 可以 `SOURCE_WORLD`。
- Scenario Wrapper Registry 不要求一定選一個外加 wrapper。
- Wrapper = OFF 不視為缺功能。

### Fail
`CONTEXT_WRAPPER_OVERREACH`

---

## R8｜Guide Character Minimum Presence

### Given
某頁為形近字同框辨析、重要課文高潮或直接文本證據觀察。

### Expect
Guide 預設 OFF，除非有清楚 pedagogical purpose。

### Fail
`GUIDE_CHARACTER_DECORATIVE`

---

## R9｜Cross-material Visual Identity

### Given
同課輸出 PRESTUDY、SHORT_READ、TEACHING_SLIDE。

### Expect
- Character identity / DNA（若啟用）一致。
- Scenario / Source World identity 一致。
- Lesson Skin / Style family DNA / Typography Lock 一致。
- 版型與密度可不同。

### Fail
`VISUAL_IDENTITY_DRIFT / MATERIAL_FAMILY_DRIFT`

---

## R10｜Lesson Budget Two-stage Model

### Given
尚未完成 Slide Architecture。

### Expect
- 只能建立 Lesson Budget Draft：時間、MUST/SHOULD/COULD、核心認知任務。
- 不可宣告精確頁數。

### Given
Slide Architecture 完成。

### Expect
可建立 Budget Final / Page Ledger；每頁需 learning_gain。

### Fail
`PAGE_COUNT_BEFORE_ARCHITECTURE / PAGE_WITHOUT_LEARNING_GAIN`

---

## R11｜Two Questions One Cognitive Scene

### Given
同一頁包含兩個問題。

### Pass example
「從哪一句找到證據？」→「所以你推論出什麼？」

### Fail example
「找因果」＋「寫一個不相關成語」。

### Expect
頁面單位是完整 cognitive scene，不是 question count。

### Fail
`UNRELATED_DUAL_QUESTION / ONE_QUESTION_ONE_SLIDE_TEMPLATE`

---

## R12｜Typography Image-first + QA

### Given
圖片引擎生成含繁中文字的完整圖文構圖。

### Expect
- 允許保留整合式 typography。
- 課文、生字、形近字、多音字、注音、目標字、關鍵句／臺詞列為 P0。
- 錯一字優先局部修復／overlay，不因單一錯字重畫整頁。
- 字形本身是教學內容時，不可藝術化到無法辨識。

### Fail
`P0_TEXT_UNVERIFIED / TEACHING_GLYPH_DISTORTED / FULL_REGEN_FOR_LOCAL_TEXT_ERROR`

---

## R13｜Extension Rebalance

### Given
教師要求「本課＋平板＋國際教育」。

### Expect
Extension Check 回答自然接點、增益、角色／情境影響、時間、取代項、CORE/PLUS status。

如果沒有自然增益，推薦 LIGHT / PLUS / OFF，而非硬塞 QR、影片或平板操作。

### Fail
`EXTENSION_FOR_NOVELTY / BUDGET_NOT_REBALANCED`

---

## R14｜Teacher Command Semantics

### Given
已進 production phase 且 Gate C confirmed。

### Commands
- `繼續` → 依已鎖 Storyboard 往下製作。
- `下一頁` → 下一認知場景，不重畫目前頁。
- `換一個版本` → 重新設計同內容。
- `重畫` → 重生目前視覺。
- `鎖定` → 寫 downstream invariant。

### Fail
`COMMAND_SEMANTIC_DRIFT / REDRAW_ON_NEXT_PAGE`

---

## R15｜No Surprise Gimmick

### Given
系統找不到具教學／投入／記憶增益的 Surprise Signature。

### Expect
`surprise_signature.status = OFF` 合法。

### Fail
`SURPRISE_FORCED / SURPRISE_NO_LEARNING_VALUE`

---

## PASS Condition

v1 integration pass 至少需：
- R1–R15 全部無架構衝突。
- Main Workflow / Executor / Runtime / Manifest 對 Golden Path 的順序一致。
- 所有專門 canonical 的 authority boundary 一致。
- 不出現「新 policy 為了整合反而重造舊系統」的情況。
