---
name: role-recommender
description: V-MAX Character Candidate Helper。只在 Scenario 已鎖定後，依 Character System 與 Scenario Character Bridge 產生 1–3 個 topology / cast 候選，供 CHARACTER LOCK 使用。不得繞過 Scenario Lock、不得自建第二套角色規則、不得在確認前生成正式 Character DNA。
---

# Role Recommender

版本：0.2.0-compat

## Status
`HELPER_NOT_CHARACTER_AUTHORITY`

角色權威：
- `core/character/character-system-2.md`
- `core/character/scenario-character-bridge.md`
- `core/character/character-registry.md`

本技能只負責 candidate retrieval / recommendation。

---

## 1. Preconditions

必須存在：
- `approved_lkb`
- Gate A confirmed
- Scenario status = `LOCKED`
- Scenario mode / wrapper ref 已知
- Teaching Skill Selection / Teacher Intent 已知

若 Scenario 未鎖：`BLOCKED_BY_SCENARIO_LOCK`，不得推薦角色。

---

## 2. Workflow

```text
Locked Scenario / Source World / OFF
→ Character System 決定最小必要 topology
→ Scenario Character Bridge 解析 role need
→ Character Registry retrieval
→ 1–3 candidate sets
→ Teacher Confirmation Card
→ CHARACTER LOCK
→ downstream Character DNA
```

不得把 Wrapper 與角色綁成一組套餐讓教師一起選。

---

## 3. Candidate Rules

候選數：1–3 組真正不同方案即可。

每組至少說明：
- topology
- role slots / pedagogical function
- candidate cast source：TEXT / REGISTRY / NEW / FALLBACK
- why fit
- risk / forcedness
- Guide 可否 OFF
- 是否會搶 Text Character 主體

優先順序依 Bridge：
1. 課文人物／文本內在角色
2. 高匹配 reusable confirmed
3. reusable candidate
4. 本課新角色
5. fallback guide

不得因角色漂亮／最近常用／已有圖就優先。

---

## 4. Bee Teacher
Bee 老師只是一個 Registry / fallback candidate，不是預設主角。

可以被推薦，但需滿足：
- 教師型 Guide 確實有教學功能
- 不搶課文人物
- Scenario / Learner Role 自然

名稱 Bee 不代表蜜蜂／昆蟲角色。

---

## 5. Teacher Lock
教師確認的是：
- topology
- cast
- role relationship
- Guide 是否啟用

未 `CHARACTER LOCK` 前：
- 不建立正式 Character DNA
- 不生成角色基準圖
- 不進大量角色視覺

---

## 6. Output

```yaml
character_cast_candidates:
  scenario_ref:
  topology_candidates:
    - topology:
      role_slots: []
      cast: []
      why_fit:
      risk:
      guide_off_possible: true|false
  recommendation:
  status: READY_FOR_CHARACTER_LOCK
```

---

## 7. Failure Codes
- `BLOCKED_BY_SCENARIO_LOCK`
- `SCENARIO_CHARACTER_COUPLED_SELECTION`
- `ROLE_RECOMMENDER_AS_CHARACTER_AUTHORITY`
- `CHARACTER_DNA_BEFORE_LOCK`
- `GUIDE_FORCED_BY_EXISTING_ASSET`

---

## 核心金句
> Scenario 先鎖；Role Recommender 只幫忙找卡司，不決定角色宇宙的規則。
