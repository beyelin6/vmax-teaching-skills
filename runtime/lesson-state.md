# V-MAX Runtime State Contract 2.1

## 定位

本檔不保存任何單一課程的即時狀態。

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

每課必須獨立存在，不得用第二課覆蓋第一課。

---

## 最低欄位

```yaml
runtime_schema_version: 2.1
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
  execution_mode: FULL_GOLDEN_PATH | CHECKPOINT_RESUME
  current_stage:
  last_completed_stage:
  teacher_confirmation_status:
  next_allowed_stage: []
  forbidden_next: []
  resume_target_skill:
  resume_from_artifact:
locked_decisions:
  source_anchor:
  step2_teaching_value:
  step2_5_language_scope:
  step2_6_idiom_expression:
  teacher_intent:
  lesson_map:
  session_map:
  scenario:
  character:
  visual_style:
language_focus:
  grade_3_4_character_deep_focus:
    - SHAPE_NEAR
    - POLYPHONIC
  source_characters_complete: true
artifacts:
  available: []
  checkpoints:
    CP_SOURCE_ANCHOR:
    CP_TEACHING_ANALYSIS:
    CP_LESSON_CONTENT_MASTER:
    CP_PRESTUDY_INPUT:
    CP_VISUAL_INTENT:
    CP_SLIDE_SCRIPT:
    CP_RENDER_READY:
  latest_by_type: {}
runtime_rules:
  single_stage_advance: true
  teacher_confirmation_advances_one_stage_only: true
  legacy_stage_aliases_forbidden: true
  model_memory_cannot_override_runtime: true
  approved_artifacts_are_reusable: true
  upstream_recompute_without_need_forbidden: true
notes: []
```

`step2_6_idiom_expression` 若本課無需成語處理，應寫入 `N/A_NO_IDIOM`，不得留空後默默跳過。

---

## Artifact / Checkpoint Registry

Runtime State 除了記「跑到哪一站」，也必須記「哪些結果已經可直接再用」。

每一個 checkpoint 至少記錄：

```yaml
artifact_id:
artifact_type:
location:
approved_status:
approved_at_stage:
content_scope:
upstream_artifacts: []
downstream_eligible_skills: []
updated_at:
```

合法 checkpoint 與執行規則依 `core/governance/modular-checkpoint-execution-policy.md`。

Checkpoint 必須指向實際可讀檔案或 Drive 文件；不得只寫「已完成」而沒有內容位置。

---

## 合法前段狀態鏈

```text
STEP_1 → HOLD_1
STEP_2 → HOLD_2
STEP_2_5 → HOLD_2_5
STEP_2_6 → HOLD_2_6
TEACHER_INTENT_LOCK
```

若本課沒有需保留成語：

```text
HOLD_2_5 confirmed
→ STEP_2_6 = N/A_NO_IDIOM
→ TEACHER_INTENT_LOCK
```

---

## 啟動與續跑

### FULL_GOLDEN_PATH

1. 先讀 `V-MAX_Runtime_Index`。
2. 依教師指定課次找到對應 State；若教師說「繼續目前這課」，才使用 Index 的 active lesson。
3. 讀取該課 `current_stage / next_allowed_stage / locked_decisions / language_focus`。
4. 只執行合法下一階段。
5. 每次 HOLD 確認或正式 stage 完成後，回寫該課 Google Drive State。
6. 必要時同步更新 Runtime Index 的 active lesson 與狀態摘要。

### CHECKPOINT_RESUME

當教師指定某個技能、產物或既有紀錄檔時：

1. 解析 `target_skill / target_artifact / target_lessons`。
2. 讀取各課 `artifacts.checkpoints / latest_by_type`。
3. 驗證目標技能的 `minimum_checkpoint / required_fields`。
4. 若資料齊全，直接執行該技能，不重跑上游。
5. 若只缺少部分欄位，只補缺少部分。
6. 新產物完成後新增 artifact registry 紀錄，不得覆蓋原 checkpoint。
7. 若為多課 batch，各課獨立記錄結果與錯誤；單課失敗不得阻塞其他課。

若 Drive Runtime 無法讀取，標記 `RUNTIME_DRIVE_BLOCKED`；不得以 GitHub 範例狀態、模型記憶或舊對話猜測目前進度。

---

## 多課工作狀態

同一次請求可指定多個 lesson_id，例如一次處理 1–6 課預習單。

Batch controller 只保存批次摘要；每一課仍以自己的 Runtime State 為權威。

```yaml
batch_run:
  batch_id:
  target_skill:
  lessons: []
  per_lesson_status: {}
  completed: []
  incomplete: []
  failed: []
```

禁止建立一份共用 Runtime State 覆蓋六課的個別決策。

---

## 核心金句

> GitHub 保存規則；Google Drive 保存每一課現在真正跑到哪裡，以及哪些成果已經可以直接再用。

> 一課可以分很多次做；續跑時先找 checkpoint，不重算老師已經確認過的內容。

> 三、四年級生字深教聚焦可以寫進課程 State，但不能讓未聚焦的教材正式生字消失。

> 課程狀態會一直變，不應讓 GitHub commit history 變成課堂操作日誌。
