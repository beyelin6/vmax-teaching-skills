# V-MAX Lesson Master Preflight 1.0

## 目的

所有平台執行預習單、短文單、簡報、教案、評量、活動或圖片前，都先確認本課已有可追溯且足以支持該任務的核准 Lesson Knowledge Book（LKB）母檔。此規則屬於 Core，不只適用於 Gemini。

## 固定流程

```text
REQUEST_RECEIVED
→ READ_LESSON_MASTER_INDEX
→ LOCATE_APPROVED_LKB
→ VERIFY_LESSON_ID_AND_SOURCE_FINGERPRINT
→ LOAD_TASK_KNOWLEDGE_REQUIREMENTS
→ RUN_LKB_COVERAGE_DIFF
├─ LKB_SUFFICIENT_FOR_TASK：進入任務
├─ LKB_ENRICHMENT_REQUIRED：局部補查並建立 LKB Patch
├─ SOURCE_NOT_PRESENT：記錄 N/A；需要延伸時交給 Learning Module
└─ BLOCKED：停止並說明缺口
```

## 首次与续跑

- 沒有核准 LKB：先取得教冊／課本／習作，完成 Official Knowledge、重要知識分析、教師確認及 LKB 建立。
- 已有有效 LKB：直接重用，不因新對話、換平台或改做其他成品而重跑。
- LKB 對任務不夠周全：只補缺少節點，教師核准 Patch 後合併為新版本。
- 來源局部更新：只使引用該來源的節點與相關 task readiness 失效。

## 最低回执

```yaml
lesson_master_preflight:
  lesson_id: ""
  index_status: VALID | MISSING | CONFLICT | STALE
  lkb_path_or_id: ""
  lkb_version: ""
  lkb_approval: approved_lkb | unapproved | missing
  source_fingerprint_match: true | false | unknown
  task_type: ""
  coverage_decision: LKB_SUFFICIENT_FOR_TASK | LKB_ENRICHMENT_REQUIRED | SOURCE_NOT_PRESENT | BLOCKED
  missing_nodes: []
  next_allowed_action: ""
```

## 禁止事項

- 不以對話記憶代替實際讀取 Index 與 LKB。
- 不在母檔缺失或必要 Patch 未核准時直接製作正式成品。
- 不因單一知識缺口整份重跑。
- 不把 AI 延伸混入 Official Knowledge。
- 不把 `AGENT_OMISSION` 誤判成母檔缺漏。
