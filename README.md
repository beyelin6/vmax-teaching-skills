# V-MAX Teaching Skills

V-MAX 是臺灣國小國語教材轉錄、課程設計、視覺渲染與交付技能庫。Repository 保存平台中立規格；ChatGPT、Codex、Gemini 與 Canva 依各自實際工具執行。

## 核心原則

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
- `prestudy-worksheet`、`postlesson-short-writing-worksheet`：定義預習單與課後短文單。
- `vmax-typography-bridge`：統一繁體中文字體 DNA、可讀性與 Canva 映射。
- `vqs-quality-validator`、`lesson-package-delivery`：品質驗證與正式交付。

完整模組以 `V-MAX_MANIFEST.md` 為準，不以本清單取代 Manifest。

## 平台安裝與能力

| 平台 | 安裝／載入方式 | 圖片執行 |
|---|---|---|
| Codex | 將 repository clone 為 Codex 可發現的 plugin／skills 目錄；本 repo 含 `.codex-plugin/plugin.json` | 當工作階段有圖片工具時直接渲染；否則 handoff |
| ChatGPT | 將 repository 作為自訂 skill／plugin bundle 匯入，或以 GitHub 連線讀取；入口為 `V-MAX_BOOTSTRAP.md` | 只有目前 ChatGPT 工作階段提供圖片工具時直接渲染 |
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
