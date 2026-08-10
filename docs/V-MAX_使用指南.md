# V-MAX 使用指南｜中文指令優先 × 中英對照

版本：1.3

## 目的

這份指南讓教師以自然中文操作 V-MAX，不要求記住工程化 checkpoint 名稱。英文／代碼只作系統對照，方便跨 ChatGPT、Codex、NotebookLM、GitHub 與其他 Renderer 共用。

核心原則：

> 老師用中文說要做什麼；系統自己判斷要讀哪個 checkpoint、呼叫哪個技能。

> 已確認的資料不重算；技能只讀自己需要的資料。

> 教師之後可能在別台電腦或手機找得到、接著做的成果，都要有 Google Drive 可搜尋副本。

---

## 1. 兩種工作方式

### A. 完整模式｜Golden Path
適合第一次完整建立一課。

常用中文：
- 「從第一課重新開始完整流程。」
- 「這課從教材開始完整跑一次。」

系統對應：`FULL_GOLDEN_PATH`

### B. 跳接模式｜Checkpoint Resume
適合已經完成一部分，只想直接做下一項工作。

常用中文：
- 「用上次分析好的資料繼續。」
- 「不要重跑分析，直接做預習單。」
- 「只做逐頁腳本。」
- 「拿之前的紀錄檔繼續。」

系統對應：`CHECKPOINT_RESUME`

---

## 2. Checkpoint 中英對照

| 系統名稱 | 中文自然說法 | 主要內容 |
|---|---|---|
| `CP_SOURCE_ANCHOR` | 教材來源整理／教材定錨 | 課文來源、生字、認讀字、頁碼、來源證據 |
| `CP_TEACHING_ANALYSIS` | 教學分析 | 教學價值、形近字、多音字、教師指定易錯字、語詞、句型、修辭、成語、閱讀方向 |
| `CP_LESSON_CONTENT_MASTER` | 教材主檔／分析主檔／內容母檔 | 可供預習單、短文單、腳本、NotebookLM、簡報重用的核准內容 |
| `CP_PRESTUDY_INPUT` | 預習單資料包 | 只保留產生預習單需要的內容 |
| `CP_VISUAL_INTENT` | 視覺教學設計／視覺意圖 | Director Intent、Visual Grammar、Gold Page Pattern、角色、畫風、文字整合 |
| `CP_SLIDE_SCRIPT` | 逐頁腳本 | 每頁教什麼、看什麼、如何發現、圖像與文字如何呈現 |
| `CP_RENDER_READY` | 簡報生成資料包／可直接產圖資料 | Renderer 所需的核准內容、文字真值與視覺意圖 |

老師不需要說代碼；中文別名與自然語句都應被系統解析成相同 checkpoint。

---

## 3. 常用中文指令

### 做六課預習單
> 請用之前分析好的第一到第六課資料，批次製作六份 A4 橫式預習單，不要重新分析教材。

系統對應：`CHECKPOINT_RESUME → 各課 CP_PRESTUDY_INPUT / CP_LESSON_CONTENT_MASTER → prestudy worksheet → 逐課渲染驗證 → 冊別 Batch Artifact`

### 做短文單
> 請用第二課整理好的教材主檔直接製作課後短文 Bonus 學習單，不重跑上游分析。

### 做逐頁腳本
> 請用第一課已確認的分析主檔建立逐頁腳本。

### 做 NotebookLM / Renderer MD
> 請用第一課已確認的逐頁腳本，直接整理成 NotebookLM 與 Renderer 可用的詳細 MD。

### 做圖片式簡報 PDF
> 請用第三課已準備好的簡報生成資料，直接製作圖片式教學 PDF。

### 停在某一步
> 今天先做到教材主檔，保存 checkpoint，下次繼續。

> 今天先做到逐頁腳本，先不要產正式簡報。

系統必須保存可重讀 artifact，不得只依聊天記憶續跑。

---

## 4. 批次工作

V-MAX 支援同一技能跨多課批次執行。

例如：
> 幫我把第一到第六課先做教材分析與整理主檔，這次不要做簡報。

