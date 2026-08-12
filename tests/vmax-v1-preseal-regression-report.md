# V-MAX v1 Pre-seal Regression Report

版本：1.0-draft
日期：2026-08-12
分支：`feature/vmax-v1-system-architecture`

## 結論

```yaml
static_contract_regression: PASS
three_lesson_tabletop_recheck: PASS
asset_persistence_regression: PASS_LIVE_DRIVE
production_mode_regression: PASS
rollback_versioning_regression: PASS_LIVE_DRIVE
live_runtime_migration_rerun: PASS_TO_LEGAL_LKB_REVIEW_CHECKPOINT
illegal_stage_jump_detected: false
v1_sealed: false
remaining_teacher_checkpoint: LKB_REVIEW
```

本輪目的不是把第一課偷偷跑到 Renderer，而是驗證新版架構能在真實 GitHub + Google Drive 環境中：
1. 正確分流 SINGLE / BATCH。
2. 保存所有可續跑資產。
3. 不覆蓋舊版。
4. rollback 只切 active ref。
5. legacy Runtime 能非破壞遷移到 Runtime 2.7，並在最早不確定依賴停下等待教師確認。

---

## A. Static Contract Recheck｜PASS

對齊版本：
- Main Workflow `2.6-draft`
- Golden Path Executor `1.8-draft`
- Runtime State Contract `2.7-draft`
- Production Mode Policy `1.0-draft`
- Google Drive Asset Authority `1.0-draft`
- Lesson Upgrade Lifecycle `1.0-draft`
- Integration Regression Cases `1.3-draft`

確認：
- Shared front path 到 `CHARACTER LOCK` 後才依 production_mode 分流。
- SINGLE 路徑保持 `Slide Architecture → Page Ledger → Storyboard → Style Recipe → Lesson Skin Final → Typography → Gate B → Representative → Gate C`。
- BATCH 路徑允許 `VISUAL SEED LOCK → Identity Pack SEED_LOCKED → PRESTUDY / SHORT_READ → safe stop`。
- `lesson_skin_seed != lesson_skin_final`。
- Save-on-Approval / Save-on-Interrupt 為硬規則。
- `_vNN` / explicit pin / newest != active / pointer-only rollback 已接入 Main Workflow、Executor、Runtime。
- Mandatory HOLD、Scenario Lock、Character Lock 未被三個 Macro Gates 刪除。

R1–R19 舊整合案例在新分流下重新檢查，未發現 authority / ordering regression。

---

## B. Three-Lesson Tabletop Recheck｜PASS

### L09〈請到我的家鄉來〉
仍走說明／描述文本所需的 COMPARE / INFER / STRUCTURE / TRANSFER；SCALE / CAUSE ARROW 等只作 visual tools。Production Mode 只改 checkpoint，不改教學技能選擇。

### L11〈兔子先生等等我〉
仍以 STAGE / PROBLEM_LOOP 為主要技能；SOURCE_WORLD 合法；SCALE 只在大小影響理解時使用。

### L12〈老鞋匠和小精靈〉
仍以 STORY_ARC / CHARACTER_EVIDENCE / TRANSFER 為主；不因新 Production Mode 套用固定模板。

結論：雙模式沒有把不同文體重新壓成同一套頁面流程。

---

## C. Asset Persistence Regression｜PASS_LIVE_DRIVE

實際 Drive sandbox：
`00_V-MAX_角色與視覺資產庫/99_System_Regression_Sandbox`
folder_id: `1d2HwIXvJNq_1o1ZlauwjN91vzAQ2Ehlf`

已實際建立並重新 list 驗證：
- `REG_identity_seed_v01`
- `REG_character_asset_v01`
- `REG_character_asset_v02`
- `REG_prestudy_v01`
- `REG_short_read_v01`
- Runtime test versions
- SINGLE final identity / derivatives

結果：
- APPROVED / LOCKED / USABLE_WIP 可實際落地 Google Drive。
- Identity Seed、Prestudy、Short Read 可在無完整簡報時持久化。
- Drive reference 可重新讀取。

R23：PASS。

---

## D. BATCH_PREP_BUILD Regression｜PASS_LIVE_DRIVE

實體鏈：

```text
REG_identity_seed_v01
  identity_pack_status: SEED_LOCKED
  character_ref: ROLE-BEE-001@v01
→ REG_prestudy_v01
→ REG_short_read_v01
→ Drive list verification
```

確認：
- 不需 Gate B / Gate C 才能生成／保存 PRESTUDY、SHORT_READ。
- Seed 明確保存角色版本、Style family seed、Book DNA、Typography base。
- 可安全停車，不需要重新猜 identity。

R21：PASS。

---

## E. SINGLE_LESSON_BUILD Derivative Lineage｜PASS_LIVE_DRIVE

