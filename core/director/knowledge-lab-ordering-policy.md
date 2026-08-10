# V-MAX Knowledge Lab Ordering Policy 2.1

## 定位

本政策定義 `STEP 2.5 語文輻射` 與後段 Knowledge Lab 的分析、推薦、教師選擇與排序邏輯。

核心：

> 教材告訴我們「有什麼」；AI 分析哪些形近字群／多音字值得教；容易搞錯的單字只由老師依班級需求主動指定。

> 預習單可以精選，正式教學不能被預習單容量反向裁切。

---

## A. 資料完整性

生成 STEP 2.5 前必須完整讀取：
- 本課正式生字
- 認讀字 status（若 PRESENT）
- 教材已列形近字／字形辨析
- 教材已列多音字
- 教材成語
- 同冊預習單已確認的字群／多音字覆蓋紀錄

正式生字必須完整保留在資料層與基礎識寫層，不因深教選擇而消失。

---

## B. 三、四年級生字深教邊界

AI 主動深教只有兩類：

1. `SHAPE_NEAR`｜形近字／易混淆字群
2. `POLYPHONIC`｜多音字

其他正式生字預設：

`BASIC_LITERACY_ONLY`

可在課文、造詞、基本形音義或識寫活動自然處理，但不預設獨立成頁。

### 教師指定易錯／易混淆單字

只有教師依班級實際狀況明確指出「這個字學生很容易搞錯」，才可建立：

`TEACHER_ADDED_WRITING_FOCUS`

教師指定後只處理實際混淆焦點，例如：易漏／多寫筆畫、部件位置與比例、局部字形看錯／寫錯、必要筆順或其他已觀察到的辨認／書寫混淆點；不擴張成完整單字百科頁。

若真正需要處理的是與另一字形近，應回到 `SHAPE_NEAR`；若是多音語境，應回到 `POLYPHONIC`。

AI 不主動列易錯字候選，也不以詢問清單要求教師逐字確認。

以下皆不是 AI 自動建立第三類深教入口的合法理由：
- 容易寫錯
- 字形複雜
- 字源有趣
- 評量重要
- 語義特殊
- 課文理解可能相關

權威邊界另見：`core/director/character-deep-teaching-focus-policy.md`。

---

## C. 形近字群分析｜Shape-near

形近字必須以字群為單位，至少包含一個本課目標字與一個比較字；單字不得自行標記為 `SHAPE_NEAR`。

每組至少包含：
- target_character
- target_zhuyin
- target_radical
- comparison_characters
- 各比較字注音／常用詞／核心字義
- component_analysis
- confusion_point
- discrimination_cue
- mnemonic（可用才給，不硬湊）
- recommendation_index 1–5
- reason
- suggested_action A–E
- prestudy recommendation P1/P2/P3/PX/PE

教師端必須看得到「為什麼值得放在一起比較」，不能只剩字群＋分數。

學生可見頁型遵循：`skills/character-group-visual-comparison/SKILL.md`。

---

## D. 多音字分析｜Polyphonic

多音字不得只列讀音表。

每個深教多音字至少包含：
- 各讀音
- 各讀音對應核心語意
- 課文中的實際用法
- 生活語境
- 易誤讀位置
- 語境判斷提示
- recommendation_index 1–5
- reason
- suggested_action

核心：

> 多音字不是兩個音，而是兩組「讀音 × 意思 × 情境」。

### 多音字來源 Gate

必須先遵循 `core/director/polyphonic-source-policy.md`。

合法來源只有：
1. `TEXTBOOK_POLYPHONIC`
2. `AI_RECOMMENDED_POLYPHONIC`：AI 只能從本課正式生字推薦
3. `TEACHER_ADDED_POLYPHONIC`：教師依班級困難指定

形近補充字、比較字、認讀字、AI 補充字、課文一般字，不因本身具有多音而由 AI 自動建立多音字單元。

若教師明確指定，才依 `TEACHER_ADDED_POLYPHONIC` 處理。

---

## E. 認讀字條件式處理

認讀字依 `core/governance/recognition-only-character-policy.md`。

- `PRESENT`：保留識讀層，重點是字音、基本字義／語境、必要辨認線索。
- `N/A_SOURCE_NOT_PRESENT`：明確 N/A，不生成認讀字模組。
- `UNCERTAIN_SOURCE_LABEL / SOURCE_CONFLICT`：維持待確認，不自行改判。

