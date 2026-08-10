# V-MAX 跨平台安裝與執行指南 1.3

## 目的

讓同一套 V-MAX 可在 ChatGPT、Claude、Codex、Gemini Spark 使用，而不需要維護四套教學規則。

核心概念：

> 一個 V-MAX Core、一套 Skill、四個 Adapter。

## 共同入口

所有平台都先讀：

1. `V-MAX_UNIVERSAL_BOOTSTRAP.md`
2. `V-MAX_MANIFEST.md`
3. `core/governance/platform-capability-matrix.md`
4. 對應平台 Adapter
5. 目標 Skill 的 `SKILL.md`

若是「用之前資料直接做」，再讀 portable artifact / checkpoint，不重新跑上游。

## Skill 安裝共同格式

```text
<skill-name>/
├── SKILL.md
├── references/
├── assets/
└── scripts/
```

`SKILL.md` 必須：
- 檔名固定大寫 `SKILL.md`
- `name` 使用 kebab-case
- YAML frontmatter 至少有 `name` 與 `description`
- V-MAX 技能另保留 `Skill I/O Contract`

### 重要：單獨複製 `SKILL.md` 不一定足夠

若 Skill 會引用 repository-level `core/...`、Manifest、Registry、Renderer Contract 或其他共通規格，安裝到 Claude／Gemini Spark 等無法直接讀完整 GitHub repository 的環境時，必須使用 **Portable Install Bundle**。

權威：`core/governance/portable-install-bundle-standard.md`。

Bundle 是由指定 canonical commit 產生的安裝 snapshot；可以複製必要 dependencies，但不是第二套 canonical。安裝 bundle 必須記錄 `canonical_commit`，並通過 dependency closure。

建議結構：

```text
vmax-portable-bundle/
├── BUNDLE_MANIFEST.md
├── V-MAX_UNIVERSAL_BOOTSTRAP.md
├── V-MAX_MANIFEST.md
├── core/...
├── adapters/{platform}.md
└── skills/...
```

正式安裝前至少檢查：

`BUNDLE_MANIFEST_PRESENT / CANONICAL_COMMIT_PINNED / DEPENDENCY_CLOSURE_PASS / ASSET_INTEGRITY_PASS / NO_CANONICAL_FORK`

## 高頻教材 Skill 必帶組

跨平台安裝 V-MAX 時，以下高頻 Skill 應視為同一套工具鏈，不可只帶其中一半：

- `lesson-content-master-builder`
- `prestudy-worksheet`：預習單內容／題目／教學任務層
- `vmax-chinese-preview-worksheet`：預習單 A／B 雙版本 Renderer、300 DPI、列印安全、PDF／Drive
- `postlesson-short-writing-worksheet`：課後短文／童詩 Bonus 學習單
- `slide-script-generator`
- `notebooklm-renderer-script`
- `infographic-pdf-lesson-deck`
- `google-drive-lesson-archive`
- `vmax-checkpoint-resume`

預習單的兩個 Skill 是上下游分工，不是兩套競爭系統：

`prestudy-worksheet → PRESTUDY_WORKSHEET_SOURCE → vmax-chinese-preview-worksheet → PNG/PDF/Drive`

Renderer 的唯一最低輸入為已核准 `PRESTUDY_WORKSHEET_SOURCE`；不得從 `CP_PRESTUDY_INPUT` 或教材主檔自行重做內容選擇。輸出模式固定為 `A_CLEAR_FRAME` 或 `B_FREEHAND`，批次採多課佇列、逐課渲染、逐課校字、逐課驗證。

PDF 共通壓縮與 preflight 直接遵循 `core/export/infographic-pdf-output-contract.md`；預習單 Skill 只加上 A4 300 dpi、3508×2480 與 4.5 mm 安全白邊等特有規則。AI 中文局部修復仍失敗時，依 Core Renderer 的 verified/native-text fallback，不無限重生整頁。

課後短文單直接從已核准 `CP_LESSON_CONTENT_MASTER` 或相容 artifact 啟動，不重跑教材分析。

## Claude 第一批安裝

