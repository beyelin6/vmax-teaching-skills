# V-MAX Runtime State Contract 2.0

## 定位

本檔不再保存任何單一課程的即時狀態。

V-MAX 的正式分工：

- GitHub：保存 Runtime schema、欄位規格、讀寫規則與平台 Adapter。
- Google Drive：保存每一課實際、持續變動的 Runtime State。

不得把每次 HOLD、stage 前進、Teacher Intent 鎖定都當成 GitHub commit。

---

## Google Drive Runtime Root

正式 Runtime 根目錄：

- Folder name: `00_Runtime_State`
- Folder ID: `1AOjYwALGVNWu99b-SnjBUSALEDrlReMt`
- Parent: `V-MAX 教材庫`

正式 Index：

- `V-MAX_Runtime_Index`
- Document ID: `1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ`

---

## 每課 State 命名

```text
V-MAX_State_{冊別}_{課次}_{課名}
```

例如：

`V-MAX_State_四上_第一課_水陸小高手`

每課必須獨立存在，不得用第二課覆蓋第一課。

---

## 最低欄位

```yaml
runtime_schema_version: 2.0
storage: GOOGLE_DRIVE
lesson_id:
workflow_version:
lesson:
  grade_volume:
  lesson_number:
  title:
source:
  library_mode:
  source_status:
  source_file:
state:
  current_stage:
  last_completed_stage:
  teacher_confirmation_status:
  next_allowed_stage: []
  forbidden_next: []
locked_decisions: {}
runtime_rules:
  single_stage_advance: true
  teacher_confirmation_advances_one_stage_only: true
  legacy_stage_aliases_forbidden: true
  model_memory_cannot_override_runtime: true
notes: []
```

---

## 啟動與續跑

1. 先讀 `V-MAX_Runtime_Index`。
2. 依教師指定課次找到對應 State；若教師說「繼續目前這課」，才使用 Index 的 active lesson。
3. 讀取該課 `current_stage / next_allowed_stage / locked_decisions`。
4. 只執行合法下一階段。
5. 每次 HOLD 確認或正式 stage 完成後，回寫該課 Google Drive State。
6. 必要時同步更新 Runtime Index 的 active lesson 與狀態摘要。

若 Drive Runtime 無法讀取，標記 `RUNTIME_DRIVE_BLOCKED`；不得以 GitHub 範例狀態、模型記憶或舊對話猜測目前進度。

---

## 核心金句

> GitHub 保存規則；Google Drive 保存每一課現在真正跑到哪裡。

> 課程狀態會一直變，不應讓 GitHub commit history 變成課堂操作日誌。
