---
name: role-recommender
description: 根據已核准的國語教材知識書、學習延伸模組、教學策略、年級與候選視覺方向，推薦適合本課的引導角色。必須提出 3 至 5 個候選角色、說明教材依據與教學功能，並停下等待教師確認。可推薦或直接選用 Bee 老師，但不得在確認前生成角色基準圖或定稿簡報。
---

# Role Recommender

版本：0.1.0

## 使命

根據每一課教材內容動態推薦引導角色，使角色服務教材與教學流程，而不是讓教材被迫套入固定角色。

## 前置輸入

必須讀取：

- 已核准的 Lesson Knowledge Book
- 已核准的 Learning Module Profile
- 已核准的 Teaching Strategy Profile
- `schemas/role-selection-profile.md`
- `libraries/roles/` 中的角色資料

若候選風格已產生，可一併讀取；未選風格時，不得假設最終視覺風格。

## 工作流程

1. 擷取教材文體、主題、場景、情緒與主要能力目標。
2. 判斷本課角色應承擔的功能。
3. 搜尋 Role Library 中符合條件的角色。
4. 對候選角色評分並排序。
5. 產生 3 至 5 個候選方案。
6. 每個方案列出：
   - 推薦理由
   - 適合出現的段落
   - 可使用的引導功能
   - 可能限制
7. 必須包含「不使用固定角色」選項。
8. 若 Bee 老師適合，可列入推薦；即使未列入前三名，教師仍可改選 Bee 老師。
9. 停下等待教師選擇。

## 推薦原則

- 角色選擇以教材內容為優先。
- 同一文體不必固定同一角色。
- 角色不得取代課文人物。
- 角色應支援教學活動，不只是裝飾。
- 角色功能比角色造型優先。
- 不因使用者曾選過某角色，就自動沿用到下一課。
- 若教材本身人物非常鮮明，可推薦降低主持角色出現頻率。

## Bee 老師規則

Bee 老師的角色資料位於：

`libraries/roles/bee-teacher/role.md`

Bee 老師可以：

- 作為通用教師主持人；
- 在角色推薦結果合適時被推薦；
- 由教師直接覆寫選用；
- 與教材情境角色分工，但預設仍只保留一名主要引導角色。

不得因名稱 Bee 自動將她設計成蜜蜂或昆蟲人物。

## 標準輸出

`working/role-recommendation.md`

內容至少包含：

```yaml
role_recommendation:
  lesson_id: ""
  status: ready_for_teacher_review
  content_summary:
    genre: ""
    topic: ""
    emotional_tone: []
    learning_goals: []
  recommendations: []
  teacher_options:
    - choose_recommended
    - choose_bee_teacher
    - choose_other_role
    - no_role
```

## 停等關卡

教師必須確認：

- 主要角色
- 角色功能
- 使用頻率
- 是否製作角色基準圖
- 是否沿用 Bee 老師初版視覺 DNA，或另行修改

未確認前不得進入角色圖像生成與最終視覺定稿。