建立：
- `REG_identity_final_v01`：FINAL_LOCKED
- `REG_teaching_slides_v01`：實際 Google Slides
- `REG_slide_detail_v01`
- `REG_notebooklm_visual_yaml_v01`
- `REG_prestudy_single_v01`
- `REG_short_read_single_v01`
- `REG_question_bank_v01`

所有 derivative 均明確引用同一 Identity Pack：
`1mXMd1QbqY2KIPHwqnitS3QhusPbHovXrc59zfUwFXog`

NotebookLM 測試檔明確標記 adapter output，不是 source of truth。

結果：SINGLE 的「正式簡報母體 → 詳細說明 / NotebookLM / 學習單 / 題庫」可保持同一 visual identity lineage。

R20：PASS。

---

## F. Never-overwrite / Rollback Regression｜PASS_LIVE_DRIVE

實體資產：
- `REG_character_asset_v01` id `1hrLkBy2i7wUe2ODjYwRLAL6319xuKPq-D7F05De9Sww`
- `REG_character_asset_v02` id `1D8tuAcAxqs3eiLvl3B3tUNTEgKJkk0RGo-xKsUA6w_k`

兩個版本同時存在。

Runtime pointer test：
1. `REG_runtime_state_v01` → active v01
2. `REG_runtime_state_v02` → active v02
3. `REG_runtime_state_v03_rollback` → active ref 回 v01

回退後 v01 / v02 均仍存在，未刪、未覆蓋、未重新生成。

結果：
- R24 Never Overwrite：PASS
- R25 Newest Is Not Active：PASS
- R26 Rollback Is Pointer Change：PASS
- R27 explicit pin / 24-month review lifecycle：PASS_STATIC_CONTRACT

---

## G. Live Runtime Migration Rerun｜PASS_TO_LEGAL_LKB_REVIEW_CHECKPOINT

Legacy active state：
- title: `V-MAX_State_四上_第一課_水陸小高手_02`
- document id: `1LQr1ZKEPk3ZHYW9vNISyggPY5L6Rzt994pl7V5TQQto`
- Runtime schema 2.1 / Workflow 2.0 / Manifest 2.5 / Executor 1.2

新 state：
- title: `V-MAX_State_四上_第一課_水陸小高手_03`
- document id: `1dNPyZfoHn-9L3jG5Cl_BPutuOxw3GCjei2TK0Im2z-Q`
- Runtime schema 2.7 / Workflow 2.6 / Executor 1.8
- production_mode: SINGLE_LESSON_BUILD
- migration_method: NON_DESTRUCTIVE_REBASE
- current_stage: `LKB_REVIEW`
- renderer: BLOCKED

新 Runtime Index：
- title: `V-MAX_Runtime_Index_v02`
- document id: `1bC3m1Y-hX1rP75-UGiEv_gH_FwwP0b9eQam0zKgH4Vw`
- active runtime: `_03`
- previous index preserved: `1q4vgqiRFbrvcMeZ7B102rY_kZVF7Z4LcqR8iL8vPKmQ`

### Migration LKB assets
正式新工作區：
`四上康軒國語/03_分課教學簡報與教材/01_第一課_水陸小高手/01_教材整理`

已建立：
- `L01_01_official-knowledge_migration_v01`
- `L01_source-map_migration_v01`
- `L01_official-knowledge-validation_migration_v01`
- `L01_02_teacher-knowledge_migration_v01`
- `L01_lesson-knowledge-book_v01`
- `L01_lkb-validation-report_v01`

LKB 狀態：`READY_FOR_LKB_REVIEW`。

### Why not FULL_RENDERER
新 v1 最早的不確定依賴是 canonical LKB approval。舊 `_02` 雖有 Source Truth、Teacher Intent、Scenario、Character、Style 等已確認證據，但：
- 沒有新版 canonical `approved_lkb`
- 沒有新版 Teaching Skill Selection Lock / Budget Draft / Gate A
- 小澄主播沒有核准 canonical Drive image asset
- 舊 Style 沒走新版 Style Recipe → Lesson Skin Final → Typography → Gate B
- 舊 Representative samples 未落 Drive，不能算 Gate C

因此 `_03` 正確停在 LKB_REVIEW，這是預期 PASS，不是失敗。

---

## H. Pre-seal Status

```yaml
technical_regressions:
  static: PASS
  three_lesson: PASS
  asset_persistence: PASS
  production_modes: PASS
  rollback: PASS
  live_runtime_migration: PASS_TO_LEGAL_CHECKPOINT
remaining:
  - teacher_confirm_migration_lkb_v01
  - after_confirmation_verify_one_legal_transition_into_new_teaching_direction_chain
  - teacher_final_v1_seal_approval
```

## 核心判定

> V-MAX v1 已通過技術 pre-seal；現在不是缺新架構，而是刻意停在真實 Teacher Interface 的 LKB Review。

> 若教師核准 migration LKB v01，下一個合法動作是：新版 Teaching Skill Selection → Lesson Budget Draft → Gate A；不得飛到舊 `_02` 的 FULL_RENDERER。
