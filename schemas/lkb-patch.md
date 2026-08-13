# LKB Patch Schema 1.0

LKB Patch 用於局部補充或修正知識節點，不取代完整母檔。

```yaml
lkb_patch:
  patch_id: ""
  lesson_id: ""
  base_lkb_version: ""
  current_lkb_version_at_merge: ""
  triggered_by_task: ""
  status: DRAFT_LKB_PATCH | PATCH_EVIDENCE_VALIDATED | READY_FOR_LKB_PATCH_REVIEW | APPROVED | REBASE_REQUIRED | MERGED

  source_changes:
    changed_source_pages: []
    unchanged_source_pages: []
    fingerprint_before: ""
    fingerprint_after: ""

  node_changes:
    - node_id: ""
      operation: ADD | UPDATE | DEPRECATE
      changed_fields: []
      previous_value: ""
      proposed_value: ""
      source_evidence: []
      change_reason: ""
      affected_tasks: []

  conflicts: []
  teacher_decision: ""
  approved_by: ""
  merged_lkb_version: ""
```

## 合併規則

1. 比對 `base_lkb_version` 與目前 active LKB。
2. 若版本不同，檢查 changed node IDs；重疊修改標記 `LKB_PATCH_REBASE_REQUIRED`。
3. 未重疊可重新套用，但仍需保留新的 base version 與驗證紀錄。
4. 未核准 Patch 不得合併。
5. 合併建立新 LKB 版本，舊版不得刪除或無痕覆寫。
6. 只讓受到 node changes 影響的 task readiness 重新進入 `NOT_CHECKED` 或 `NEEDS_ENRICHMENT`。

