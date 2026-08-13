# Gemini Task Knowledge Requirement Registry 1.0

本表定義各下游任務的最低知識需求。Gemini 必須以此為 Coverage Diff 基線；可依該課增加需求，不得自行刪除必要項。

## Pre-study Worksheet

必要：課程定位、文體、課文結構、核心文意、正式生字、認讀字狀態、形近字、多音字、核心語詞、教師手冊的課前重點、題目答案證據、學生可能困難。

## Post-lesson Writing Worksheet

必要：核心詞語及來源、可入文語詞、正式句型、修辭、寫作特色、文體結構、遷移目標依據、適齡寫作困難與教師引導。

## Presentation

必要：Teacher Intent、主旨與段落證據、關鍵事件／關係、Knowledge Selection、語詞／句型／修辭原文證據、閱讀理解與答案、學生迷思、教師引導、下游不可遺失節點。

## Lesson Plan

必要：完整課程定位、核心知識、學習目標、教師手冊教學重點、學生困難、教學順序依據、評量依據、差異化所需證據。策略與時間安排不寫回 Official Knowledge。

## Assessment

必要：學習目標、可評量知識節點、題目來源、答案與判準依據、常見迷思、難度線索、學生版／教師版分流規則。

## Activity

必要：活動對應知識節點、學習目的、必要先備知識、學生預期產出、教師統整依據與無裝置替代所需內容。

## Image / Visual Asset

必要：畫面對應的教材節點、正式繁體中文、人物／情境事實、不可改寫文字、視覺化關係與來源定位。圖片 prompt 不屬 Official Knowledge。

## Coverage 狀態

每個必要項只能標記：

- `AVAILABLE_AND_SELECTED`
- `AVAILABLE_NOT_SELECTED`
- `N/A_SOURCE_NOT_PRESENT`
- `EXCLUDED_BY_TEACHER`
- `MISSING_FROM_LKB`
- `INSUFFICIENT_EVIDENCE`
- `AGENT_OMISSION`

`MISSING_FROM_LKB / INSUFFICIENT_EVIDENCE` 觸發局部增補；`AGENT_OMISSION` 必須先修正執行結果，不得錯誤建立 Patch。
