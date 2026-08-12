# V-MAX Lesson Upgrade Lifecycle Policy 1.0-draft

## 定位
V-MAX 的教材與視覺資產可以定期升級，但任何升級都必須可追溯、可比較、可回退。

> 可升級，不可覆蓋。
>
> 更新永遠另存新版本；舊版保留，後悔才有救。

---

## 1. Review / Refresh Cadence
教師可約每 24 個月重新檢視既有課程。24 個月只代表 `REVIEW_DUE`，不是自動改寫命令。

可能更新：
- 新的背景知識或補充資料
- 教學重點／學生卡點
- Teaching Skill / Storyboard / Extension
- Character / Style / Book DNA / Identity Pack
- NotebookLM、Kahoot 或其他平台 adapter
- 預習單、短文單、正式簡報

---

## 2. Change Classes

### PATCH
局部修正，例如錯字、注音、一張圖、少量頁面、補附件。

### REFRESH
同一教材來源下定期重新備課，重新評估 LKB / Teaching Direction / Visual Identity / outputs。

### REBASE
教材來源本身改版，例如出版社版本、課文、教冊或官方教學內容有實質變更。必須重新做 Source Truth / LKB。

---

## 3. Never-Overwrite Rule
任何已保存到 Google Drive 的成品或可續跑半成品，只要內容要被替換，就必須建立新檔名，不得覆蓋舊檔。

### 檔案版本格式

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
L09_VisualIdentity_v01.yaml
L09_VisualIdentity_v02.yaml
ROLE-BEE-001_canonical_v01.png
ROLE-BEE-001_canonical_v02.png
```

### 半成品
半成品同樣不可覆蓋：

```text
L09_storyboard_wip_v01.md
L09_storyboard_wip_v02.md
L09_representative_slide_wip_v01.png
```

`wip` 可以升級為正式版，但正式版仍另建立新檔，不把 WIP 原檔改名覆蓋。

---

## 4. Folder Version vs File Version

### Lesson Package Folder Version
完整重跑一整課：

```text
09_第九課_請到我的家鄉來
09_第九課_請到我的家鄉來_01
09_第九課_請到我的家鄉來_02
```

### File Version
同一課資料夾內的局部更新／迭代：

```text
L09_教學簡報_v01.pptx
L09_教學簡報_v02.pptx
```

規則：
- 完整 REFRESH / REBASE → 新 Lesson Package folder。
- 同一版本內 PATCH / WIP iteration → 新 file version。
- 不得用覆蓋檔案來表示「最新版」。

---

## 5. Active Pointer Rule
`最新建立` 不等於 `目前採用`。

Runtime 必須保存明確 active ref：

```yaml
active_assets:
  teaching_slides_ref:
  prestudy_ref:
  short_read_ref:
  identity_pack_ref:
  character_asset_refs: []
  style_asset_ref:
```

建立新版本後，只有教師確認或合法 Gate / Lock 通過，才更新 active ref。

因此回退不需要刪檔或改檔：

```text
active_ref: v03
→ teacher rollback
→ active_ref: v02
```

舊檔保持原樣。

---

## 6. Asset Pinning
完成教材必須 pin 明確版本，禁止浮動引用 `latest`。

例如：

```yaml
character_ref:
  role_id: ROLE-BEE-001
  asset_version: v02

identity_pack_ref:
  lesson_id: zh-4a-l09
  version: v03
```

若角色庫出現 v04，舊課仍使用 v02／v03，直到教師在 REFRESH 時明確升級。

---

## 7. Upgrade Decision
重新跑舊課時，對每個可重用資產做：

```yaml
upgrade_decision:
  KEEP_PINNED: 保留舊版
  UPGRADE: 升到指定新版
  FORK: 舊版保留，建立本課專用變體
  RETIRE_FROM_NEW_VERSION: 新版不再使用，但舊版仍保留
```

不得因共用角色／Style 有新版本，就自動改掉所有歷史教材。

---

## 8. Lineage / Change Log
每次 REFRESH / REBASE 保存：

```yaml
lesson_lineage:
  lesson_id:
  package_version:
  parent_package_ref:
  change_class: PATCH | REFRESH | REBASE
  source_baseline_ref:
  created_at:
  reviewed_at:
  next_review_due:
  inherited_refs: []
  upgraded_refs: []
  retired_refs: []
  change_summary: []
```

目的不是寫長報告，而是讓兩年後可以知道：
- 哪些東西沿用
- 哪些升級
- 為什麼改
- 要退回哪一版

---

## 9. Delete / Cleanup Guard
舊版預設 `ARCHIVED`, 不自動刪除。

只有教師明確要求刪除時才可移除；系統不能因為「已有新版」清掉舊檔。

Failure codes：
- `OVERWRITE_EXISTING_ASSET`
- `FLOATING_LATEST_REFERENCE`
- `VERSION_LINEAGE_MISSING`
- `ACTIVE_POINTER_UNVERIFIED`
- `HISTORICAL_ASSET_DELETED_WITHOUT_APPROVAL`

---

## 核心金句
> 新版是新增，不是取代；目前採用哪一版由 active ref 決定。

> 最好的後門不是偷偷改，而是每一版都留著，想回去隨時有路。
