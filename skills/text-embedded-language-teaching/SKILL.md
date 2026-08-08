# V-MAX Text-Embedded Language Teaching Skill

版本：1.0

## 目的

本技能是 `core/pedagogy/text-embedded-language-teaching-policy.md` 的執行摘要，供 AI／Agent 在課文、Knowledge Lab、預習單、寫作單與 Renderer 階段快速載入。

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

## E. 快速檢查

```yaml
text_embedded_language_check:
  vocabulary_has_source_excerpt: true
  vocabulary_has_student_friendly_meaning: true
  sentence_pattern_has_source_sentence: true
  rhetoric_has_source_sentence: true
  rhetoric_discovery_before_label: true
  renderer_preserves_source_evidence: true
```

任一為 false：不得視為完成。

## F. Fail Codes

- `LANGUAGE_TEXT_DETACHMENT`
- `SOURCE_SENTENCE_DROPPED`
- `PATTERN_WITHOUT_SOURCE`
- `RHETORIC_LABEL_FIRST`

---

## 核心金句

> 語詞隨文理解；句型回到原句；修辭從文本發現。原文不可消失。
