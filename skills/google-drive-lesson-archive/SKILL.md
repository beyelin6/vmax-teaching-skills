# V-MAX Google Drive Lesson Archive Skill

版本：1.1-draft

## 目的

本技能定義 V-MAX 每課教材成果、半成品、核准視覺資產在 Google Drive 的正式保存位置、分類資料夾與版本管理規則。

核心原則：

> 教材做完不只要存在 Chat 或暫存區；所有可續跑的成品與半成品都必須落地到教師指定的 Google Drive。

> GitHub 管規則；Google Drive 管實際工作成果與可恢復資產。

> 同一課完整重做時不覆蓋舊版；共享角色與 Style 不在每課重複複製，而以 asset reference 引用。

---

## A. 固定教材庫根目錄

```yaml
google_drive_archive_root:
  title: V-MAX 教材庫
  folder_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

只要此根目錄可存取，就不得在 My Drive 另建第二個同名教材庫。

`00_Runtime_State` 仍為每課執行狀態專用。

---

## A2. 共享角色與視覺資產庫

共享可重用資產固定放：

```yaml
shared_visual_asset_library:
  title: 00_V-MAX_角色與視覺資產庫
  folder_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
  parent_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

固定結構：

```text
00_V-MAX_角色與視覺資產庫/
├── 01_角色庫/
├── 02_整冊Book_DNA/
├── 03_Style_Reference/
├── 04_共用圖示與視覺語彙/
└── 05_Lesson_Visual_Identity_Packs/
```

角色實例：

```text
01_角色庫/
└── ROLE-BEE-001_Bee老師/
    ├── 01_角色設定/
    ├── 02_核准基準圖/
    ├── 03_表情姿勢/
    └── 04_服裝變體/
```

### 共享資產規則

- GitHub `libraries/roles/...` 保存 role_id、人格、教學功能與穩定文字 Visual DNA。
- Drive `01_角色庫` 保存角色真正核准過的長相、基準圖、表情姿勢、服裝變體與 asset_version。
- 未來再生成簡報、預習單、短文單時，必須讀既有角色 reference，不得只靠文字 prompt 猜回角色長相。
- Book DNA / Style Reference / 共用視覺語彙同理，核准後必須持久保存。

---

## B. 冊別／教材層

每課成果進入對應冊別資料夾，例如：

```text
V-MAX 教材庫/
└── 四上康軒國語/
```

名稱以教師實際教材版本／冊別為準。

---

## C. 課資料夾命名

基礎格式：

```text
{兩位數課次}_{課次中文}_{課名}
```

例如：

```text
02_第二課_放學後
```

第一個正式版本不加尾碼。

---

## D. 重做版本管理

完整重做不得覆蓋舊版本：

```text
02_第二課_放學後
02_第二課_放學後_01
02_第二課_放學後_02
...
```

建立新版本前必須先讀 Drive 現況；不得依模型記憶猜版本號。

- 完整重跑 Golden Path／另一套完整教材包 → 新版本資料夾。
- 局部修一張圖、補一份文件、修同版文字 → 留在原版本。

---

## E. 每課固定六類資料夾

```text
{課資料夾}/
├── 01_教材整理/
├── 02_逐頁腳本/
├── 03_NotebookLM/
├── 04_角色視覺/
├── 05_簡報成品/
└── 06_延伸教材/
```

### `01_教材整理`
- Source Master / Official Knowledge / LKB 匯出
- Lesson DNA / Teaching Direction
- Lesson Visual Identity Pack reference
- 可續跑的分析半成品

### `02_逐頁腳本`
- Storyboard
- Page Ledger
- Renderer Script
- 逐頁教學腳本／講者備註草稿

### `03_NotebookLM`
- NotebookLM Source / Curated Briefing
- NotebookLM Visual YAML
- NotebookLM 生成指令

NotebookLM YAML 是 adapter output；不得取代 `Lesson Visual Identity Pack` 的跨平台權威。

### `04_角色視覺`
只放本課使用紀錄與本課變體：
- role_id / asset_version / shared Drive reference
- 本課特殊服裝、道具、表情
- 本課角色樣張

