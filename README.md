# V-MAX Teaching Skills

V-MAX 是臺灣國小國語教材轉錄、課程設計、視覺渲染與交付技能庫。Repository 保存平台中立規格；ChatGPT、Codex、Gemini 與 Canva 依各自實際工具執行。

## 核心原則

國語視覺簡報採 [整合審核工作流](core/governance/chinese-visual-presentation-workflow.md)：完整課程內容 → 課程調整與視覺方案 → 逐頁稿 → 角色視覺 → 代表頁／逐批製作。每個大階段完成再集中審核；四層次閱讀包含在內容包，預習單與短文單沿用核准課程分支製作。

- Skill 保存方法與工作流；Library 保存可重用風格、角色、版型與教學資源。
- GitHub 保存規格；Google Drive `00_Runtime_State` 保存每一課即時狀態。
- 每課內容、頁數與模組動態判斷，不使用固定頁數模板。
- 圖片需求必須產生實際資產並重新檢查；prompt 或 Render Request 不是成品。
- 教學關鍵繁體中文預設由可控正式文字層合成。

## 主要技能

- `vmax-course-orchestrator`：管理單課狀態、模式與教師核准關卡。
- `chinese-textbook-transcriber`、`chinese-lesson-knowledge-builder`：忠實轉錄並建立課程知識書。
- `learning-module-builder`、`teaching-strategy-builder`、`presentation-engine`：建立學習模組、教學策略與多平台輸出。
- `vmax-image-renderer`：探測平台圖片能力，實際生圖／改圖／合成／重檢，或產生可執行 handoff。
- `prestudy-worksheet`、`postlesson-short-writing-worksheet`、`postlesson-short-writing-presentation`：定義預習單、課後短文單與短文單解說簡報。
- `vmax-typography-bridge`：統一繁體中文字體 DNA、可讀性與 Canva 映射。
- `vqs-quality-validator`、`lesson-package-delivery`：品質驗證與正式交付。

完整模組以 `V-MAX_MANIFEST.md` 為準，不以本清單取代 Manifest。

## Codex 安裝模式（擇一）

Codex 有兩種互斥的安裝模式：Plugin 模式由 `.codex-plugin/plugin.json` 直接發現 repository 的 `skills/`；同步模式才執行 `scripts/sync_codex_skills.ps1`，將 GitHub `skills/` 鏡像到 `~/.codex/skills/`。不要同時啟用兩種模式，否則同名技能會重複載入，來源與版本優先順序不明。切換模式前停用另一個來源，並重新啟動 Codex。

## ChatGPT Work 單技能安裝

ChatGPT Work 不應把 `skills/` 下的所有模組逐一保存為個人技能。唯一的 Launcher 技能名稱是 `vmax-teaching-skills-chatgpt-work`，其 GitHub 安裝來源是：

`chatgpt-work/vmax-teaching-skills/SKILL.md`

