# Digital Interaction Learning Modules

版本：0.1.0

## 核心原則

- 平板互動是 Learning Module 的呈現方式，不是新的教材知識來源。
- 所有題目、成語、修辭、句型與課文內容都必須回溯 LKB 節點。
- 活動需有明確學習目標、操作步驟、回饋方式與離線替代方案。
- 不為了使用平板而增加無意義點擊。

## 模組索引

### 成語

- `DIGI-IDIOM-CONTEXT-001`：情境選擇，點選最符合成語的生活情境。
- `DIGI-IDIOM-MISUSE-002`：易誤用辨識，判斷句子並標記錯誤位置。
- `DIGI-IDIOM-SYNONYM-003`：近義辨析，拖曳成語到最適合的語境。
- `DIGI-IDIOM-IMAGE-004`：看圖判斷，選擇或排序符合成語的圖片。
- `DIGI-IDIOM-SENTENCE-005`：造句應用，輸入、錄音或重組句子。

### 修辭

- `DIGI-RHETORIC-HIGHLIGHT-011`：在課文中標示修辭線索。
- `DIGI-RHETORIC-MATCH-012`：將例句與修辭名稱配對。
- `DIGI-RHETORIC-REWRITE-013`：改寫句子並提交比較。

### 句型

- `DIGI-SENTENCE-ORDER-021`：拖曳重組句子。
- `DIGI-SENTENCE-COMPLETE-022`：補句與即時回饋。
- `DIGI-SENTENCE-RECORD-023`：口頭造句錄音。

### 課文理解

- `DIGI-TEXT-HIGHLIGHT-031`：標示課文證據。
- `DIGI-SEQUENCE-032`：事件排序。
- `DIGI-MINDMAP-033`：拖曳節點完成心智圖。
- `DIGI-DOK-RESPONSE-034`：短答或錄音回答 DOK 問題。

### 合作與評量

- `DIGI-COLLAB-BOARD-041`：小組共編便利貼或證據牆。
- `DIGI-PEER-REVIEW-042`：同儕檢核與回饋。
- `DIGI-EXIT-TICKET-043`：課末快速檢核。

## 每個模組必要欄位

```yaml
module:
  id: ""
  title: ""
  knowledge_type: ""
  source_nodes: []
  learning_goal: ""
  interaction_mode: ""
  device_mode: one_student_one_device
  estimated_minutes: 5
  student_instructions: ""
  teacher_instructions: ""
  feedback_mode: teacher_review
  answer_visibility: teacher_only
  platform_neutral_spec: ""
  offline_fallback: ""
  accessibility_notes: []
```

## 教學負荷限制

- 每節課原則上不超過兩個主要平板活動。
- 單一活動建議 3～10 分鐘。
- 長篇輸入不作為中年級的預設互動形式。
- 優先使用點選、拖曳、標示、排序、短答與錄音。
