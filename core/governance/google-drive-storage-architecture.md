# V-MAX Google Drive Storage Architecture 1.0

## 定位

本檔定義 V-MAX 在 Google Drive 的 canonical 儲存分層。目的不是強迫所有成果都塞進單課資料夾，而是依「系統／跨課共用／冊別批次／單課版本」分層，讓教師能在不同電腦、手機與 AI 平台中快速找到並續作。

核心原則：

> 系統資料放系統層；跨課共用資產放主體架構；冊別批次成果放冊別層；真正屬於單課版本的成果才進 Lesson Package。

> Batch Artifact 不必為了符合單課六類而重複複製六份實體檔。

---

## 1. Canonical Root Structure

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
    └── {冊別}/
        ├── 00_教材鎖定主檔/
        ├── 原始教材手冊/
        ├── {批次範圍}_預習單規劃/
        ├── {批次範圍}_課後短文學習單/
        └── 03_分課教學簡報與教材/
            └── {課次}_{課名}/
                ├── 01_教材整理/
                ├── 02_逐頁腳本/
                ├── 03_NotebookLM/
                ├── 04_角色視覺/
                ├── 05_簡報成品/
                └── 06_延伸教材/
```

現行四上康軒國語案例：

```text
01_國語教學資源/
└── 四上康軒國語/
    ├── 00_教材鎖定主檔/
    ├── 原始教材手冊/
    ├── 01-06課_預習單規劃/
    ├── 01-06課_課後短文學習單/
    └── 03_分課教學簡報與教材/
```

---

## 2. Level 0｜00_系統與數據管理

只放跨課、跨冊、跨平台運作需要的系統性資料：

- 使用指南與中文指令速查表
- Runtime State / checkpoint registry
- 國語文教材轉錄數據
- 其他全域系統操作文件

不得把單課成品、單課角色圖或單課 PDF 混入此層。

---

## 3. Level 1｜主體架構

`主體架構/` 定義為「跨課、跨冊可重用的 V-MAX 教學與視覺資產層」。可放：

- recurring Character DNA / 角色資料庫
- Canva 中文字型庫與後製修字規則
- 視覺語言與跨課 Style Reference
- 可重用 Gold Page / Layout Reference
- 共用教學框架、模板或視覺資產

禁止：
- 單課正式教材主檔
- 單課成品 PDF
- 只屬於某課的臨時角色／插圖

若資產尚未經教師確認為跨課重用，先留在單課或 candidate 區，不自動升級到主體架構。

---

## 4. Level 2｜學科／冊別資源

`01_國語教學資源/{冊別}/` 是冊別工作台。

### 4.1 `00_教材鎖定主檔`

定位：冊別權威資料來源層。

存放各課已鎖定的教材 Markdown／Source Master，例如：
- 第01課教材鎖定主檔
- 第02課教材鎖定主檔
- ...

它不同於單課版本中的 `01_教材整理`：

> `00_教材鎖定主檔` = 冊別資料庫／權威來源。
>
> 單課 `01_教材整理` = 該次 Golden Path／Checkpoint Resume 實際使用的版本化工作資料。

兩者可互相引用，但不得因歸檔方便而混為同一層。

### 4.2 `原始教材手冊`

放原始 PDF、教師手冊與來源文件，不放 AI 生成成品。

---

## 5. Level 3｜冊別 Batch Artifact

當一項技能一次跨多課產出「同系列教材」，且教師使用時本來就會整批查找／下載／合併，應保存為冊別 Batch Artifact，而不是強迫實體檔分散到各課 `06_延伸教材`。

典型：
- `01-06課_預習單規劃`
- `01-06課_課後短文學習單`
- 未來的 01-06 課仿作單、複習單、評量系列

Batch Artifact Folder 最低建議結構：

```text
{批次範圍}_{教材類型}/
├── 單課PNG/
├── 合併PDF/
└── {冊別}_{批次範圍}_{教材類型}內容確認主檔.md
```

若同一教材有多個視覺版本，可在 `單課PNG/` 下再分版本，例如：

```text
單課PNG/
├── 一般版/        # alias of A｜清楚框線版
└── 自由手繪版/    # B｜自由手繪版
```

### Batch 規則

- 每課仍必須使用自己的 checkpoint / content scope，不得混課。
- 一次可下六課任務，但執行採逐課渲染、逐課驗證。
- 某課缺必要資料時，只阻塞該課，不阻塞其他課。
- 若內容、角色、版本模式已核准，不要求每課重複確認同一決定。
- 合併 PDF 只在所有納入頁面通過各自驗證後建立。

### 單課 `06_延伸教材` 與 Batch 的關係

- 單課獨立產物 → 可直接放該課 `06_延伸教材`。
- 跨課系列的正式實體檔 → 優先放冊別 Batch Artifact Folder。
- 單課 Lesson Package 如需追溯，可保存 reference / artifact pointer，不必再複製一份相同實體檔。

---

## 6. Level 4｜分課 Lesson Package

`03_分課教學簡報與教材/{課次}_{課名}/` 保留六類：

```text
01_教材整理/
02_逐頁腳本/
03_NotebookLM/
04_角色視覺/
05_簡報成品/
06_延伸教材/
```

映射：
- `CP_SOURCE_ANCHOR / CP_TEACHING_ANALYSIS / CP_LESSON_CONTENT_MASTER` → `01_教材整理`
- `CP_SLIDE_SCRIPT / RENDERER_DETAILED_SCRIPT_MD` → `02_逐頁腳本`
- `NOTEBOOKLM_SOURCE_MD / NOTEBOOKLM_INSTRUCTION_MD` → `03_NotebookLM`
- lesson-specific Character DNA / reference → `04_角色視覺`
- `INFOGRAPHIC_TEACHING_PDF / INFOGRAPHIC_PAGE_PNGS / PAGE_PREFLIGHT_REPORT` → `05_簡報成品`
- 單課獨立延伸教材 → `06_延伸教材`

---

## 7. Alias Rule

目前教師使用的資料夾名稱可保留，不需要為了 canonical 名稱搬動 Drive。

```yaml
folder_aliases:
  A_CLEAR_FRAME:
    canonical_name: 清楚框線版
    accepted_drive_aliases:
      - 一般版
      - 標準版
      - 清楚框線版
  B_FREEHAND:
    canonical_name: 自由手繪版
    accepted_drive_aliases:
      - 自由手繪版
