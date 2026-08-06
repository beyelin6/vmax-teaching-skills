# V-MAX Master Architecture v4

> 狀態：Foundation Draft  
> 版本：0.1.0  
> 目標平台：Codex、GitHub、NotebookLM、簡報生成流程

## 1. 系統定位

V-MAX 不是固定頁數的教材模板，而是一套依每課教材動態分析、組合與生成的課程製作系統。

核心公式：

> Skill 保存方法；Library 保存可重用資源；Lesson Project 保存當課事實與教師決策；Output 保存當課成果。

## 2. 四層架構

### 2.1 Skill Layer

保存穩定的工作方法與驗證規則，不保存特定課文內容。

初始核心技能：

1. `chinese-textbook-transcriber`
2. `chinese-lesson-designer`
3. `chinese-slide-architect`
4. `chinese-extension-materials`

### 2.2 Library Layer

保存跨課程可重用資源：

- Style Library
- Role Library
- Layout Library
- Illustration Prompt Library
- Teaching Activity Library
- Knowledge Library

Library 只提供選項與規則，不得覆蓋教材事實。

### 2.3 Lesson Project Layer

每課建立獨立專案，保存：

- 原始教材
- 教師手冊
- 教師補充
- 忠實轉錄
- 當課分析
- 教師確認紀錄
- 視覺與角色選擇
- 當課輸出設定

### 2.4 Output Layer

保存當課生成成果：

- NotebookLM Source MD
- NotebookLM 生成指令
- 投影片腳本
- PPTX
- 教師講者備註
- 預習單、仿作單、評量等延伸教材
- Output Manifest

## 3. 動態工作流

```text
輸入教材
  ↓
來源盤點
  ↓
忠實轉錄
  ↓
防漏與分類檢查
  ↓
教師確認 Gate 1
  ↓
本課教學分析
  ↓
必要／條件／選配模組決策
  ↓
教師確認 Gate 2
  ↓
風格、角色與輸出設定
  ↓
NotebookLM Source 與生成指令
  ↓
投影片腳本與插圖需求
  ↓
品質驗證
  ↓
簡報與延伸教材
```

## 4. 每課動態原則

每課必須重新判斷：

- 年級、學期與課次
- 文體
- 課文結構
- 教學目標
- 語文焦點
- 生字、認讀字、所有核心詞語與成語
- 修辭與句型
- 教學難點
- 必要模組
- 條件模組
- 教師選配模組
- 建議投影片頁數
- 適合的風格與角色
- 適合的延伸教材

禁止：

- 固定使用 43 頁或任何預設頁數
- 無條件複製上一課章節
- 把上一課內容帶入下一課
- 為了套版而刪除教材必要內容

## 5. 三類課程模組

### 5.1 必要模組

依來源存在且通常必須處理，例如：

- 課程基本資訊
- 課文理解
- 生字與認讀字
- 所有核心詞語
- 課文結構與主旨
- 課程總結

### 5.2 條件模組

只有教材具備時才生成，例如：

- 成語
- 修辭
- 特殊句型
- 寫作手法
- 心智圖
- 比較表
- 四格漫畫
- 語文活動

### 5.3 教師選配模組

由教師決定是否生成，例如：

- 課前預習單
- 童詩仿作單
- 閱讀理解單
- DOK 任務
- 評量
- Exit Ticket
- Padlet 或線上活動

## 6. Skill 邊界

### 6.1 Chinese Textbook Transcriber

負責：

- PDF／文件來源盤點
- 課文與教材內容忠實擷取
- 生字、認讀字、詞語、成語與題目分類
- 圖表、插圖與版面資訊描述
- 防漏檢查

不負責：

- 選風格
- 決定投影片頁數
- 擴寫教學活動

### 6.2 Chinese Lesson Designer

負責：

- 文體、結構與主旨分析
- 教學焦點與難點
- 必要、條件與選配模組判斷
- DOK 與課堂活動建議
- 動態頁數範圍建議

前提：轉錄已確認。

### 6.3 Chinese Slide Architect

負責：

- 將已確認教學藍圖轉為 NotebookLM Source
- 產生精簡生成指令
- 建立逐頁腳本
- 規畫畫面、文字、插圖與教師備註
- 驗證學生頁無答案

### 6.4 Chinese Extension Materials

負責：

- 預習單
- 仿作單
- 學習單
- 閱讀理解
- 評量與 Exit Ticket

