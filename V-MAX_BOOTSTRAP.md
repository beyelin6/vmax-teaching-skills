# V-MAX Bootstrap 1.8.0

## 目的

國語視覺簡報預設 `CHINESE_VISUAL_PRESENTATION`，必讀 `core/governance/chinese-visual-presentation-workflow.md`。本模式按五個大階段集中審核；本檔的細部內容檢查保留，小步 HOLD、先後與停等只適用 `DETAILED_LESSON`。內部分析與候選準備不等於正式選教核准。

本檔是任何 AI／Agent／Renderer 進入 V-MAX 時的第一讀取入口。

核心原則：

> GitHub Repository 是 V-MAX 的平台中立規格 Source of Truth；ChatGPT、Codex、Gemini、NotebookLM、Canva 或未來模型都只是執行器／轉譯器，不得以模型記憶或舊版對話覆蓋 Repository 的現行正式規格。

> 每一課的即時 Runtime State 不放 GitHub；預設保存在教師指定 Drive；LOCAL／HANDOFF 依可攜政策綁定唯一正式來源。

---

## Front Door 與載入回條

先依 `core/governance/portable-runtime-policy.md` 選 BUNDLED、REPOSITORY 或 REMOTE 規格快照。完整包／checkout 不需要即時 GitHub；輕量 Launcher 才從同一 commit 載入，已核驗 LAST_KNOWN_GOOD 可沿用。GitHub refresh 失敗不阻擋已有可信必要原文。

完整課程只先讀 VERSION、Manifest、本檔、可攜政策、Runtime 契約及 Executor 路由段。續作讀正式後端 State／Index 與必要核准證據；新課查無既有課程後初始化。再按當前 stage 讀模組，教師審核時讀 Teacher Review View。相同版本原文仍在時不重讀。獨立文件／學習單不啟動整課流程。

第一個實質回覆顯示 `V-MAX LOAD｜Plugin {VERSION}｜Manifest {manifest_version}｜Executor {executor_version}｜Stage {runtime_stage}｜UI {teacher_review_view_version}`，可另註快照模式。版本從同一快照讀取，stage 從實際 State 或新課初始化紀錄讀取；缺回條仍為 LOAD_RECEIPT_MISSING。不得把離線版說成遠端最新版。

## 更新與能力

規格在啟動、教師要求更新或大階段邊界按需檢查，不逐頁查 GitHub。不混讀不同快照；更新影響分 NO_CURRENT_IMPACT、FORWARD_ONLY、RETROACTIVE_REVIEW，後者只審受影響項目，不撤銷未受影響的核准。

各模組從選定快照按需讀取。實際程式排字時才做 font preflight，生圖／編圖時讀 Image Renderer 並確認各項真實能力；不預先用字型、角色或生圖工具阻擋來源整理。

儲存／同步與離線分支唯一依可攜政策。Drive 預設保留；其他後端不能虛報雲端同步。必要規格不存在才 BOOTSTRAP_BLOCKED；缺來源或缺核准只限制依賴它的操作。

## 高優先語文教學摘要

當目前階段進行課文語詞、句型或修辭的教學設計時（來源擷取不適用），必須載入：

- `skills/text-embedded-language-teaching/SKILL.md`
- 完整規格：`core/pedagogy/text-embedded-language-teaching-policy.md`

執行口訣：

> **語詞隨段落，句型帶原文，修辭從文本發現。原文不可消失。**

最低要求：
- 語詞：原文片段＋重點語詞＋學生易懂的意義。
- 句型：先有課文原句，再抽出結構與仿用。
- 修辭：先讀原文、觀察效果，再命名。
- Renderer 不得為版面美化刪除原文證據層。

---

## 執行優先級

發生衝突時採以下優先級：

1. Teacher latest explicit decision
2. 該課正式儲存後端 Runtime State 的已鎖定狀態
3. `V-MAX_MANIFEST.md` 指定的 canonical files
4. Current Main Workflow
5. Current Executor
6. Module policy / skill
7. Legacy files / model memory / old conversation patterns

