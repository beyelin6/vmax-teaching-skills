# V-MAX Workflow HOLD Regression Cases 1.13

## 用途

本檔用真實失敗案例檢查 V-MAX 在重跑時是否仍遵守：Teacher UI、STEP 1 邊界、認讀字雙來源核對、STEP 2 / 2.5 / 2.6、三四年級生字聚焦、多音字來源 Gate、文本嵌入、Lesson Visual Map 保留、單階段前進與頁數延後。

---

## W-01｜STEP 1 不得提前進視覺／情境
PASS：教材真值、課文結構、完整正式生字、認讀字 status、教材詞語／成語／語文活動、來源與待確認處、HOLD 1。
BLOCKER：Scenario / Character / Style / 頁數先決定。

## W-02｜STEP 2.5 必須先分析，再推薦
形近字 PASS：注音、部件、詞義、共同／差異、混淆點、辨認提示、推薦指數與理由。
多音字 PASS：合法來源、各讀音、語意、課文／生活語境、易混淆點、推薦理由。
成語 PASS：推薦指數、理由、教學層級；不提前鎖最終頁型。

## W-03｜預習單 3–5 組不得裁切正式教學
PASS：正式生字完整、Knowledge Lab 無 3–5 組硬上限、P3/PX 不等於刪除。

## W-04｜HOLD 教師介面優先
PASS：Teacher Confirmation Card → 明確 HOLD → 最少決策方式 → 唯一下一步。machine payload 不得當主要 UI。

## W-05｜STEP 2.5、2.6、Knowledge Lab 不可合併
PASS：2.5 做語文分析與保留；2.6 做成語例句／理解／視覺關係；Knowledge Lab 後段才分 Chunk。

## W-06｜AI 教學推薦不可被跳過
PASS：頁數／逐頁腳本之前必須先看見有理由的推薦、可縮短與 Bonus，並停 HOLD 2。

## W-07｜文本單位不得機械套固定模板
PASS：每段／詩節依自己的理解任務決定頁數與教法。
BLOCKER：每段固定步驟、固定頁數、固定問題數。

## W-08｜頁數只能在 Slide Architecture 後估算
PASS：Teacher Intent、Lesson Map、Session Map、Knowledge Lab、Visual Grammar / Slide Architecture 已成立。

## W-09｜一次確認不得飛站
```text
HOLD 1 → STEP 2 → HOLD 2
HOLD 2 → STEP 2.5 → HOLD 2.5
HOLD 2.5 → STEP 2.6 → HOLD 2.6
HOLD 2.6 → Teacher Intent Lock
```

## W-10｜HOLD 下一步指向必須正確
禁止 HOLD 2 指向頁數／角色／風格；禁止 HOLD 2.5 直接跳 Teacher Intent；禁止 HOLD 2.6 跳逐頁腳本。

## W-11｜成語不能只留下名稱
PASS：每個保留成語仍可追溯 student_friendly_meaning、life_example、understanding_goal、visual_expression、independent_page_recommendation。
FAIL：只有名稱／定義、沒有生活例句、所有成語固定同一漫畫格數。

## W-12｜三、四年級生字：AI 只主動形近字＋多音字
### 真實失敗模式
系統把「易錯字／字形複雜／字源有趣／評量重要」變成第三個 AI 自動深教入口，或每個生字平均做獨立頁。

### PASS
- 教材正式生字全部留在 Source / 基礎識寫層。
- AI 主動深教只有 `SHAPE_NEAR`、`POLYPHONIC`。
- 一般單字為 `BASIC_LITERACY_ONLY`，不自動獨立成頁。
- AI 想提醒單字，只能標 `AI_SUGGESTION_SINGLE_CHARACTER`。
- 只有教師明確指定，才升級 `TEACHER_ADDED_SINGLE_CHARACTER`。

### BLOCKER
- `ERROR_PRONE_WRITING` 成為 AI 自動第三入口。
- 「特殊構形／語義／評量價值」直接讓 AI 建單字頁。
- 每字固定同規格頁面。

分類：`SINGLE_CHARACTER_AUTO_DEEPENING / CHARACTER_SCOPE_EXPANSION / CHARACTER_DEPTH_FLATTENING`

## W-13｜認讀字必須雙來源核對
PASS：同時檢查課文頁下方小字與課後獨立生字表／生字教學頁。
- 無方格只作線索，不單獨判定。
- 兩處不一致 → `SOURCE_CONFLICT`。
- 來源無認讀字 → `N/A_SOURCE_NOT_PRESENT`。
BLOCKER：只看一處、把形近補充字當認讀字、無方格直接等於認讀字。

