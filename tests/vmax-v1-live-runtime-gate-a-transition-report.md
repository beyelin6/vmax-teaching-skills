# V-MAX v1 Live Runtime Gate A Transition Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
teacher_lkb_confirmation: RECEIVED
approved_lkb: PASS_LIVE_DRIVE
migration_resume: PASS
redundant_hold_reconfirmation: NOT_TRIGGERED
teaching_skill_selection: PASS
lesson_budget_draft: PASS
runtime_transition: PASS_TO_GATE_A
illegal_stage_jump_detected: false
renderer_entered: false
current_teacher_checkpoint: GATE_A_TEACHING_DIRECTION
```

## A. Teacher LKB Approval

教師於 2026-08-12 明確核准 migration LKB 作為新版 Runtime 基線，並接受 `SOURCE_REF_ONLY` 課文正文模式：完整課文仍以官方 PDF 為權威，不從 legacy Runtime 拼湊全文。

Drive approved LKB：
- title: `L01_lesson-knowledge-book_v02`
- document id: `1osHATF7Cj05gB820LOrKn2Va_m7znjF3GgBrgmxaLuQ`
- status: `approved_lkb`

## B. Evidence-aware Migration Resume

Runtime `_03` 已記錄下列教師舊決策為明確 confirmed evidence：
- HOLD 2
- HOLD 2.5
- HOLD 2.6
- Teacher Intent

新版 LKB 沒有推翻這些決策，因此依 `runtime-migration-resume-policy.md`：
- 不重問 HOLD 2 / 2.5 / 2.6。
- 不把舊 Scenario / Character / Style / Representative evidence 自動升格成新版 lock。
- 合法重跑點為 `Teaching Skill Selection → Lesson Budget Draft → Gate A`。

結果：PASS。

## C. Teaching Skill Selection

Drive：
- title: `L01_teaching-skill-selection_v01`
- id: `1Q4xcSBODkHVYGvUK6OUvrMRD_Z0N3R9T0LOi69PJWNQ`

選擇：
```yaml
core_skills:
  - INFER
  - COMPARE
  - TRANSFER
support_skills:
  - STRUCTURE
conditional_skills:
  - RETURN
```

理由：
- INFER 解決「動作文字 → 想像畫面／感受」的核心閱讀困難。
- COMPARE 解決雙詩動作、速度、心情、節奏只停在表面比較的問題，也支援已確認字群的比較辨析。
- TRANSFER 把來源句方法轉成一小節運動童詩與朗讀修訂。
- STRUCTURE 只作兩首／三詩節導航，不升格為第四核心技能。
- RETURN 僅在證據驗證／語境辨義／防止圖像漂移時使用。

未選 STAGE / PROBLEM_LOOP / STORY_ARC / CHARACTER_EVIDENCE，也未先由 visual tool 反推 teaching skill。

## D. Lesson Budget Draft

Drive：
- title: `L01_lesson-budget-draft_v01`
- id: `1IPRJ6DjkO-IEBg0pEAdmRqajJUWHMjSS-HZ18gwy0Kk`

Baseline：
```yaml
period_length_minutes: 40
standard_sessions: 7
total_core_minutes: 280
exact_page_count: FORBIDDEN_AT_DRAFT_STAGE
```

7 堂分配：
1. 雙詩完整初讀與定位。
2. 〈游泳〉證據→畫面→感受→節奏。
3. 〈溜直排輪〉＋雙詩比較＋「一般」語境辨義。
4. 前五組字群＋「溜」兩音。
5. 後五組字群＋「轉」。
6. 五個核心成語＋完整情境／表達。
7. 一小節運動童詩創作、朗讀、修訂與收束。

舊 `56頁 / 54–60頁` 只保留 legacy evidence，不成為新版 Page Ledger。精確頁數仍必須等新版 Slide Architecture 後才可成立。

重要診斷：280 分鐘幾乎已被教師確認的 CORE scope 完整占用；新增 DIGITAL / CROSS / PBL / SEL 等核心延伸時，必須先回答「它取代什麼？」。

## E. Gate A Artifact

Drive：
- title: `L01_gate-a-teaching-direction_v01`
- id: `1ix9PQcdx6-nNKhIh36lVGiyGGEAGq0lPfY_nE3H3O6o`
- status: `WAITING_CONFIRMATION`

Gate A 核心：
- 孩子用動作證據形成想像與感受。
- 讀出文字本身造成的詩歌節奏。
- 比較兩首童詩的動態、速度、心情、節奏。
- 遷移成一小節可朗讀運動童詩。
- 完成教師已確認的十組字群／溜兩音／轉／一般／五成語 scope。

## F. Runtime `_04`

Drive：
- title: `V-MAX_State_四上_第一課_水陸小高手_04`
- id: `1uN4ksPZVlB4Wws2RUvh_OcleZGDRY_A4D2aBak6deG4`

```yaml
runtime_schema_version: 2.7-draft
workflow_version: 2.6-draft
manifest_version: 3.9-draft
executor_version: 1.8-draft
runtime_version: 04
current_stage: GATE_A_TEACHING_DIRECTION
last_completed_stage: LESSON_BUDGET_DRAFT
teacher_confirmation_status: WAITING_CONFIRMATION
renderer_status: BLOCKED_UNTIL_GATE_C
```

Runtime active refs include approved LKB v02 and persisted Gate A-chain artifacts. Legacy `_02` / `_03` remain intact.

## G. Runtime Index v03

Drive：
- title: `V-MAX_Runtime_Index_v03`
- id: `1Sq3muBVTSLd9w7l5BUFWRPAd0PUVW68R-zBe3BUehJU`
- active runtime: `_04`
- previous index: `1bC3m1Y-hX1rP75-UGiEv_gH_FwwP0b9eQam0zKgH4Vw`

Index 使用 non-destructive versioning；v02 未覆蓋。

## H. Legal Next Step

Gate A 尚未由教師確認，因此目前禁止：
- Scenario Decision
- Character Topology
- Gate B / Gate C
- Full Renderer

教師確認 Gate A 後唯一合法前進：

`Gate A confirmed → Scenario Decision → SCENARIO LOCK`

本輪到 Gate A 為止，未發現 stage leap。
