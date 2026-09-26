# V-MAX Adapter｜ChatGPT 1.9

## Lesson Artifact Registry

製作預習單、課後短文單或簡報前，必須讀取 `core/governance/lesson-artifact-registry.md` 與該課 registry（若存在），優先引用 `APPROVED`／`LOCKED`／`FINAL` artifact，並在下游輸出保留 `source_artifact_refs`。

## 目的

本檔只處理 ChatGPT 如何載入、執行與回寫 V-MAX；不得改寫 V-MAX Core。

## 啟動契約

每個新的 V-MAX 任務開始時，ChatGPT 應先：

1. 讀取 `V-MAX_BOOTSTRAP.md`
2. 讀取 `V-MAX_MANIFEST.md`
3. 讀取 `runtime/lesson-state.md`
4. 依 Manifest 讀取 current main workflow 與 current executor
5. 只載入當前 stage 直接需要的 policy / skill
6. 任何教師審核或 HOLD 載入 `core/ui/teacher-review-view-contract.md`

先實際嘗試可用 GitHub 讀取工具；失敗依 Bootstrap 的可信 LKG fallback 處理，無可信規格才回報 `BOOTSTRAP_BLOCKED`，不得假裝已載入。

## Runtime 執行

- `runtime/lesson-state.md` 只提供 schema 與位置規則；以 Google Drive 該課 State 的 `current_stage` 為目前真實位置。
- 使用者回覆「確認／好／可以／OK／沿用」時，依對應 HOLD 範圍執行下一個合法 stage；局部來源裁定只回到 current_stage 補齊來源，不推定全文核准。next_allowed_stage 為空不阻擋 current_stage 的合法未完成工作。
- 不得以聊天記憶、舊對話、模型習慣自行補回舊版 STEP 3 / STEP 4。
- 每完成正式 stage 或 HOLD 決策後，應更新 Runtime State，再繼續後續工作。
- 若當前對話內容與 Runtime State 衝突，以教師最新明確決策優先；修正 Runtime 後再續跑。

## GitHub / Drive 邊界

- GitHub：V-MAX 規格、版本與 Runtime schema 的 Source of Truth。
- Google Drive `00_Runtime_State`：每一課實際 Runtime State 的 Source of Truth。
- Google Drive Source Library：原始教師手冊／課本／習作來源。
- Google Drive V-MAX 教材庫：完整 Lesson Package 歸檔。

ChatGPT 不得以「使用者先前上傳過」取代 Source Library 尋源規則；來源庫存在時優先由 Drive 取得。

## 工具行為

若目前環境具備 GitHub / Drive connector：
- 應實際讀取，不只引用記憶。
- GitHub 寫入前先 fetch 最新檔案。
- Drive 歸檔後再次搜尋／列出驗證。

若缺少必要 connector：
- 明確標記 `CONNECTOR_BLOCKED`。
- 不宣稱已同步、已上傳、已回寫。

## 教師畫面

- ChatGPT 對話預設先顯示 Teacher Review View；完整 JSON／YAML 保存為 Machine Payload，不直接鋪滿對話。
- 第一屏先顯示結論、證據、知識層、缺口與本次唯一決定；教師要求時才展開完整母檔。
- STEP 1 必要來源未核對完成時回報 `STEP1_INCOMPLETE`，不得要求核准完整定錨。
- 知識層使用 `[教材明載] / [教師補充] / [AI 延伸] / [待核對]`；來源狀態另顯示 `[教材已確認] / [教育部辭典已核對] / [AI 建議，待教師確認] / [尚待教材來源核對]`。外部字典不能證明某詞屬於教材。
- STEP 2.5 只顯示形近字、多音字、教材詞語／成語審核表與待確認項目，然後停在 HOLD 2.5。
- 嚴格遵守 `HOLD 1 → STEP 2 → HOLD 2 → STEP 2.5 → HOLD 2.5 → STEP 2.6 → HOLD 2.6`；不得產生 `STEP 2.75`。

## 平台輸出

ChatGPT 可負責：
- 教師確認卡
- Source Master / Script / Visual YAML MD
- 依 `skills/vmax-image-renderer/SKILL.md` 探測工具後，實際生成／修改／驗證圖片；缺少圖片工具時只輸出 handoff，不宣稱完成
- PPTX / PDF / Worksheet 產出
- Google Drive Runtime State 回寫；無法連線時輸出精確 state handoff
- Google Drive 歸檔驗證

但所有輸出仍受 Core / Manifest / Runtime 約束。

Runtime 實際進入簡報／視覺階段時，ChatGPT 必須實際載入 `skills/presentation-engine/SKILL.md`、`core/presentation/classroom-image-slide-policy.md`、`core/renderer/image-first-hybrid-renderer.md`、`skills/vmax-image-renderer/SKILL.md`、`core/quality/visual-drift-detector.md` 與 `core/quality/quality-gate-2.md`。除課文閱讀頁外，預設以整頁圖片式合成交付；高風險文字用可控排字合成後扁平化。不得把圖片模型連續錯字當作刪頁理由，也不得在跨頁型代表頁組全數核准前製作完整頁數。

