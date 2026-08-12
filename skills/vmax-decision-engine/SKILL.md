---
name: vmax-decision-engine
description: V-MAX Teaching Direction Candidate Helper。依 approved LKB、Teacher Intent、班級與時間條件，協助產生學習難點、MUST/SHOULD/COULD、Learning Path 候選與 Teaching Skill 候選，供 STEP 2 / Gate A 使用。不得推薦最終 Scenario、Character、Style，不得維護第二套主流程。
---

# V-MAX Decision Engine

版本：0.2.0-compat

## Status
`TEACHING_DIRECTION_HELPER_NOT_WORKFLOW_AUTHORITY`

正式主流程：Main Workflow + Golden Path Executor。

---

## 1. Mission
把 approved LKB、學生條件、教師要求與時間限制轉成**可解釋的教學方向候選**，但不取代：
- Teaching Skill Selection Policy
- Lesson Budget Policy
- Teacher Intent Lock
- Gate A

---

## 2. Preconditions

必須讀取：
- approved LKB
- Teacher Knowledge / Teacher Profile（若有）
- 課堂時間、班級條件
- 教師當次要求
- STEP 2 已知的文本／學習難點，或本技能協助整理後交回 STEP 2

不得要求 Role Library / Style Library 作為 Teaching Direction 的必要輸入。

---

## 3. Allowed Outputs

可提出：
- student friction / learning difficulty
- MUST / SHOULD / COULD
- 2–4 個 Learning Path 候選（若真的有必要比較）
- Teaching Skill candidates
- standard / quick / high_interaction / review 等時間版本的差異
- device / no-device constraint notes
- 哪些內容刻意不做

所有候選都要說明：why fit / risk / time implication / evidence from LKB。

---

## 4. Forbidden Outputs

本技能不得：
- 決定 Scenario Wrapper
- 決定 Character topology / cast
- 推薦最終 Style Recipe
- 宣告精確 slide count
- 直接啟動 Presentation Engine
- 因平板可用就硬加 digital activity

Scenario / Character / Style 只能在 Gate A 後依各自 canonical 處理。

---

## 5. Flow

```text
approved LKB
+ Teacher Intent / class constraints
→ learning difficulty
→ MUST / SHOULD / COULD
→ Teaching Skill candidates
→ optional Learning Path comparison
→ Teaching Skill Selection Policy
→ Lesson Budget Draft
→ Gate A
```

若 Gate A confirmed，Decision Engine 本輪任務結束；不得越過 Gate A 直接做 Experience。

---

## 6. Device / Interaction
平板只作 constraint / extension candidate：
- 若能提升分類、重組、錄音、合作、即時診斷或學習證據，可記為 Extension candidate。
- 若只是把紙本搬到螢幕，不推薦。
- 正式 digital design 交 Extension Layer / Digital Interaction Planner。

---

## 7. Output

```yaml
teaching_direction_candidates:
  learning_difficulties: []
  priorities:
    must: []
    should: []
    could: []
  skill_candidates: []
  optional_paths: []
  time_constraints:
  device_constraints:
  deliberate_omissions: []
  status: READY_FOR_TEACHING_SKILL_SELECTION
```

---

## 8. Failure Codes
- `DECISION_ENGINE_AS_MAIN_WORKFLOW`
- `ROLE_STYLE_RECOMMENDED_BEFORE_GATE_A`
- `PAGE_COUNT_FROM_DECISION_ENGINE`
- `DIGITAL_ACTIVITY_FORCED`
- `TEACHING_SKILL_WITHOUT_LEARNING_DIFFICULTY`

---

## 核心金句
> Decision Engine 幫忙把「教什麼」想清楚；它不再決定「舞台長什麼、誰來演、畫成什麼風格」。