```

系統在讀取 Drive 時應先解析 alias，再判斷版本；不得因資料夾叫「一般版」就另建第二個「清楚框線版」資料夾。

---

## 8. Source + Output Pairing

凡教師之後可能需要重新生成、修改或跨平台續作的系列教材，不應只保存 PNG / PDF。

至少保存：
- 內容確認主檔／source artifact
- 單課成品
- 合併成品（若有）

例如課後短文系列建議：

```text
01-06課_課後短文學習單/
├── 單課PNG/
├── 合併PDF/
└── 四上國語_第一至六課_課後短文內容確認主檔.md
```

---

## 9. 不搬檔優先

當 Drive 現況已符合新架構但 GitHub 規格落後：

1. 優先更新 GitHub 規則。
2. 不為了文字一致而大量搬動現有 Drive 檔案。
3. 只有實際發生查找困難、重複檔案或錯誤歸檔時才進行 Drive migration。

---

## 失敗分類

- `DRIVE_STORAGE_LAYER_DRIFT`
- `BATCH_ARTIFACT_SCATTERED`
- `BATCH_SOURCE_MASTER_MISSING`
- `SYSTEM_FILE_MISPLACED`
- `LESSON_ARTIFACT_MISPLACED`
- `FOLDER_ALIAS_DUPLICATION`

---

## 核心金句

> 冊別資料集中管理，單課版本獨立演化；批次成果不必為了形式被拆散。

> Drive 的目標不是「每個規則都有一個資料夾」，而是老師換裝置後仍能最快找到下一步要用的東西。
