# Learning Path and Teaching Flow Schema

本規格定義 Decision Engine 如何把核准的教材知識與 Learning Modules 組合成學習路徑，再安排成實際課堂節奏。

## Learning Path

Learning Path 是同一知識目標的教學順序，不是教材內容。

```yaml
learning_path:
  id: LP-IDIOM-CONTEXT-001
  title: 成語情境理解路徑
  target_nodes: []
  learning_goal: contextual_vocabulary
  grade_band: middle_elementary
  mode: blended
  estimated_minutes: 15
  modules:
    - official_definition
    - official_example
    - context_understanding
    - image_reasoning
    - life_connection
  digital_components: []
  paper_alternative: true
  rationale: ""
  risks: []
  teacher_approved: false
```

## 預設路徑類型

### 理解型

官方知識 → 例句 → 情境理解 → 生活連結

### 應用型

官方知識 → 情境辨析 → 造句或改寫 → 分享

### 探究型

圖片或問題 → 學生推測 → 找教材證據 → 官方說明 → 統整

### 平板互動型

任務說明 → 平板操作 → 即時結果 → 同儕比較 → 全班討論

### 複習評量型

快速回想 → 分類或判斷 → 錯誤診斷 → Exit Ticket

## Teaching Flow

Teaching Flow 是以分鐘為單位的課堂執行計畫，必須先於投影片頁數決策。

```yaml
teaching_flow:
  id: TF-G4S1-L02-01
  mode: standard
  total_minutes: 40
  tablet_activity_count: 1
  steps:
    - step_id: TF-01
      minutes: 5
      phase: motivation
      teacher_action: ""
      student_action: ""
      source_nodes: []
      learning_path_id: ""
      role_action: ""
      tablet_state: stored
      assessment: ""
      transition_note: ""
```

## tablet_state

- `stored`：平板收起。
- `prepare`：拿出並登入。
- `active`：正在操作。
- `share`：展示或討論結果。
- `close`：結束操作並收起。

## 教學模式

### standard｜標準版

依完整學習目標安排正常課堂節奏。

### quick｜快速版

適用剩餘時間不足；保留核心教材知識、單一主要練習與快速檢核。

### high_interaction｜高互動版

增加學生操作、討論與回應頻率，但不得犧牲官方教材重點。

### open_class｜公開觀課版

加強學習目標可視化、學生證據、合作任務、形成性評量與課末反思。

### review｜複習版

以提取、診斷、修正與遷移為主，不重複完整講述教材。

### no_device｜無裝置版

把所有數位活動轉為紙本、口頭、實體卡片或小白板替代方案。

## 強制規則

1. Presentation Engine 必須依 Teaching Flow 產生投影片，不能用固定頁數反推課堂。
2. 每一個主要活動都必須對應 LKB 節點或已核准 Learning Module。
3. 每節課原則上最多兩個主要平板活動。
4. 平板活動需計入拿取、登入、操作、提交與收回時間。
5. 每條 Learning Path 必須說明推薦理由、學習目標與可能限制。
6. 模式切換後必須重新計算時間、活動與輸出，不得只刪除投影片。
7. 教師確認前，Teaching Flow 狀態只能是 `ready_for_teacher_review`。
