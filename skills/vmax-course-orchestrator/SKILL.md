---
name: vmax-course-orchestrator
description: 管理 V-MAX 單課教材專案的完整工作流、三種工作模式、狀態、必要檔案、教師核准關卡與下一個可執行技能。適用於寒暑假整課基準教材製作、學期中局部增修、實際上課版本切換，以及 Transcriber、LKB Builder、Learning Module Builder、Decision Engine、Teaching Strategy Builder、Digital Interaction Planner、Role Recommender、Style Recommender 與 Presentation Engine 的流程協調。不得代替各專業技能產生內容。
---

# V-MAX Course Orchestrator

版本：0.3.0

## 使命

作為單課專案的流程總控，確保每個技能只在前置條件完成且教師核准後執行，並支援「寒暑假完成整課教材、學期中局部增修、上課前快速切換版本」的實際教師工作流程。

Orchestrator 不產生教材內容；它只負責：

- 建立課程專案骨架
- 選擇與記錄工作模式
- 讀取與更新專案狀態
- 檢查必要輸入與核准紀錄
- 指定下一個可執行技能
- 阻止跳過教師確認
- 記錄版本、錯誤、退回與重新生成
- 管理 Baseline、Patch 與 Classroom Variant 的關係
- 確保先決定 Learning Path 與 Teaching Flow，再進入呈現設計

## 唯一狀態檔

每課必須有：

`project/project-status.md`

所有技能執行前先讀取此檔，完成後回寫自身階段結果。不得只依聊天記憶判斷進度。

## 三種工作模式

### 1. `full_lesson_build`

寒暑假整課製作模式。從教材來源開始，完成可直接上課的 Baseline Lesson Package，包括：

- Official Knowledge
- Lesson Knowledge Book
- Learning Modules
- Learning Path 與 Teaching Flow
- Teaching Strategy
- Digital Interaction 與紙本替代
- 角色與風格
- 完整簡報、講者備註、學習單及評量

完成後建立 Baseline Version，例如 `1.0.0`。

### 2. `adaptive_patch`

學期中局部增修模式。必須以已核准的 Baseline 或 Classroom Variant 為基礎，只修改受影響的範圍。

Patch 類型：

- `add_on`：新增補充頁、活動或特殊任務
- `replace`：替換指定頁面、活動或教學模組
- `reflow`：保留主要內容，重新安排時間、順序或教學節奏

Patch 不得直接覆蓋 Baseline 原檔，必須建立 Patch Profile、影響分析與新版本。

### 3. `classroom_variant`

依實際上課條件建立本次使用版本，例如：

- 標準版
- 快速版
- 高互動版
- 公開觀課版
- 複習版
- 無平板版
- 學習支援版
- 進階挑戰版

Classroom Variant 應引用 Baseline 與已核准 Patch，不重做官方教材知識與 LKB。

## Baseline、Patch、Variant 關係

```text
Lesson Knowledge Book
        ↓
Baseline Lesson Package
        ↓
Adaptive Patch Layer
        ↓
Classroom Variant
        ↓
Presentation／Tablet／Worksheet／Assessment
```

- Baseline 是寒暑假完成的完整整課基準教材。
- Patch 是針對特定原因的可追蹤增修，不取代 Baseline。
- Classroom Variant 是某次實際上課採用的組合版本。
- 修改官方教材知識時，不能只建立 Patch，必須回到上游更新 LKB 與 Baseline。

## `full_lesson_build` 標準工作流

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
31. `baseline_completed`

若本課不使用平板或數位互動，仍需建立 Digital Interaction Profile，將模式標記為 `no_device` 或 `not_required`。

## `adaptive_patch` 工作流

1. `patch_requested`
2. `patch_scope_analysis_in_progress`
3. `ready_for_patch_scope_review`
4. `approved_patch_scope`
5. `patch_generation_in_progress`
6. `ready_for_patch_review`
7. `approved_patch`
8. `patched_outputs_generation_in_progress`
9. `ready_for_patched_output_review`
10. `patch_completed`

Patch 開始前必須確認：

- `based_on_version`
- 修改原因
- 修改範圍
- Patch 類型
- 是否影響 LKB、Learning Modules、Teaching Flow、Role、Style 或 Presentation
- 是否需要新的平板活動或紙本替代

