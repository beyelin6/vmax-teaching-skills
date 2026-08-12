# V-MAX Production Mode Policy 1.0-draft

## 定位

V-MAX 有兩種合法製作模式，共用同一套知識、角色、Style、Typography 與 Drive 資產權威，不建立第二套系統。

```yaml
production_mode:
  - SINGLE_LESSON_BUILD
  - BATCH_PREP_BUILD
```

---

## 1. SINGLE_LESSON_BUILD｜單課完整製作

適合：現在就要把一課完整備到可上課、可匯入 NotebookLM、可產出延伸教材。

流程：

```text
完整來源 / LKB / Teaching Direction
→ Scenario Lock
→ Character Lock
→ Knowledge Lab / Visual Grammar / Slide Architecture
→ Page Ledger / Storyboard
→ Style Recipe
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative Visual / Gate C
→ 正式簡報
→ Renderer Script / 簡報詳細說明
→ NotebookLM Source / Visual YAML
→ 預習單 / 短文單
→ 題庫 / Kahoot / 評量 / 其他附件
→ Drive 完整歸檔
```

原則：
- 正式簡報是本課最完整教學母體。
- 後續教材繼承同一 `Lesson Visual Identity Pack`，依 Material Mode 轉譯。
- NotebookLM YAML 是 adapter output，不是視覺真值。

---

## 2. BATCH_PREP_BUILD｜批次大量備課

適合：寒暑假一次處理多課，先把重點知識、角色／模式、預習單與短文單準備完成，正式簡報留到上課前再做。

每課流程：

```text
Source / LKB
→ Teaching Direction
→ Scenario Lock
→ Character Lock
→ VISUAL SEED LOCK
→ Lesson Visual Identity Pack = SEED_LOCKED
→ PRESTUDY / SHORT_READ production
→ BATCH_PREP_CHECKPOINT_COMPLETE
→ Drive persistence
```

批次模式不要求：
- 完整 Slide Architecture
- 精確 Page Ledger
- 完整 Storyboard
- Lesson Skin Final
- Gate B / Gate C
- 完整正式簡報

但不得省略 `VISUAL SEED LOCK`。

---

## 3. VISUAL SEED LOCK｜批次模式的視覺身分鎖

用途：讓預習單／短文單先生成，同時保證幾週或幾個月後正式簡報仍能找回「同一個角色、同一家族的風格」。

最低內容：

```yaml
visual_seed:
  status: SEED_LOCKED
  book_dna_ref:
  scenario_ref:
  character_refs:
    - role_id:
      asset_version:
      drive_asset_ref:
  style_family_seed_ref:
  style_reference_asset_ref:
  lesson_skin_seed:
    palette_direction:
    material_direction:
    motif_direction:
    illustration_tone:
  typography_base_ref:
  material_modes:
    prestudy:
    short_read:
  drift_guardrails: []
```

注意：
- `lesson_skin_seed` 不是 `Lesson Skin Final`。
- 不提前鎖 slide camera / slide layout / full cinematic language。
- 若既有角色與 Style Reference 已核准，直接 REUSE；不必每課重新生成。

---

## 4. 從批次模式回到正式簡報

未來要正式做某一課時：

```text
讀 Runtime
→ 讀 BATCH_PREP_CHECKPOINT
→ 讀 Lesson Visual Identity Pack (SEED_LOCKED)
→ 讀 shared character canonical assets
→ 讀既有 PRESTUDY / SHORT_READ
→ Knowledge Lab / Slide Architecture
→ Page Ledger / Storyboard
→ Style Recipe Finalization
→ Lesson Skin Final
→ Typography Lock
→ Gate B
→ Representative / Gate C
→ 正式簡報
```

### Inheritance Rule
Final visual 必須繼承 Seed 中已鎖的：
- Character identity / asset_version
- Scenario identity
- Book DNA
- Style family direction
- Typography base

可以細化：
- lighting
- camera language
- slide density
- page-family visual grammar
- cinematic level
- teaching-slide specific treatment

若要改 Seed 已鎖內容，必須教師明確 reopen；不得因 Renderer 方便自行漂移。

---

## 5. 角色與 Style 確認成本

批次模式預設採三類：

### REUSE_CONFIRMED
既有角色／Style reference 已核准。
- 只確認引用與本課功能。
- 不重新生成基準圖。

### NEW_SKIN
角色沿用，但本課 Style Seed 不同。
- 只需確認 Lesson Skin Seed / style keyframe。

### NEW_CHARACTER
需要新角色。
- 建立新 role_id。
- 核准 canonical reference image。
- 存入 Drive shared character library。
- 之後其他課可 REUSE。

---

## 6. Drive Checkpoint

`BATCH_PREP_CHECKPOINT_COMPLETE` 前必須確認：

```yaml
batch_prep_checkpoint:
  lkb_ref: PASS
  teaching_direction_ref: PASS
  scenario_lock_ref: PASS
  character_lock_ref: PASS
  visual_seed_pack_ref: PASS
  character_drive_assets_ref: PASS
  prestudy_asset: PASS | N/A
  short_read_asset: PASS | N/A
  drive_persistence_verified: PASS
```

若 Identity Pack 或角色 reference 只存在對話中，不得 PASS。

---

## 7. Single vs Batch 共同規則

兩種模式都必須：
- 共用 approved LKB。
- 共用 Character System / Role Library。
- 共用 Scenario Registry / Teacher Lock。
- 共用 Style Recipe Families。
- 共用 Typography Engine。
- 共用 Google Drive Asset Authority。
- 所有可續跑成品／半成品落地 Drive。

差別只是「做到哪個 checkpoint」，不是兩套教學邏輯。

---

## 核心金句

> 單課模式把一課做到底；批次模式先把很多課做到可安全停車的位置。

> 批次模式不是少做視覺身分，而是先鎖 Visual Seed、晚一點再長成 Lesson Skin Final。
