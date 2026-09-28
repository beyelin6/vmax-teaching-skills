---
name: vmax-teaching-skills-chatgpt-work
description: ChatGPT Work 專用的 V-MAX 啟動技能；製作或續作國語教材時，從 GitHub 載入共用規格、同步當課 Drive Runtime，再按目前階段載入模組。
---

# V-MAX ChatGPT Work Launcher

版本：1.9

## 安裝與來源

這是 ChatGPT Work 唯一需要永久保存的 V-MAX 個人技能。不要將 GitHub repository 中 `skills/` 下的其他模組逐一轉存為個人技能。

規格來源：`https://github.com/beyelin6/vmax-teaching-skills` 的 `main`。GitHub 管共用規則；單課教材、教師決定與進度保存在 Drive。一般共用規則更新不需重裝；Launcher 本身改版才替換此檔。

## 啟動與續作

國語視覺簡報預設 `CHINESE_VISUAL_PRESENTATION`，必讀 `core/governance/chinese-visual-presentation-workflow.md`。本模式按五個大階段集中審核；本檔的細部內容檢查保留，小步 HOLD、先後與停等只適用 `DETAILED_LESSON`。內部分析與候選準備不等於正式選教核准。

1. 以可用 GitHub 工具先取得 main commit，再以同一 commit ref 讀取 `VERSION`、`V-MAX_MANIFEST.md` 與本次必要規則。瀏覽器失敗不代表 GitHub connector 不可用；先檢查並實際嘗試可用讀取工具，不能猜測網路受限。版本回條須對應該 commit 實際讀到的檔案內容。
2. 依 Manifest 載入 `skills/vmax-teaching-skills/SKILL.md`、`V-MAX_BOOTSTRAP.md`、Runtime contract、Continuation State Gate、current main workflow、executor、HOLD policy、Teacher Review View 與 `adapters/chatgpt.md`。這些檔案的條件式要求僅於適用 stage 執行。
3. 在任何實質教材分析或製作前，讀最新 Drive Runtime Index 與教師指定課次的 State，依 Continuation State Gate 核對 revision、目前 stage、教師決定及必要產物。版本回條須在這些前置讀取後顯示，並以實際 Drive stage 為準。沿用現有重製 Runtime；未指定重建時不另開版本。別課 active index、尚未進入階段的產物或舊 P01 不得阻擋來源整理。
4. 確定 `current_stage` 後，才載入下表對應規則。續作先讀最新 Drive revision；同一已驗證 GitHub commit 的規格依 Bootstrap freshness／selective reload 重用，不逐頁重讀整套技能。

GitHub 暫時無法更新時依 Bootstrap 使用可核對 commit、版本與完整原文的 `LAST_KNOWN_GOOD`，標示 `GITHUB_REFRESH_PENDING`；沒有可信規格才 `BOOTSTRAP_BLOCKED`。記憶或舊對話不算 LKG。Drive 無法讀取或當前階段有實質狀態衝突，依 State Gate 回報具體阻礙，不宣稱已同步。

## 按目前階段載入

國語簡報先按整合工作流識別 VP1–VP5；下表舊 stage 名稱是大階段內的工作分類，用於按需載入，不是新的確認點。VP1 按順序載入來源與分析模組，來源驗證後可以建立待教師確認的教學候選，所有視覺生成仍到對應後段。

