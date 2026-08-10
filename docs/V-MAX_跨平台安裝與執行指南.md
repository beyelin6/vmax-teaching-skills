# V-MAX 跨平台安裝與執行指南 1.0

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

## ChatGPT

定位：對話式主要工作台。

使用方式：
- 讀 Universal Bootstrap + ChatGPT Adapter。
- 連接器可用時直接讀 GitHub / Google Drive。
- 適合 Golden Path、Checkpoint Resume、學習單、腳本、圖像與 PDF。
- 缺 connector 時不得假裝已同步；輸出 portable artifact 等待其他執行端保存。

## Claude

定位：Skill 執行、長文件分析與結構化產出。

安裝方式：
- 以每個 V-MAX skill folder 的 `SKILL.md` 為主檔。
- references / assets / scripts 隨 Skill 一起提供。
- Claude 端 Skill 是執行副本；更新以 GitHub canonical 為準。

## Codex

定位：Repository、程式、驗證、批次與自動化。

使用方式：
- 讀 Universal Bootstrap、Manifest、Codex Adapter。
- 適合改 Skill / Policy / Schema、Renderer pipeline、測試與批次工具。
- 不因程式化方便而改 Teacher Intent 或重算已核准教材。

## Gemini Spark

定位：可安裝 Skill 的 Workspace / Drive 導向執行端。

安裝方式：
- Skill 主檔固定 `SKILL.md`。
- Skill name 使用 kebab-case。
- frontmatter 至少包含 `name`、`description`。
- 多檔技能可包含 references / assets / scripts。
- 同名 Skill 更新前先比對 canonical；不要用舊副本覆蓋新版。

## Google Drive

Drive 保存：
- portable checkpoint / artifact
- 教材主檔
- 預習單／短文單來源與成品
- NotebookLM / Renderer MD
- 圖片與正式 PDF
- 使用指南與跨平台操作文件

GitHub 管規則；Drive 管老師帶著走的成果。

## 換平台時怎麼說

最簡單：

> 請載入 V-MAX，使用這份已確認的教材主檔／checkpoint，直接做＿＿＿，不要重新分析教材。

例如：

> 請載入 V-MAX，用第一到第六課已確認資料，直接做自由手繪版預習單，不重新分析。

## Skill 更新

GitHub canonical Skill 更新後：

1. 比對平台同名 Skill。
2. 無本地客製 → 更新。
3. 有本地客製 → 比較差異。
4. 會改 Teacher Intent / schema / HOLD → 先人工審核。
5. 平台臨時改動不得直接變成 V-MAX 全域規則。

## 跨平台品質測試

同一 artifact + 同一 target skill 在不同平台應保持：
- 教材事實一致
- Teacher Intent 一致
- 形近字／多音字等已核准決策一致
- checkpoint 邊界一致
- 不重算上游
- artifact schema 可續接

視覺細節可不同，但 Canonical Decision 不得漂移。

## 核心金句

> V-MAX 不屬於任何一個 AI；換平台是在換駕駛，不是在換教材系統。
