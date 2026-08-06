# Lesson Knowledge Book Schema

版本：0.1.0

## 目的

Lesson Knowledge Book（LKB）是單一課程的唯一知識主檔。所有簡報、NotebookLM 來源、學習單與評量均由 LKB 派生。

## 文件控制

```yaml
lkb:
  lesson_id: ""
  title: ""
  grade: ""
  semester: ""
  version: "0.1.0"
  status: draft
  created_at: ""
  updated_at: ""
  approved_by: ""
  source_files: []
```

允許狀態：

- `draft`
- `needs_review`
- `ready_for_teacher_review`
- `approved_lkb`
- `superseded`

## 知識節點共同欄位

每個重要節點至少包含：

```yaml
node:
  id: ""
  title: ""
  layer: official | teacher | extended | teaching | presentation
  source_type: textbook | teacher_guide | workbook | publisher_resource | teacher_input | system_extension
  source_file: ""
  source_page: ""
  source_section: ""
  content: ""
  confidence: confirmed | probable | needs_review
  teacher_approved: false
  notes: ""
```

## 來源標籤

- `[官方｜課本]`
- `[官方｜教師手冊]`
- `[官方｜習作]`
- `[官方｜出版社資源]`
- `[教師補充]`
- `[系統延伸]`
- `[教學設計]`
- `[呈現映射]`

## 必要章節

### 0. 文件控制與來源索引

記錄版本、狀態、來源檔、頁碼範圍、教師核准紀錄與變更摘要。

### 1. 基本資訊與教材定位

課次、課名、作者、文體、年級、單元、官方主旨、官方大意、學習重點與議題。

### 2. 課文原文

完整課文、段落編號、標點與來源頁碼。不得改寫。

### 3. 官方教材知識

#### 3.1 字詞基礎工程

生字、認讀字、部首、筆畫、字形提醒與教材例詞。

#### 3.2 全部核心詞語與成語

全部教材詞語、詞義、語境原句、教材延伸成語。

#### 3.3 字形字音辨析

形近字、音近字、多音字、易錯字與教材例詞。

#### 3.4 文本解析

文體、主旨、大意、賞析、結構圖、段落大意。

#### 3.5 官方修辭、句型與寫作特色

教師手冊或教材明確提供的修辭、句型、短語、複句分類、寫作特色與例句。

#### 3.6 語文焦點與教材活動

我會認字、認識句子、我會說話、習作、教材閱讀理解、參考答案、教學引導與亮點教學。

### 4. 教師知識與教學決策

教師補充、修正、刪減、班級迷思、教學需求與核准決策。

### 5. 系統延伸知識

教材未提供的補充分析。每項需附 `[系統延伸]` 與支持依據。

### 6. 意義段知識單元

每段整合官方資訊、教師補充、系統延伸與教學設計，來源標籤不可省略。

### 7. 教學設計

DOK、差異化教學、活動、評量、課堂節奏與延伸任務。

### 8. 呈現與輸出映射

標記知識節點預計進入：

- NotebookLM
- 教師版簡報
- 學生版簡報
- 講者備註
- 學習單
- 評量
- 插圖或圖表需求

### 9. 驗證、差異與待確認事項

記錄完整性驗證、來源衝突、教師決策與尚未確認項目。

## 派生輸出規則

任何派生檔案開頭都要包含：

```yaml
derived_from:
  lkb_file: ""
  lkb_version: ""
  generated_at: ""
  included_nodes: []
```

派生檔案不得反向取代 LKB。內容修正要先更新 LKB，再重新生成。
