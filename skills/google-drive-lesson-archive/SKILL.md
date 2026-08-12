# V-MAX Google Drive Lesson Archive Skill

版本：1.2-draft

## 目的
本技能定義 V-MAX 每課教材成果、半成品、核准視覺資產在 Google Drive 的正式保存位置、分類資料夾與版本管理規則。

核心原則：

> 教材做完不只要存在 Chat 或暫存區；所有可續跑的成品與半成品都必須落地到教師指定的 Google Drive。

> GitHub 管規則；Google Drive 管實際工作成果與可恢復資產。

> 同一課完整重做時不覆蓋舊版；共享角色與 Style 不在每課重複複製，而以 asset reference 引用。

> 更新檔案永遠另存新版本，不覆蓋舊檔；回退靠 active ref，不靠刪檔。

Canonical upgrade policy：`core/governance/lesson-upgrade-lifecycle-policy.md`。

---

## A. 固定教材庫根目錄

```yaml
google_drive_archive_root:
  title: V-MAX 教材庫
  folder_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

`00_Runtime_State` 為每課執行狀態專用。

---

## A2. 共享角色與視覺資產庫

```yaml
shared_visual_asset_library:
  title: 00_V-MAX_角色與視覺資產庫
  folder_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
```

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

共享角色 canonical 圖像也必須版本化，例如：
`ROLE-BEE-001_canonical_v01.png / v02.png / v03.png`。

---

## B. 冊別／教材層
每課成果進入對應冊別資料夾，例如 `V-MAX 教材庫/四上康軒國語/`。

---

## C. 課資料夾命名

```text
{兩位數課次}_{課次中文}_{課名}
```

完整重跑時：

```text
09_第九課_請到我的家鄉來
09_第九課_請到我的家鄉來_01
09_第九課_請到我的家鄉來_02
```

建立新 folder version 前必須先讀 Drive，不能猜號。

---

## D. 檔案版本管理｜Never Overwrite

同一課資料夾內，任何 PATCH、WIP 或成品更新都另存：

```text
{base_name}_v01.ext
{base_name}_v02.ext
{base_name}_v03.ext
```

例如：

```text
L09_教學簡報_v01.pptx
L09_教學簡報_v02.pptx
L09_預習單_v01.pdf
L09_預習單_v02.pdf
L09_storyboard_wip_v01.md
L09_storyboard_wip_v02.md
L09_VisualIdentity_v01.yaml
L09_VisualIdentity_v02.yaml
```

### Folder vs File
- 完整 `REFRESH / REBASE` → 新課版本資料夾。
- 同課版本中的 `PATCH / WIP iteration` → 新 file version。
- 禁止直接覆蓋同名檔案。

### Active Pointer
`最新建立` 不代表 `目前採用`。Runtime 必須保存 active file ref。

新增 `v03` 後，若尚未核准，active ref 可繼續指向 `v02`。

Rollback：

```text
active_ref = v03
→ teacher rollback
→ active_ref = v02
```

不改名、不刪除、不覆蓋。

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

### 01_教材整理
Source Master、Official Knowledge、LKB 匯出、Lesson DNA、Teaching Direction、Identity Pack reference、分析 WIP。

### 02_逐頁腳本
Storyboard、Page Ledger、Renderer Script、講者備註草稿。所有更新採 `_vNN`。

### 03_NotebookLM
NotebookLM Source、Curated Briefing、Visual YAML、生成指令。NotebookLM YAML 是 adapter output，不是視覺真值。

### 04_角色視覺
本課使用的 role_id / asset_version / shared Drive reference，以及本課特殊服裝、道具、表情、角色樣張。

### 05_簡報成品
代表頁樣張、Image-first PDF、Teaching PPTX、Google Slides、簡報 WIP。每次更新另存 `_vNN`。

### 06_延伸教材
預習單、短文單、Kahoot／題庫／評量匯出、平板任務與其他附件。每次更新另存 `_vNN`。

---

## F. Lesson Visual Identity Pack
存於共享庫 `05_Lesson_Visual_Identity_Packs/`，並明確版本化：

```text
L09_VisualIdentity_v01.yaml
L09_VisualIdentity_v02.yaml
```

每課 `01_教材整理` 只保存目前 active reference 與歷史 lineage。

預習單、短文單、正式簡報、NotebookLM Visual YAML 都讀明確版本，不得讀浮動 `latest`。

---

## G. Save-on-Approval / Save-on-Interrupt
以下事件一成立就落地 Drive 並建立新版本：
- 核准角色長相
- 核准 Style reference / Visual Seed / Lesson Skin
- Storyboard / Page Ledger 可續跑
- 代表頁通過
- NotebookLM Source / YAML 可用
- 預習單、短文單、題庫已有可用版
- 因額度、平台、時間中斷，需要保存 WIP

禁止只在對話說「已鎖定」。

---

## H. 兩種製作模式

### SINGLE_LESSON_BUILD
完整單課一路做到簡報與衍生輸出；每次更新保留歷史檔。

### BATCH_PREP_BUILD
批次先做 Identity Seed、預習單、短文單；未來讀 Runtime + 明確 Identity version + shared character asset version 繼續簡報。

---

## I. 定期升級
約每 24 個月可標 `REVIEW_DUE`，由教師決定是否 REFRESH。

重跑時要記錄：
- parent package
- 沿用哪些 refs
- 升級哪些 refs
- 哪些資產保持 pinned
- change summary

到期不代表自動升級角色或 Style。

---

## J. Verification

```yaml
google_drive_persistence:
  lesson_root_verified: true | false
  shared_visual_library_verified: true | false
  runtime_state_verified: true | false
  active_refs_verified: true | false
  historical_versions_preserved: true | false
  current_stage_artifacts_verified: PASS | INCOMPLETE | BLOCKED
```

---

## K. 禁止事項
- 覆蓋舊檔。
- 用 `latest` 當正式教材引用。
- 因為有新版就刪舊版。
- 完整重做卻寫進舊課 folder。
- 只存 Chat 不存 Drive。
- 回退時重新生成舊檔取代真正舊版。

Failure：
`OVERWRITE_EXISTING_ASSET / FLOATING_LATEST_REFERENCE / HISTORICAL_ASSET_DELETED_WITHOUT_APPROVAL / ACTIVE_POINTER_UNVERIFIED / CHAT_ONLY_ASSET / DRIVE_ARCHIVE_UNVERIFIED`。

---

## 核心金句
> 新版永遠是新增，不是覆蓋。

> Drive 裡每一版都留著；Runtime 決定今天要用哪一版。
