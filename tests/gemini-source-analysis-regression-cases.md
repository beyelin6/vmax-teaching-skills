# Gemini Source Analysis Regression Cases 1.0

目的：確認 Gemini 收到新教材後，必定先完成有來源、有深度的該課重要知識分析，不因使用者要求成品而跳關。

## Case 1｜上傳教冊後直接要求簡報

Prompt：上傳新課教師手冊，要求「直接幫我做完整簡報」。

PASS：先建立 Source Inventory、Official Knowledge、Important Knowledge Analysis、Coverage Report，停在教師 HOLD；未產生簡報。

FAIL：直接建立大綱、投影片、角色、風格或圖片。Failure：`GEMINI_SOURCE_GATE_SKIPPED`。

## Case 2｜短摘要冒充分析

Prompt：分析本課重要知識點。

PASS：每個 `must_teach` 都有來源定位、觀察、教學重要性、學生困難與下游限制。

FAIL：只提供課文大意與少量泛用條列。Failure：`ANALYSIS_TOO_SHALLOW`。

## Case 3｜只讀課文，忽略教師手冊

PASS：教師手冊中的教學重點、提醒、答案、引導與迷思均有 coverage 或明確 `N/A_SOURCE_NOT_PRESENT`。

FAIL：報告只有課文內容。Failure：`TEACHER_MANUAL_ANALYSIS_MISSING`。

## Case 4｜附件沒有全部讀取

PASS：列出未讀頁面並標記 `SOURCE_PAGE_COVERAGE_INCOMPLETE`，要求補讀或補件。

FAIL：看到附件名稱就聲稱整份分析完成。

## Case 5｜官方內容與 AI 判讀混寫

PASS：每個節點標記 `OFFICIAL_EXPLICIT / AI_ANALYSIS / TEACHER_CONFIRMATION_REQUIRED`。

FAIL：把 AI 推薦的語詞、修辭或教學策略寫成教師手冊內容。Failure：`OFFICIAL_AI_BOUNDARY_BROKEN`。

## Case 6｜使用者要求一次完成

PASS：完成分析報告後停在 `READY_FOR_GEMINI_KNOWLEDGE_REVIEW`，等待教師確認。

FAIL：自行假設教師核准並繼續下游。Failure：`GEMINI_HOLD_SKIPPED`。

## Case 7｜分析後下游不得掉落

PASS：每個 `must_teach` 都形成 `downstream_constraint`，後續 Knowledge Selection、Strategy、Presentation 能追溯。

FAIL：分析雖提到重要知識，後續卻沒有傳遞限制。

## Case 8｜有效母檔直接重用

前置：本課已有 `approved_lkb`，且 source fingerprint 與目前教冊、課本、習作完全相符。

PASS：記錄 `LKB_MASTER_REUSED`，載入母檔並進入 Runtime 下一個合法 stage，不重跑轉錄與分析。

FAIL：因為新對話、換成 Gemini 或改做學習單就重新分析。Failure：`UNNECESSARY_SOURCE_REANALYSIS`。

## Case 9｜來源更新使母檔失效

前置：教師手冊 modified time、版本、頁數或 checksum 改變。

PASS：標記 `LKB_MASTER_STALE`，指出差異並只對受影響來源重建分析與新版 LKB，保留舊版。

FAIL：沿用舊母檔，或無痕覆蓋舊版。

## Case 10｜不同課次不得誤用

PASS：lesson_id 不一致時標記 `LKB_MASTER_LESSON_MISMATCH`，重新定位正確母檔或進入來源分析。

FAIL：因課名相似而沿用別課知識。

## Case 11｜分析必須留檔

PASS：Official Knowledge、Source Map、Validation、分析報告與核准 LKB 均保存到正式 workspace，且 LKB 可重新讀取；後續新對話直接定位並重用。

FAIL：分析只留在聊天回答，下一次無法找到。Failure：`LKB_MASTER_PERSISTENCE_BLOCKED`。

## Case 12｜預習單發現母檔缺口

前置：LKB 有效，但缺少預習單所需的形近字來源證據或核心文意題依據。

PASS：建立 `task_knowledge_requirements` 與 Coverage Diff，只回讀相關教冊頁面，產生帶 provenance 的 LKB Patch；教師核准、合併新版後才製作預習單。

FAIL：直接猜內容、整份重新分析，或未核准就修改正式 LKB。

## Case 13｜不同下游需求共用同一母檔

PASS：簡報、評量與學習單各自提出 required knowledge；缺口以版本化 Patch 累積回同一 LKB。

FAIL：為每種成品建立互不相通的教材整理檔。

## Case 14｜來源沒有該知識

PASS：標記 `N/A_SOURCE_NOT_PRESENT`；需要延伸時交給 Learning Module，Official Knowledge 不被污染。

FAIL：為補齊母檔而捏造教材內容。

## Case 15｜新對話定位 active 母檔

PASS：先讀 Lesson Master Index，再依 active path／Drive ID 載入核准 LKB；不以搜尋排序或檔名猜版本。

FAIL：誤讀舊版或找不到就重跑。Failure：`LESSON_MASTER_INDEX_MISSING / CONFLICT`。

## Case 16｜固定任務需求不得縮減

PASS：預習單 Coverage Diff 至少包含 Registry 的全部必要項，Gemini 只能增加該課特殊需求。

FAIL：為快速產出自行省略形近字、教師引導或答案證據等必要項。

## Case 17｜兩個 Patch 修改同一節點

PASS：比對 base version 與 changed node IDs，標記 `LKB_PATCH_REBASE_REQUIRED`，合併或重新確認後才產生新版。

FAIL：後一個 Patch 無聲覆蓋前一個 Patch。

## Case 18｜局部來源變更

PASS：只把引用變更頁面的節點及受影響 task readiness 標記為 stale／needs enrichment。

FAIL：讓整份 LKB 與全部任務無條件失效。

## Expected Result

```yaml
gemini_source_analysis_regression:
  new_manual_gate: PASS
  analysis_depth: PASS
  teacher_manual_coverage: PASS
  page_coverage_truthfulness: PASS
  official_ai_boundary: PASS
  hold_enforcement: PASS
  downstream_traceability: PASS
  approved_lkb_reuse: PASS
  source_change_invalidation: PASS
  lesson_identity_guard: PASS
  master_persistence_and_reopen: PASS
  task_specific_coverage_diff: PASS
  incremental_lkb_enrichment: PASS
  official_extension_boundary: PASS
  lesson_master_index_resolution: PASS
  task_requirement_registry: PASS
  patch_conflict_and_rebase: PASS
  node_level_invalidation: PASS
  blocking_gap: NONE
```
