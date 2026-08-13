# Gemini Source Analysis Contract 1.0

## 目的

防止 Gemini 收到新教材後直接製作成品，或以短摘要冒充完整的該課知識分析；同時避免每次任務重跑已完成的教材分析。本合約只約束 Gemini 執行方式，不改寫 V-MAX Core 的正式知識分類。

## 1. 母檔模型

本課唯一可供下游重用的知識母檔是核准的：

`lkb/{課次}_{課名}_lesson-knowledge-book.md`

建立鏈：

```text
教師手冊／課本／習作／出版社資源
→ Official Knowledge + Source Map + Validation
→ Important Knowledge Analysis
→ Lesson Knowledge Book
→ Teacher Approval
→ APPROVED_LKB_MASTER
```

Gemini 不另建第二套知識真相。分析報告是 LKB 建立與核准的證據；核准 LKB 才是簡報、學習單、策略、活動、評量與圖片流程共同引用的母檔。

首次完成後必須實際留存，不得只存在對話內容：

```text
knowledge/01_official-knowledge.md
knowledge/source-map.md
knowledge/official-knowledge-validation.md
analysis/gemini-source-analysis-report.md
lkb/{課次}_{課名}_lesson-knowledge-book.md
```

若本次環境可寫 Google Drive，保存到該課正式 Lesson workspace 並再次讀取驗證；無法寫入時輸出上述完整檔案與精確 handoff，標記 `LKB_MASTER_PERSISTENCE_BLOCKED`，不得宣稱母檔已保存。

## 2. 每次任務的 Preflight

跑任何 V-MAX 流程前先依 `schemas/lesson-master-index.md` 定位 active LKB，再檢查：

1. 課次與 `lesson_id` 是否一致。
2. LKB 是否存在且狀態為 `approved_lkb`。
3. LKB 記錄的 `source_fingerprint` 是否與目前來源集合一致。
4. 是否存在較新的教師手冊、課本、習作、勘誤或教師明確修訂。
5. Runtime 是否已鎖定新的知識決策但尚未同步到 LKB。
6. 母檔能否從正式儲存位置實際重新讀取，而不是只存在模型對話記憶。

全部通過時記錄 `LKB_MASTER_REUSED`，直接沿用，不重跑轉錄與分析。

## 3. 任務需求與 Coverage Diff

來源未改變但下游任務需求不同時，不把 LKB 判成整體失效。先由下游技能建立：

```yaml
task_knowledge_requirements:
  task_type: prestudy_worksheet | presentation | lesson_plan | assessment | activity | image
  required_nodes:
    - knowledge_type: ""
      purpose: ""
      minimum_evidence: ""
  optional_nodes: []
```

再比對 LKB：

```yaml
lkb_coverage_diff:
  satisfied_nodes: []
  missing_nodes: []
  insufficient_evidence_nodes: []
  source_pages_to_revisit: []
  decision: LKB_SUFFICIENT_FOR_TASK | LKB_ENRICHMENT_REQUIRED | SOURCE_NOT_PRESENT | BLOCKED
```

`LKB_ENRICHMENT_REQUIRED` 時只回讀與缺口相關的來源頁面，建立 `lkb-patch`。Patch 每個新增或修訂節點都要有來源定位、變更理由、影響的下游任務與原節點 ID；不得整份重跑。

各任務的最低需求依 `core/governance/task-knowledge-requirement-registry.md`；Patch 格式與 rebase 規則依 `schemas/lkb-patch.md`。

Patch 狀態：

```text
DRAFT_LKB_PATCH
→ PATCH_EVIDENCE_VALIDATED
→ READY_FOR_LKB_PATCH_REVIEW
→ Teacher Approval
→ MERGED_AS_NEW_LKB_VERSION
```

未核准 Patch 不得直接改寫正式母檔。合併時保留舊版、更新 source／knowledge coverage，並記錄哪些下游需求促成增補。

## 4. Source Fingerprint

Fingerprint 不要求特定雜湊演算法，但至少記錄：

```yaml
source_fingerprint:
  lesson_id: ""
  sources:
    - stable_id_or_path: ""
      source_type: ""
      edition_or_revision: ""
      modified_at: ""
      size_or_page_count: ""
      checksum_if_available: ""
  generated_at: ""
```

只以檔名相同不能判定來源未變。若平台無法取得 checksum，可用 Drive file ID、modified time、頁數與版本資訊組合；仍無法判定時標記 `SOURCE_FINGERPRINT_UNKNOWN`，不得靜默假設有效。

## 5. 觸發重新分析的條件

出現下列任一情形即強制啟動：

- 使用者上傳或指定新的課本、教師手冊、習作、出版社補充資源，且沒有可驗證的核准母檔。
- 新增課次，或無法證明本課已有核准的 Official Knowledge。
- 使用者要求根據新教材製作簡報、學習單、教案、活動、評量或圖片，且 LKB 為 `MISSING / STALE / UNAPPROVED / LESSON_MISMATCH`。
- Gemini 只能看到部分頁面、附件或摘錄，無法確認來源覆蓋。
- 來源 fingerprint 改變、課次不符、LKB 未核准、教師要求重建或官方勘誤造成知識異動。

不得因新對話、新工作階段、換模型、改做另一種成品或 Gemini 自己想「重新整理」而重跑。

## 6. 首次建立／失效後重建順序

### A. Source Inventory

先列出每個實際可讀來源：檔名、類型、課次、總頁數、已讀頁面、未讀頁面、解析方式與品質。附件存在不等於已讀取。

### B. Official Knowledge Extraction

使用 `skills/chinese-textbook-transcriber/SKILL.md` 忠實擷取並建立來源定位。教師手冊中的教學重點、官方分析、答案與提醒仍屬 Official Knowledge，不得降格成隨意參考。

