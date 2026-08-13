---
name: vmax-course-orchestrator
description: 管理 V-MAX 單課教材專案的完整工作流、工作模式、狀態、教師核准關卡與下一個可執行技能。支援寒暑假整課基準教材、學期中增修、一般課堂版本，以及平板公開課四學模式。不得代替各專業技能產生內容。
---

# V-MAX Course Orchestrator

版本：0.4.0

## 使命

作為單課專案流程總控，確保每個技能只在前置條件完成且教師核准後執行，並支援：

- 寒暑假完成整課 Baseline
- 學期中 Adaptive Patch
- 上課前 Classroom Variant
- 平板公開課 `open_class_four_learning`

Orchestrator 不產生教材內容；只負責建立專案骨架、記錄狀態、檢查前置條件、指定下一技能、管理版本與阻止不必要的重跑。

## 狀態權威與本機鏡像

每課工作目錄可維護：

`project/project-status.md`

此檔是本機工作鏡像與 handoff，不是跨平台唯一權威。跨 ChatGPT、Codex、Gemini 續跑時，以 Manifest 指定的 Google Drive 該課 Runtime State 為準；讀取後同步到本機檔，完成 HOLD 或 stage 後先回寫 Drive。Drive 無法讀取時標記 `RUNTIME_DRIVE_BLOCKED`，不得用本機舊檔猜測進度。

## 三種主要工作模式

### 1. `full_lesson_build`

寒暑假完成可直接上課的 Baseline Lesson Package。

核心成果：

- Official Knowledge
- Lesson Knowledge Book
- Learning Modules
- Learning Path 與 Teaching Flow
- Teaching Strategy
- Digital Interaction 與替代方案
- Role／Theme／Visual
- 完整簡報與教師備註
- 預習單與短文創作單可接續完成

### 2. `adaptive_patch`

依學生反應或特殊任務進行局部增修：

- `add_on`
- `replace`
- `reflow`

Patch 不得直接覆蓋 Baseline。

### 3. `classroom_variant`

依實際課堂條件組合 Baseline 與 Patch，可建立：

- `standard`
- `quick`
- `high_interaction`
- `open_class`
- `open_class_four_learning`
- `review`
- `no_device`
- `support`
- `challenge`

## `open_class_four_learning`

此模式是 Classroom Variant 的特殊公開課版本，只在教師需要四學公開觀課時啟用，不反向要求日常課程採四學。

必須讀取：

- `schemas/classroom-variant-profile.md`
- `schemas/four-learning-open-class-profile.md`
- `libraries/digital-platforms/four-learning-open-class.md`
- `skills/four-learning-open-class-planner/SKILL.md`
- 已核准 Digital Interaction Profile

工作流：

```text
Baseline／既有 Classroom Variant
        ↓
確認公開課核心學習目標
        ↓
Four Learning Open Class Planner
        ↓
學生自學
→ 組內共學
→ 組間互學
→ 教師導學
        ↓
Digital Interaction Planner 平台映射
        ↓
學習證據與備案檢查
        ↓
Presentation Engine 產生公開課圖片式簡報
        ↓
教師核准
```

### 四學完成條件

觀課者必須能看見：

1. 學生自學：個人思考與原始產出。
2. 組內共學：比較、理由、修正或共識。
3. 組間互學：跨組差異、回應、補充或互評。
4. 教師導學：明確引用前三階段學生證據進行統整或澄清。
5. 導學後有二次作答、修正或 Exit Ticket。

四學不得被僵化為固定分鐘數。

### 五大學習平台候選

- 學習吧
- 因材網
- 均一教育平台
- PaGamO
- Cool English

規則：

- 五大平台是候選平台庫，不代表一堂課五個都要用。
- 先設計平台中立任務，再選平台。
- 國語課不為湊平台而硬塞 Cool English。
- 不確定平台當前功能時，標記 `PLATFORM_CAPABILITY_CHECK_REQUIRED`。
- 平台必須能提升蒐集、互動、回饋、差異化或學習證據價值。

### 公開課的 V-MAX 視覺要求