舊版流程不得因模型熟悉而復活。

---

## Runtime Gate

開始或續跑一課前，必須從該課綁定儲存後端的 State 讀取：

- `current_stage`
- `last_completed_stage`
- `teacher_confirmation_status`
- `next_allowed_stage`
- `forbidden_next`
- `locked_decisions`

目前 stage 尚未完成時，允許依其規則持續搜尋、擷取、校對與存檔；`next_allowed_stage` 為空不阻擋這些階段內工作。只有準備跨階段，且目標不符合唯一 `next_allowed_stage` 或尚未取得對應 HOLD 核准時，才停止並回報：

`RUNTIME_STAGE_CONFLICT`

不得自行跳階段、改名階段或推測教師已確認。

每次 HOLD 確認或正式 stage 完成後，應依可攜政策回寫該課 State，而不是建立 GitHub commit。

---

## 平台中立原則

V-MAX Core 不依賴：

- 特定 ChatGPT 版本
- 特定 Gemini 版本
- NotebookLM 限制
- Canva 版型能力
- 任一 Renderer 的頁數／批次／圖像限制

平台差異只能由 `adapters/` 處理，不得反向改寫 Core、Teacher Intent、Lesson Map 或 Session Map。

## 教師審核畫面

所有需要教師閱讀、確認或修正的 stage／HOLD，必須載入 `core/ui/teacher-review-view-contract.md`。完整 JSON／YAML 保存為 Machine Payload；對話預設先顯示人類可讀的結論、教材證據、知識層、缺口、這次唯一決定與唯一下一步。

- 不得以 raw schema dump 取代教師確認卡。
- STEP 1 必要來源未核對完成時顯示 `STEP1_INCOMPLETE`，持續完成可自行查明的來源；真正無法解決的缺口集中詢問，不開放全文核准。
- `[教材明載] / [教師補充] / [AI 延伸] / [待核對]` 不得混層。
- `STEP 2.75` 不在 Golden Path，出現即視為 `LEGACY_STAGE_ALIAS`。

## 圖片能力與降級

當目前 Runtime 階段允許且實際要產生或修改圖片時，必須載入 `skills/vmax-image-renderer/SKILL.md`，並依本次工作階段實際可用工具探測 `generate_image / edit_image / inspect_image / compose_verified_text / export_asset`。不得只因平台叫 ChatGPT、Codex、Gemini 或 Canva 就假設具備圖片能力。

- 有可用圖片工具：實際生成／修改、重新檢查成品，再回報 `RENDER_VERIFIED`。
- 沒有圖片工具：輸出 Render Request 與 handoff bundle，回報 `IMAGE_HANDOFF_READY` 或 `IMAGE_TOOL_BLOCKED`。
- prompt、Renderer Script、Visual YAML 與 Render Request 都不是完成圖片。
- 課文頁獨立文字；非課文頁由圖片引擎忠實繪製核准文字，依 Text Layer Construction Policy 校對與局部修正。

## Lesson Master Preflight

SOURCE 0／STEP 1 的來源擷取不以 LKB 或本 Preflight 為前置條件。任何平台實際進入下游製作預習單、短文單、簡報、教案、評量、活動或圖片前，都必須執行 `core/governance/lesson-master-preflight.md`，並依 `core/governance/task-knowledge-requirement-registry.md` 做任務 Coverage Diff。

- 有效且足夠的核准 LKB：直接重用。
- 母檔不足：只補缺少節點，教師核准 Patch 後合併新版。
- 沒有母檔：先完成教材轉錄、重要知識分析與 LKB 核准。
- 此規則屬於 Core，不得只在 Gemini Adapter 執行。

---

## 核心金句

> 先載入 V-MAX，再讀這一課現在跑到哪裡，才開始教學設計。

> GitHub 發布規格；選定快照執行規則；每課綁定後端保存生命週期。

> 語詞隨文理解；句型回到原句；修辭從文本發現。
