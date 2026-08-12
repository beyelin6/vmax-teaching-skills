# V-MAX v1 Three-Lesson Tabletop Regression Report

Status: `THREE_LESSON_TABLETOP_PASS`

Live status: `LIVE_RUNTIME_RERUN_PENDING`

## 1. Scope

以三種不同文體壓力測試現行 V-MAX contract：
- Lesson 9 `〈請到我的家鄉來〉`：平行式說明／描述文本
- Lesson 11 `〈兔子先生等等我〉`：劇本
- Lesson 12 `〈老鞋匠和小精靈〉`：故事

本測試使用本輪設計中已核對過的教材／教冊事實作 tabletop input，不重新進行來源 OCR，也不寫入 Google Drive Runtime，因此不是 live runtime pass。

Regression goals：
1. 不同文體是否選出不同 Minimum Necessary Skill Set。
2. Visual tools 是否沒有冒充 Teaching Skills。
3. Text Anchor / Spiral Learning 是否保留。
4. Scenario Lock → Character Lock 是否依序成立。
5. Budget Draft / Final 是否沒有提前鎖頁數。
6. Style Recipe → Lesson Skin → Gate B → Representative → Gate C 是否合理。

---

# 2. Lesson 9｜〈請到我的家鄉來〉

## 2.1 Input diagnosis

Text traits：
- 四個國家平行介紹：泰國、埃及、荷蘭、奧地利。
- 荷蘭段核心關係：地勢低窪 → 築堤防潮；風車為排水而建；木鞋適應濕重環境。
- 語言焦點：`所以` = cause → result；`為了` = purpose。
- 形近字：`堤／提／題`。
- whole-text 有平行／散列式介紹結構，適合最後做臺灣 transfer。

## 2.2 Skill Selection

### Selected core skills
- `COMPARE`：四國線索與特色比較；所以 vs 為了。
- `INFER`：由荷蘭環境與生活方式推論適應關係。
- `STRUCTURE`：發現四段平行介紹模式。
- `TRANSFER`：用同一介紹結構設計「第五個家鄉：臺灣」。

### Conditional
- `RETURN`：在低窪／生活智慧推論後回原文驗證。

### Not selected as core teaching skill
- `SCALE`：若用海平面高低示意，只是 visual tool。
- `CAUSE_ARROW`：visual tool。
- `ZOOM`：visual tool。
- `STAGE / STORY_ARC / PROBLEM_LOOP`：不符合本課主要閱讀困難，不啟用。

Result: PASS — `MINIMUM_NECESSARY_SKILL_SET`。

## 2.3 Spiral Routing

`堤／提／題`：

```text
PREVIEW：初遇／辨認
→ CORE_REINFORCE：字形 + 字義 + 語境 + 同框視覺比較
→ RECOGNIZE：無圖快速辨認
→ APPLY：詞句判讀
```

預習做過沒有造成正式課堂自動刪除。

Result: PASS。

## 2.4 Budget Draft

Gate A 前只鎖：
- MUST：荷蘭環境→生活智慧、所以/為了、全文平行結構
- SHOULD：堤/提/題正式深化、四國 evidence compare
- COULD：奧地利音樂家小知識等 extension
- Transfer：臺灣第五軌

不宣告精確頁數。

Result: PASS — `NO_PREMATURE_PAGE_LOCK`。

## 2.5 Scenario / Character

### Scenario Decision
Recommended: `SOURCE_WORLD`

Reason：課文本身就是「請到我的家鄉來」的邀請／世界旅行語境，不需要再外加偵探、RPG 等 Wrapper。

→ `SCENARIO LOCK: SOURCE_WORLD`

### Character after Scenario Lock
Candidate topology：`SINGLE_GUIDE` 或 `NO_GUIDE`；本 tabletop 選 `SINGLE_GUIDE / KEY_MOMENTS_ONLY` 作旅行觀察引導，只在轉場、提問、臺灣 transfer 時出現。

Guide 不替四國文本說話者回答，也不遮住原文證據。

→ `CHARACTER LOCK` 後才建立 DNA。

Result: PASS — Scenario 先於 Character；Guide 非每頁吉祥物。

## 2.6 Slide / Visual Decision

Cognitive scenes 可包含：
- 原文母畫面／Text Anchor
- 荷蘭低窪 → 堤防因果
- 風車 purpose + `為了`
- 木鞋／生活智慧 evidence→inference
- `所以 vs 為了`
- `堤／提／題` 同框比較
- 四國 evidence / structure compare
- 臺灣第五軌 transfer

