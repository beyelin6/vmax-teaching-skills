# Lesson Architecture Profile

版本：1.1

本檔是每課國語教學簡報的 canonical 內容骨架。目標是指定內容完整、可直接投影教學；依內容決定頁數，不固定堂數、總頁數或每段頁數。課時需求另依 Session Director，不改變必備內容的覆蓋。

## 十項呈現流程

| 順序 | 教學內容 | 呈現要求 |
| --- | --- | --- |
| 1 | 課程封面 | 課次、課名、作者或改寫來源與本課意境主圖。 |
| 2 | 讀前引導 | 貼近學生生活並連結課文核心的問題；不先公布練習答案。 |
| 3 | 整課學習地圖 | 圖像呈現理解路線與本課重點；課文總說可整合在此，不強制另增一頁。 |
| 4 | 依序閱讀課文 | 完整原文、標點與段落順序，合理分頁；插圖對應原文，核准語詞標記及短解釋優先同頁相鄰。 |
| 5 | 隨文語文教學與提問 | 隨相關段落穿插文意、關鍵句、句型、修辭、課文成語與口說練習；必要時另頁，不套每段固定活動或頁數。 |
| 6 | 正式生字總覽 | 全部正式生字、注音、例詞及助理解小插圖，可分頁；不等於每字獨立詳解。認讀字若有須分流，不混入正式書寫字數。 |
| 7 | 形近字／字群辨析 | 依核准範圍比較相同／不同部件，搭配注音、例詞、短字義與情境圖。 |
| 8 | 多音字教學 | 清楚區分讀音、詞義、例詞、必要例句與情境；使用已確認的教材主欄及旁欄補充，按核准範圍呈現。 |
| 9 | 生字延伸補充成語 | 與課文成語分開檢核；逐正式生字完成適齡判讀，呈現核准成語、短解釋、自然例句及對應小插圖。依內容可一頁兩個或分頁。 |
| 10 | 全課統整與生活遷移 | 回顧核心脈絡，連結生活問題或行動任務；放在多音字與生字補充成語之後。 |

第 4、5 項交錯進行，不是兩個各自集中到最後的單元。段內可採「原文與詞義 → 圖像理解 → 適用的語文焦點／文意提問 → 下一段」；不是每段都必須有句型、修辭或同一套題目。已核准的教材語文活動嵌入相關段落或語文區段並保留回指，不能因不另設固定尾段而遺漏。

## Baseline 結構

以下為內容區段，不是投影片頁碼或頁型 enum；第 4、5 項共用 paragraph_learning。

```yaml
lesson_architecture:
  id: baseline_language_lesson
  baseline_version: "1.1"
  status: draft
  planning_mode: CONTENT_COVERAGE
  sections:
    - { id: cover, title: 課程封面, required: true }
    - { id: reading_prompt, title: 讀前引導, required: true }
    - { id: visual_mind_map, title: 整課學習地圖, required: true }
    - id: paragraph_learning
      title: 課文閱讀與隨文語文教學
      required: true
      integrated_functions: [text_and_context, vocabulary_explanation, applicable_language_focus, meaning_comprehension]
    - { id: character_overview, title: 正式生字總覽, required: true }
    - { id: character_comparison, title: 形近字與字群辨析, applicability: approved_content }
    - { id: polyphonic_learning, title: 多音字, applicability: approved_content }
    - { id: idiom_learning, title: 生字延伸補充成語, applicability: approved_content }
    - { id: summary_transfer, title: 全課統整與生活遷移, required: true }
```

形近字、多音字與成語區段的檢核必做；內容依教材與教師核准結果成立，確實無適用內容時記錄 N/A 與理由，不虛構內容。生字延伸成語須先完成逐字判讀，不能用空區段或已有課文成語代替雙軌覆蓋。

## 呈現與覆蓋

- 圖像須幫助理解原文、字義、例句或問題；角色依教學需要出場，不強制每頁都有。
- 正式文字清晰、留白充分、標記一致且不遮擋。語詞標記細節沿用課文頁 canonical 規則，正式文字及來源仍須核對。
- 學生可見內容使用臺灣繁體中文；保留必要解釋和示範例句，提問／練習不直接展示答案或教師提示。
- 每項核准內容回指預定呈現區段；逐頁稿階段再回指實際頁碼。成語雙軌與教材活動不得因頁數或模板消失。
- Lesson Map、內容模式 Session Map 與其他內部規劃服務此骨架，不另外要求教師逐項核准已確認的同一份內容。新增內容取捨及後段風格、角色、畫布、逐頁稿、代表頁與批次確認仍按原 stage／HOLD 執行。
- 新課採本骨架；既有確認稿記錄原 baseline_version，僅作差異檢查，不自動重排或重生圖片。教師授權改版後，以 architecture_mapping 保存舊 opening／overview 對封面、引導或總說的實際對應；不能只換 ID 就聲稱內容已補齊。缺少生字總覽等項目須實際補稿。教師要求保留舊順序時記錄變體核准。

## 外加模板

外加模板是同一份 Baseline 的教學呈現變體，可改變活動、媒介、互動、時間配置、轉場與頁面組織。它可以重新設計「怎麼教」，但必須回指 Baseline，逐項標記：

- `preserved`：直接保留
- `transformed`：換一種活動或呈現方式
- `extended`：增加教師核准的延伸
- `omitted`：只可在教師明確決定並記錄理由時省略

外加模板不得把 Official Knowledge 改寫成未標示的 AI 內容；它必須保留教材證據、教師確認的學習重點、成語 provenance 與 Baseline 的必修學習結果。

可選模板：

- `tablet_interaction`：平板標註、排序、分類、錄音、共編或 Exit Ticket。
- `open_class_four_learning`：在 Baseline 上重新組織自學、組內共學、組間互學與教師導學。
- `issue_integration`：將核准的生活議題或跨域連結嵌入相關段落、語文活動或總結遷移。
- `teacher_custom`：教師指定的其他呈現方式。

每個模板都必須保存 `baseline_version`、`architecture_mapping`、`changed_teaching_moves`、`preserved_learning_outcomes`、`fallbacks` 與 `teacher_approved_variant`。模板可以改寫教學呈現，不得讓教師指定的學習骨架與教材必要內容無聲消失。