直接安裝／更新可使用：[ChatGPT Work Launcher raw SKILL.md](https://raw.githubusercontent.com/beyelin6/vmax-teaching-skills/main/chatgpt-work/vmax-teaching-skills/SKILL.md)。此歷史來源路徑為保持既有安裝連結而保留；可攜包輸出名稱與 frontmatter 一致。`skills/vmax-teaching-skills/SKILL.md` 則是 canonical Front Door，不是 ChatGPT Work 個人 Launcher。兩者不可互相替代。

這個 Launcher 在新任務、跨大階段或教師要求更新時檢查 GitHub `main`，同階段固定使用同一 commit，按需載入 Manifest、Golden Path 與當前 stage 規則，可避免跨資料夾引用在個人技能轉存時失效，也避免批次保存造成 HTTP 422。

## 可攜安裝包（Plugin 0.5.0）

可使用 `scripts/build_portable_bundle.py --output <repo外的新資料夾>` 產生 Claude、ChatGPT、Antigravity 與 Codex 的資料夾及 zip；不自動安裝或改動既有課程。每包根目錄為 `vmax-chinese-teaching`，只有一份 SKILL.md，內部技能改名 MODULE.md 並重寫本機引用。既有 GitHub 輕量 Launcher 路徑保留；輸出的入口資料夾與 name 一致。

完整包從內附 VERSION／Manifest 執行，不依賴即時 GitHub。`bundle-manifest.json` 記錄來源 commit、修改狀態與每檔 hash；用 `scripts/verify_portable_bundle.py <包根目錄>` 檢查。保留被引用的 docs、schemas、scripts、資源與回歸案例，不一律排除 docs。不要在同一環境同時安裝完整包與舊同用途入口。

Drive 仍為既有課程預設；LOCAL／HANDOFF 與待同步分支依 `core/governance/portable-runtime-policy.md`。完整包安裝不會遷移雲端進度。自動測試只證明包與資料契約；跨平台實跑案例見 `tests/portable-platform-scenarios.md`，未跑的環境不得宣稱通過。

## 平台安裝與能力

| 平台 | 安裝／載入方式 | 圖片執行 |
|---|---|---|
| Claude / Claude Code | 優先安裝 `launchers/vmax-teaching-skills-claude/SKILL.md`，依實際平台安裝入口載入；見 adapters/claude.md | 實測圖片生成與局部編輯能力，缺少時 handoff |
| Antigravity | 優先安裝 `launchers/vmax-teaching-skills-antigravity/SKILL.md`，只註冊此入口；見 adapters/antigravity.md | 依當次可用圖片工具，無工具不宣稱成品 |
| Codex | 將 repository clone 為 Codex 可發現的 plugin／skills 目錄；本 repo 含 `.codex-plugin/plugin.json` | 當工作階段有圖片工具時直接渲染；否則 handoff |
| ChatGPT Work | 只安裝 `chatgpt-work/vmax-teaching-skills/SKILL.md`；輕量 Launcher 從 GitHub 載入；完整 ChatGPT 可攜包從包內載入 | 只有目前 ChatGPT 工作階段提供圖片工具時直接渲染 |
| Gemini / Gemini CLI | 將 `skills/` 暴露給 Gemini 的 skills／檔案工作區，並把 Bootstrap 設為入口；如用 API，另行配置圖片模型與憑證 | 有 image tool/API 才直接渲染，文字模型只有 prompt 不算完成 |
| Canva | 以 `adapters/canva.md` 與 Render Request 作為橋接 | 需有實際建立／編輯、匯出與重檢能力 |

不同產品版本的安裝 UI 可能不同，但平台不得改寫 Core。啟動後先讀：

1. `V-MAX_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `runtime/lesson-state.md`
4. 對應 `adapters/*.md`

## 圖片渲染狀態

- `RENDER_VERIFIED`：實際成品存在且已重新檢查，才能正式交付。
- `IMAGE_HANDOFF_READY`：規格已備妥，但仍需另一個有圖片能力的平台執行。
- `IMAGE_TOOL_BLOCKED`：本次環境沒有可用圖片工具。

詳細契約見 `skills/vmax-image-renderer/SKILL.md`。

## 教材母檔

所有下游任務先讀取 Lesson Master Index 與核准 LKB，再執行任務 Coverage Diff。資料足夠就重用；不足時只增補帶來源的 LKB Patch，不重跑整份教冊。

## 教師審核畫面

完整 JSON／YAML 保存為可續跑的 Machine Payload；對話預設依 `core/ui/teacher-review-view-contract.md` 顯示精簡的 Teacher Review View。畫面先呈現結論、教材證據、知識層、缺口、這次唯一決定與唯一下一步，教師要求時才展開完整母檔。

## Repository 邊界

- `core/`、`skills/`、`schemas/`：正式可執行規格。
- `adapters/`：平台差異，不得覆寫 Core。
- `libraries/`：仍可被正式流程重用的資源。
- `docs/`：現行架構說明與品質基準，只有被正式規格引用時才影響執行。
- `tests/`、`scripts/`、`.github/`：回歸案例與自動驗證。
- `runtime/lesson-state.md`：只保存 Runtime schema；單課即時狀態保存在 Google Drive。

Repository 不保存：

- `runtime/lessons/` 或其他單課即時狀態
- `lessons/` 下的特定課程成品
- `docs/legacy/`、migration audit 或 legacy resource

## GitHub 輕量入口更新

希望只更新 GitHub 就讓各平台讀取共用規則時，選輕量入口；完整可攜包僅供明確選擇離線快照的情境。Claude 與 Antigravity 入口位於 `launchers/`，ChatGPT 保留上列歷史來源路徑。安裝資料夾需與 frontmatter name 相同。一般共用規則更新不必重裝；入口本身變更才替換。實際讀取仍須有 GitHub 連線能力，不能保證未提供工具的平台自動同步。

### 建包來源與精簡範圍

建包支援 Git clone 與 GitHub Download ZIP 解壓資料夾。後者記錄 source_kind=archive、source_commit=unknown、source_dirty=null，不宣稱已核對遠端版本。只收錄發布用目錄；排除隱藏檔、快取、Python 測試及未被引用的 docs/visual-validation 圖片。保留 docs 規則與 tests/*.md 回歸案例，避免斷開現有引用。完整性驗證不代表平台實際行為驗收。

### Claude.ai 檔案數限制

Claude 完整包依實測上傳拒絕訊息採 200 檔上限，建包預算為 190 檔（含 bundle-manifest.json），超過即失敗；ZIP 不加入目錄 entry。各平台設定集中在 scripts/verify_portable_bundle.py 的 TARGET_PROFILES，其他三平台不精簡內容。

Claude 僅省略 agents/openai.yaml，將 schemas 及 core/governance、visual、director、pedagogy、presentation 的純 Markdown 合併為各目錄 BUNDLE_REFERENCE.md。全部原文保留，只重寫本機路徑為章節引用，逐節 hash 與原路徑對照寫入 manifest；JSON schema 與腳本原路徑不動。沒有停用四學、平板、決策或教學記憶。其他平台 adapter 與 launcher 保留作交接參考，不作 Claude 入口。品質 docs 和引用的 tests 文件保留。此為檔案及引用驗證，尚未證明 claude.ai 實際上傳或執行成功。