同一認知場景可兩問，例如：
「為什麼木鞋適合？」→「堤防、風車、木鞋共同點是什麼？」

Result: PASS — no one-question-one-slide drift。

## 2.7 Style / Lesson Skin
只有在 Visual Grammar / Storyboard 形成後才選 Style Recipe，再形成旅行／世界探索的 Lesson Skin，套 Typography Lock，進 Gate B。

Result: PASS — Lesson Skin not pre-locked before Style Recipe。

### Lesson 9 verdict
`PASS`

---

# 3. Lesson 11｜〈兔子先生等等我〉

## 3.1 Input diagnosis

Text type：`劇本`。

Core reading needs：
- 角色
- 臺詞
- 舞臺提示
- 愛麗絲遇問題、判斷、嘗試、結果、新問題的循環
- 尺寸改變影響門／行動理解

## 3.2 Skill Selection

### Selected core skills
- `STAGE`：誰演｜怎麼演｜說什麼。
- `PROBLEM_LOOP`：problem → think/predict → try → check/result。

### Interaction grammar
- `PREDICT / VERIFY`：改舞臺提示前先預測表演差異，再驗證。

### Visual tools only
- `SCALE`：同一扇門下，愛麗絲 normal / small / too large，用於理解尺寸影響。
- `STAGE_VIEW`：把劇本資訊看成舞臺。

### Explicitly not copied from Lesson 9
- 不因前課有 COMPARE / STRUCTURE 就強迫本課使用同一組 skill。
- 可在局部做 comparison，但不升格為本課核心 skill，除非教師方向需要。

Result: PASS。

## 3.3 Text Anchor / Verify

Example cognitive scene：
- Text Anchor：`(不慌不忙)` 等舞臺提示。
- Question：這是角色說出口的臺詞，還是給演員的提示？
- Verify：把 `(不慌不忙)` 改成 `(驚慌失措)`，臺詞不變，比較表演與人物感受。

Visual cannot replace stage direction text.

Result: PASS — `TEXT_ANCHOR_PRESERVED`。

## 3.4 Budget Draft

MUST：
- 看懂劇本三元素
- 舞臺提示對表演／人物理解的作用
- Problem Loop

SHOULD：尺寸改變的場景化理解。

COULD：更長的角色演出活動／表演延伸。

Gate A 不宣告精確頁數。

Result: PASS。

## 3.5 Scenario / Character

### Scenario Decision
Recommended: `SOURCE_WORLD`

Reason：劇本與兔子洞故事已提供強烈舞臺／奇幻世界，不需要外加 Wrapper。

→ `SCENARIO LOCK: SOURCE_WORLD`

### Character after Scenario Lock
Recommended topology：`TEXT_CHARACTER_LED`。

- 愛麗絲／兔子等 Text Characters 是畫面與敘事主體。
- Guide 預設 OFF；只在必要的策略轉場才可能短暫出現。

→ `CHARACTER LOCK` 後才建立必要 DNA / cast refs。

Result: PASS。

## 3.6 Experience / Surprise

Potential Surprise Signature：同一場景／同一門保持不變，愛麗絲比例突然改變，讓 SCALE 成為視覺驚喜。

但 Surprise 服務尺寸理解，不升格成教學技能。

Result: PASS。

## 3.7 Style / Gate B / Gate C
Storyboard 後才選 Style Recipe / Lesson Skin / Typography；Gate B 鎖設計語言，代表頁驗證同一舞臺世界與 Alice 尺寸連續性，Gate C 後才批次。

Result: PASS。

### Lesson 11 verdict
`PASS`

---

# 4. Lesson 12｜〈老鞋匠和小精靈〉

## 4.1 Input diagnosis

Text type：故事／記敘文。

Core meaning：感恩與回饋能帶來幸福與喜悅。

Story evidence：
- 老鞋匠生計變差，只剩最後皮革
- 夜裡皮革變成鞋
- 生意改善
- 夫妻躲起來看到小精靈
- 夫妻做衣服／鞋子回報
- 小精靈收到禮物，彼此感到幸福

## 4.2 Skill Selection

### Selected core skills
- `STORY_ARC`：背景 → 困境 → 幫助 → 發現 → 回報 → 結果。
- `CHARACTER_EVIDENCE`：人物特質／價值理解必須由行動證據支持。
- `TRANSFER`：生活中遇到默默幫助自己的人，可以怎麼回應？

### Visual concept, not teaching skill
- `GIVE ↔ RETURN`：把幫助→感謝→回饋→共同幸福視覺化。

