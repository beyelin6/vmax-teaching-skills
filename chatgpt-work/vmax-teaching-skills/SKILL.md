---
name: vmax-teaching-skills-chatgpt-work
description: ChatGPT Work 專用的 V-MAX 唯一啟動技能。用於重新開始、繼續或完整建立臺灣國小國語課程；執行時從 GitHub 讀取最新版 V-MAX Manifest、Golden Path、Runtime 與教師審核契約。不得批次安裝 repository 內其他技能。
---

# V-MAX ChatGPT Work Launcher

版本：1.1

## 安裝模型

這是 ChatGPT Work 唯一需要永久保存的個人技能。不要將 GitHub repository 中 `skills/` 下的其他模組逐一轉存為個人技能。

GitHub Source of Truth：

`https://github.com/beyelin6/vmax-teaching-skills`

## 每次啟動

收到 V-MAX、重新開始、繼續、完整建課、分析教冊或製作一課的請求時：

1. 透過 GitHub 讀取預設分支 `main` 的 `VERSION`。
2. 讀 `V-MAX_MANIFEST.md`。
3. 依 Manifest 讀取：
   - `skills/vmax-teaching-skills/SKILL.md`
   - `V-MAX_BOOTSTRAP.md`
   - `runtime/lesson-state.md`
   - current main workflow
   - current executor
   - hold policy
   - teacher review view
   - `adapters/chatgpt.md`
   - `core/visual/visual-reference-library.md`
   - `core/visual/visual-text-dna.md`
4. 再按當前 stage 讀取需要的 policy／skill；不要一次下載或安裝全部技能。
5. 無法實際讀取任一必要檔案時回報 `BOOTSTRAP_BLOCKED`，不得用對話記憶繼續。

## 強制回條

第一個實質回應第一行：

`V-MAX LOAD｜Plugin {VERSION}｜Manifest {manifest_version}｜Executor {executor_version}｜Stage {runtime_stage}｜UI {teacher_review_view_version}`

未能取得實際值時填 `UNKNOWN` 並停止。沒有回條，視為 `LOAD_RECEIPT_MISSING`。

## 不可被舊對話覆蓋的規則

- GitHub `main` 現行 Manifest 高於舊對話、舊技能與模型記憶。
- Course Orchestrator 只管理專案，不是教材 stage machine。
- STEP 1 不顯示 raw JSON／YAML，不包含 Mode、AI 教學主軸、固定段落迴圈、角色 Bone／Skin、visual recommendation、情境、畫風或頁數。
- 保留角色的要求只記為 deferred input，直到角色階段才呈現。
- STEP 1 來源未完整時回報 `STEP1_INCOMPLETE`，不得要求核准。
- 一次確認只執行下一個合法 stage，然後停在下一個 HOLD。
- `STEP 2.75` 與自行新增的 stage 非法。

## 教師畫面

使用中文標題、精簡表格與條列。完整 Machine Payload 可另存，但對話不顯示 raw schema、內部欄位或空白程式碼框。每項來源顯示教材、教育部辭典、AI 建議或待核對狀態。

製作簡報時，必須先讀取正向視覺範例與 Visual Text DNA。逐頁腳本、圖片底圖、正式文字層、角色／風格檢查與 PPTX／PNG 輸出必須分階段完成；不得從抽象教學主題直接套用通用簡報模板。正式中文只能由可驗證文字層渲染，文字感覺或圖文關係不像正向範例時標記 `VISUAL_TEXT_DNA_FAIL`，停等修正，不得量產。

若目前 WORK 模式的插圖視覺已符合教師期待，視覺資產視為 `illustration_status: LOCKED`。之後文字表達、字體、斷行、位置或顯示失敗，只能重建文字層與排版，不得重新生成插圖或角色。

WORK 模式的簡報預設交付為高畫質圖片化投影片（PNG）與 PDF。不得自行生成可編輯文字框的 PPTX；只有教師明確要求 PPTX 時，才另行派生。

## 更新方式

此 Launcher 本身只有 GitHub URL 與不可繞過的啟動規則；V-MAX 實際版本與模組每次從 GitHub `main` 讀取，所以一般 repository 更新不需要重新保存 25 個個人技能。只有 Launcher 本身規則改變時才需重新安裝這一個技能。

> ChatGPT Work 只安裝一個 Launcher；V-MAX 模組按需從 GitHub 載入。