### C. Important Knowledge Analysis

依 `schemas/gemini-source-analysis-report.md` 產生報告。至少分析來源實際包含的下列項目：

1. 課程基本資訊、文體與教材定位。
2. 課文主旨、段落功能、敘事／說明結構與關鍵關係。
3. 正式生字、認讀字、形近字、多音字與字群辨析。
4. 核心語詞、成語、詞義、語境與易混淆處。
5. 句型、修辭、寫作特色及對應課文證據。
6. 閱讀理解問題、答案依據與推論要求。
7. 教師手冊明列的教學重點、教學提醒、學生可能困難與引導方式。
8. 習作／評量對應的能力要求與知識回扣。
9. 圖片、圖表、側欄或版面承載的必要資訊。
10. 來源衝突、OCR 疑義、缺頁與需要教師確認的事項。

來源沒有某類內容時寫 `N/A_SOURCE_NOT_PRESENT`；不得空白，也不得自行創造內容填滿欄位。

### D. Knowledge Prioritization

每個知識點只能列入一種：

- `must_teach`：直接影響本課核心理解、官方學習焦點或習作／評量。
- `should_teach`：支援理解或遷移，但不是本課最低完成條件。
- `optional_extension`：來源外延伸或有時間才處理，必須與 Official Knowledge 分流。
- `teacher_confirmation_required`：來源衝突、判讀不確定或涉及教師取捨。

每個 `must_teach` 至少包含一筆可定位的來源證據、重要性理由、學生可能困難與下游不可遺失條件。

### E. Coverage Validation

逐項完成 coverage matrix。必要來源仍有未讀頁、重要欄位沒有來源定位、報告只重述課文而未分析教師手冊，皆為 FAIL。

### F. HOLD

輸出報告後停止，狀態為 `READY_FOR_GEMINI_KNOWLEDGE_REVIEW`。明確詢問教師是否修正或核准；教師核准後，使用 `skills/chinese-lesson-knowledge-builder/SKILL.md` 組裝或更新 LKB，保存 source fingerprint。LKB 再經教師核准後才記錄 `GEMINI_KNOWLEDGE_GATE_APPROVED`、`APPROVED_LKB_MASTER`，並進入 Core 的下一個合法 stage。

重建時建立新版並保留舊版與失效原因，不得無痕覆蓋已核准母檔。

## 7. 深度判定

每個正式分析節點至少具備：

```yaml
knowledge_point:
  claim: ""
  classification: OFFICIAL_EXPLICIT | AI_ANALYSIS | TEACHER_CONFIRMATION_REQUIRED
  source_evidence:
    - file: ""
      page: ""
      section: ""
      evidence_summary: ""
  observation: ""
  instructional_significance: ""
  student_difficulty_or_misconception: ""
  priority: must_teach | should_teach | optional_extension | teacher_confirmation_required
  downstream_constraint: ""
```

單純列出名詞、複述課文或提供沒有來源的泛用教學建議，不構成分析。

## 8. 禁止事項

- 不因使用者要求成品就跳過分析。
- 不把「附件已上傳」寫成「所有頁面已讀」。
- 不只分析課文而忽略教師手冊、習作、答案與頁面資訊。
- 不用 5～10 個短條列取代完整知識覆蓋。
- 不把 AI 推論寫成官方教材明載。
- 不把 `SOURCE_INVENTORY`、摘要或初稿標記為完成分析。
- 不在 HOLD 前啟動任何下游生成技能。
- 不在有效 LKB 存在時重跑同一份教冊分析。
- 不為簡報、學習單、評量各自建立不同的教材分析母檔。
- 不以模型記憶或舊對話取代實際載入 LKB。
- 不因新任務需要額外欄位就宣告整份 LKB 失效。
- 不把某個下游技能專用的 AI 延伸混入 Official Knowledge。
- 不未經教師核准就把 LKB Patch 合併到正式母檔。

## 9. Failure Codes

- `GEMINI_SOURCE_GATE_SKIPPED`
- `SOURCE_INVENTORY_INCOMPLETE`
- `SOURCE_PAGE_COVERAGE_INCOMPLETE`
- `TEACHER_MANUAL_ANALYSIS_MISSING`
- `WORKBOOK_ALIGNMENT_MISSING`
- `EVIDENCE_NOT_LOCATABLE`
- `ANALYSIS_TOO_SHALLOW`
- `GENERIC_RECOMMENDATION`
- `OFFICIAL_AI_BOUNDARY_BROKEN`
- `GEMINI_DOWNSTREAM_STARTED_EARLY`
- `GEMINI_HOLD_SKIPPED`
- `LKB_MASTER_MISSING`
- `LKB_MASTER_UNAPPROVED`
- `LKB_MASTER_LESSON_MISMATCH`
- `LKB_MASTER_STALE`
- `SOURCE_FINGERPRINT_UNKNOWN`
- `UNNECESSARY_SOURCE_REANALYSIS`
- `LKB_MASTER_PERSISTENCE_BLOCKED`
- `TASK_KNOWLEDGE_REQUIREMENTS_MISSING`
- `LKB_COVERAGE_DIFF_MISSING`
- `LKB_ENRICHMENT_REQUIRED`
- `LKB_PATCH_EVIDENCE_MISSING`
- `LKB_PATCH_UNAPPROVED`
- `LKB_FULL_REBUILD_UNNECESSARY`
- `LESSON_MASTER_INDEX_MISSING`
- `LESSON_MASTER_INDEX_CONFLICT`
- `LKB_PATCH_REBASE_REQUIRED`

任一 failure 未解決時，狀態不得是 `COMPLETE`、`APPROVED` 或任何 downstream-ready 狀態。