| Runtime 目前階段 | 本階段工作與規則 |
| --- | --- |
| VP1_COURSE_REVIEW | 先載入來源政策與 Transcriber，再按需載入語文／成語與閱讀分析；候選集中 VP1 審核，不停在舊 HOLD 1／2／2.5／2.6。 |
| VP2_DESIGN_REVIEW | 同包完成已選課程調整、角色用途、風格／混搭、心智圖及畫布方案。 |
| VP3_PAGE_PLAN_REVIEW | 依 Page Detail Profile 建立全文／配置，角色資產可待 VP4；不載入正式生圖門檻阻擋規劃。 |
| VP4_CHARACTER_REVIEW | 角色庫、角色視覺候選與 Registry writeback；完整綁定後才批准施工母稿。 |
| VP5_REPRESENTATIVE_REVIEW／VP5_BATCH_REVIEW／VP_COMPLETE | 按整合工作流載入施工／QA／交付技能；代表頁整組審核、批次逐批審核。 |
| SOURCE 0／STEP 1／來源補漏 | 依 `core/governance/step1-source-anchor-policy.md`，尤其第 G 節，載入 `skills/chinese-textbook-transcriber/SKILL.md` 及其來源庫、認讀字與擷取契約。讀回已存資料，只補必要缺口。 |
| STEP 2／STEP 2.5／STEP 2.6 | 依 main workflow 與 executor 載入該階段模組；到 STEP 2.5 才載入 `core/governance/presentation-preconstruction-policy.md` 的成語雙軌覆蓋規則。 |
| 教學架構、角色、風格、畫布等後段階段 | 依 main workflow 載入當前模組，在各自階段完成決定與鎖定。 |
| 簡報規劃、逐頁施工、代表頁、渲染、批次與 QA | 載入 Front Door 的簡報／視覺強制鏈、`core/governance/presentation-preconstruction-policy.md` 與 adapter 的圖片式產物要求；保留逐頁確認、代表頁逐類確認、小批次逐批確認與文字層局部修正。 |

「我要製作簡報」是最終目標，不代表 Runtime 已到視覺階段。SOURCE 0／STEP 1 不預載渲染、字型、角色、風格或畫布規則，也不要求 LKB、頁數、延伸成語選教或代表頁先核准。Course Orchestrator 不取代 executor 的 stage machine。

## 來源擷取的完成方式

依既定教材清單連續處理本課正文、相關頁面、側欄與補充框，包括多音字讀音、詞義、例詞、例句與辨析提醒。已核准的教師裁定須保留；來源原字與教學採用字分開記錄，不反覆請教師裁定同一問題。

`next_allowed_stage` 為空代表尚未允許跨階段，不阻止完成 `current_stage` 內的搜尋、擷取、校對與存檔。不要每查完一頁、補一欄或存一次檔就停下要求「繼續」。可自行查明的項目持續完成，真正無法解決的必要缺口集中提出；來源完整後在國語簡報 VP1 繼續完成語文、成語與四層次閱讀候選，再交付整合課程審核稿；DETAILED_LESSON 才單獨停 HOLD 1。未完整時如實標記 `STEP1_INCOMPLETE`，不請求全文核准，也不開始教學規劃或生圖。

教師確認只授權對應 HOLD 的下一個合法 stage；局部來源裁定不等於全文或下游核准。從目前未完成 stage 接續，已核准來源、頁面、角色、風格與決定均直接沿用；只有教師要求修改或新證據指出特定錯誤時，才修補受影響項目，不重跑未受影響階段。每完成 stage／HOLD，非破壞性更新並讀回驗證 Drive State 與 Index；候選不得覆蓋確認稿。不得自行新增 stage 或使用 `STEP 2.75`。

## 回條與教師畫面

第一個實質回應第一行：

`V-MAX LOAD｜Plugin {VERSION}｜Manifest {manifest_version}｜Executor {executor_version}｜Stage {runtime_stage}｜UI {teacher_review_view_version}`

Plugin 取自 repository `VERSION`，不是本 Launcher 的版本。各欄填同一已驗證 GitHub commit 的實際讀取或可信 LKG 版本；Runtime stage 必須來自本次 Drive 讀取，不能由規格推定。使用 LKG 附註 `GITHUB_REFRESH_PENDING`。缺少回條為 `LOAD_RECEIPT_MISSING`。

依 Teacher Review View 使用中文結論、來源證據與精簡表格；不顯示 raw JSON／YAML。STEP 1 只呈現教材內容與必要缺口，角色偏好先保存為 deferred input，不詢問視覺設定。正式教材與 AI 延伸分層，不以摘要冒充完整來源。
