---
name: teaching-memory-recorder
description: 在實際授課後，以半結構化方式記錄單課教學成效、學生投入、時間配置、平板活動、常見迷思與下次修改建議，並在累積多次紀錄後更新 Lesson Evolution。適用於課後反思、版本改進與下一年度備課。不得修改 Official Knowledge，也不得記錄學生姓名或敏感個資。
---

# Teaching Memory Recorder

版本：0.1.0

## 使命

把教師每次實際上課的經驗，轉成可被未來 Decision Engine 使用的 Teaching Memory，讓 V-MAX 能依真實教學結果逐年改進。

## 啟用時機

- 一課、一次主要課堂或一個 Classroom Variant 實際使用後
- 教師要求記錄課後反思
- 教師指出某活動成功、失敗或需要調整
- 教師希望明年保留、刪除或新增某內容

## 必讀輸入

至少讀取：

- 實際使用的 Baseline Version
- Classroom Variant Profile
- Applied Patch IDs
- Teaching Flow
- Presentation Version
- Tablet Interaction Profile（若有）
- 教師當次反思

## 工作流程

### 1. 確認實際使用版本

不得以計畫版本代替實際上課版本。若教師臨時跳頁、改用紙本或縮短時間，必須記錄。

### 2. 快速反思

優先詢問或整理：

- 達成度 1～5
- 學生投入度 1～5
- 時間不足、剛好或有餘
- 最成功的模組或活動
- 最需要補強的知識
- 平板活動是否成功
- 下次保留、修改或移除什麼

不要求教師每次撰寫長篇文字。

### 3. 產生 Teaching Memory

輸出：

`memory/{school_year}/{class_id}/{lesson_id}_{date}_teaching-memory.md`

使用 `schemas/teaching-memory-profile.md`。

### 4. 建議後續處理

依紀錄提出下列其中一項，但不得自動執行：

- 不需修改
- 建立 `add_on` Patch
- 建立 `replace` Patch
- 建立 `reflow` Patch
- 建立新的 Classroom Variant
- 下一年度重建 Baseline 的候選事項

### 5. 更新 Lesson Evolution

若同課已有多筆 Teaching Memory，彙整至：

`evolution/{lesson_id}_lesson-evolution.md`

只有重複出現的趨勢才標記為穩定發現；單次觀察保留在年度紀錄中。

## 資料分層

Teaching Memory 屬於：

`Reflection / Teaching Memory`

它不是：

- Official Knowledge
- Teacher Knowledge 的永久教材內容
- Learning Expansion
- Teaching Strategy 原始規格

未來若教師決定把反思轉為正式教學決策，應透過 Patch 或新 Baseline 寫入對應層級。

## 隱私規則

- 不記錄學生姓名、座號、照片或可識別個資。
- 班級只用代碼或教師可接受的簡稱。
- 學生困難以群體趨勢描述，例如「多數學生混淆近義成語」。
- 若使用平台分析資料，只保存必要的整體統計，不保存個別帳號資料。

## 完成條件

- 實際使用版本可追溯
- 最低反思欄位完整
- 建議修改與教材事實分流
- 隱私檢查通過
- 教師確認紀錄內容