> 用第一到第六課整理好的教材主檔，批次製作六份課後短文 Bonus 學習單。

> 第一到第六課只準備預習單資料包，先不要生成學習單。

批次規則：
- 每課使用自己的 checkpoint。
- 一課缺資料，不阻塞其他課。
- 不得跨課混用生字、多音字、閱讀題、答案或 Teacher Intent。
- 可共用技能規則、版面家族與教師明確指定的跨課偏好。
- 一次可以下六課任務，但正式圖像採逐課渲染、逐課驗證。
- 已確認的內容、角色、版本模式不重複詢問；只有缺少必要資料的課才停等。

---

## 5. 同時做不同課不同工作

允許：
> 第一課做逐頁腳本，第二課做預習單，第三課做短文單，第四課先停在教材主檔。

執行器應逐課解析 target skill 與可用 checkpoint，不要求所有課走同一 stage。

---

## 6. 局部重做

可以直接說：
- 「只重做第二課形近字頁。」
- 「第三課簡報只修改成語部分。」
- 「第一課只換角色，不改教學內容。」
- 「只重做第 8、9、10 頁。」
- 「預習單只修改多音字區。」

系統應沿用未受影響的已核准 artifact，只重做受影響部分。

---

## 7. 中文別名解析

```yaml
checkpoint_aliases:
  CP_SOURCE_ANCHOR: [教材來源整理, 教材定錨, 來源整理]
  CP_TEACHING_ANALYSIS: [教學分析, 教材分析結果]
  CP_LESSON_CONTENT_MASTER: [教材主檔, 分析主檔, 內容母檔, 整理好的教材資料]
  CP_PRESTUDY_INPUT: [預習單資料包, 預習單輸入資料]
  CP_VISUAL_INTENT: [視覺教學設計, 視覺意圖, 導演視覺設計]
  CP_SLIDE_SCRIPT: [逐頁腳本, 簡報腳本]
  CP_RENDER_READY: [簡報生成資料包, 可直接產圖資料, 渲染資料包]
```

中文自然語句優先；系統代碼只作內部映射。

---

## 8. 在哪裡可以跑｜Platform Roles

### ChatGPT｜主要互動工作台
適合教材分析、Checkpoint Resume、批次學習單、逐頁腳本、NotebookLM MD、圖片／PDF 生成與 Drive/GitHub 操作（工具可用時）。

### Codex｜規格、程式與大量檔案維護
適合 GitHub skill / policy / registry、Renderer、驗證器、批次腳本與 repository 一致性修改。

### NotebookLM｜來源導向生成
適合匯入已核准 Source MD / Instruction MD 後做來源導向圖文生成；不取代 V-MAX canonical 教學判斷。

### Google Drive｜跨裝置工作台
保存教師跨電腦／手機需要查找、續作、下載或重用的 checkpoint、腳本、角色資產、學習單、PDF 與指南。

### GitHub｜系統規格權威
保存 skill、policy、schema、registry、adapter、quality rule 與指南來源版本；不取代 Google Drive 的工作成果庫。

> **ChatGPT / Codex 負責執行；NotebookLM 負責來源導向生成；Google Drive 負責帶著走；GitHub 負責規則。**

---

## 9. Google Drive canonical 分層

權威：`core/governance/google-drive-storage-architecture.md`。

```text
V-MAX 教材庫/
├── 00_系統與數據管理/
│   ├── 00_使用指南與系統文件/
│   ├── 00_Runtime_State/
│   └── 國語文教材轉錄數據/
│
├── 主體架構/
│
└── 01_國語教學資源/
    ├── V-MAX國語教學簡報/
    └── 四上康軒國語/
        ├── 00_教材鎖定主檔/
        ├── 原始教材手冊/
        ├── 01-06課_預習單規劃/
        ├── 01-06課_課後短文學習單/
        └── 03_分課教學簡報與教材/
```

### 9.1 `00_系統與數據管理`
放系統設定、Runtime、使用指南與教材轉錄數據，不放單課成品。