## W-14｜多音字來源不得滲漏
PASS 合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`（AI 只從本課正式生字推薦）
3. `TEACHER_ADDED_POLYPHONIC`

BLOCKER：
- 形近補充字因本身多音被 AI 拉進多音字單元。
- 認讀字／比較字／課文一般字被 AI 自動升級多音字。

分類：`POLYPHONIC_SOURCE_LEAK`

## W-15｜語詞、句型、修辭不得脫離原文
PASS：
- 語詞：原文片段＋語詞＋學生易懂意義。
- 句型：課文原句＋結構＋仿用。
- 修辭：原文 → 發現效果 → 命名。
FAIL：語詞只有定義、句型只有公式、修辭只有名稱。

## W-16｜已選整課圖像心智地圖不得消失
PASS：若教師已選 Lesson Visual Map，簡報大綱、Slide Architecture、頁數估算、Renderer 都明確保留。
FAIL：只藏在策略欄、簡報大綱找不到、後段靜默刪除。
分類：`LVM_OUTLINE_DROPPED`

## W-17｜Drive 歸檔不得回到舊五類結構
PASS：每課版本固定六類：
`01_教材整理 / 02_逐頁腳本 / 03_NotebookLM / 04_角色視覺 / 05_簡報成品 / 06_延伸教材`。
完整重做依 Drive 現況建立 `_01 / _02...`，上傳後再 list/search 驗證。
FAIL：使用舊 `01_來源主檔 / 02_生成腳本 / 03_角色與視覺資產 / 04_簡報成品 / 05_學習單` 結構。

## W-18｜真實失敗：大段 JSON、STEP 1 未完整與 STEP 2.75

輸入情境：STEP 1 以巢狀 JSON 顯示 Mode、教學主軸與固定每節迴圈，同時承認完整生字／認讀字尚未逐字核對；教師回覆「確認」後直接進 STEP 2.5，並宣告下一步 STEP 2.75。

### PASS
- 對話只顯示 Teacher Review View，完整 JSON 保存為 Machine Payload。
- 因必要來源未完成，狀態為 `STEP1_INCOMPLETE`，不開放核准。
- Mode、教學主軸、固定段落迴圈移出 STEP 1。
- 教材項目明確標記知識層及 provenance。
- 完整後遵守 `HOLD 1 → STEP 2 → HOLD 2`。
- 明確拒絕不存在的 `STEP 2.75`。

### BLOCKER
- raw JSON 是主要教師畫面。
- 一面承認來源未核對，一面要求核准 STEP 1。
- 一次確認後跳到 STEP 2.5。
- 把字典查核當作教材來源證明。
- 下一步指向 STEP 2.75。

分類：`RAW_SCHEMA_DUMP / TEACHER_INTERFACE_OVERLOAD / STEP1_INCOMPLETE / KNOWLEDGE_LAYER_MIXED / PREMATURE_DESIGN_LOCK / TEMPLATE_FLATTENING / STAGE_LEAP / SKIPPED_HOLD / LEGACY_STAGE_ALIAS`

## W-19｜STEP 2.5 必須以審核表停等

### PASS
- 只顯示形近字、多音字、教材詞語／成語審核表與待確認項目。
- 每項顯示來源狀態、證據、核對結果、AI 建議與教師決定。
- 最後停在 HOLD 2.5，等待「確認」或修改。

### BLOCKER
- 顯示 raw JSON、內部狀態欄位或空白程式碼框。
- 未完成來源核對卻標成已鎖定。
- 同一回覆提前展開六個詩節或其他教學流程。

分類：`RAW_SCHEMA_DUMP / SOURCE_STATUS_MISSING / UNVERIFIED_ITEM_LOCKED / SKIPPED_HOLD`

## W-20｜ChatGPT 更新後仍走舊 Orchestrator

輸入情境：教師要求重新開始第一課。模型未顯示版本回條，直接宣布引導模式，STEP 1 顯示 raw JSON、Mode A、AI 教學主軸、visualStructureRecommendation 與保留角色 Bone。

### PASS
- 第一行顯示 `V-MAX LOAD`，版本來自實際讀取檔案。
- 先由 `vmax-teaching-skills` 路由至 Golden Path Executor。
- Course Orchestrator 只管理專案成果，不產生 STEP 1。
- 角色 Bone 只記為 deferred input，不在 STEP 1 顯示。
- STEP 1 只呈現教材真值、來源與缺口的 Teacher Review View。

### BLOCKER
- 沒有載入回條仍開始分析。
- Course Orchestrator 的成果依賴圖被當成正式流程。
- STEP 1 顯示 Mode、角色、視覺建議或 AI 教學主軸。

分類：`LOAD_RECEIPT_MISSING / V-MAX_FRONT_DOOR_REQUIRED / WRONG_EXECUTOR_SELECTED / PREMATURE_DESIGN_LOCK / RAW_SCHEMA_DUMP`

## W-21｜長對話／換平台續作不得靠記憶

輸入情境：前一輪已完成部分簡報候選與教師修正，對話中斷或改用另一個 AI；教師只說「繼續」。聊天中存在多個候選版本，但 Google Drive Runtime State 尚未載入或 revision 不明。

### PASS

- 先讀 GitHub Manifest、Google Drive Runtime Index 與指定課次最新 State。
- 建立 State Sync Receipt，顯示目前 stage、唯一下一步、教師最新決定、上游版本、視覺基準與候選版本狀態。
- Runtime revision 不明、State 與聊天內容衝突或教師決定尚未回寫時，標記 `CONTINUATION_STATE_BLOCKED`。
- 只列出缺少項目、衝突與受影響下游，等待教師決定；不生成圖片、腳本、學習單或批次成果。
- 上下文整理或換平台後重新執行完整同步，不沿用上一段摘要。

### BLOCKER

- 依聊天記憶猜測目前課次、stage、HOLD 或最新版本。
- 直接採用本地候選輸出覆蓋 Drive State 或已確認稿。
- State 尚未同步就開始「先試跑一張」。
- 將未確認候選混入下一版或靜默重算下游。

分類：`CONTINUATION_STATE_BLOCKED / STATE_REVISION_UNKNOWN / HOLD_POSITION_UNKNOWN / TEACHER_DECISION_NOT_PERSISTED / CANDIDATE_VERSION_MIXED / WORK_BLOCKED_BEFORE_RENDER`

---

## W-22｜簡報畫布比例不得漂移

輸入情境：同一輪候選成果曾出現 16:9、4:3 或 3:2；教師要求繼續製作，但 Slide Script、Render Request 或 Runtime State 沒有共同的畫布鎖定。

### PASS

- 若沒有已確認畫布，先只詢問教師選擇 4:3 或 16:9；不能讓 provider 自行決定。
- 教師選定後建立同一份 `canvas_lock`，含 profile、比例、實際寬高、方向、安全邊界、fit mode 與決定紀錄。
- 代表頁與批次輸出都驗證實際 PNG／PDF 尺寸，拒絕另一比例、3:2、9:16 或平台預設尺寸。
- 外部插圖與角色圖只能等比縮放、contain 或已記錄的核准裁切；不可拉伸。
- 畫布設定缺失、衝突或成品漂移時，停止渲染並列出受影響下游。

### BLOCKER

- 直接沿用聊天記憶猜測本課要 16:9。
- 同一份簡報混用 16:9、4:3 或 3:2。
- 先生成圖片，最後才嘗試裁成目標比例。
- 為填滿畫布拉伸角色、插圖或文字元件。

分類：`CANVAS_SPEC_BLOCKED / CANVAS_DRIFT / OUTPUT_PROFILE_MISMATCH / ASSET_STRETCH_DETECTED / ASSET_CROP_UNAUDITED`

---

## W-23｜文字層不得退化成打字貼圖

輸入情境：同一課同時存在路線圖式總覽頁、情境語詞頁與完整課文頁；候選稿中有文字融入畫面，也有左右硬切、四格拼貼與逐行打字版。

### PASS

- 依頁型選擇文字施工方式：總覽短句融入路線／物件，情境頁使用物件錨定標籤，課文頁保留連續原文文字元件。
- 所有正式文字先經校對，再以透明圖片元件嵌入紙張、筆刷、書頁、泡泡或自然留白。
- 文字與插圖、角色視線、動作或原文位置有明確關係。
- 文字密度、段落連續性、學生／教師層分流與投影可讀性均通過檢查。

### BLOCKER

- 課文與圖片左右硬切，互不參與理解。
- 每句或每個詞被拆成獨立卡片、平均四格或固定資訊框。
- 語詞解釋過小、脫離段落或只是裝飾性貼字。
- 幸福證據、進度卡、教師答案或講者備註出現在學生頁。

分類：`TYPED_TEXT_LAYOUT_FAIL / TEXT_OBJECT_DETACHED / TEXT_DENSITY_OVERLOAD / PARAGRAPH_FRAGMENTED / ANSWER_LEAK / TEACHER_LAYER_LEAK`

---

## 整體 PASS

```yaml
workflow_hold_regression:
  source_anchor: PASS
  recognition_dual_source: PASS
  step2_recommendation: PASS
  step2_5_analysis: PASS
  teacher_only_single_character: PASS
  polyphonic_source_gate: PASS
  idiom_expression_preserved: PASS
  text_embedded_language: PASS
  lesson_visual_map_preserved: PASS
  drive_archive_structure: PASS
  no_template_drift: PASS
  no_premature_page_lock: PASS
  single_stage_advance: PASS
  teacher_review_view: PASS
  machine_payload_separated: PASS
  step1_incomplete_blocked: PASS
  no_step_2_75: PASS
  step2_5_review_table: PASS
  source_status_visible: PASS
  unverified_not_locked: PASS
  front_door_loaded: PASS
  load_receipt_rendered: PASS
  course_orchestrator_not_stage_machine: PASS
  continuation_state_sync: PASS
  no_render_before_state_sync: PASS
  canvas_lock: PASS
  no_4_3_or_3_2_drift: PASS
  no_asset_stretch: PASS
  text_layer_construction: PASS
  no_typed_text_split_layout: PASS