### Explicitly OFF
- `STAGE`：不是劇本核心。
- `SCALE`：沒有必要。
- 不複製 Lesson 9 的地理／比較路徑。

Result: PASS — zero-template generalization。

## 4.3 Budget Draft

MUST：故事因果與互惠核心、人物行動證據。
SHOULD：Story Arc、`不是……就是……` 等適合的語文深化。
COULD：更多價值討論／延伸故事。
Transfer：生活回應。

Gate A 不宣告頁數。

Result: PASS。

## 4.4 Scenario / Character

### Scenario Decision
Recommended: `SOURCE_WORLD`

Reason：夜晚鞋店／小精靈祕密幫忙本身已有強烈故事世界。

→ `SCENARIO LOCK: SOURCE_WORLD`

### Character after Scenario Lock
Recommended topology：`TEXT_CHARACTER_LED`。

Guide 預設 OFF 或只在故事轉場／課末 transfer 出現；鞋匠夫妻與小精靈是主體。

→ `CHARACTER LOCK` 後才建立正式 DNA。

Result: PASS。

## 4.5 Surprise Signature
Natural candidate：夜晚「究竟是誰把鞋做好？」的祕密揭曉。

它來自原故事，不需發明遊戲 gimmick。

Result: PASS。

## 4.6 Visual / Text
GIVE↔RETURN 可用同一視覺世界呈現互惠，但 Text Anchor 仍要保留角色具體行動，不把「感恩」畫成抽象愛心就算教完。

Result: PASS。

## 4.7 Style / Gate B / Gate C
Storyboard 後才選 Style Recipe / Lesson Skin；Gate B 鎖故事世界的視覺 identity，Gate C 用代表頁驗證夜間場景與角色連續性。

Result: PASS。

### Lesson 12 verdict
`PASS`

---

# 5. Cross-Lesson Comparison

| Check | Lesson 9 | Lesson 11 | Lesson 12 |
|---|---|---|---|
| Text type drives diagnosis | PASS | PASS | PASS |
| Different core skills | COMPARE/INFER/STRUCTURE/TRANSFER | STAGE/PROBLEM_LOOP | STORY_ARC/CHARACTER_EVIDENCE/TRANSFER |
| Visual tools kept separate | PASS | PASS | PASS |
| Text Anchor preserved | PASS | PASS | PASS |
| Budget Draft no exact pages | PASS | PASS | PASS |
| Scenario before Character | PASS | PASS | PASS |
| Character before DNA | PASS | PASS | PASS |
| Source World legal | PASS | PASS | PASS |
| No forced Guide mascot | PASS | PASS | PASS |
| Style before Lesson Skin Final | PASS | PASS | PASS |
| Gate B before representative visual | PASS | PASS | PASS |
| Gate C before batch renderer | PASS | PASS | PASS |

---

# 6. Tabletop Findings

## Finding A｜Generalization works
三課沒有被同一 skill template 套平。

## Finding B｜SOURCE_WORLD is important
三篇文本都能合理使用文本本身的世界；Scenario Registry 的價值包含「知道什麼時候不要外加 Wrapper」。

## Finding C｜Guide Character must remain optional
不同課都可能有 Guide，但 Guide 的存在是功能決策，不是品牌貼紙。

## Finding D｜Visual surprise can be text-native
Lesson 11 的比例改變、Lesson 12 的夜間揭曉都來自文本本身；不用另造 gimmick。

## Finding E｜Style timing fix was necessary
把 Style Recipe / Lesson Skin / Typography 移到 Gate B 前後，解決了「先鎖 Lesson Skin，後選 Style」的邏輯倒置。

---

# 7. Verdict

```yaml
three_lesson_tabletop:
  lesson_9: PASS
  lesson_11: PASS
  lesson_12: PASS
  genre_generalization: PASS
  skill_minimum_necessary: PASS
  visual_tool_separation: PASS
  text_anchor: PASS
  spiral_learning: PASS
  budget_two_phase: PASS
  scenario_character_lock_order: PASS
  style_lesson_skin_order: PASS
  gate_b_gate_c_separation: PASS
  overall: THREE_LESSON_TABLETOP_PASS
```

## Still pending

`LIVE_RUNTIME_RERUN_PENDING`

下一個真正需要驗證的是：選一課，從 Google Drive Runtime 依新 schema 實際走 Source/HOLD/LKB Review/Gate/Lock transitions，確認不只是 Markdown contracts 看起來一致。

V-MAX v1 此刻仍維持 `draft`，尚未宣告 sealed。
