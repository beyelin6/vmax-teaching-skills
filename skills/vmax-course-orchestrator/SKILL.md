---
name: vmax-course-orchestrator
description: 管理 V-MAX 單課教材專案的完整工作流、狀態、必要檔案、教師核准關卡與下一個可執行技能。適用於建立新課程專案、判斷目前階段、阻止跨關卡生成，並依序安排 Transcriber、LKB Builder、Learning Module Builder、Decision Engine、Teaching Strategy Builder、Digital Interaction Planner、Role Recommender、Style Recommender 與 Presentation Engine。不得代替各專業技能產生內容。
---

# V-MAX Course Orchestrator

版本：0.2.0

## 使命

作為單課專案的流程總控，確保每個技能只在前置條件完成且教師核准後執行。

Orchestrator 不產生教材內容；它只負責：

- 建立課程專案骨架
- 讀取與更新專案狀態
- 檢查必要輸入與核准紀錄
- 指定下一個可執行技能
- 阻止跳過教師確認
- 記錄版本、錯誤、退回與重新生成
- 確保先決定 Learning Path 與 Teaching Flow，再進入呈現設計

## 唯一狀態檔

每課必須有：

`project/project-status.md`

所有技能執行前先讀取此檔，完成後回寫自身階段結果。不得只依聊天記憶判斷進度。

## 標準工作流

1. `project_initialized`
2. `sources_registered`
3. `official_knowledge_in_progress`
4. `ready_for_official_knowledge_review`
5. `approved_official_knowledge`
6. `lkb_in_progress`
7. `ready_for_lkb_review`
8. `approved_lkb`
9. `learning_modules_in_progress`
10. `ready_for_learning_modules_review`
11. `approved_learning_modules`
12. `decision_planning_in_progress`
13. `ready_for_decision_review`
14. `approved_learning_path_and_flow`
15. `teaching_strategy_in_progress`
16. `ready_for_teaching_strategy_review`
17. `approved_teaching_strategy`
18. `digital_interaction_planning_in_progress`
19. `ready_for_digital_interaction_review`
20. `approved_digital_interaction`
21. `role_recommendation_in_progress`
22. `ready_for_role_review`
23. `approved_role`
24. `style_recommendation_in_progress`
25. `ready_for_style_review`
26. `approved_style`
27. `output_selection_pending`
28. `approved_output_profile`
29. `presentation_generation_in_progress`
30. `ready_for_final_review`
31. `completed`

若本課不使用平板或數位互動，仍需建立 Digital Interaction Profile，將模式標記為 `no_device` 或 `not_required`，再核准進入角色階段。

## 技能路由

| 當前狀態 | 下一技能 |
|---|---|
| `sources_registered` | `chinese-textbook-transcriber` |
| `approved_official_knowledge` | `chinese-lesson-knowledge-builder` |
| `approved_lkb` | `learning-module-builder` |
| `approved_learning_modules` | `vmax-decision-engine` |
| `approved_learning_path_and_flow` | `teaching-strategy-builder` |
| `approved_teaching_strategy` | `digital-interaction-planner` |
| `approved_digital_interaction` | `role-recommender` |
| `approved_role` | `style-recommender` |
| `approved_style` | 請教師選擇輸出格式 |
| `approved_output_profile` | `presentation-engine` |

## Decision Engine 的流程位置

Decision Engine 必須在 Teaching Strategy Builder 之前執行，負責提出：

- 2～4 條 Learning Path
- 1～3 組 Teaching Flow
- 教學模式建議
- 平板活動需求與紙本替代需求
- 角色功能需求
- 版型與視覺需求

教師核准其中一個方案後，Teaching Strategy Builder 才能把方案細化為可執行的課堂步驟。

Presentation Engine 不得反向決定教學節奏；投影片數量必須由已核准的 Teaching Flow 與策略需求推導。

## 核准關卡

以下關卡不得自動跳過：

- Official Knowledge Review
- LKB Review
- Learning Modules Review
- Learning Path and Teaching Flow Review
- Teaching Strategy Review
- Digital Interaction Review
- Role Review
- Style Review
- Output Profile Review
- Final Review

教師未明確核准時，Orchestrator 必須停止，不得啟動下一技能。

## 退回規則

教師修正某一層後，下游成果視情況標記為 stale：

- 修改 Official Knowledge：LKB 及所有下游成果全部 stale。
- 修改 LKB：Learning Modules 及所有下游成果 stale。
- 修改 Learning Modules：Decision Plan、Teaching Strategy 與所有下游成果 stale。
- 修改 Learning Path 或 Teaching Flow：Teaching Strategy、Digital Interaction、Role、Style 與 Presentation stale。
- 修改 Teaching Strategy：Digital Interaction、Role、Style 與 Presentation 需重新檢查。
- 修改 Digital Interaction：Presentation stale；若改變角色功能或畫面需求，Role、Style 也需重新檢查。
- 修改 Role：Style 與 Presentation stale。
- 修改 Style：Presentation stale。
- 只修改 Output Profile：不影響上游知識、路徑與策略。

不得直接修改派生輸出來取代上游修正。

## 錯誤處理

遇到以下情況時，狀態改為 `blocked` 並記錄原因：

- 必要檔案不存在
- 前置階段未核准
- 使用舊檔名而未完成遷移
- 發現跨課內容污染
- 官方內容被未標示改寫
- 學生版出現教師答案
- 未核准 Learning Path 或 Teaching Flow 就安排教學策略
- 未完成數位互動適配就生成平板活動頁
- 角色或風格尚未核准即開始生成
- Presentation Engine 反向改變已核准的教學時間與活動順序

## 完成條件

只有當：

- 所有核准關卡完成
- 最終輸出通過驗證
- Output Manifest 可追溯所有來源版本
- 投影片與學習單符合核准的 Teaching Flow
- 平板活動均有實際連結或標記 `LINK_PENDING`，並提供替代方案
- 教師完成 Final Review

狀態才能設為 `completed`。