若 Google Drive 或對話中存在該課已核准的 Lesson Baseline／施工總表，ChatGPT 進入 slide_script、Render Request、修圖、生圖或排版前必讀。Baseline 的逐頁清單只約束該課；可抽象成全域規則的項目須先由教師明確要求更新技能。

## 核心金句

> ChatGPT 是 V-MAX 的一個執行器，不是 V-MAX 本身。

## 國語簡報施工前確認（GLOBAL_SKILL_RULE）

Runtime 到 STEP 2.5 語文規劃或後續簡報施工階段（含這些階段的續作／下一步／確認）時，必須載入 `core/governance/presentation-preconstruction-policy.md`。先讀最新 Drive Runtime；到 STEP 2.5 才檢核成語雙軌與每個正式生字的延伸成語覆蓋；缺漏為 `VOCABULARY_IDIOM_COVERAGE_INCOMPLETE`。風格、角色、畫布與頁數帳本鎖定後，建立逐頁施工稿並停等確認；核准後才選代表頁，逐類核准後才進每批最多 8 頁的小批次，每批完成必須停等教師確認。每個 stage／HOLD 都回寫並驗證 Runtime State 與 Runtime Index；不得以舊流程簡寫跳過這些關卡。

## STEP 1 整合擷取

SOURCE 0／STEP 1、重新製作或來源補漏時，必讀 `core/governance/step1-source-anchor-policy.md` 第 G 節。依既定清單完成所有可查頁區與類別，包含多音字旁欄補充；階段內持續處理，剩餘缺口集中詢問，完整後才交付一份審核稿並停在 HOLD 1。LKB、成語延伸選教、風格、角色、頁數及代表頁不作為 STEP 1 前置條件。

## 圖片式產物的呈現與修訂（簡報／視覺階段適用）

以下要求於 Runtime 進入對應教學架構或視覺製作階段才執行；不作為 SOURCE 0／STEP 1 的載入或完成條件。

圖片式簡報與文件預設使用可用的 ChatGPT 原生圖像生成／影像編輯工具，直接顯示原生圖片結果，保留平台提供的編輯入口與原圖引用；不得只輸出 PNG 檔案卡片。依教師指定範圍引用原圖續編，另附下載檔供保存。文字／來源 QA 仍須執行；合成後圖片也須直接預覽。若平台不支援原生編輯，明確說明，不能把一般圖片預覽宣稱為有「編輯」功能。

使用中文標題、精簡表格與條列。完整 Machine Payload 可另存，但對話不顯示 raw schema、內部欄位或空白程式碼框。每項來源顯示教材、教育部辭典、AI 建議或待核對狀態。

目前 Runtime 已進入簡報／視覺 stage 時，必須先讀取正向視覺範例、Visual Text DNA、Canvas Lock Policy 與 Text Layer Construction Policy。到畫布鎖定階段若尚無鎖定畫布，詢問教師選擇 `4:3` 或 `16:9`；選定後續跑不得切換。逐頁腳本、圖片底圖、正式文字層、角色／風格檢查與 PPTX／PNG 輸出必須分階段完成；不得從抽象教學主題直接套用通用簡報模板。正式中文只能由可驗證文字層渲染，文字感覺或圖文關係不像正向範例時標記 `VISUAL_TEXT_DNA_FAIL`，停等修正，不得量產。

每課先建立並鎖定 `Lesson Architecture Profile`：依 `schemas/lesson-architecture-profile.md` 的十項流程：封面 → 讀前引導 → 學習地圖 → 課文閱讀與隨文教學交錯 → 正式生字總覽 → 形近字 → 多音字 → 生字延伸成語 → 統整遷移；教材語文活動嵌入相關區段並檢查完整覆蓋。完成 Baseline 確認後，才詢問是否加入平板操作、四學公開課、議題融入或教師自訂外加模板。外加模板可以重新設計教學活動、互動、媒介與時間配置，但必須逐項回指 Baseline 的學習結果；不得靜默刪除教師指定內容，也不得把變體誤當成新的 Official Knowledge。

若目前 WORK 模式的插圖視覺已符合教師期待，視覺資產視為 `illustration_status: LOCKED`。之後文字表達、字體、斷行、位置或顯示失敗，只能重建文字層與排版，不得重新生成插圖或角色。

每個圖片／腳本候選都必須保留版本與教師狀態；未確認候選不得覆蓋確認稿、改寫 Runtime 或觸發其他頁面重算。代表頁未確認前，不得批次製作。

WORK 模式的簡報預設交付為高畫質圖片化投影片（PNG）與 PDF。不得自行生成可編輯文字框的 PPTX；只有教師明確要求 PPTX 時，才另行派生。
