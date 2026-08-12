# V-MAX Lesson Package Delivery

版本：1.4-draft

## 目的

本技能定義一課的正式教材包，以及尚未完成但必須能日後接續的持久化成果。

核心：

> 一課完成不等於只有簡報；任何已確認或需要續跑的工作都必須能從 Google Drive 恢復。

> Google Drive 是實際成果與半成品權威；GitHub 只保存規則與可重用技能。

---

## A. Production Mode

```yaml
production_mode: SINGLE_LESSON_BUILD | BATCH_PREP_BUILD
```

### SINGLE_LESSON_BUILD
典型順序：完整分析 → Storyboard / Style / Identity → 正式簡報 → 詳細說明 / Renderer Script → NotebookLM → 預習單 / 短文單 → 題庫／其他附件。

### BATCH_PREP_BUILD
典型順序：多課分析 → 批次確認 Teaching Direction / Scenario / Character / Style → 建立各課 Lesson Visual Identity Pack → 批量預習單 / 短文單 → 未來讀回 Identity Pack 再做正式簡報。

批次模式可暫時沒有 PPTX，但 `Lesson Visual Identity Pack` 與角色／Style reference 不得省略。

---

## B. 核心持久化資產

每課至少追蹤：

1. `Source Master / LKB Export`
2. `Teaching Direction / Lesson Map / Session Map`
3. `Storyboard / Page Ledger / Renderer Script`（進到該階段後）
4. `Lesson Visual Identity Pack`
5. `Character Asset References / Lesson Variants`
6. `NotebookLM Source / Visual YAML`（若啟用）
7. `Representative Visual / Slide Work-in-progress / Final Slides`
8. `Pre-study Worksheet`
9. `Post-lesson Short Reading/Writing Worksheet`
10. `Question Bank / Kahoot Export / Assessment / Other Add-ons`（若啟用）

其中 1–5 是跨平台續跑的基礎資產；7–10 視 production mode 與進度存在。

---

## C. Lesson Visual Identity Pack

此 Pack 是跨教材、跨平台視覺引用權威，必須可追溯：

```yaml
lesson_visual_identity:
  lesson_id:
  version:
  book_dna_ref:
  scenario_ref:
  character_refs:
    - role_id:
      asset_version:
      drive_asset_ref:
  style_recipe_ref:
  lesson_skin:
  style_reference_asset_ref:
  typography_lock_ref:
  material_modes:
    prestudy:
    short_read:
    teaching_slide:
    extension:
  drift_guardrails: []
```

NotebookLM Visual YAML、Canva mapping、Renderer prompt 都是此 Pack 的 adapter output，不得反過來成為視覺真值。

---

## D. Character Assets

角色文字規則依 GitHub Role Library；角色真正核准的長相依 Google Drive shared visual asset library。

每課只保存：
- role_id
- asset_version
- shared Drive reference
- 本課專用服裝／道具／姿勢變體

共享角色 canonical reference 不在每課重複複製。

---

## E. Google Drive 歸檔

唯一權威：

`skills/google-drive-lesson-archive/SKILL.md`

教材庫根目錄：

```text
V-MAX 教材庫
folder_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

共享視覺資產庫：

```text
00_V-MAX_角色與視覺資產庫
folder_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
```

每課版本固定六類：

```text
01_教材整理/
02_逐頁腳本/
03_NotebookLM/
04_角色視覺/
05_簡報成品/
06_延伸教材/
```

對應：
- `01_教材整理`：Source / LKB / Teaching Direction / Identity Pack ref
- `02_逐頁腳本`：Storyboard / Page Ledger / Renderer Script
- `03_NotebookLM`：NotebookLM Source / Visual YAML / 指令
- `04_角色視覺`：本課 role refs / lesson variants
- `05_簡報成品`：代表頁、WIP、PPTX、PDF、Slides
- `06_延伸教材`：預習單、短文單、題庫、Kahoot、評量與其他附加文件

---

## F. Save-on-Approval / Save-on-Interrupt

以下狀態一成立就必須寫入 Drive：
- 教師核准角色長相
- Style / Lesson Skin 鎖定
- Storyboard / Page Ledger 可續跑
- 代表頁通過
- NotebookLM Source / YAML 可用
- 預習單／短文單／題庫已有可用版
- 因額度、時間、平台切換而中斷

禁止只在聊天內保留已確認成果。

---

## G. Worksheet Typography Gate

```yaml
worksheet_typography_gate:
  print_size: A4_100_PERCENT
  min_student_visible_font_pt: 12
  prestudy: PASS | FAIL
  postlesson_short_writing: PASS | FAIL
  export_scale_preserved: PASS | FAIL
```

學生需要閱讀、辨認或作答依據的文字低於 12 pt 即 FAIL。

---

## H. Delivery / Persistence Gate

```yaml
lesson_package_delivery:
  production_mode:
  source_and_lkb_persisted: PASS | BLOCKED
  teaching_direction_persisted: PASS | BLOCKED
  lesson_visual_identity_pack: PASS | BLOCKED
  character_asset_refs: PASS | BLOCKED
  storyboard_page_ledger: PASS | PENDING_NOT_REACHED | BLOCKED
  notebooklm_assets: PASS | N/A_BY_TEACHER | PENDING
  slide_assets: PASS | PENDING_NOT_REACHED | N/A_BY_MODE
  prestudy_worksheet: PASS | PENDING
  short_read_or_writing_worksheet: PASS | PENDING
  question_bank_kahoot: PASS | N/A_BY_TEACHER | PENDING
  worksheet_typography_gate: PASS | PENDING
  google_drive_persistence: PASS | BLOCKED
```

`BATCH_PREP_BUILD` 不因尚未完成正式簡報而 FAIL；只要該模式預定的階段性成果與 Identity refs 都已持久化即可。

---

## I. 完成判定

### 單課完整模式
只有本次教師選定的正式輸出與 Google Drive persistence 驗證完成，才可宣告 Lesson Package 完成。

### 批次備課模式
可宣告 `BATCH_PREP_CHECKPOINT_COMPLETE`，但不得冒充 `FULL_LESSON_PACKAGE_COMPLETE`。

未來進正式簡報時必須先讀回：

```text
Runtime State
+ Lesson Visual Identity Pack
+ Character shared asset refs
+ 已存在預習／短文教材
```

---

## 核心金句

> 成品要存，半成品也要存；下一個平台能接著做，才是真正可用的 V-MAX 教材資產。

> 角色的規則在 GitHub；角色的臉、課的視覺身分、所有實際成果都在 Drive。
