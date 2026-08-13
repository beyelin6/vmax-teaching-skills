# V-MAX Adapter｜Gemini 2.4

## 目的

本檔只定義 Gemini 如何載入與執行 V-MAX。Gemini 可作為分析／生成執行器，但不得以自己的對話記憶、Gem 或專案內舊提示覆蓋 GitHub 現行 Core。

## 啟動契約

每個新的 V-MAX 任務開始時，Gemini 應先取得並讀取：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `runtime/lesson-state.md`
4. Manifest 指定的 current main workflow
5. Manifest 指定的 current executor
6. 當前 stage 需要的 policy / skill
7. `adapters/gemini/source-analysis-contract.md`
8. `schemas/lesson-master-index.md`
9. `core/governance/task-knowledge-requirement-registry.md`
10. `core/ui/teacher-review-view-contract.md`

若平台無法直接讀 GitHub，應透過可用的 Repository / Drive / file bridge 導入以上檔案；若仍無法載入，回報 `BOOTSTRAP_BLOCKED`，不得自行猜流程。

開始工作前必須輸出簡短的 `gemini_load_receipt`，列出實際讀取的檔案、版本或 commit、來源檔與頁面範圍。未實際讀取的檔案不得列入 receipt。

## 母檔優先入口

Gemini 在跑任何流程前，先讀 `Lesson Master Index`，再由 Index 尋找本課已核准的 `Lesson Knowledge Book`（LKB）母檔與其 Source Fingerprint。不得用 Drive 搜尋排序、檔名相似度或對話記憶猜最新版。

```text
REQUEST_RECEIVED
→ READ_LESSON_MASTER_INDEX
→ LOCATE_APPROVED_LKB
→ VERIFY_LESSON_ID_AND_SOURCE_FINGERPRINT
├─ VALID：載入母檔，直接進入 Runtime 的下一個合法 stage
└─ MISSING / STALE / UNAPPROVED：啟動 GEMINI_SOURCE_ANALYSIS_GATE
```

只要本次工作階段出現新上傳或新指定的課本、教師手冊、習作、出版社資源或新課次，而且沒有仍有效的核准 LKB，無論使用者要求什麼成品，都先啟動 `GEMINI_SOURCE_ANALYSIS_GATE`：

```text
SOURCE_FILES_RECEIVED
→ SOURCE_INVENTORY
→ OFFICIAL_KNOWLEDGE_EXTRACTION
→ IMPORTANT_KNOWLEDGE_ANALYSIS
→ KNOWLEDGE_COVERAGE_VALIDATION
→ HOLD_FOR_TEACHER
→ APPROVED_LKB_MASTER
```

Gate 完成前禁止製作簡報、學習單、教案、活動、評量、角色、風格、圖片與任何正式成品。使用者說「直接做」「一次完成」也不能跳過；只能先完成該課重要知識點分析並等待確認。

Gemini 在此情境的第一個實質回應必須是來源盤點與分析進度，不得先展示成品草稿。若來源很多，可分批讀取，但在 coverage PASS 前始終標示進度與未讀範圍，不得為了快速回答縮短分析。

詳細輸出、母檔重用、失效判定與阻擋條件依 `adapters/gemini/source-analysis-contract.md`，報告結構依 `schemas/gemini-source-analysis-report.md`。

有效母檔存在時不得為了「重新分析得更完整」而自行重跑。先載入既有 LKB、保留核准決策，只處理 Runtime 指定的下一階段。若教師要求重做分析，或來源版本確實改變，才建立新版，不覆蓋舊版。

但母檔有效不代表對每個下游任務都已足夠。開始預習單、簡報、教案、評量、活動或圖片前，先依 `core/governance/task-knowledge-requirement-registry.md` 建立 `required_knowledge`，再和 LKB 做 Coverage Diff；Gemini 可增加該課特殊需求，不得刪除 Registry 最低要求。

- 無缺口：`LKB_SUFFICIENT_FOR_TASK`，直接執行。
- 有來源可補的缺口：`LKB_ENRICHMENT_REQUIRED`，只補查相關教冊頁面並建立 LKB Patch。
- 來源未提供：標記 `N/A_SOURCE_NOT_PRESENT`，不得捏造；若需要 AI 延伸，另走 Learning Module，不混入 Official Knowledge。
- Patch 經教師確認並合併成新 LKB 版本後，才執行受影響的下游任務。

增補是局部、可追溯、版本化的；不得因一個欄位不足就整份重跑或刪除既有核准內容。

Patch 必須符合 `schemas/lkb-patch.md`。合併前比較 `base_lkb_version`、active LKB version 與 changed node IDs；衝突時標記 `LKB_PATCH_REBASE_REQUIRED`，不得後寫覆蓋先寫。合併後更新 Lesson Master Index 與受影響任務的 readiness，再重新讀取驗證。

