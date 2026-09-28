---
name: vmax-teaching-skills-claude
description: Claude 的 V-MAX GitHub 輕量入口。製作、分析或續作臺灣國小國語教材與視覺簡報時，從 GitHub main 讀取共用規則及既有課程進度，再按任務路由；獨立學習單或美編使用專門模組，不啟動整課流程。
---

# V-MAX Claude GitHub Launcher

版本：1.0

本資料夾只保存啟動方法；共用規則以 `https://github.com/beyelin6/vmax-teaching-skills` 的 main 為來源。一般規則更新不重裝入口，入口本身改版才替換。只安裝本入口，不同時安裝完整包或其他同用途入口，不把內部模組逐一註冊為技能。

## 啟動與更新

1. 實際檢查可用 GitHub connector、HTTP／瀏覽讀取或 git。先取得 main 的完整 commit SHA，例如 GitHub API `https://api.github.com/repos/beyelin6/vmax-teaching-skills/commits/main`；再從同一 SHA 讀檔。不能拿搜尋摘要或舊記憶宣稱已讀最新版。
2. 檔案網址為 `https://raw.githubusercontent.com/beyelin6/vmax-teaching-skills/<SHA>/<path>`；以實際 SHA 取代占位。依序讀 VERSION、V-MAX_MANIFEST.md、V-MAX_BOOTSTRAP.md、core/governance/portable-runtime-policy.md 及 adapters/claude.md。後續 core／skills 路徑同樣從該 SHA 取得，不當作本入口資料夾內的檔案。
3. 選 REMOTE。新任務、進入下一個大階段或教師要求讀取最新版時，檢查 main；同階段不逐頁查版本。發現更新先依可攜政策分類影響，再整體切換快照，不混用新舊檔案。
4. 暫時無法更新但已有可讀必要原文、commit 與版本的 LAST_KNOWN_GOOD 時可續作並標記 GITHUB_REFRESH_PENDING；沒有必要規則原文才 BOOTSTRAP_BLOCKED。這不免除實際讀取教材、State 與核准證據。

## 任務與進度

先判斷整課或獨立任務。整課／國語簡報讀 canonical Front Door 與 Executor 的路由段，再依目前 stage 載入；預習單、短文單、純美編直接讀各自技能。

教師明確指定課次時依該課既有 State、Index、核准事件與產物續作；不得從別課 active pointer 猜階段，不以新規格重開課程。Drive 為既有課程預設；缺連接器依可攜政策保存待同步資料，不能自動切換正式後端。新課才依能力初始化。

版本更新與課程核准是兩件事：保留來源、頁面、角色與風格的有效核准。舊施工稿和新規則不一致時列出受影響項目，不能默默改掉已核准內容，也不能整課退回來源分析。

第一個實質回覆使用 Bootstrap 的五欄回條：`V-MAX LOAD｜Plugin {VERSION}｜Manifest {manifest_version}｜Executor {executor_version}｜Stage {runtime_stage}｜UI {teacher_review_view_version}`。版本來自同一 SHA，stage 來自實際 State 或新課初始化；獨立任務註明 standalone 與實際工作，不偽造 lesson stage。

圖片生成、編輯、原圖引用、預覽與 Drive 讀寫逐項確認實際能力；缺能力提供可追溯交接，不把提示詞當完成圖片。課文與非課文頁的文字方式依現行 Text Layer Construction Policy，教師一次審核一大步，階段內連續完成可查工作。
