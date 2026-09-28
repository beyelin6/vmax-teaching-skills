# V-MAX Runtime State Contract 2.6

## 定位

本檔不保存任何單一課程的即時狀態。

V-MAX 的正式分工：

- GitHub：保存 Runtime schema、欄位規格、讀寫規則與平台 Adapter。
- 每課綁定的正式後端：保存實際 Runtime；Drive 預設，LOCAL／HANDOFF 依 `core/governance/portable-runtime-policy.md`。

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

## 可攜儲存欄位

依 `core/governance/portable-runtime-policy.md` 保存 storage_binding 與 spec_snapshot；下列原欄位完整保留。舊 Drive State 可依核驗 ID／revision 補記 binding，不撤銷原核准。

## 最低欄位

```yaml
runtime_schema_version: 2.6
storage: GOOGLE_DRIVE # LOCAL | HANDOFF 依 portable-runtime-policy
lesson_id:
workflow_version:
workflow_mode: CHINESE_VISUAL_PRESENTATION # 或 DETAILED_LESSON
lesson:
  grade_volume:
  lesson_number:
  title:
source:
  library_mode:
  source_status:
  source_file:
state:
  current_stage: # 國語簡報使用 VP1–VP5 stage ID，詳見整合工作流
  stage_status: WORKING # WORKING | WAITING_REVIEW | BLOCKED | COMPLETE
  last_completed_stage:
  teacher_confirmation_status:
  next_allowed_stage: []
  forbidden_next: []
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
runtime_rules:
  single_stage_advance: true
  teacher_confirmation_advances_one_stage_only: true
  legacy_stage_aliases_forbidden: true
  model_memory_cannot_override_runtime: true
  continuation_state_sync_required: true
  teacher_decision_must_be_persisted_before_advance: true
  candidate_outputs_do_not_advance_stage: true
  canvas_ratio_locked_before_render: true
  asset_ratio_must_not_stretch: true
  output_profile_conflict_blocks_render: true
output_profile:
  product: TEACHER_IMAGE_SLIDE
  canvas_profile: lesson_presentation_16_9_v1 | lesson_presentation_4_3_v1
  canvas_ratio: 16:9 | 4:3
  width_px:
  height_px:
  orientation: LANDSCAPE
  safe_area: locked_reference
  fit_mode: PRESERVE_ASPECT_CONTAIN_OR_APPROVED_CROP
  output_formats: [PNG, PDF]
  pptx_requested_by_teacher: false
  teacher_decision_ref:
  status: LOCKED | WAITING_TEACHER | BLOCKED
continuation:
  state_sync_status: PASS | BLOCKED | CONFLICT
  runtime_revision:
  last_sync_receipt:
  active_work_item:
  pending_teacher_decision:
  source_master_version:
  slide_script_version:
  visual_benchmark_version:
  role_style_version:
  candidate_outputs: []
  conflicts: []
  downstream_impact: []
review_package_ref: null
review_package_revision: null
approval_scope: [] # artifact ref、revision、item IDs、教師事件，不可用一個全域 true
internal_work_items: [] # 同一大階段內待做／完成項；非額外 HOLD
course_master_ref: null
product_branches: {} # 各產物 source_artifact_refs、revision、status、review_ref、resume_stage
migration_ref: null
notes: []
```

`step2_6_idiom_expression` 若本課無需成語處理，應寫入 `N/A_NO_IDIOM`，不得留空後默默跳過。

---

## 合法前段狀態鏈

國語簡報 stage 使用 `core/governance/chinese-visual-presentation-workflow.md` 的 VP1–VP5 與 VP_COMPLETE 表。以下細分狀態鏈只適用 DETAILED_LESSON；小步結果保存在 internal_work_items。舊課依核准證據作非破壞性映射，不重置已確認頁面。

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
→ HOLD_2_6
→ HOLD_2_6 confirmed
→ TEACHER_INTENT_LOCK
```

---

## 啟動與續跑

1. 先依可攜政策讀取正式後端 Index；新課查無既有紀錄才初始化。
2. 依教師指定課次找到對應 State；若教師說「繼續目前這課」，才使用 Index 的 active lesson。
3. 讀取該課 `current_stage / next_allowed_stage / locked_decisions / language_focus`。
4. 讀取並通過 `core/governance/continuation-state-gate.md` 的 State Sync；未通過時不得執行下一階段或開始製作。
5. 目前階段尚未完成時，繼續其已授權工作；跨階段時才使用唯一 next_allowed_stage。
6. 每次 HOLD 確認或正式 stage 完成後，先回寫該課正式後端 State，再允許派生下游。
7. 每完成 stage、建立 HOLD 或完成 HOLD 決策，都非破壞性更新 Runtime Index 的該課狀態摘要與 State revision 引用；active lesson 僅在教師指定切換課程時更新。

Drive 暫時不可讀時依可攜政策保存 pending branch，不換正式後端；LOCAL／HANDOFF 讀取其綁定版本。必要 State 真正不可取得才阻擋依賴它的續作，不以範例或記憶補值。

---

## 核心金句

> GitHub 保存規則；Google Drive 保存每一課現在真正跑到哪裡。

> 三、四年級生字深教聚焦可以寫進課程 State，但不能讓未聚焦的教材正式生字消失。

> 課程狀態會一直變，不應讓 GitHub commit history 變成課堂操作日誌。

## 簡報施工確認接續欄位

依 `core/governance/presentation-preconstruction-policy.md`，在該課 State 保存 `presentation_confirmation`：`source_master_ref`、`page_ledger_ref`、`style_matrix_ref`、`role_lock_ref`、`canvas_lock_ref`、`page_rules_ref`、`vocabulary_idiom_coverage_ref`、`page_detail_ref`／revision／status、`representative_family_approvals`、`current_batch`（id、page_ids、limit、batch_type、reason、status、approval_ref）、`previous_revision_ref`。引用須帶版本／hash；不存在的核准不得填 true。

`next_allowed_stage` 只控制跨階段，每次最多一個值；尚未允許跨階段時為空。空值不禁止目前 stage 的已授權工作：STEP1_INCOMPLETE 且來源可讀時繼續擷取。只有實際缺來源、未決裁定或工具失敗阻擋剩餘工作時才停，不能從空值推導停工。逐頁稿 pending、代表頁待逐類確認或批次待確認時，不得執行下游。每個 stage／HOLD 的候選與核准記錄分開保存，更新 State 與 Index 後回讀驗證；未驗證不可宣稱完成同步。