只有當課設定啟用時才執行。

## 7. Style Library 規格

每個風格資料夾至少包含：

```text
style.md
palette.json
layout-rules.md
illustration-rules.md
```

`style.md` 必須記錄：

- `style_id`
- 名稱與版本
- 適用年級、文體與主題
- 不適用情境
- 視覺語言
- 材質與配色
- 標題與圖卡系統
- 依文體動態適配規則

風格不是固定版面，而是可依教材內容調整的視覺 DNA。

## 8. Role Library 規格

每個角色至少包含：

- `role.md`
- `visual-dna.md`
- `dialogue-style.md`
- `pose-library.md`

角色控制外觀與引導語氣，不控制教材事實。

## 9. Lesson Project 標準結構

```text
lesson-id/
├── input/
│   ├── textbook.pdf
│   ├── teacher-guide.pdf
│   └── teacher-additions.md
├── working/
│   ├── transcription.md
│   ├── quality-report.md
│   ├── lesson-profile.md
│   ├── review-notes.md
│   └── approved-plan.md
├── config/
│   ├── lesson-config.md
│   ├── selected-style.md
│   └── selected-role.md
└── output/
    ├── notebooklm-source.md
    ├── notebooklm-instruction.md
    ├── slide-script.md
    ├── presentation.pptx
    └── output-manifest.md
```

## 10. Lesson Configuration 核心欄位

```yaml
lesson:
  id: G4S1-L02
  title: 第二課 放學後
  grade: 四年級
  semester: 上學期

workflow:
  current_stage: transcription_review
  require_teacher_approval: true
  allow_generation_before_approval: false

content:
  preserve_all_textbook_content: true
  include_all_core_vocabulary: true
  slide_count_mode: dynamic

visual:
  style_id: null
  role_id: null
  illustration_policy: regenerate_by_meaning

outputs:
  notebooklm_source: true
  notebooklm_instruction: true
  slide_script: true
  pptx: true
  speaker_notes: true
```

## 11. NotebookLM 原則

- Source MD 保存完整教材與教學內容。
- 生成指令只保存操作規則、版型規則與輸出限制。
- 不在指令檔重複貼入大量來源內容。
- 避免生成兩個 `slides` 節點。
- 角色 DNA 變數必須在輸出前完成替換。
- 學生可見內容不得洩漏教師答案。

## 12. 驗證系統

### 12.1 可腳本化檢查

- 必要檔案存在
- 核心詞語是否完整
- 認讀字與習寫字是否混淆
- 是否存在重複 `slides` 節點
- 是否仍有未替換變數
- 學生頁是否出現答案標記
- 輸出是否寫入正確課程資料夾

### 12.2 需模型判斷

- 主旨與結構分析
- 修辭與寫作手法
- 教學活動適切性
- 視覺風格適配
- 插圖是否符合句意
- 頁面敘事是否連貫

## 13. 版本管理

採語意化版本：

- Major：架構或輸出契約不相容變更
- Minor：新增技能、風格或可選功能
- Patch：修正文案、規則與驗證錯誤

技能、風格、角色與 Schema 各自保留版本欄位。

## 14. Repository 目標結構

```text
vmax-teaching-skills/
├── AGENTS.md
├── README.md
├── VERSION
├── docs/
├── skills/
├── libraries/
│   ├── styles/
│   ├── roles/
│   ├── layouts/
│   ├── illustration-prompts/
│   ├── teaching-activities/
│   └── knowledge/
├── schemas/
├── templates/
├── examples/
├── scripts/
└── tests/
```

## 15. 第一階段里程碑

1. 建立四個核心 `SKILL.md`。
2. 建立 Lesson Configuration 與 Lesson Profile 樣板。
3. 匯入兩個代表性測試課程：童詩與記敘文。
4. 建立最初兩套風格與一個角色 DNA。
5. 建立核心詞語、防重複節點與未替換變數檢查。
6. 驗證同一套技能可生成不同模組與不同頁數。

## 16. 驗收標準

- 不同課文不會產生完全相同的固定章節。
- 所有教材核心詞語皆有追蹤紀錄。
- 文體不同時，教學藍圖與視覺配置會實質改變。
- 教師確認關卡生效。
- Source MD 與生成指令責任分離。
- 學生版不顯示答案，教師資訊可被完整保存。