公開課不得退回純文字 PPT。

必須保留：

- Theme／Visual DNA
- Guided Narrative Layer
- Bee 老師或核准引導者
- 圖像化理解
- 適量 Meaningful Quote
- 原有 Lesson Flow

Bee 老師可依四學切換角色：

- 自學：`ROLE-COACH`
- 共學：合作提醒者
- 互學：比較主持者
- 導學：統整與金句提示者

## Full Lesson Build 標準流程

```text
sources_registered
→ official_knowledge
→ LKB
→ Learning Modules
→ Decision Engine
→ Learning Path／Teaching Flow
→ Teaching Strategy
→ Digital Interaction
→ Role
→ Style／Theme
→ Output Profile
→ Presentation
→ Final Review
→ baseline_completed
```

重要階段仍需教師核准；開學快速模式可依 `references/back-to-school-fast-track.md` 合併確認點。

## Adaptive Patch

Patch 開始前確認：

- `based_on_version`
- 修改原因
- 修改範圍
- Patch 類型
- 是否影響 LKB、Learning Modules、Teaching Flow、Role、Style、Presentation、Worksheet、Podcast 或 Digital Interaction

不得為了新增一頁補充內容而無條件重跑整套流程。

## Classroom Variant

必須記錄：

- Baseline Version
- Patch IDs
- Teaching Mode
- 實際時間
- 平板環境
- 支援／挑戰需求
- Presentation Version

若 `teaching_mode: open_class_four_learning`，另外建立：

`planning/four-learning-open-class-profile.md`

並路由至 `four-learning-open-class-planner`。

## 技能路由

### Full Lesson Build

| 當前成果 | 下一技能 |
|---|---|
| 已登記教材來源 | `chinese-textbook-transcriber` |
| Official Knowledge 核准 | `chinese-lesson-knowledge-builder` |
| LKB 核准 | `learning-module-builder` |
| Learning Modules 核准 | `vmax-decision-engine` |
| Learning Path／Flow 核准 | `teaching-strategy-builder` |
| Teaching Strategy 核准 | `digital-interaction-planner` |
| Digital Interaction 核准 | `role-recommender` |
| Role 核准 | `style-recommender` |
| Style 核准 | Output Profile |
| Output Profile 核准 | `presentation-engine` |

### Classroom Variant

- 一般 Variant：Decision Engine／Teaching Strategy Builder → Presentation Engine
- `open_class_four_learning`：`four-learning-open-class-planner` → `digital-interaction-planner` → Presentation Engine

## 版本與影響規則

- `1.0.0`：首個完整 Baseline
- `1.1.0`：新增延伸、特殊任務或 Learning Module
- `1.1.1`：文字、答案、連結、版面小修正
- `2.0.0`：官方教材、LKB 或主要課程結構大幅改變

修改上游知識時，下游成果必須重新檢查；Patch 只影響其 Profile 所列範圍；Classroom Variant 永遠不得回寫 Baseline。

## 錯誤處理

遇到以下情況設為 `blocked`：

- 前置成果未核准
- 官方內容被未標示改寫
- 學生版出現教師答案
- 平板活動沒有替代方案
- 未核准 Role／Style 即生成
- Presentation Engine 反向修改 Teaching Flow
- Patch 無 `based_on_version`
- Variant 無 Baseline 來源
- 公開課為了形式硬湊四學
- 公開課為了展示硬塞平台
- 教師導學沒有引用學生證據
- 平台功能未確認卻被虛構

## 完成條件

### Baseline

所有必要成果可追溯且通過教師 Final Review，狀態：`baseline_completed`。

### Patch

差異可追溯且通過教師核准，狀態：`patch_completed`。

### Classroom Variant

可追溯 Baseline／Patch 並通過教師核准，狀態：`variant_completed`。

### Four Learning Open Class Variant

除一般 Variant 條件外，必須通過：

- 四學完整性
- 學習證據鏈
- 平台學習價值
- 教師數據／證據導學
- 無裝置與網路備案
- V-MAX Theme／Visual／Guide Character 一致性