Manifest：`install/claude/V-MAX_CLAUDE_INSTALL_MANIFEST.md`

定位：Skill 執行、長文件分析與結構化產出。

安裝方式：
- 使用 `CORE_PLUS_HIGH_FREQUENCY` Portable Bundle。
- 以每個 V-MAX skill folder 的 `SKILL.md` 為主檔。
- references / assets / scripts 與 repository-level dependencies 一起封裝。
- Claude 端 Skill 是執行副本；更新以 GitHub canonical 為準。

## Gemini Spark 第一批安裝

Manifest：`install/gemini-spark/V-MAX_GEMINI_SPARK_INSTALL_MANIFEST.md`

定位：可安裝 Skill 的 Workspace / Drive 導向執行端。

安裝方式：
- 使用 `CORE_PLUS_HIGH_FREQUENCY` Portable Bundle。
- Skill 主檔固定 `SKILL.md`。
- Skill name 使用 kebab-case。
- frontmatter 至少包含 `name`、`description`。
- 多檔技能可包含 references / assets / scripts。
- 同名 Skill 更新前先比對 bundle 的 `canonical_commit`；不要用舊副本覆蓋新版。

## ChatGPT

定位：對話式主要工作台。

使用方式：
- 讀 Universal Bootstrap + ChatGPT Adapter。
- 連接器可用時直接讀 GitHub / Google Drive。
- 適合 Golden Path、Checkpoint Resume、學習單、腳本、圖像與 PDF。
- 缺 connector 時不得假裝已同步；輸出 portable artifact 等待其他執行端保存。

## Codex

定位：Repository、程式、驗證、批次與自動化。

使用方式：
- 讀 Universal Bootstrap、Manifest、Codex Adapter。
- 適合改 Skill / Policy / Schema、Renderer pipeline、測試與批次工具。
- 不因程式化方便而改 Teacher Intent 或重算已核准教材。

## Google Drive

Drive 保存：
- portable checkpoint / artifact
- 教材主檔
- 預習單／短文單來源與成品
- NotebookLM / Renderer MD
- 圖片與正式 PDF
- 使用指南與跨平台操作文件

實際 Drive folder/file ID 不寫死在 canonical Skill；由 project/runtime artifact、checkpoint 或執行當次 Drive 查詢取得。GitHub 管規則；Drive 管老師帶著走的成果。

## 換平台時怎麼說

最簡單：

> 請載入 V-MAX，使用這份已確認的教材主檔／checkpoint，直接做＿＿＿，不要重新分析教材。

例如：

> 請載入 V-MAX，用第一到第六課已確認資料，直接做自由手繪版預習單，不重新分析。

> 請載入 V-MAX，用第一到第六課教材主檔，直接做六份課後短文 Bonus 學習單，不重新分析。

## Skill 更新

GitHub canonical Skill 更新後：

1. 重新建立 bundle 或比對平台同名 Skill。
2. 比對 `canonical_commit`。
3. 無本地客製 → 更新。
4. 有本地客製 → 比較差異。
5. 會改 Teacher Intent / schema / HOLD → 先人工審核。
6. 平台臨時改動不得直接變成 V-MAX 全域規則。

## 跨平台品質測試

同一 artifact + 同一 target skill 在不同平台應保持：
- 教材事實一致
- Teacher Intent 一致
- 形近字／多音字等已核准決策一致
- checkpoint 邊界一致
- 不重算上游
- artifact schema 可續接

視覺細節可不同，但 Canonical Decision 不得漂移。

預習單與課後短文單都必須列入 conformance test；預習單另驗證 A／B 模式、300 DPI、安全白邊、逐課 batch queue、verified/native-text fallback 與 portable Drive target 語意。

靜態規格檢查見：`tests/platform-conformance/2026-08-11-static-conformance-report.md`。

`SPEC_PASS` 不等於 runtime PASS；沒有實際四平台測試資料時不得標記 `FULLY_VERIFIED_CROSS_PLATFORM`。

## 核心金句

> V-MAX 不屬於任何一個 AI；換平台是在換駕駛，不是在換教材系統。

> Bundle 可以重建，canonical 不分叉。
