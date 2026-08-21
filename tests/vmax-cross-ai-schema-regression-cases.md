# V-MAX Cross-AI Schema Regression Cases 0.1.0

## 用途

驗證 Codex、ChatGPT、Gemini、Antigravity、Spark 或其他讀取同一 repository 的工具，使用同一套 V-MAX schema 時，不會自行跳階段、選邊或放行未確認內容。

## S-01｜Schema package 完整

PASS：`core/schemas/vmax/README.md` 與所有核心 JSON Schema 都存在且可解析，且 package manifest、範例與 migration policy 均存在。

## S-02｜Source Master 來源分層

PASS：Source Master 分開保存 `OFFICIAL_TEXT`、`TEXTBOOK_MARKUP`、`PUBLISHER_TEACHER_RESOURCE`、`TEACHER_KNOWLEDGE`、`AI_SUGGESTION`、`EXTENSION`。

BLOCKER：AI 建議寫入課文原文；教冊說明覆寫課本原文；來源層混成單一 authority。

## S-03｜Source evidence 定位

PASS：證據可保存 `pdf_page`、`printed_page`、`region_ref`、`crop_ref` 與分層 fingerprint。

BLOCKER：只有無法回看的檔名或頁碼，無法定位小字區、部首標記或邊欄。

## S-04｜完整候選不等於教師選教

PASS：`CANDIDATE_INVENTORY` 可以完整列出候選，但未經教師確認不得進正式學生產出。

BLOCKER：AI 將候選直接寫成 `MUST_TEACH` 或直接進 Slide Script。

補充：`CANDIDATE_INVENTORY` 不保存 `teacher_decision`；教師決定只寫入 `APPROVED_TEACHING_SELECTION`，且必須有 `confirmed_by_teacher: true`。

## S-05｜HOLD 必須停等

PASS：HOLD 有證據、衝突摘要、至少一筆 downstream impact 與教師必須決定的問題。

BLOCKER：沒有影響清單仍繼續；AI 選項被視為教師決定；raw machine payload 取代確認卡。

## S-06｜狀態轉移

PASS：`TEACHER_REVIEW → LESSON_LOCKED` 有教師確認；`OUTPUT_QA` 失敗只能回到 `OUTPUT_DRAFT`。

BLOCKER：`BATCH_DRAFT → APPROVED_OUTPUT`、`TEACHER_REVIEW → APPROVED_OUTPUT` 或 `SUPERSEDED → OUTPUT_DRAFT`。

補充：`STATUS_TRANSITION` 必須符合 schema 的合法 from/to/actor 組合；`OUTPUT_QA → APPROVED_OUTPUT` 另需教師確認參照與 QA gate summary。

## S-07｜最小必要回退

PASS：只改單頁圖片只影響該頁與直接下游；改教學選擇回到 Phase 2；改來源文字回到 Phase 1。

BLOCKER：局部修改自動重算整課、整冊或歷史版本。

## S-08｜Slide Script 單一主檔

PASS：NotebookLM、Google Slides、Canva、PPTX、PNG／PDF 都保留 `derived_from`，且不回寫 Slide Script。

BLOCKER：平台 adapter 自行補頁、改寫課文、改變順序或形成第二份簡報主檔。

## S-09｜學生層

PASS：學生層只使用已確認內容，可有簡短非答案任務提示；沒有答案、講者備註或未確認延伸。

BLOCKER：圖片層承載正式文字；學生頁出現答案提示；Extension 未經教師確認即顯示。

## S-10｜跨平台一致性

同一份物件交給不同 AI 時，所有平台都應辨識：

- 未解決來源衝突
- OPEN HOLD
- 未確認候選
- 非法狀態轉移
- 學生層答案提示
- 不完整版本鏈

若平台無法執行某些 conditional schema，仍必須依 README 與本 regression case 阻擋流程，不得自行放行。

## S-20｜Spark Teacher Review View
PASS：Spark 讀取 Runtime State 後，將 Machine Payload 轉換為教師可讀的 Teacher Review View；JSON 僅保存於母檔或教師明確要求時顯示。
BLOCKER：直接顯示 `vocabulary[]`、`shapeSimilar`、`polyphonic`、`idiom` 或完整 JSON code block 取代確認卡；未讀取 Runtime State 就重新開啟舊 stage；沒有教師確認就要求進入下一階段。

## S-11｜NotebookLM 雙輸入包

PASS：Knowledge Source Package 與 Slide／Audio Package 分開；前者保存完整來源與核准知識，後者由已核准 Slide Script 派生。

BLOCKER：把簡報腳本混入知識來源包後讓 NotebookLM 自行重排，或讓 NotebookLM 產物回寫 Source Master／Slide Script。

## S-12｜PPTX 教師要求條件

PASS：只有存在 `pptx_requested_by_teacher: true` 時才生成 PPTX；人工修改保留衍生關係且不回寫上游。

BLOCKER：沒有教師要求卻自動生成 PPTX，或把 PPTX 人工改字當成新的簡報主檔。

## S-13｜Source Ingestion Record

PASS：Phase 1 先建立 `SOURCE_INGESTION_RECORD`，逐頁保存正文、底欄、小字區、部首標記、詞語框、句型／修辭框與出版社備註的掃描狀態、完整擷取文字與證據定位。

