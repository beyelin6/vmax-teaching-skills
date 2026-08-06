# V-MAX 四層教材工程架構

版本：1.0.0

## 核心原則

V-MAX 採四層分工：教材知識固定、學習模組可組合、教學策略可調整、輸出形式可選擇。

```text
Lesson Knowledge
      ↓
Learning Modules
      ↓
Teaching Strategy
      ↓
Presentation Engine
```

## 第一層：Lesson Knowledge

唯一可信教材來源。完整保留課本、教師手冊、習作、出版社資源與教師確認內容。

包含：

- 課文原文
- 生字與認讀字
- 全部核心詞語
- 教材明示成語
- 教材明示修辭與句型
- 文體、主旨、結構與寫作特色
- 教材活動、閱讀理解、習作與官方參考答案

此層不得因簡報需求而刪改，也不得把系統延伸冒充官方教材內容。

## 第二層：Learning Modules

針對 LKB 中的知識節點掛載可選學習模組。模組只增加學習支援，不改寫官方知識。

例如成語可掛載：

- 情境理解
- 易誤用辨識
- 近義與反義辨析
- 看圖判斷
- 造句應用
- 生活連結
- 討論
- 遊戲
- 練習與評量

修辭、句型、生字、課文理解與寫作知識亦可掛載各自模組。

## 第三層：Teaching Strategy

將已選定的 Learning Modules 編排成教學流程，例如：

- 引起動機
- 示範講解
- 同儕討論
- 個別練習
- 差異化支援
- 形成性評量
- Exit Ticket

此層處理「怎麼教」，不是「教材寫了什麼」。

## 第四層：Presentation Engine

將前面三層映射成所需格式：

- Lesson Knowledge Book
- Curated Briefing
- NotebookLM Source
- 教師版 Markdown
- 學生版 Markdown
- Slide Source
- PPTX
- 學習單
- 評量

每個輸出必須記錄來源 LKB 版本、啟用模組及教學策略設定。

## Skill 職責

Skill 是執行工具，不是知識主體。

- `chinese-textbook-transcriber`：建立官方知識與來源索引。
- `chinese-lesson-knowledge-builder`：建立 LKB。
- `learning-module-builder`：依設定掛載學習模組。
- `teaching-strategy-planner`：編排教學流程。
- `presentation-engine`：產生不同輸出。

## 變動原則

每課教材不同，因此：

- LKB 依教材動態建立。
- Learning Modules 依能力目標與年級選擇。
- Teaching Strategy 依課堂需求調整。
- Presentation 依輸出目的選擇。
- 不固定頁數、不固定章節數、不沿用上一課內容。
