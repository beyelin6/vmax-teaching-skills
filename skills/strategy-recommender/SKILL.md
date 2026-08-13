---
name: strategy-recommender
description: 依教材內容、學習目標、學生條件與教師意圖推薦可執行的教學策略，並說明選擇理由與限制；需要比較或決定教學策略時使用。
---

# V-MAX Strategy Recommender

## Purpose

依課文內容、學習目標、班級學習樣貌、教師意圖與 Director Intent，推薦適合的教學策略。此 Skill 不直接決定唯一做法，也不以新奇活動為優先。

## Inputs

Required:
- Text DNA / lesson content
- primary learning goal
- target node or paragraph

Optional:
- Learning Profile
- Teacher Intent
- Director Intent
- existing strategies to avoid repetition
- digital access / open class requirements
- student observation from previous lesson

## Workflow

1. 找出此節點最可能的理解障礙。
2. 判斷學生需要的是辨識、理解、比較、推論、表達、應用或創作。
3. 讀取 Director Intent，避免策略與視覺觀看路徑互相衝突。
4. 產生 2～4 個候選策略。
5. 每個候選說明：為什麼適合、適合什麼學生、可能代價、可觀察證據。
6. 教師指定後，再映射到紙本／口語／平板／Padlet／ClassSwift／Wordwall 等 Delivery。
7. 若教師只要求快速版，提供 2 個差異明顯且可直接執行的候選。

## Output Contract

```yaml
strategy_recommendation:
  target:
  learning_goal:
  common_barrier:
  recommendations:
    - rank:
      type:
      title:
      method:
      teaching_point:
      application:
      why_this_strategy:
      evidence_to_watch:
      best_for:
      tradeoff:
      recommended_delivery: []
      director_alignment:
```

## Strategy Types

不限制固定清單，可使用：

- OBSERVE_DISCOVER
- TEXT_EVIDENCE
- COMPARE_CLASSIFY
- CAUSE_EFFECT
- ROLE_PERSPECTIVE
- INQUIRY
- REWRITE_TRANSFORM
- VISUAL_ORGANIZATION
- ORAL_RECONSTRUCTION
- CREATIVE_APPLICATION
- GAME_TASK
- DISCUSSION
- FOUR_LEARNING
- FORMATIVE_CHECK

類型只是標籤，不是強制流程。

## Guardrails

- 不得自行發明課文不存在的人物、事件或作者意圖。
- 不得因「活動看起來有趣」而偏離主要學習目標。
- 不得把數位工具名稱當作教學策略本身。
- 不得全域禁止朗讀、圈選、找證據等基礎動作；若它們是更高層理解的必要鷹架即可使用。
- 不得要求所有學生完成相同高階任務；可提供 support / core / challenge 變體。
- 公開課若啟用四學模式，策略需標出自學、共學、互學、導學中的責任轉移與學習證據。

## Legacy Compatibility

舊 Omni Architect 的 StrategyItem：

```ts
{
  type,
  title,
  method,
  teachingPoint,
  application
}
```

可直接遷移為新版 Strategy Card，再補上：

- `common_barrier`
- `why_this_strategy`
- `evidence_to_watch`
- `recommended_delivery`
- `director_alignment`

舊策略內容不因升級而自動淘汰；先保留，再依新版規則評估。

## Handoff

輸出可交給：
- Lesson Designer
- Director Designer
- Digital Delivery Designer
- Four-Learning Open Class Planner
- Assessment Designer
- Slide Script Builder
