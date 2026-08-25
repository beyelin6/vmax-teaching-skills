---
name: text-embedded-language-teaching
description: 執行課文脈絡內的語文教學政策，將詞語、句型、修辭與理解任務嵌入課文教學流程；設計或檢查國語課文內嵌語文任務時使用。
---

# V-MAX Text-Embedded Language Teaching Skill

版本：1.1

## 目的

本技能是 `core/pedagogy/text-embedded-language-teaching-policy.md` 的執行摘要，供 AI／Agent 在課文、Knowledge Lab、預習單、寫作單與 Renderer 階段快速載入。

This skill consumes only locked source text and teacher-confirmed `APPROVED_TEACHING_SELECTION`. It may embed approved language items in context, but it does not select unresolved candidates or promote `AI_SUGGESTION` into student content.

核心口訣：

> 語詞隨段落，句型帶原文，修辭從文本發現。

---

## A. 語詞

- 跟著最有教學價值的段落／詩節處理。
- 學生可見：**原文片段＋重點語詞＋學生易懂的意義**。
- 可加句意圖，但不可用圖片取代正式文字。
- 不把整課語詞預設抽成字典式清單。

## B. 句型

- 必須先顯示課文原句或足夠理解的原文片段。
- 順序：**原文 → 找結構 → 看懂意思 → 抽出句型 → 仿說／仿寫**。
- 禁止只剩 `……一般……` 等空架構而找不到來源句。

## C. 修辭

- 順序：**讀原文 → 找特點 → 說效果 → 發現寫法 → 最後命名**。
- 學生頁必須保留原句與關鍵文字。
- 禁止先丟修辭名稱／定義，再讓文本退場。

## D. 共通必守

所有語詞／句型／修辭教學頁都必須能回答：

> 這是從課文哪一句看出來的？

原文證據層不可因 Knowledge Lab、Slide Architecture、Style Recipe 或 Renderer 而消失。

## D1. 課文循環頁

課文循環頁不是重複投影全文，而是配合教學進度，讓學生用不同閱讀角度重新理解同一篇課文。可依本課需要選用下列任務，不強制每課固定五輪：

1. 初讀：看懂內容與場景。
2. 關鍵詞回看：找動作、感官、情緒、時間、轉折或變化詞。
3. 段落功能：理解段落寫了什麼、發生什麼變化，以及和前後文的關係。
4. 全文線索：串連時間線、情緒線、行動線、地點、事件發展或前後對比。
5. 主旨統整：從事件、感受與課文證據回到作者想法。

課文循環頁必須：

- 保留課文原文與自然段／語意單位順序。
- 一頁只處理一個主要閱讀任務。
- 用淡色標記、底線、手繪圈選、箭頭或角色視線引導，不一次標滿所有重點。
- 讓插圖補充情境，不取代課文，也不把課文改成密集講義。
- 學生頁不直接印出完整答案；答案與詳細解說留在教師層。

## D2. 文意理解頁

文意理解必須回到「課文哪裡看得出來」，並依需要安排：明確訊息、事件關係、人物感受推論、前後變化、作者想法與生活連結。不可讓所有題目都只是抄找原句。

建議構圖順序：情境引題 → 課文證據／關鍵詞 → 一個主要問題（最多一個追問）→ 學生思考或口頭表達。可用課文片段、放大鏡、箭頭、手繪紙條、問號路徑或留白提示，但不得用顏色、標籤或旁白直接揭露答案。

## D3. 修辭發現頁

固定順序：**課文原句 → 看見特色 → 猜想效果 → 命名修辭 → 仿造／應用**。

原句必須完整或保留足以理解的連續片段。動作描寫、摹寫、設問、擬人、譬喻等，應先用畫面、聲音、表情、動線或物件讓學生感受到效果，再揭示術語。每頁只教一個主要修辭，不做「名稱／定義／例句」三欄表，不把原句切成支離破碎的字詞堆。

## D4. 句型發現頁

固定順序：**課文原句 → 句意理解 → 結構拆解 → 情境變化 → 分層仿說／仿寫**。

課文例句優先於公式。結構可用手繪箭頭、色彩對應、紙條拼接、角色對話或路徑表示，但不可只放抽象公式。每頁只處理一個主要句型；仿說／仿寫須依序提供提示填空、替換詞語、替換情境到完整創作的梯度。教師投影頁以口頭發想與圖像引導為主，實際書寫線另由學習單處理。

## D5. 代表頁確認門檻

課文循環、文意、修辭與句型頁都採「代表頁先確認，確認後才批次」：

1. 先完成每個本課啟用頁型的一頁代表頁。
2. 教師確認原文、教學焦點、證據層、構圖、角色與文字層。
3. 代表頁通過後，才可批次製作同類頁面。
4. 批次仍須逐頁檢查；若發生原文錯誤、文字跑位、構圖退化或角色漂移，立即停批。

這不等於每一頁都要在生成前停等；未通過的代表頁不得推導出全批次通過。

若目前輸出是國語圖片式簡報，另讀取 `skills/presentation-engine/references/classroom-language-page-rules.md`，以取得課文循環、文意、修辭、句型與成語頁的共同文字／構圖規則；學習單或課後短文不自動套用簡報頁的版面限制。

## E. 快速檢查

```yaml
text_embedded_language_check:
  vocabulary_has_source_excerpt: true
  vocabulary_has_student_friendly_meaning: true
  sentence_pattern_has_source_sentence: true
  rhetoric_has_source_sentence: true
  rhetoric_discovery_before_label: true
  renderer_preserves_source_evidence: true
  selected_text_cycle_has_one_focus: true
  comprehension_has_source_evidence_path: true
  sentence_pattern_starts_from_source_sentence: true
  representative_page_approved_before_batch: true
```

任一為 false：不得視為完成。

## F. Fail Codes

- `LANGUAGE_TEXT_DETACHMENT`
- `SOURCE_SENTENCE_DROPPED`
- `PATTERN_WITHOUT_SOURCE`
- `RHETORIC_LABEL_FIRST`
- `TEXT_CYCLE_FOCUS_MISSING`
- `COMPREHENSION_WITHOUT_EVIDENCE_PATH`
- `REPRESENTATIVE_PAGE_NOT_APPROVED`

---

## 核心金句

> 語詞隨文理解；句型回到原句；修辭從文本發現。原文不可消失。
