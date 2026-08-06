---
name: language-application-builder
description: 依已核准的 Lesson Knowledge Book、Learning Modules 與語文應用輸出設定，分別產生短文創作單與其他可選語文應用任務。短文創作單為固定獨立成果，對話、新聞、圖文、口說、家庭與平板任務可單選、多選或全部產出；不得以其他任務取代短文創作單。
---

# Language Application Builder

版本：0.1.0

## 核心定位

本技能負責產生兩條並行成果線：

1. `Short Writing Worksheet｜短文創作單`
2. `Language Missions｜其他語文應用任務`

兩者必須並存且可獨立選擇。教師可以：

- 只產出短文創作單
- 只產出指定語文應用任務
- 同時產出短文創作單與數個任務
- 一次產出全部語文應用成果

## 前置條件

必須讀取：

- 已核准的 LKB
- 已核准的 Learning Modules
- `schemas/language-application-output-profile.md`
- 當課 Output Profile
- Teacher Profile
- 如有需要，Teaching Memory 與 Classroom Variant

## 教材忠實規則

短文創作單的下列內容必須來自來源教材或已核准 LKB：

- 重要生字語詞
- 四字語詞與官方成語
- 官方句型
- 官方修辭
- 官方寫作特色

系統可以新增：

- 寫作題目
- 寫作鷹架
- 任務情境
- 學生自評表
- 教師評量規準
- 支援版與挑戰版

不得把系統新增的成語、修辭或句型冒充為本課官方內容。

## 短文創作單工作流

1. 依課文文體、主題與教學重點建立短文題目。
2. 從 LKB 選取適合作文應用的重要語詞。
3. 列出教材原有四字語詞或成語。
4. 列出本課官方句型與修辭。
5. 依文體建立構思鷹架。
6. 設定合理必用條件。
7. 產生 Support、Core、Challenge 版本。
8. 教師版加入評量規準與參考提示。
9. 學生版移除所有答案與內部標記。

## 其他語文應用任務

可產生：

- `dialogue_creation`
- `news_report`
- `illustrated_writing`
- `oral_recording`
- `family_task`
- `tablet_interaction`

每一任務需包含：

- 任務目標
- 對應 LKB 節點
- 指定使用的語詞、句型或修辭
- 操作步驟
- 完成形式
- 時間建議
- 評量方式
- 平板需求與紙本替代方案（如適用）

## 選擇規則

若 `selection_mode: teacher_choice`，先呈現候選任務與理由，等待教師選擇。

若 `allow_multiple: true`，允許複選。

若 `allow_all: true`，提供「全部產出」選項。

教師未明確選擇時，不得擅自把所有任務加入 Baseline。

## 差異化與反應調整

可依學生能力或 Teaching Memory 建立：

- Support Variant
- Core Variant
- Challenge Variant
- Adaptive Patch
- 新 Classroom Variant

修改原則：

- 不覆蓋 Baseline。
- 記錄修改原因與依據的版本。
- 保留原任務與新版任務的關係。
- 學生表現不足時，可降低字數、增加詞語框或句型鷹架。
- 學生表現良好時，可增加修辭、四字語詞、段落或轉折要求。

## 標準輸出

```text
worksheets/short-writing/
worksheets/language-missions/
```

並產生：

```text
worksheets/language-application-manifest.md
```

Manifest 必須記錄：

- source_lkb
- source_lkb_version
- selected_outputs
- selected_levels
- applied_patch_ids
- classroom_variant_id
- teacher_approved

## 驗證

完成前檢查：

- 短文創作單與其他語文任務未混為同一成果。
- 短文創作單可獨立產出。
- 任務可單選、多選或全部產出。
- 官方語詞、成語、句型與修辭可追溯來源。
- 支援版、核心版與挑戰版差異清楚。
- 學生版無答案。
- 平板任務有無裝置替代方案。
- 後續調整未覆蓋 Baseline。

完成後狀態設為 `ready_for_language_application_review`，等待教師確認。