```

任一 FAIL，不得宣告工作流回歸測試完成。

## STEP 1 整合擷取回歸情境

以下是行為驗收案例，需以執行記錄判斷，不以規則文字匹配當成已通過。

| 輸入情境 | 預期行為 | 失敗判準 |
| --- | --- | --- |
| 原始教冊完整可讀，舊摘要少一個生字 | 核對正式字表及原頁，補漏後繼續全課擷取 | 每發現一字即停問教師是否收錄 |
| 多音字主欄旁有補充框，含另外讀音、例詞及例句 | 全數擷取並保留主欄／補充來源，選教留待 STEP 2.5 | 只記字名或把教材補充當 AI 擴張而忽略 |
| 一頁局部 OCR 不清，其餘頁可讀 | 回看原圖；仍不清則登錄，完成獨立項目後集中報缺口 | 每翻一頁就要求繼續，或憑猜測填字 |
| 兩份原始來源不同，其他內容可查 | 保留差異、完成獨立核對後集中請求裁定 | 靜默選一邊，或把已命名衝突算成完整 |
| 必要例句／教學欄尚未擷取，教師只說繼續 | 補齊同一 stage；缺口未解不開放完整 HOLD 1 核准 | 用摘要或方向確認取代來源完整性 |
| STEP 1 沒有 LKB、角色、風格、畫布或代表頁 | 記為本階段尚未產生，持續擷取 | 因缺少後段輸出而 BLOCKED |
| 教師指定另一課，Index active lesson 尚為前課 | 核對指定課 State、記錄切換、更新 Index 後繼續適用 stage | 僅因 active lesson 不同而要求舊課素材 |
| 明確重製且舊 P01 缺失，已核准來源可驗證 | 新 revision 保留舊成果，核驗並引用來源，從記錄的新起點執行 | 為來源重整索取舊 P01，或把所有核准來源丟棄 |
| 教師只針對一字回答是 | 只記該字裁定，完成其他核對後才請求來源整體核准 | 擴張成其他改字或整份 STEP 1 已核准 |
| 擷取全部完成但尚未教師核准 | 一份整合審核入口停在 HOLD 1，保存 State／Index | 直接進 STEP 2，或只給多張零散檔案卡片 |

## 確認範圍與重製引用補充驗收

- 兩份原始字表衝突，教師裁定其中一字：只 resolve 該 SOURCE_CONFLICT，回 STEP 1 重驗；即使最後一個缺口解決，也須展示整體版本後另取 HOLD 1 核准。
- UNCERTAIN 全有名稱但仍未解：保持 NEEDS_REVIEW，不得因已登錄就 EXTRACTION_VERIFIED。
- 多選項沒有唯一推薦，教師回覆「是」：保持原 stage，釐清該決定；不得自動選第一項或關閉整體 HOLD。
- 新來源重整分支只歷史引用舊 P01：缺圖不阻擋來源整理；若本次明確沿用 P01，則依有效輸入檢核阻擋，不能用重製豁免。

## STEP 1 持續執行驗收

- State Sync 通過、STEP1_INCOMPLETE、next_allowed_stage 為空，PDF 可讀且尚有五頁：持續擷取五頁，不等教師再次說繼續；不進 STEP 2。
- 原頁可回看、頁碼與 region_ref 明確、crop_ref 為 null：允許完整性驗收，不為補裁切檔阻塞；必要影像辨識仍要實做。
- 影像工具失敗但文字層與其他頁仍可處理：先完成獨立工作，最後集中列出工具錯誤與需協助項目，不假稱已核對影像或承諾背景完成。

## 擷取效率驗收

- 已知來源 file ID、版本未變、七頁已驗證只缺一個旁欄：讀取既有結果並補該旁欄，不重新轉錄七頁。
- 課文與語文清單齊全，只剩通用分組指令未抄：標明清單外範圍，允許完整稿審核；多音字例句若缺漏仍阻塞。
- 同一頁含通用教學步驟與字義辨析：保留辨析全文及來源，不能整欄刪除。
- 文字層順序可靠：重用文字資料核對各類別；只有一表格欄位不明時回看該區影像，不反覆 OCR 全課。
- 教師明確要求全文轉錄：通用教師操作也收錄，不能以效率規則刪掉教師指定範圍。
- 完成數頁文字但未發生確認事件：合併保存變動；不因每頁存檔製作整課快照，正式 stage／HOLD 仍完成雲端同步驗證。