## `classroom_variant` 工作流

1. `variant_requested`
2. `variant_conditions_registered`
3. `variant_reflow_in_progress`
4. `ready_for_variant_review`
5. `approved_variant`
6. `variant_outputs_generation_in_progress`
7. `ready_for_variant_output_review`
8. `variant_completed`

Classroom Variant 必須記錄：

- 所引用的 Baseline Version
- 所套用的 Patch IDs
- 教學模式
- 實際時間
- 平板環境
- 支援或挑戰對象
- 本次上課採用的 Presentation Version

## 技能路由

### Full Lesson Build

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

### Adaptive Patch

Patch 先由 Orchestrator 執行影響分析，再依實際影響路由到：

- `learning-module-builder`
- `vmax-decision-engine`
- `teaching-strategy-builder`
- `digital-interaction-planner`
- `role-recommender`
- `style-recommender`
- `presentation-engine`

不得為了新增一個補充活動而無條件重跑整套流程。

### Classroom Variant

優先讀取已核准的 Baseline、Patch Profile、Teaching Flow 與 Output Manifest，再由 Decision Engine 或 Teaching Strategy Builder進行有限度重排，最後交由 Presentation Engine 產生本次使用版本。

## 核准關卡

`full_lesson_build` 不得跳過：

- Official Knowledge Review
- LKB Review
- Learning Modules Review
- Learning Path and Teaching Flow Review
- Teaching Strategy Review
- Digital Interaction Review
- Role Review
- Style Review
- Output Profile Review
- Baseline Final Review

`adaptive_patch` 不得跳過：

- Patch Scope Review
- Patch Content Review
- Patched Output Review

`classroom_variant` 不得跳過：

- Variant Review
- Variant Output Review

## 版本規則

- `1.0.0`：首個寒暑假完整 Baseline
- `1.1.0`：新增教學延伸、特殊任務或新的 Learning Module
- `1.1.1`：修正文句、答案、連結或版面小錯誤
- `2.0.0`：官方教材知識、LKB、整體課程結構或主要教學路徑大幅改變

必須同時記錄：

- `baseline_version`
- `active_classroom_version`
- `source_lkb_version`
- `applied_patch_ids`

## 退回與影響規則

- 修改 Official Knowledge：LKB、Baseline 與全部 Patch／Variant 都需重新檢查。
- 修改 LKB：Learning Modules、Baseline 與全部下游成果 stale。
- 修改 Learning Modules：Decision Plan、Teaching Strategy、Baseline Presentation 與相關 Patch／Variant stale。
- 修改 Learning Path 或 Teaching Flow：Teaching Strategy、Digital Interaction、Role、Style 與 Presentation stale。
- 修改 Teaching Strategy：Digital Interaction、Role、Style 與 Presentation 需重新檢查。
- 修改 Digital Interaction：Presentation stale；若改變角色功能或畫面需求，Role、Style 也需重新檢查。
- 修改 Role：Style 與 Presentation stale。
- 修改 Style：Presentation stale。
- 只修改 Output Profile：不影響上游知識、路徑與策略。
- Patch 只影響其 Profile 所列範圍；不可默認全部下游成果 stale。
- Classroom Variant 不得回寫或覆蓋 Baseline。

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
- Patch 沒有 `based_on_version`
- Patch 直接覆蓋 Baseline
- Classroom Variant 沒有記錄 Baseline 與 Patch 來源

## 完成條件

### Baseline 完成

- 所有核准關卡完成
- 最終輸出通過驗證
- Output Manifest 可追溯所有來源版本
- 投影片與學習單符合核准的 Teaching Flow
- 平板活動均有實際連結或標記 `LINK_PENDING`，並提供替代方案
- 教師完成 Baseline Final Review

狀態設為 `baseline_completed`。

### Patch 完成

- Patch Profile、影響分析與版本更新完整
- 修改內容與 Baseline 的差異可追溯
- Patched Output 通過教師核准

狀態設為 `patch_completed`。

### Classroom Variant 完成

- Variant Profile 記錄實際課堂條件
- 可追溯 Baseline 與所有 Patch
- 本次輸出通過教師核准

狀態設為 `variant_completed`。
