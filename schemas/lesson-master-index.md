# Lesson Master Index Schema 1.0

每課只維護一筆 active master index，讓新對話與不同平台能直接定位最新版 LKB，不靠搜尋結果、檔名排序或模型記憶猜測。

```yaml
lesson_master_index:
  lesson_id: ""
  grade_semester_publisher: ""
  lesson_number: ""
  lesson_title: ""

  active_lkb:
    path_or_drive_id: ""
    version: ""
    approval_status: draft | ready_for_lkb_review | approved_lkb | stale_by_source_change
    approved_at: ""
    approved_by: ""

  source_fingerprint:
    fingerprint_id: ""
    generated_at: ""
    sources: []

  task_readiness:
    prestudy_worksheet: NOT_CHECKED | READY | NEEDS_ENRICHMENT | BLOCKED
    postlesson_writing: NOT_CHECKED | READY | NEEDS_ENRICHMENT | BLOCKED
    presentation: NOT_CHECKED | READY | NEEDS_ENRICHMENT | BLOCKED
    lesson_plan: NOT_CHECKED | READY | NEEDS_ENRICHMENT | BLOCKED
    assessment: NOT_CHECKED | READY | NEEDS_ENRICHMENT | BLOCKED
    activity: NOT_CHECKED | READY | NEEDS_ENRICHMENT | BLOCKED
    image: NOT_CHECKED | READY | NEEDS_ENRICHMENT | BLOCKED

  open_patches: []
  previous_lkb_versions: []
  updated_at: ""
```

## 規則

- 新任務先讀 Index，再讀 `active_lkb.path_or_drive_id`。
- 只有已核准 LKB 可標記任務 `READY`。
- 合併 Patch 或來源更新後，同步更新 Index；未再次讀取驗證前不得宣稱完成。
- `previous_lkb_versions` 只供追溯，不可被模型誤當 active LKB。
- Index 缺失或同課出現多個 active entry 時標記 `LESSON_MASTER_INDEX_CONFLICT`。

