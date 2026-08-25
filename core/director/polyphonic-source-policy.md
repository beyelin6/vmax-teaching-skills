# V-MAX Polyphonic Source Policy 1.3

## 定位

本政策定義多音字教學的合法來源與升級邊界，避免形近補充字、比較字或 AI 額外補充字因本身具有多音而被自動拉入多音字單元。

核心原則：

> 多音字先看身分，再看讀音。

> 合法來源只有三種：教材明列、本課正式生字的 AI 推薦、教師指定加入。

---

## A. 三種合法來源

### A1. TEXTBOOK_POLYPHONIC｜教材明列

若教材明確將某字列為多音字、辨音活動或正式語文學習內容，必須保留。

- provenance: TEXTBOOK
- 不因 AI 判斷而靜默刪除
- 若與課文語境相關，仍應以「讀音 × 語意 × 語境」教學

### A2. AI_RECOMMENDED_POLYPHONIC｜本課正式生字中的 AI 推薦

若教材未明列，AI 只能從「本課正式生字」中檢查多音字候選。

先通過：

`is_official_lesson_character = true`

再判斷是否具有教學價值，例如：
- 學生容易誤讀
- 不同讀音連動不同語意
- 課文情境可清楚支持辨義
- 有明確閱讀或遷移價值

只有通過教學價值判讀，才可進入深教候選。

### A3. TEACHER_ADDED_POLYPHONIC｜教師指定加入

教師可依班級實際學習困難指定加入某個多音字，即使它不是本課正式生字。

適用理由包括：
- 學生反覆誤讀
- 學生無法依語境判斷讀音
- 影響課文理解
- 班級已有持續性迷思概念

教師指定後：
- provenance: TEACHER
- status: TEACHER_ADDED_POLYPHONIC
- 必須保留 teacher_reason
- 一經教師確認，後段不得因「非本課正式生字」而靜默刪除
- 應納入 Teacher Intent Lock / locked_decisions

---

## B. 非合法自動來源

下列內容即使本身具有多音，也不得由 AI 自動建立多音字教學：

- 形近補充字
- 比較字
- AI 額外補充字
- 成語中偶然出現的字
- 課文中出現但不是本課正式生字的其他字
- 認讀字（除非教材明列，或教師指定）

例如：

`爭 = 本課正式生字`

`掙 = 形近補充字`

即使「掙」具有多音，也只能維持 `SHAPE_NEAR_SUPPORT`，不得自動升級成 `POLYPHONIC`。

---

## C. Gate

```text
多音字候選
↓
教材是否明列？
├─ 是 → TEXTBOOK_POLYPHONIC
└─ 否
    ↓
教師是否明確指定？
├─ 是 → TEACHER_ADDED_POLYPHONIC
└─ 否
    ↓
是否為本課正式生字？
├─ 否 → STOP
└─ 是
    ↓
AI 是否判斷有明確教學價值？
├─ 是 → AI_RECOMMENDED_POLYPHONIC
└─ 否 → 不建立獨立多音字深教
```

---

## D. 讀音與例詞核對

1. 本課使用讀音以課本生字欄、課文注音或教材明列辨音活動為第一來源。
2. 教材已列出的讀音集合是本課多音字的有效範圍；AI 不得因模型記憶、一般語文常識或辭典另列讀音，自行擴張本課讀音集合、列數或學生可見教學內容。
3. 教育部《國語辭典簡編本》用於補充、驗證讀音、詞義與例詞，不能取代本課教材身分。
4. 若 AI 發現教材未列但可能存在的其他讀音，只能建立 `AI_SUGGESTED_READING` 候選；必須以教育部《國語辭典簡編本》或教師指定的其他權威來源驗證，並在教師確認單中標示「教材未列／延伸候選／待教師確認」、來源證據與受影響下游，不得直接列入多音字正式列數、預習單或簡報。
5. 每個多音字例詞必須逐詞查核；不得只確認單字有某讀音後，自行類推所有例詞。
6. 課本與辭典不一致、教材讀音集合與補充來源不一致、詞條無法支持例詞、OCR 不清或語境無法判定時，標記 `PRONUNCIATION_SOURCE_CONFLICT / EXAMPLE_WORD_UNVERIFIED`，停在當前 STEP，不得自行選邊。
7. 未完成核對的讀音、例詞與口訣不得標示 `CONFIRMED / LOCKED`。

### D1. 教材列數優先

多音字的正式呈現列數，先由教材來源決定，再由教師確認：

```text
教材明列 2 個讀音 → 正式候選最多先呈現 2 列
教材未列的第 3 個讀音 → 只能另列 AI_SUGGESTED_READING，完成來源驗證並停等教師
教材與辭典對讀音數量或讀法不一致 → PRONUNCIATION_SOURCE_CONFLICT，停等教師
```

「《國語辭典簡編本》查得到」不等於「本課應教」；不得把辭典的完整字音表直接轉成教材教學列。

## E. 必填欄位

```yaml
polyphonic_item:
  character:
  source_type: TEXTBOOK_POLYPHONIC | AI_RECOMMENDED_POLYPHONIC | TEACHER_ADDED_POLYPHONIC
  official_lesson_character: true | false
  teacher_reason:
  textbook_evidence:
  lesson_pronunciation_evidence:
    - source_file:
      pdf_page:
      printed_page:
      region_ref:
      exact_text:
      extraction_method: TEXT_LAYER | OCR | MANUAL_TRANSCRIPTION | IMAGE_REVIEW
      extraction_confidence: HIGH | MEDIUM | LOW
      verification_status: UNVERIFIED | TEACHER_GUIDE_VERIFIED | DICTIONARY_VERIFIED | CONFLICTED
  dictionary_entry_evidence: []
  readings: []
  reading_source_status: TEXTBOOK_CONFIRMED | AI_SUGGESTED_READING | TEACHER_SPECIFIED
  reading_expansion_status: NONE | VERIFIED_PENDING_TEACHER | SOURCE_CONFLICT
  downstream_impact: []
  example_word_verification: []
  meaning_by_reading: []
  lesson_context:
  confusion_risk:
  teaching_value:
  teacher_decision: PENDING | CONFIRMED | DROPPED
```

---

## F. 教學表達

一旦正式納入多音字教學，仍遵守：

> 多音字不是兩個音，而是兩組「讀音 × 意思 × 情境」。

學生可見頁面優先採 `skills/character-group-visual-comparison/SKILL.md` 的多音字小站邏輯：
- 同一大字
- 不同讀音分區
- 每個讀音對應語意／例詞／情境
- 回到課文或句子判斷實際讀音

---

## G. Failure Codes

- `POLYPHONIC_SOURCE_LEAK`：從非法來源自動建立多音字單元
- `SHAPE_NEAR_TO_POLYPHONIC_DRIFT`：形近補充字被錯誤升級為多音字
- `TEACHER_POLYPHONIC_DROPPED`：教師指定多音字在後段被刪除
- `POLYPHONIC_IDENTITY_MISSING`：未記錄來源身分
- `PRONUNCIATION_SOURCE_CONFLICT`：教材讀音與補充來源衝突
- `UNVERIFIED_AI_READING_EXPANSION`：AI 未完成來源驗證就自行增加教材未列讀音
- `EXAMPLE_WORD_UNVERIFIED`：例詞未逐詞取得來源支持
- `PRONUNCIATION_INFERENCE_DRIFT`：只查單字後自行類推例詞讀音

---

## 核心金句

> 多音字先看身分，再看讀音。

> 教材明列保留；AI 只從正式生字推薦；老師可以因班級真實困難指定加入。
