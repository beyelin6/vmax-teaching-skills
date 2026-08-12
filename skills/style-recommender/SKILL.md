---
name: style-recommender
description: V-MAX Style Recipe Candidate Helper。只依 canonical Style Recipe Families 產生少量風格候選，供 Gate B 後的 Style Recipe / Typography Lock 使用。不得自建第二套 Style Library，不得以風格反推教學技能、Scenario 或 Character。
---

# Style Recommender

版本：0.2.0-compat

## Status
`HELPER_NOT_STYLE_AUTHORITY`

風格權威：
- `core/visual/style-recipe-families.md`
- `libraries/styles/index.md` 僅作舊素材／變體來源
- `vmax-typography-bridge/SKILL.md` 管 Typography

---

## 1. Preconditions

至少需要：
- approved_lkb
- Gate A confirmed
- Scenario locked
- Character locked
- Gate B confirmed 或 Storyboard / Page Ledger 已達可供 style 判讀狀態
- Visual Grammar / Slide Architecture 已知

若 Character / Scenario 尚未鎖，不得把 style 當作前置選項反推角色或情境。

---

## 2. Workflow

```text
Locked Teaching Direction
+ Locked Scenario / Character
+ Visual Grammar / Storyboard
→ choose Primary Style Family
→ optional 0–3 Secondary Families
→ define Lesson Skin variables
→ Typography Bridge mapping
→ Representative Visual
→ Gate C
```

---

## 3. Candidate Rules

預設 1–3 個真正不同 Style Recipe 候選，不需要固定 3–5 組。

每個候選包含：
- primary_family
- optional secondary_families
- why_fit：文體／情緒／認知任務／Visual Grammar
- material / palette / lighting / illustration notes
- continuity with Character DNA
- Typography direction
- risk / avoid_when

不得只是換色或換材質冒充不同方案。

---

## 4. Style vs Lesson Skin

- Style Recipe Family = canonical 美術家族。
- Lesson Skin = 本課對已選 Family 的具體化。
- Book DNA = 跨課熟悉感。
- Material Mode = PRESTUDY / SHORT_READ / TEACHING_SLIDE / EXTENSION 適配。

不得把 Lesson Skin 另建成第二套 style taxonomy。

---

## 5. Typography
Style 候選只能輸出 Typography DNA direction；正式字形／mapping／Safety Lock 交由 `vmax-typography-bridge`。

不得因風格可愛、漫畫、RPG 就把 BODY 改成裝飾字。

---

## 6. Teacher / Gate Behavior
Style selection 不建立新的全課必經大 Gate；它屬 Gate B 後、Representative Visual 前的 production decision。

教師若需比較，可在代表頁階段看 1–2 個有意義版本；最終由 Gate C 鎖定可批次生成的視覺方向。

---

## 7. Failure Codes
- `STYLE_RECOMMENDER_AS_STYLE_AUTHORITY`
- `STYLE_BEFORE_SCENARIO_CHARACTER_LOCK`
- `STYLE_DRIVES_TEACHING_SKILL`
- `LESSON_SKIN_AS_SECOND_STYLE_LIBRARY`
- `TYPOGRAPHY_SAFETY_BYPASS`

---

## 核心金句
> Style Recommender 幫忙挑 Style Recipe；它不再自己發明另一套風格系統。
