# V-MAX Polyphonic Source Policy 1.0

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

## D. 必填欄位

```yaml
polyphonic_item:
  character:
  source_type: TEXTBOOK_POLYPHONIC | AI_RECOMMENDED_POLYPHONIC | TEACHER_ADDED_POLYPHONIC
  official_lesson_character: true | false
  teacher_reason:
  textbook_evidence:
  readings: []
  meaning_by_reading: []
  lesson_context:
  confusion_risk:
  teaching_value:
  teacher_decision: PENDING | CONFIRMED | DROPPED
```

---

## E. 教學表達

一旦正式納入多音字教學，仍遵守：

> 多音字不是兩個音，而是兩組「讀音 × 意思 × 情境」。

學生可見頁面優先採 `skills/character-group-visual-comparison/SKILL.md` 的多音字小站邏輯：
- 同一大字
- 不同讀音分區
- 每個讀音對應語意／例詞／情境
- 回到課文或句子判斷實際讀音

---

## F. Failure Codes

- `POLYPHONIC_SOURCE_LEAK`：從非法來源自動建立多音字單元
- `SHAPE_NEAR_TO_POLYPHONIC_DRIFT`：形近補充字被錯誤升級為多音字
- `TEACHER_POLYPHONIC_DROPPED`：教師指定多音字在後段被刪除
- `POLYPHONIC_IDENTITY_MISSING`：未記錄來源身分

---

## 核心金句

> 多音字先看身分，再看讀音。

> 教材明列保留；AI 只從正式生字推薦；老師可以因班級真實困難指定加入。