共享角色的 canonical 基準圖留在 `00_V-MAX_角色與視覺資產庫/01_角色庫`，不要每課重複複製。

### `05_簡報成品`
- 代表頁樣張
- Image-first PDF
- Teaching PPTX
- Google Slides（若建立）
- 尚未完工但需保存的簡報半成品

### `06_延伸教材`
- 預習單
- 短文單／微寫作／仿作單
- Kahoot／題庫／評量匯出
- 平板任務與其他延伸文件

---

## F. Lesson Visual Identity Pack

每課跨教材需要一致角色／風格時，建立：

`00_V-MAX_角色與視覺資產庫/05_Lesson_Visual_Identity_Packs/`

每課資料夾 `01_教材整理` 只保存 reference。

最低需能追溯：
- lesson_id / version
- Book DNA ref
- Scenario ref
- role_id + asset_version + Drive asset ref
- Style Recipe ref
- Lesson Skin
- approved style/reference image
- Typography Lock ref
- Material Mode rules
- drift guardrails

預習單、短文單、正式簡報、NotebookLM Visual YAML 都應讀同一 Pack。

---

## G. Save-on-Approval / Save-on-Interrupt

以下事件一成立就必須落地 Drive，不等整課完成：

- 教師核准角色長相
- 教師核准 Style reference / Lesson Skin
- Storyboard / Page Ledger 已可續跑
- 代表頁通過
- NotebookLM Source / YAML 已可用
- 預習單、短文單、題庫已有可用版
- 因額度、平台、時間中斷，任何半成品需要日後續跑

禁止只在對話中說「已鎖定」但 Drive 找不到可恢復資產。

Failure：
`CHAT_ONLY_ASSET / APPROVED_ASSET_NOT_PERSISTED / VISUAL_REFERENCE_MISSING`。

---

## H. 兩種製作模式的 Drive 行為

### SINGLE_LESSON_BUILD
簡報可先完成，再由同一 Identity Pack 衍生預習單／短文單／題庫；每個正式階段與可續跑半成品都寫入本課資料夾。

### BATCH_PREP_BUILD
可先批次完成多課分析、角色／風格確認與 Lesson Visual Identity Pack，再批量生成預習單／短文單；未來正式做簡報時，直接讀回該課 Runtime + Identity Pack + shared character assets。

批次模式不得因尚未做簡報而省略角色 reference／Style reference 的保存。

---

## I. 正式歸檔流程

```text
1. 讀 V-MAX 教材庫根目錄
2. 找冊別資料夾
3. 決定課版本名稱
4. 建立／確認六類資料夾
5. 寫入目前階段的成品與半成品
6. 若有角色／Style 核准資產，寫入共享資產庫
7. 每課保存 shared asset refs / Identity Pack refs
8. 再次 list/search Drive 驗證
9. 驗證成功才回報 Archive / Persistence PASS
```

---

## J. Verification

```yaml
google_drive_persistence:
  lesson_root_verified: true | false
  shared_visual_library_verified: true | false
  runtime_state_verified: true | false
  lesson_visual_identity_ref_verified: true | false
  role_asset_refs_verified: true | false
  current_stage_artifacts_verified: PASS | INCOMPLETE | BLOCKED
```

完整 Lesson Package 另依 `skills/lesson-package-delivery/SKILL.md` 檢查。

---

## K. 禁止事項

- 不得把已核准角色長相只留在 Chat。
- 不得把 NotebookLM YAML 當成唯一視覺真值。
- 不得每課複製一套共享角色基準圖造成多個互相漂移的版本。
- 不得完整重做卻覆蓋舊課版本。
- 不得宣稱已保存但未用 Drive Connector / API 再次驗證。

Failure：
`DRIVE_ARCHIVE_ROOT_DRIFT / LESSON_FOLDER_VERSION_COLLISION / DRIVE_ARCHIVE_UNVERIFIED / SHARED_ASSET_DUPLICATION / CHAT_ONLY_ASSET`。

---

## 核心金句

> GitHub 管方法，Drive 管工作。

> 角色的規則在 GitHub；角色的臉在 Drive。

> 做完要存，做到一半也要存；能從 Drive 接回來，才算 V-MAX 的成果。