BLOCKER：只保存 PDF 路徑或摘要；`UNCERTAIN` 被當成 `NOT_FOUND`；擷取記錄中混入教師選教或 AI 教學決策；沒有 ingestion record 就直接組裝 Source Master。

## S-14｜Learning Modules／Teaching Strategy 核准狀態

PASS：Learning Module Profile 與 Teaching Strategy Profile 都保存 Source Master、Approved Teaching Selection、LKB、版本與直接上游；`CONFIRMED` 狀態與教師確認狀態一致。

BLOCKER：未確認的 Learning Module 或 Teaching Strategy 進入 Presentation Engine；只改一個狀態欄位就繞過教師確認；companion object 反向改寫 Source Master。

## S-15｜角色核心 DNA 與風格核心

PASS：角色保存 `base_character_id`／`core_dna_ref`，情境變體只記錄允許變化與保留 DNA；風格分成 `style_core` 與 `page_variants`，兩者都有教師確認版本。

BLOCKER：只沿用角色名稱而沒有 DNA 參照；換課或換頁型時改變臉型、髮型、配色或畫風；頁型變體自行改掉整課核心風格。

## S-16｜頁面骨架必須先停等

PASS：Presentation Engine 先產生頁面骨架，至少包含頁序、頁面目的、頁型、主要教學焦點、頁數估算與左右構圖方向；教師確認後才展開逐頁詳細腳本。

BLOCKER：AI 直接生成完整逐頁腳本、圖片或平台匯入腳本，未經頁面骨架確認；AI 自行決定衝突的頁序、頁數或教學焦點。

## S-17｜左右構圖不可被當成固定模板

PASS：每頁明確記錄 `TEXT_LEFT_IMAGE_RIGHT`、`IMAGE_LEFT_TEXT_RIGHT` 或教師確認的其他配置；AI 依文字量、角色視線、圖像動線與閱讀順序提出理由。

BLOCKER：Skill 固定所有頁面文字在左、圖片在右；或在教師確認配置後自行交換左右位置。

## S-18｜圖片文字層與文字真值分離

PASS：`SLIDE_SCRIPT` 保存可驗證的 Verified Teaching Text；圖片式簡報以 `VERIFIED_RASTER_TEXT_LAYERS` 渲染，每個文字區塊都有 `source_ref`、可見層、位置與局部修復範圍。

BLOCKER：把生圖模型產生的中文字當成教材真值；把所有文字合成一個不可局部修復的圖片；或圖片層文字沒有來源引用。

## S-19｜PPTX 只能下游派生

PASS：只有 `pptx_requested_by_teacher: true` 才建立 PPTX；PPTX 的可編輯文字由 Verified Teaching Text 派生，並保留 `derived_from`。人工修改不回寫 Slide Script。

BLOCKER：未經教師要求自動生成 PPTX；將 PPTX 修改結果當成新的簡報主檔；或因 PPTX 可編輯而改用它取代圖片式簡報主檔。

## S-20｜局部文字修復

PASS：文字錯字、缺字、位置或樣式錯誤時，建立新的文字層版本並標記 `repair_scope: LOCAL_LAYER_ONLY`；未受影響的背景、角色、其他文字層與頁面版本保持不變。

BLOCKER：修正一個中文字就重生整頁，或為了保留整頁而接受未驗證文字；局部修復後沒有更新版本與衍生關係。

## S-24｜圖片化文字不可退化為打字排版
PASS：正式文字層與插圖、色塊、標籤、角色視線及留白共同構成整頁圖片化視覺；已通過的插圖可鎖定，只局部重建文字層。
BLOCKER：成品只是背景圖上放置普通文字框、文件段落或 PowerPoint 文字框；即使文字正確，也標記 `TYPED_TEXT_LAYOUT_FAIL`，不得交付。

## S-21｜平台 Adapter 只做轉譯

PASS：NotebookLM、Google Slides、Canva 都從同一份已核准 `SLIDE_SCRIPT` 派生；保留頁序、`slide_id`、學生／教師層、來源引用與 `derived_from`。

BLOCKER：平台 adapter 自行補頁、刪頁、改變教學順序、改寫課文、加入未確認延伸，或把平台修改回寫成新的 `SLIDE_SCRIPT`。

## S-22｜圖片式輸出與可編輯輸出分流

PASS：NotebookLM、圖片式 Google Slides、Canva 視覺輸出預設使用 `VERIFIED_RASTER_TEXT_LAYERS`；只有教師指定可編輯輸出時，才派生 Native Text。

BLOCKER：平台因方便編輯而直接把 Native Text 當成圖片式簡報主檔，或未經教師指定自動產生可編輯 PPTX／投影片。

## S-23｜平台能力不足必須回報

PASS：若平台無法完整保留頁序、文字層、圖片品質或角色視覺，標記 `RENDERER_CAPABILITY_BLOCKED` 或平台對應的 `HANDOFF_READY`，並列出受影響頁面。

BLOCKER：平台限制導致內容靜默縮水、錯字未修、頁面重排或教師未看見的輸出差異。

## S-24｜簡報畫布比例

PASS：所有 presentation `STYLE_SELECTION_PROFILE`、Slide Script 與 slide Render Request 使用 `16:9` 橫式；worksheet 等非簡報輸出仍依自己的 Output Profile。

BLOCKER：AI 將簡報改成 `9:16`、A4 或其他比例；自動重算既有歷史成品；或把學習單的 A4 比例套用到簡報。