## Runtime 執行

- `runtime/lesson-state.md` 定義 schema；Google Drive 該課 State 決定當前合法位置。
- 教師「確認」只解鎖 `next_allowed_stage`。
- 不得恢復舊版 STEP 3 / STEP 4 或把角色／視覺提前。
- 每次完成 stage 或 HOLD 決策後，應把狀態回寫到 Google Drive 該課 Runtime State；若 Gemini 所在環境無法直接回寫，必須輸出精確 state patch / handoff，不得假裝已同步。
- 新教材尚未取得 `GEMINI_KNOWLEDGE_GATE_APPROVED` 與 `APPROVED_LKB_MASTER` 時，`next_allowed_stage` 只能是來源補讀、分析修訂、LKB 組裝或教師確認。

## 教師畫面

Gemini 的完整分析報告必須保存為可續用母檔，但對話預設只顯示 Teacher Review View。禁止用縮短分析來換取短畫面，也禁止把完整巢狀 JSON 直接丟給教師。

- 第一屏顯示結論、來源證據、知識層、缺口、AI 建議與本次唯一決定。
- 完整明細保存在 LKB／分析報告，教師要求時才展開。
- STEP 1 不完整時只顯示補讀與衝突處理，不開放核准。
- 不得產生 `STEP 2.75` 或跳過 STEP 2／HOLD 2。

## 分析品質

Gemini 不得用摘要取代分析。每個重要判斷必須具備：`source_evidence → observation → instructional_significance → priority → downstream_constraint`。

以下內容不能作為單獨理由：`很重要 / 適合學生 / 增加興趣 / 提升理解 / 可融入教學 / 建議加強`。若使用這些詞，後面必須接具體教材證據、學習困難或能力要求。

正式分析必須：

- 覆蓋課文、教師手冊與習作中實際存在的知識類別。
- 區分官方明載、AI 判讀與待教師確認，不得混寫。
- 對每個 `must_teach` 提供來源頁碼／區塊與重要性理由。
- 說明遺漏、來源衝突、OCR 不確定與未讀頁面。
- 產出下游限制，避免後續技能遺失已確認知識點。

缺少上述證據時標記 `ANALYSIS_TOO_SHALLOW`，不得宣告分析完成。

每次分析輸出結尾固定提供：

```yaml
gemini_execution_receipt:
  current_gate: GEMINI_SOURCE_ANALYSIS_GATE
  lkb_master_status: VALID | MISSING | STALE | UNAPPROVED | LESSON_MISMATCH
  lkb_master_path: ""
  source_fingerprint_match: true | false | unknown
  sources_read: []
  pages_read: []
  pages_unread: []
  artifacts_created: []
  validation_status: PASS | FAIL | BLOCKED
  failure_codes: []
  next_allowed_action: ""
```

Receipt 只記錄可驗證事實；不得把「準備讀取、預計建立、建議執行」列為已完成。

## 圖片能力

Gemini 必須依當前環境實際工具判斷能否生圖，不得把文字模型產生的 prompt 視為圖片。需要圖片時載入 `skills/vmax-image-renderer/SKILL.md`：有圖片生成／編輯與檢視能力才實際渲染並驗證；否則輸出 `IMAGE_HANDOFF_READY`，交給具備能力的 Gemini image/API、Canva 或其他 renderer 執行。

## Gemini 的主要責任

Gemini 可適合：
- 大量教材來源解析與比對
- Source Master 草擬
- 教學候選分析
- Renderer Script / Visual YAML 生成
- NotebookLM 前置資料整理
- 視覺／角色提示語轉譯

但「適合」不代表可跳過來源分析、教師 HOLD 或證據式驗證。

但不得自行改寫：
- Golden Path
- Teacher Intent
- Lesson Map / Session Map
- Knowledge selection
- Runtime stage

## NotebookLM 邊界

Gemini 若要把資料交給 NotebookLM：
- 以 Source Master / Renderer Script / Visual YAML MD 為橋接層。
- NotebookLM 的批次、頁數、格式限制不得反向決定 Lesson / Session 結構。
- 若 NotebookLM 不支援某格式，僅做格式轉譯，不改內容母體與教學結構。

## Google Drive 邊界

- Source Library：讀原始教師手冊／課本／習作。
- V-MAX 教材庫：存完整 Lesson Package。
- 能連 Drive 時應實際驗證；不能連時明確回報 `CONNECTOR_BLOCKED`。

## 核心金句

> Gemini 可以換，V-MAX 不跟著換；平台只負責轉譯與執行。