認讀字不因身分自動進：
- 完整書寫深教
- 形近字深教
- 多音字深教

若教師要額外處理，走教師指定入口；AI 不得因「認讀字本身是多音」自行升級。

---

## F. 成語推薦

STEP 2.5 先決定：
- recommendation_index 1–5
- reason
- CORE / FLEX / BONUS / LOW_PRIORITY
- teacher decision

保留的成語再交給 STEP 2.6 決定：
- student_friendly_meaning
- life_example
- understanding_goal
- visual_expression
- independent_page_recommendation

不得在 STEP 2.5 直接鎖漫畫格數或 Style Recipe。

---

## G. 預習單精選與同冊去重

`3–5 組` 只適用於預習單主要形近字／多音字練習區，不是正式簡報上限。

代號：
- `P1` 預習核心
- `P2` 預習短看
- `P3` 本課不放
- `PX` 冊內已覆蓋
- `PE` 調整

同冊多音字查重採「字＋讀音／語意對比」，形近字群採正規化群組比對。

---

## H. STEP 2.5 教師可見卡

第一輸出必須是教師可讀卡，不得以 raw JSON/YAML 取代。

形近字順序：
`字群 → 分析 → 混淆點／辨認提示 → 推薦指數＋理由 → A–E → P1/P2/P3/PX`

多音字順序：
`字 → 合法來源 → 各讀音／語意／語境 → 課文用法 → 易混淆點 → 推薦指數＋理由 → 教學／預習單建議`

易錯／易混淆單字欄只顯示教師已主動指定的 `TEACHER_ADDED_WRITING_FOCUS`，並記錄 `confusion_focus`；未指定時標示 `NONE_TEACHER_SPECIFIED`，不得由 AI 補候選。

---

## I. 必填資料骨架

```yaml
step_2_5_language_radiation:
  status: WAITING_CONFIRMATION
  source_characters_complete: true
  recognition_only_status: PRESENT | N/A_SOURCE_NOT_PRESENT | UNCERTAIN_SOURCE_LABEL | SOURCE_CONFLICT
  ai_active_deep_teaching_categories:
    - SHAPE_NEAR
    - POLYPHONIC
  writing_focus_rule: TEACHER_SPECIFIED_ONLY
  teacher_added_confusion_focus:
    status: NONE_TEACHER_SPECIFIED | PRESENT
    items: []
  items:
    - id:
      category: CHARACTER | RECOGNITION_ONLY | SHAPE_NEAR | POLYPHONIC | IDIOM | OTHER
      provenance:
      analysis:
      recommendation_index:
      reason:
      ai_suggested_decision:
      teacher_decision: PENDING
      prestudy:
        ai_recommendation:
        volume_duplication_status:
```

---

## J. Failures

以下視為 `INCOMPLETE / FAIL`：
- 正式生字不完整
- 每個生字平均深教
- AI 提出易錯字候選，或以易錯／字源／評量理由自行建立單字詳解頁
- 教師只指定混淆焦點，後段卻擴張成百科式單字頁
- 形近補充字因本身多音而被 AI 拉進多音字單元
- 認讀字因本身多音而被 AI 自動升級
- 多音字只有音表
- 形近字不是以字群呈現，或只有字群＋推薦結果、沒有辨析分析
- 預習單 3–5 組反向刪掉正式教學
- WAITING_CONFIRMATION 只輸出 machine payload

失敗分類：
`CHARACTER_SCOPE_EXPANSION / WRITING_FOCUS_AUTO_SUGGESTED / WRITING_FOCUS_SCOPE_EXPANSION / SINGLE_CHARACTER_AUTO_DEEPENING / POLYPHONIC_SOURCE_LEAK / CHARACTER_DEPTH_FLATTENING / POLYPHONIC_CONTEXT_FAIL / SHAPE_NEAR_NOT_GROUPED / SHAPE_NEAR_ANALYSIS_DROPPED`

---

## 核心金句

> 生字表 ≠ 生字教學清單。

> 形近字用字群教，多音字用語境教；老師可依班級需要指定「孩子容易搞錯的字」額外提醒，其餘不另提深教。

> 多音字先看來源身分，再談讀音教學。
