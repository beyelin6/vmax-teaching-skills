# Page Family Construction Contracts

版本：1.0

每一頁正式施工前都必須選定一個 `page_family_contract_id`。版型可以由 Style Matrix 提供多種視覺變體，但不能省略頁型契約或用通用模板代替。`PAGE_DETAIL_CONFIRMATION` 必須保存契約 ID、頁型專屬計畫與對應來源。

## Contract registry

| Contract ID | 適用 page family | 學生頁必備內容 | 圖像／版型規則 | 禁止事項 |
|---|---|---|---|---|
| `OPENING` | `OPENING`、`COVER` | 課名、單一導入訊息、必要導覽 | 主題主視覺＋清楚閱讀動線；留足投影安全區 | 塞入課文、成語清單或教師講解 |
| `OVERVIEW` | `OVERVIEW`、`LESSON_OVERVIEW` | 課文總說、核心問題或學習目標 | 1 個主訊息＋最多 3–5 個導覽節點 | 把整課知識表格化或提前講完答案 |
| `VISUAL_MIND_MAP` | `VISUAL_MIND_MAP`、`LESSON_VISUAL_MAP` | 中心主題、3–5 個有來源的關係節點 | 圖像關係優先，節點沿閱讀方向排列 | 把所有生字、成語、活動硬塞同一張 |
| `TEXT_READING` | `TEXT_READING_PAGE`、`PARAGRAPH_TEXT`、`TEXT_AND_CONTEXT` | 完整自然段／意義單位、原文語詞、相鄰解釋 | 課文為獨立文字物件；一段一頁，過長才依完整句子拆頁 | 摘錄代表句、改寫、獨立語詞清單頁 |
| `COMPREHENSION` | `COMPREHENSION`、`MEANING_COMPREHENSION` | 課文證據、1 個主問題、最多 1 個追問 | 證據靠近問題；保留學生思考空間 | 學生頁直接放答案或密集考卷題 |
| `RHETORIC` | `RHETORIC`、`RHETORIC_DISCOVERY` | 完整原句、關鍵詞、效果推測、修辭名稱、短練習 | 一頁一種主要修辭；先看見效果再命名 | 名稱／定義／例句三欄表、先給術語答案 |
| `SENTENCE_PATTERN` | `SENTENCE_PATTERN` | 課文例句、句意、結構骨架、新情境、分層仿說 | 例句先於公式，結構用視覺關係呈現 | 只放抽象公式、一次塞多個句型 |
| `SHAPE_NEAR` | `CHARACTER_COMPARISON_PAGE`、`SHAPE_NEAR` | 1–2 組形近字；每字大字、注音、部件、例詞、字義情境 | 預設一組，最多兩組；部件差異是主視覺焦點 | 第三組、滿版字表、圖片模型生成國字 |
| `POLYPHONIC` | `POLYPHONIC`、`POLYPHONIC_PAGE` | 同字不同音、各自語意、例詞／例句、情境、回到課文問題 | 每頁一個多音字，兩個讀音清楚對照 | 把不同字誤當多音字、只背注音不連語境 |
| `IDIOM` | `IDIOM`、`IDIOM_APPLICATION` | 成語、學生友善釋義、自然例句、引申義、例句情境圖 | 一頁一成語為預設；圖配合例句實際用法 | 畫成語字面、為配圖硬改例句、密集三欄卡片 |
| `LANGUAGE_ACTIVITY` | `LANGUAGE_ACTIVITY`、`TEXTBOOK_ACTIVITY`、`ACTIVITY` | 教材活動原題／任務、操作步驟、學生產出格式 | 任務動線清楚，答案放教師層 | 自行改寫官方題目、把答案放學生頁 |
| `SUMMARY_TRANSFER` | `SUMMARY_TRANSFER`、`SUMMARY`、`TRANSFER` | 一句總結、關鍵證據、生活／寫作遷移提示 | 收束整課並保留學生回應空間 | 新增未教內容、重複整課知識表 |

## Shared construction fields

所有契約都必須具備：`page_purpose`、`student_visible_text`、`source_refs`、`image_spec`、`layout_spec`、`character_refs`、`OBJECT_COMPOSITION_PLAN`、`canvas_lock`、`projection_typography`、`teacher_notes_ref` 與 `page_spec_sha256`。頁型專屬欄位放在 `page_specific_plan`，不得只寫一句圖片 prompt。

## Gate

缺少 `page_family_contract_id`、契約 ID 與 `page_family` 不相容、專屬計畫缺欄或違反容量／文字／圖像規則時，標記 `PAGE_FAMILY_CONTRACT_MISSING`、`PAGE_FAMILY_CONTRACT_MISMATCH` 或該契約專屬 failure code，停止代表頁與批次 Renderer。
