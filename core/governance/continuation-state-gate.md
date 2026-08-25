# V-MAX Continuation State Gate 1.0

## 定位

本政策防止 V-MAX 在長對話、上下文整理、平台切換或多個候選版本並存時遺失教師已確認的決定。任何「繼續／下一步／確認／沿用／重新開始／試跑」都必須先通過本 Gate。

核心原則：

> 先同步目前狀態，再決定是否能做下一步；不能用聊天記憶代替 Runtime State。

## 每次啟動或續作必讀

執行器必須實際讀取：

1. GitHub `main` 的 `V-MAX_MANIFEST.md`。
2. Google Drive `V-MAX_Runtime_Index`。
3. 教師指定課次的最新 Runtime State 與 revision。
4. Runtime State 指向的 Source Master、LKB、Learning Modules、Teaching Strategy 與教師確認紀錄。
5. 若任務涉及簡報或視覺：目前 `SLIDE_SCRIPT`、Approved Visual Benchmark、Visual Text DNA、角色定錨、Style Recipe 與上一個代表頁狀態。
6. 若任務涉及簡報或視覺：`output_profile.canvas_profile`、教師選定比例、實際像素、方向、安全邊界與素材 fit mode；畫布未鎖定時不得建立代表頁。

必要檔案或 Drive State 無法實際讀取時，標記 `CONTINUATION_STATE_BLOCKED`，不得用舊對話、模型記憶、上一輪輸出或猜測值繼續。

## State Sync Receipt

在任何分析、設計、生成、改版或批次之前，必須建立本次同步結果，至少包含：

```yaml
state_sync:
  status: PASS | BLOCKED | CONFLICT
  lesson_id:
  runtime_state_id:
  runtime_revision:
  manifest_version:
  executor_version:
  current_stage:
  last_completed_stage:
  next_allowed_stage:
  pending_teacher_decision:
  locked_decisions_loaded: true | false
  source_master_version:
  slide_script_version:
  visual_benchmark_version:
  role_style_version:
  output_profile_version:
  canvas_profile:
  canvas_ratio:
  canvas_width_px:
  canvas_height_px:
  candidate_outputs_preserved: true | false
  conflicts: []
  downstream_impact: []
```

教師介面不直接顯示 raw YAML；只顯示可讀的 State Sync Receipt 摘要與唯一需要教師決定的項目。

## 續作 Gate

只有以下條件全部成立，才可執行下一個合法 stage 或產出：

- `state_sync.status: PASS`。
- `current_stage`、`last_completed_stage` 與 `next_allowed_stage` 互相一致。
- 最新教師確認已回寫 Runtime State；聊天中的「好／確認」若尚未回寫，只能標記為待寫入事件，不得直接推進。
- 本次任務使用的來源版本、逐頁腳本版本與視覺基準版本已載入。
- 若要渲染，當頁的 Verified Teaching Text、版面構圖、角色定錨、字體 DNA 與輸出模式均已存在。
- 若要渲染，`canvas_lock` 必須已鎖定且與 Slide Script、Runtime State、Output Profile 一致；缺少或衝突時標記 `CANVAS_SPEC_BLOCKED`。
- 尚未確認的候選輸出不會被當成鎖定版本。

任一條件不成立，停止並顯示：目前狀態、缺少項目、衝突項目、受影響下游與唯一補救動作；不得先做部分製作。

## 教師決定與候選版本

- 教師的新決定必須先形成一筆可追溯事件，再回寫 Runtime State，最後才可派生下游。
- `v01`、`v02`、`v03` 等圖片或腳本只是候選版本；未經教師確認，不得覆蓋既有確認稿、改寫上游鎖定或自動重算其他頁面。
- 教師拒絕某一候選時，只記錄拒絕理由與受影響範圍，不得把候選內容默默混入下一版。
- Runtime State 與教師最新訊息衝突時，必須列出差異與下游影響並停等；不得自行選邊。

## 防止白做

開始圖片、腳本、PPTX、PNG 或 PDF 製作前，必須確認：

1. 本次唯一工作項目已明確指定。
2. 來源原文與教師確認內容已鎖定。
3. 正向視覺範例與版面規則已載入。
4. 上一版失敗原因與不可重犯事項已載入。
5. 代表頁是否已確認，以及本次是否允許進入批次，已明確記錄。

缺少任一項時，只能回報 `WORK_BLOCKED_BEFORE_RENDER`，不得先生成「試看看」。

## 上下文整理與平台切換

若發生上下文整理、對話中斷、換用 Codex／ChatGPT Work／Gemini／Spark，或使用者只說「繼續」：

- 重新執行完整 State Sync，不沿用上一段對話中的未驗證摘要。
- 先讀最新 Runtime revision，再讀取該 revision 指向的母檔。
- 若最新 revision 與本地候選輸出不同，候選輸出保留但不得自動採用。
- 若無法判定上次停在哪一個 HOLD，標記 `HOLD_POSITION_UNKNOWN` 並停等教師。

## 每次事件後回寫

每次教師確認、修改、拒絕、代表頁通過、代表頁失敗或批次停止後，都要回寫：

- event id 與時間
- 觸發者與教師原話／決定
- 前一狀態與新狀態
- 上游版本與下游影響
- 候選輸出路徑
- 下一個合法 stage 或 HOLD
- 是否需要教師再次確認

若 Drive 回寫失敗，標記 `RUNTIME_WRITE_BLOCKED`，不得宣告狀態已保存，也不得繼續高風險製作。

## 失敗碼

- `CONTINUATION_STATE_BLOCKED`
- `STATE_REVISION_UNKNOWN`
- `STATE_SYNC_STALE`
- `HOLD_POSITION_UNKNOWN`
- `TEACHER_DECISION_NOT_PERSISTED`
- `RUNTIME_WRITE_BLOCKED`
- `WORK_BLOCKED_BEFORE_RENDER`
- `CANDIDATE_VERSION_MIXED`
- `CANVAS_SPEC_BLOCKED`
- `CANVAS_DRIFT`
- `OUTPUT_PROFILE_MISMATCH`
