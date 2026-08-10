# V-MAX 中文指令速查表

版本：1.4

## 你不需要記英文代碼

只要直接用中文說你要做什麼。

### 從頭完整做
> 從第一課重新開始完整流程。

→ `FULL_GOLDEN_PATH`

### 用之前資料繼續
> 用上次分析好的資料繼續，不要重跑前面。

→ `CHECKPOINT_RESUME`

### 批次做預習單
> 用第一到第六課分析好的資料，批次做六份 A4 橫式預習單，不要重新分析教材。

→ 先由 `prestudy-worksheet` 產生已核准 `PRESTUDY_WORKSHEET_SOURCE`，再由 `vmax-chinese-preview-worksheet` 逐課渲染、逐課校字、逐課驗證。

### 指定預習單版本
> 用第一到第六課已確認的預習單內容，直接做自由手繪版。

→ `output_mode: B_FREEHAND`

> 用已確認內容做清楚框線版。

→ `output_mode: A_CLEAR_FRAME`

A 版別名：一般版／標準版／清楚框線版。B 版別名：自由手繪版／手繪版。

Renderer 不重新分析教材；唯一最低輸入為 `PRESTUDY_WORKSHEET_SOURCE`。AI 中文局部修復仍失敗時改走 verified/native-text fallback。PDF 共通壓縮與 preflight 讀 Core PDF Contract；A4 維持 300 dpi、3508×2480、4.5 mm 安全白邊。

### 批次做短文單
> 用第一到第六課整理好的教材主檔，批次做六份課後短文 Bonus 學習單。

### 做逐頁腳本
> 用第一課分析主檔直接做逐頁腳本。

### 做 NotebookLM / Renderer MD
> 用第一課逐頁腳本直接整理成 NotebookLM 與 Renderer 詳細 MD。

### 做圖片式簡報
> 用第三課簡報生成資料直接做圖片式教學 PDF。

### 先停下來
> 今天先做到教材主檔，存起來下次接著做。

> 今天先做到逐頁腳本，先不要產簡報。

→ 停下來時不只建立 checkpoint，也要確認 Google Drive 已保存可續作副本。

### 局部重做
> 只重做第二課形近字頁。

> 只改第三課成語部分。

> 第一課只換角色，不改教學內容。

> 只重做第 8、9、10 頁。

---

## 中文名稱 ↔ 系統名稱

| 中文 | 系統名稱 |
|---|---|
| 教材來源整理／教材定錨 | `CP_SOURCE_ANCHOR` |
| 教學分析 | `CP_TEACHING_ANALYSIS` |
| 教材主檔／分析主檔／內容母檔 | `CP_LESSON_CONTENT_MASTER` |
| 預習單資料包 | `CP_PRESTUDY_INPUT` |
| 已核准預習單內容 | `PRESTUDY_WORKSHEET_SOURCE` |
| 視覺教學設計／視覺意圖 | `CP_VISUAL_INTENT` |
| 逐頁腳本 | `CP_SLIDE_SCRIPT` |
| 簡報生成資料包 | `CP_RENDER_READY` |

---

## 在哪裡跑

- **ChatGPT**：直接用中文操作、續跑 checkpoint、批次做預習單／短文單／腳本／PDF。
- **Claude**：安裝 V-MAX Skill 後執行長文件分析、結構化工作與 portable artifact。
- **Codex**：GitHub 規格、技能、Renderer、批次腳本與大量檔案維護。
- **Gemini Spark**：以 `SKILL.md` 安裝 V-MAX Skill，搭配 Drive／Workspace 使用。
- **NotebookLM**：讀已核准的 Source MD / Instruction MD，做來源導向生成。
- **Google Drive**：跨電腦／手機找檔、續作、下載與保存 checkpoint／成果。
- **GitHub**：保存 V-MAX 的 skill、policy、schema、registry 與系統規則。

---

## Google Drive｜新版分層

```text
V-MAX 教材庫/
├── 00_系統與數據管理/
├── 主體架構/
└── 01_國語教學資源/
    └── 冊別/
        ├── 冊別共用來源／教材鎖定主檔/
        ├── Batch Artifact/
        └── 03_分課教學簡報與教材/
```

跨多課的同系列教材不必重複塞進每課 `06_延伸教材`；集中放冊別 Batch Folder，單課只需要 reference。

實際 Drive folder/file ID 不寫死在 canonical Skill；執行時從 project/runtime artifact、checkpoint 或 Drive 查詢取得。

---

## 三句最常用

> **從頭完整做……**

> **用之前做好的資料，直接做……**

> **今天先做到……，存起來下次接著做。**

---

## 維護

若 checkpoint、技能 I/O、批次能力、常用輸出、中文別名、平台角色、預習單內容／Renderer 邊界或 Google Drive 分層規則更新，本速查表必須與 `docs/V-MAX_使用指南.md`、`docs/V-MAX_跨平台安裝與執行指南.md` 及 Google Drive 現行副本同步更新；不同步標記 `USER_GUIDE_STALE / USER_GUIDE_DRIVE_STALE`。
