---
name: learning-module-builder
description: 讀取已核准的 Lesson Knowledge Book 與教師選定的能力目標，為成語、修辭、句型、生字詞與課文理解建立可選的學習延伸模組。教材知識不得被改寫；本技能只產生情境理解、易誤用辨識、近義反義比較、看圖判斷、造句、討論、遊戲、練習與 Exit Ticket 等教學延伸，並在完成後停下等待教師確認。
---

# Learning Module Builder

版本：0.1.0

## 使命

將已確認的教材知識轉換為可選、可組合、可依年級與能力目標調整的學習延伸模組。所有模組都必須明確追溯至 LKB 中的知識節點，且不得修改官方教材內容。

## 前置條件

必須存在並讀取：

- `lkb/lesson-knowledge-book.md`
- `lkb/validation-report.md`
- `config/learning-module-profile.md`

LKB 狀態必須為 `approved`。若尚未核准，停止並要求教師先確認教材知識。

## 輸出

預設產生：

- `learning-modules/idiom-modules.md`
- `learning-modules/rhetoric-modules.md`
- `learning-modules/sentence-pattern-modules.md`
- `learning-modules/vocabulary-modules.md`
- `learning-modules/text-comprehension-modules.md`
- `learning-modules/module-manifest.md`

只產生設定檔中啟用的模組。未啟用的類別不得自行生成。

## 核心邊界

### 不可變動

- 課文原文
- 教材成語名稱、詞義、例句與對應生字
- 教材明示修辭、句型與寫作特色
- 教材主旨、結構、教學重點與官方問題

### 可產生

- 學生友善解釋
- 情境理解
- 易誤用辨識
- 近義與反義比較
- 看圖或圖像推理
- 造句、改寫與仿寫
- 生活連結
- 小組討論
- 遊戲與互動活動
- 練習題與 Exit Ticket

所有產生內容標記為 `learning_extension`，不得寫入 Official Knowledge。

## 成語模組

成語來源預設為 `official_only`。只針對 LKB 中來源教材明確提供的成語建立延伸。

可選模組：

- `context_understanding`
- `misuse_detection`
- `synonym_antonym`
- `image_reasoning`
- `sentence_application`
- `life_connection`
- `discussion`
- `game`
- `practice`
- `exit_ticket`

近義或反義成語屬延伸比較材料，不得加入本課官方成語清單。

## 修辭模組

只針對 LKB 中已確認的官方修辭節點建立延伸，可選：

- `identify`
- `effect_analysis`
- `compare`
- `rewrite`
- `imitation_writing`
- `image_reasoning`

若修辭僅為系統分析，必須在模組中保留來源標記。

## 句型模組

只針對 LKB 中已確認的句型節點建立延伸，可選：

- `identify`
- `sentence_completion`
- `transformation`
- `sentence_application`
- `error_correction`
- `oral_practice`

不得擅自改變教材句型定義或複句分類。

## 生字詞模組

可選：

- `component_analysis`
- `shape_comparison`
- `sound_comparison`
- `context_meaning`
- `word_collocation`
- `error_correction`
- `character_card`

核心詞語必須以 LKB 完整清單為準，不得只選代表性詞語，除非教師設定為抽樣練習。

## 課文理解模組

可選：

- `sequence`
- `main_idea`
- `evidence_finding`
- `inference`
- `summary`
- `mind_map`
- `perspective_taking`
- `dok_question`

不得把系統新增問題冒充教材原題。

## 年級適配

模組內容應依年級調整語言與認知負荷：

- 低年級：圖像、口語、配對與簡短情境。
- 中年級：情境判斷、造句、比較與簡要說理。
- 高年級：辨析、修正、證據推論、短文應用與討論。

年級適配不得改變教材知識本身。

## 工作流程

1. 驗證 LKB 已核准。
2. 讀取能力目標與教師選定模組。
3. 建立「LKB 節點 → Learning Module」映射。
4. 依年級與教學時間生成內容。
5. 分離學生內容、教師答案與內部來源標記。
6. 執行品質檢查。
7. 產生 module manifest。
8. 停下等待教師確認，不得直接生成簡報。

## 品質檢查

- 每個模組都有對應 LKB 節點。
- 未修改官方詞義、例句與分類。
- 成語只取自來源教材。
- 近義、反義與易誤用內容均標記為延伸。
- 學生版不顯示答案。
- 教師版保留答案、來源與教學目的。
- 問題難度符合年級與能力目標。
- 未混入其他課次內容。

## 完成狀態

完成後設為 `ready_for_teacher_review`。教師確認前不得交由 Teaching Strategy 或 Presentation Engine 使用。
