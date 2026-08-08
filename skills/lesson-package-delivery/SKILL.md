# V-MAX Lesson Package Delivery

版本：1.1

## 目的

本技能定義一課完成後的正式教材包交付與 Google Drive 歸檔流程。

核心原則：

> 一課完成不等於只產出簡報；必須形成可重用、可編修、可再生成、可備份的完整 Lesson Package。

> 交付完成後，若 Google Drive 可用，需同步歸檔至教師指定的 V-MAX 教材庫；不得只停留在 Chat 對話附件。

---

## A. 八項核心交付物

每課基本 Lesson Package 包含：

1. `Source Master MD`｜整個來源整理後的 MD
2. `Renderer Script MD`｜NotebookLM／Renderer 詳細腳本 MD
3. `Visual YAML MD`｜YAML 結構的視覺細節（副檔名使用 `.md`，供 NotebookLM）
4. `Character Visual Assets`｜角色視覺基準圖／本課角色資產
5. `Image-first Slide PDF`｜圖片式簡報 PDF
6. `Teaching Slides PPTX`｜可編輯教學簡報 PPTX
7. `Pre-study Worksheet`｜課前預習單
8. `Post-lesson Short Writing Worksheet`｜課後短文／童詩 Bonus 寫作單

若某課因 Teacher Intent 明確不需要角色或某延伸教材，可標記 `N/A_BY_TEACHER`；不得由 AI 靜默省略。

---

## B. 最低內容規格

### B1. Source Master MD
至少包含：
- 課名／作者／冊別／文體
- 課文原文與自然段／詩節
- 來源 provenance
- 完整生字
- 完整教材詞語聯集
- 教材成語
- 形近字／多音字／部件識字
- 句型／修辭／教材正式語文活動
- 主旨／結構／段意／文本證據
- 閱讀理解素材
- 教師手冊提示
- AI 教學價值判讀
- Teacher Decision / Teacher Intent
- Lesson Map / Session Map
- 補充內容與來源標記
- 預習單與課後短文任務方向

### B2. Renderer Script MD
每頁／每 Shot 至少包含：
- page_id / session / act
- page_function
- learning_gain
- student_visible_text
- source_text / evidence
- core_question
- student_action
- teacher_guidance
- teacher_answer_or_rubric
- reveal_strategy
- pacing / reading / discussion action
- knowledge_chunk
- image_requirement
- visual_grammar
- visual_sequence
- layout_intent
- character role / presence
- scenario use
- renderer_must_preserve
- do_not_do

### B3. Visual YAML MD
內容採 YAML-like 結構，但副檔名一律 `.md`，至少包含：
- lesson_visual_identity
- theme_world
- style_recipe
- art_medium
- palette
- background_texture
- typography
- Traditional Chinese text rules
- hierarchy / spacing / margins
- UI / card / badge rules
- image treatment
- illustration density
- whitespace / depth / layering / rhythm
- Character DNA
- Character placement rules
- Lesson Visual Map rules
- page-family visual intents
- hybrid renderer / native text rules
- visual drift guardrails
- prohibited visual behaviors

### B4. Character Visual Assets
至少定義：
- character name / role
- front / 3-4 view
- key expressions / gestures
- costume / hair / head accessory
- proportions / identifying features
- immutable DNA
- lesson-specific variant
- drift guardrails

### B5. Image-first Slide PDF
需：
- 學生可見內容完整
- 不顯示教師答案
- 關鍵中文字／課文／注音正確
- 圖像與句意一致
- 成語依句意視覺化，不預設典故故事
- 頁面節奏與視覺模式不機械重複
- 可直接投影／分享

### B6. Teaching Slides PPTX
需：
- 可編輯
- 與正式 PDF 教學內容一致
- 學生頁無答案
- 教師答案／引導／判準放講者備註
- 關鍵文字盡量 Native Text
- Session / CORE / FLEX / BONUS 可辨識與調整

### B7. Pre-study Worksheet
權威技能：`skills/prestudy-worksheet/SKILL.md`

最低要求：
- A4 橫式
- 課前探索＋學後複習雙用途
- 任務式分區，不是縮小版講義
- 三、四年級主要語文預習聚焦高價值形近字／多音字
- 同冊去重
- 閱讀理解大區與足夠書寫空間
- 至少一個開放式聯想／預測／畫面任務
- 學生版無答案

### B8. Post-lesson Short Writing Worksheet
權威技能：`skills/postlesson-short-writing-worksheet/SKILL.md`

最低要求：
- A4 橫式
- 素材／畫面啟動區
- 語文 Bonus 工具箱
- 正式創作區為最大面積
- 語詞／四字語詞或成語／句型／修辭皆為可選工具
- Bonus 不要求全部使用
- 可依 Teacher Intent 寫短文、童詩或彈性創作
- 成語使用需承接 STEP 2.6 已確認語意
- 學生版不放完整示範答案

核心：語文工具是選用，不要求學生全部使用。

---

## C. Google Drive 歸檔

正式根目錄預設：`V-MAX 教材庫`

若教師已指定既有資料夾，優先使用該資料夾，不重複建立同名根目錄。

建議課次結構：

```text
V-MAX 教材庫/
└── 國語/
    └── {冊別}/
        └── {課次}_{課名}/
            ├── 01_來源主檔/
            ├── 02_生成腳本/
            ├── 03_角色與視覺資產/
            ├── 04_簡報成品/
            └── 05_學習單/
```

對應：
- 01：Source Master MD
- 02：Renderer Script MD + Visual YAML MD
- 03：Character Visual Assets
- 04：Image-first PDF + Teaching PPTX
- 05：Pre-study Worksheet + Post-lesson Short Writing Worksheet

---

## D. Delivery Gate

```yaml
lesson_package_delivery:
  source_master_md: PASS | N/A_BY_TEACHER
  renderer_script_md: PASS | N/A_BY_TEACHER
  visual_yaml_md: PASS | N/A_BY_TEACHER
  character_visual_assets: PASS | N/A_BY_TEACHER
  image_first_pdf: PASS | N/A_BY_TEACHER
  teaching_pptx: PASS | N/A_BY_TEACHER
  prestudy_worksheet: PASS | N/A_BY_TEACHER
  postlesson_short_writing_worksheet: PASS | N/A_BY_TEACHER
  worksheet_regression: PASS
  google_drive_archive: PASS | BLOCKED | NOT_REQUESTED
```

若 Google Drive 已由教師指定為固定交付位置，`google_drive_archive` 預設必須是 `PASS` 才算完整交付；若平台權限／連線阻擋，需明確回報 `BLOCKED`，不得假裝已上傳。

---

## E. 驗證原則

上傳後需核實：
- 根目錄存在
- 課次資料夾位置正確
- 8 項交付物沒有漏件或被放錯層
- 預習單符合 `skills/prestudy-worksheet/SKILL.md`
- 短文／Bonus 寫作單符合 `skills/postlesson-short-writing-worksheet/SKILL.md`
- `tests/worksheet-regression-cases.md` 通過
- 檔名可辨識
- 上傳完成後能由 Drive 搜尋／列出

不得只說「會上傳」而沒有實際 connector / API 驗證。

---

## 核心金句

> 來源主檔是內容母體，腳本是施工圖，Visual YAML 是視覺規格，PPTX / PDF 是成品，學習單是學生延伸；Google Drive 是正式歸檔層。

> 做完一課，要留下的不只是作品，而是一個可再教、可再生、可再改的完整教材包。
