# V-MAX Workflow Gates — Legacy Compatibility Map

## Status

`LEGACY_REFERENCE_NOT_EXECUTABLE`

此檔保留舊版 Gate 1–10 的歷史概念，但**不得再被當成 V-MAX 現行可執行主流程**。

現行權威：
- `V-MAX_MANIFEST.md`
- `core/governance/vmax-main-workflow.md`
- `core/governance/hold-teacher-interface-policy.md`
- `skills/vmax-golden-path-executor/SKILL.md`
- `runtime/lesson-state.md`

---

## 舊 Gate → 現行對應

| 舊 Gate | 舊概念 | 現行位置 |
|---|---|---|
| Gate 1 | Official Knowledge Review | STEP 1 → HOLD 1 Source Truth |
| Gate 2 | LKB Review | LKB ASSEMBLY → LKB REVIEW / approved_lkb |
| Gate 3 | Learning Modules Review | Content Routing / Extension candidates；不再是固定全課 Gate |
| Gate 4 | Learning Path / Teaching Flow | Teacher Intent / Lesson Map / Session Map / Teaching Skill Selection |
| Gate 5 | Teaching Strategy | Teaching Skill Selection + Lesson Budget Draft → Gate A |
| Gate 6 | Digital Interaction | Extension Check；需要才啟用 |
| Gate 7 | Role Review | SCENARIO LOCK 後 → Character Topology/Cast → CHARACTER LOCK |
| Gate 8 | Style Review | Gate B 後 Style Recipe / Typography → Representative Visual |
| Gate 9 | Output Profile | Delivery / Material Mode / Package config；不是固定教學 Gate |
| Gate 10 | Final Review | Gate C + Quality Gate + Lesson Package Delivery |

---

## 現行教師確認鏈摘要

```text
HOLD 1
→ LKB REVIEW
→ HOLD 2
→ HOLD 2.5
→ HOLD 2.6
→ Gate A
→ SCENARIO LOCK
→ CHARACTER LOCK
→ Gate B
→ Gate C
```

其中：
- 前段 HOLD / Review = source / teaching safety
- Scenario / Character Lock = Experience dependency
- Gate A/B/C = large production decisions

不得把這張摘要當成省略中間執行 stage 的捷徑；完整順序以 Main Workflow 為準。

---

## Legacy Data Preservation

舊版以下資料仍有價值，可被現行系統讀取／遷移：
- Official Knowledge validation
- LKB validation
- Learning Modules / Expansion content
- Teaching Strategy notes
- Digital Interaction profile
- Role selection profile
- Style selection profile
- Output profile

但讀取舊資料後必須映射到現行 Runtime / canonical locks，不得讓舊檔案直接覆蓋現行決策。

---

## 禁止

- 復活固定 Gate 1→10 作為現行主流程
- Gate 6 平板活動變成每課必做
- Gate 7 直接選 Role，跳過 Scenario Lock
- Gate 8 Style 反推教學技能或 Scenario
- 舊 project-status 覆蓋 Google Drive Runtime

Failure codes：
`LEGACY_GATE_SEQUENCE_REVIVED / SCENARIO_LOCK_BYPASSED_BY_LEGACY_ROLE_GATE / LEGACY_PROJECT_STATUS_OVERRIDE`

---

## 核心金句

> 舊 Gate 保留歷史知識；新 Main Workflow 才決定現在怎麼跑。
