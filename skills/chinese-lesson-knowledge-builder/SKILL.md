---
name: chinese-lesson-knowledge-builder
description: 讀取已確認的國語教材事實層，建立分析層、教學層與可匯入 NotebookLM 的 Curated Briefing。適用於修辭、句型、寫作手法、主旨結構、意義段解析、DOK 1-4 提問與完整結構化教材知識庫生成。不得改寫教材原文，也不得在事實層未確認前執行。
---

# Chinese Lesson Knowledge Builder

版本：0.1.0

## 使命

將已確認的教材事實轉換成可重複利用的課程知識模型，並依需求輸出接近使用者提供之 Curated Briefing 的完整 Markdown。

## 前置條件

必須存在並讀取：

- `working/01_fact.md`
- `working/fact-validation-report.md`

且事實層狀態必須為 `approved`。未經教師確認不得執行。

## 四層輸出

1. `working/01_fact.md`：教材事實，由 Transcriber 產生，本技能不得改寫。
2. `working/02_analysis.md`：文體、修辭、句型、寫作手法、結構與段意分析。
3. `working/03_teaching.md`：教學重點、DOK 提問、迷思概念、活動與延伸建議。
4. `output/{課次}_{課名}_curated-briefing.md`：整合前三層的完整 NotebookLM 來源檔。

## Curated Briefing 固定骨架

0. 基本資訊
1. 課文原文
2. 字詞基礎工程
3. 課文核心詞語與生字成語
4. 字形字音深度辨析
5. 綜合語文活動
6. 本課主旨與結構心智圖
7. 意義段全息深度解析
8. 執行終點自檢

章節名稱固定，內容與意義段數量依每課動態生成。

## 分析層規則

- 每項分析標示 `來源：系統分析` 或對應教師手冊來源。
- 不得把分析句子寫回課文原文。
- 文體、修辭、句型與寫作手法必須引用對應課文原句。
- 教材已有明示分析時優先採用教材或教師手冊說法。
- 無足夠依據的項目標示「待教師確認」，不得硬填。

## 教學層規則

每個實際意義段可包含：

- 大意
- 課文原句
- 修辭與寫作分析
- 句型分析
- DOK 1-2 閱讀理解題 1 至 2 題
- DOK 3-4 策略思考題 1 題
- 對應位置
- 提問類型或思考維度

題目數量可依段落複雜度調整，不得為了固定格式製造低品質問題。

## 合併規則

- Curated Briefing 必須保留事實、分析、教學三層的來源界線。
- 完整內容集中於 Curated Briefing；後續 NotebookLM 生成指令只保留操作規則。
- 核心詞語仍以 `01_fact.md` 為準，不得在合併時漏掉。
- 認讀字與生字分類不得因後續分析而改變。
- 不加入投影片版面、配色、角色 DNA 或圖像生成指令；這些屬於 Slide Architect。

## 終點自檢

確認：

- 事實層未被改寫
- 所有分析都有原句或來源支持
- 意義段結構與教材相符，或清楚標示為系統建議
- 每段提問符合標示的 DOK 層級
- 全部核心詞語均保留
- 未混入其他課次內容
- Curated Briefing 可單獨匯入 NotebookLM 使用

完成後狀態設為 `ready_for_teacher_review` 並停止等待教師確認。