### 9.2 `主體架構`
定義為跨課、跨冊可重用的教學／視覺資產層，例如：
- recurring Character DNA
- Canva 中文字型庫與後製修字規則
- 視覺語言
- Gold Page / Layout Reference
- 共用教學框架

一個角色／素材若尚未被教師確認為跨課重用，不自動升級到此層。

### 9.3 冊別共用層
`00_教材鎖定主檔` 是冊別權威資料來源；`原始教材手冊` 保存原始 PDF／來源文件。

`00_教材鎖定主檔` 不等於單課版本的 `01_教材整理`：前者是冊別資料庫，後者是某次 Golden Path／Checkpoint Resume 的版本化工作資料。

### 9.4 冊別 Batch Artifact
跨多課的同系列教材集中保存，例如：
- `01-06課_預習單規劃`
- `01-06課_課後短文學習單`

最低建議：

```text
{批次教材}/
├── 單課PNG/
├── 合併PDF/
└── 內容確認主檔.md
```

跨課正式實體檔不必重複塞進每課 `06_延伸教材`；單課 Lesson Package 可保存 reference / artifact pointer。

### 9.5 分課 Lesson Package
真正屬於單課版本的成果放：

```text
01_教材整理
02_逐頁腳本
03_NotebookLM
04_角色視覺
05_簡報成品
06_延伸教材
```

---

## 10. 預習單雙版本資料夾 alias

正式模式：
- A｜清楚框線版
- B｜自由手繪版

Drive 可接受：

```yaml
A_CLEAR_FRAME:
  accepted_drive_aliases: [一般版, 標準版, 清楚框線版]
B_FREEHAND:
  accepted_drive_aliases: [自由手繪版]
```

找到合法 alias 就沿用，不因名稱不同另建重複資料夾。

---

## 11. Google Drive 跨裝置保存

教師會需要查找、續作、下載或重用的成果，都必須有 Drive 可搜尋副本。

老師說「今天先到這裡」時，除了建立 checkpoint，也必須確認 Drive persistence；只存在聊天或暫存區不算完成。

對預習單、短文單等系列教材，應保存：

> **內容確認主檔 + 單課成品 + 合併成品**

不要只保存最後 PDF。

若 Drive 現況已符合教師工作需求、只是 GitHub 規格較舊，優先更新 GitHub，不為名稱一致大量搬動現有檔案。

---

## 12. 最簡單的三句話

> **從頭完整做……** → Golden Path

> **用之前做好的資料，直接做……** → Checkpoint Resume

> **今天先做到……，存起來下次接著做。** → Save Checkpoint + Drive Persistence

---

## 13. 文件維護規則

以下任一項發生 canonical 變更時，必須同步更新本指南、中文速查表與 Google Drive 現行副本：

- checkpoint 名稱、用途或 schema
- `skill_io_contract`
- standalone / batch 能力
- 新增、刪除或更名技能
- Golden Path 與 Checkpoint Resume 的交界
- 常用輸出格式
- 使用者可用的中文別名
- 合法 HOLD
- 平台角色
- Google Drive 分層、Batch Artifact 或 alias 規則

若系統規格已更新但指南未同步，標記：`USER_GUIDE_STALE`；若 GitHub 已更新而 Drive 指南仍舊，標記：`USER_GUIDE_DRIVE_STALE`。

權威來源：
- `V-MAX_MANIFEST.md`
- `core/governance/modular-checkpoint-execution-policy.md`
- `core/governance/skill-io-registry.md`
- `core/governance/google-drive-portable-artifact-policy.md`
- `core/governance/google-drive-storage-architecture.md`
- `skills/vmax-checkpoint-resume/SKILL.md`

---

## 核心金句

> 老師不需要學會系統語言；系統要學會理解老師的中文。

> 一課可以分很多天做，技能可以跳著用、批次用、局部重做；已確認的資料要能一直重用。

> 保存不是模型記得，而是 Drive 找得到。

> 冊別資料集中管理，單課版本獨立演化；批次成果不必為了形式被拆散。
