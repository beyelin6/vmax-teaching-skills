# Director Designer

版本：2.1.0

## 目的

Director Designer 是 V-MAX 的導演技能。它把 Text DNA、Knowledge Network、Lesson Intent、Learning Profile 與 Teacher Intent 轉譯成可執行的 `Director Map` 與 `Shot Map`。

完整規則以：

- `core/director/director-engine.md`
- `core/visual/visual-grammar.md`
- `core/visual/visual-sequence.md`
- `core/visual/style-recipe-families.md`
- `core/visual/scenario-wrapper-family-model.md`
- `core/visual/scenario-wrapper-language-arts-selector.md`
- `core/visual/scenario-wrapper-archaeology-index.md`

為準。

核心問題：

> 孩子應該怎麼一路看懂這一課？

而不是：

> 這一頁要畫什麼？

---

## 必讀輸入

- Text DNA：文體、段落功能、作者觀看／敘事順序
- Knowledge Network：字詞、句型、修辭、成語、概念關係
- Lesson Intent：本課學習目標
- Teacher Intent：教師指定焦點、節奏、保留／刪除項目
- Learning Profile：班級目前需要的支架程度
- Scenario Wrapper Registry / Family Model：若本課需要情境包裝
- Bee Visual Language / Style Recipe：若已選定

選配：

- 既有課堂版本與 Patch
- Bee Quality Benchmark
- 公開課／平板 Classroom Variant

---

## 決策順序

1. 先判斷整課的理解旅程與真正轉折。
2. 依自然段／意義段形成 Learning Acts；`3–7` 只作常見軟參考，不是硬限制，不先算投影片頁數。
3. 每幕只設定一個主要 `act_goal`。
4. 為每幕決定 ENTER / NOTICE / DISCOVER / PAUSE / REVEAL / TRANSFER 等節奏動作。
5. 決定 Reveal Policy：open / guided / delayed / progressive / hold。
6. 判斷本課是否需要 `Scenario Wrapper`：
   - 若包裝不能改變學生的學習行動，只是變漂亮，預設 `OFF`。
   - 若需要，先選 Wrapper Family，再選 Variant；不得從舊 76 種風格直接挑皮。
   - 只向教師提出最多 1–3 個候選，包含「不包裝」方案；不得把整個資料庫丟給教師選。
7. 依認知關係呼叫完整 Visual Grammar；不得從固定 Layout 或 Wrapper 反推。
8. 判斷是否需要 Visual Sequence。
9. 依已確認的文本需求與 Wrapper 判斷 Character Topology；角色不是 Wrapper 的固定配件。
10. 最後才生成 Shot Map、估算頁數，交給 Layout / Style / Renderer。

不得先從「喜歡哪種畫風」、「今天想玩哪個節目」或「NotebookLM 一次能做幾頁」反推課程。

---

## Scenario Wrapper｜情境包裝規則

### 定位

Scenario Wrapper 回答：

> 孩子今天要用什麼身分、進入哪一個學習世界，才能更自然地完成這一課的理解任務？

它不等於 Style Recipe，也不等於 Character。

```text
Text DNA / Teacher Intent
→ Learning Task / Director Intent
→ Scenario Wrapper（可 OFF）
→ Character Topology
→ Visual Grammar
→ Style Recipe
→ Renderer
```

### 選擇原則

1. 文體只是訊號之一，不採「某文體固定某包裝」。
2. 優先看學生真正要做的認知行動：觀察、推論、比較、取景、報導、整理、說服、創作等。
3. 先選 Family，再選 Variant。
4. 新想法若只是既有教學世界的主題變形，新增 Variant，不新增 Family。
5. 同一 Family 可跨課重用；同一 Variant 與同一角色連續出現時提高 recent-use penalty。
6. 主包裝可搭一個局部 accent，但不得每個 Act 換一套世界。
7. 包裝不得改寫教材事實、作者語氣或 Teacher Intent。

### 國語課常用母型

- `WF-01 LIVE_REPORTING`：現場報導／特派記者
- `WF-02 INVESTIGATION`：偵探／調查
- `WF-03 QUEST`：冒險／任務
- `WF-04 STORY_SERIAL`：故事／說書／連載
- `WF-05 FILM_PRODUCTION`：導演／影像製作
- `WF-06 FIELD_EXPLORATION`：探索／野外觀察
- `WF-07 CURATION`：博物館／展覽／策展
- `WF-08 ANALYSIS_LAB`：研究室／專家分析
- `WF-09 EDITORIAL`：編輯部／媒體製作
- `WF-10 SHOW_HOSTING`：節目／主持／直播
- `WF-11 ARGUMENT_PITCH`：提案／辯論／宣言
- `WF-12 QUIET_STUDY`：陪伴閱讀／私人學習空間

其中：
- 運動播報中心 = `WF-01` 的運動變體，不是獨立母型。
- 大導演拍片現場 = `WF-05` 的高價值變體。
- 美食節目製作室 = `WF-10` 的生活／五感變體。
- 偵探辦案所 = `WF-02` 的高價值變體。

### Wrapper 候選輸出

```yaml
scenario_wrapper_candidates:
  - family:
    variant:
    why_fit:
    student_action:
    reading_or_language_gain:
    possible_character_topology:
    visual_opportunity:
    risk:
    provenance:
```

每課最多 3 個候選，包含 `OFF` 時最多仍為 3 個。

---

## 三個尺度

### Lesson Arc
整課觀看與理解弧線。

### Act
一段完整的理解任務，不綁固定頁數。

### Shot
單頁／單畫面注意單位；每頁必須說得出學生多懂了什麼。

---

## Director Map 必備欄位

```yaml
director_map:
  lesson_id:
  central_learning_journey:
  opening_hook:
  final_takeaway:

  scenario_wrapper:
    status: OFF | SUGGESTED | TEACHER_SELECTED | REUSABLE_CONFIRMED
    family:
    variant:
    rationale:
    secondary_accent:
    secondary_scope:

  acts:
    - act_id:
      title:
      act_goal:
      text_evidence: []
      entry_mode:
      primary_pacing:
      reveal_policy:
      primary_visual_grammar:
      secondary_visual_grammar: []
      sequence_mode:
      guide_role:
      emotional_target:
      closure:
      handoff:

  rhythm_curve: []
  protected_moments: []
  do_not_do: []
```

---

## Shot Map 必備欄位

```yaml
shot:
  id:
  act_id:
  function:
  learning_gain:
  first_focus:
  attention_path: []
  text_evidence:
  reveal_policy:
  pacing:
  visual_grammar:
    primary:
    secondary: []
  sequence:
    mode:
    panel_count:
  character:
    role:
    purpose:
  scenario_wrapper_use:
    mode: OFF | WORLD | ACCENT
    purpose:
  layout_intent:
  renderer_must_preserve: []
```

---

## Knowledge Chunk 原則

不得把「一個教材項目」機械地當成「一頁」。

一個 Chunk = 一個學生需要建立的認知關係。

- 形近字：同一比較關係優先同場。
- 多音字：讀音 × 語意 × 情境對照。
- 成語：先判斷是否需要事件序列；不一律漫畫化。
- 句型／修辭：先從原句發現，再命名。
- 主旨／結構：若需推論，先累積證據，再 Reveal。

---

## 角色規則

預設 `OFF`，只有角色能改變注意、理解、策略或情緒時才出場。

合法功能：

- HOST
- NOTICE
- COACH
- INTERVIEW
- TRANSITION
- REFLECT
- MISSION
- OFF

禁止每頁固定 guideTalk，禁止角色代替學生說出應自行發現的答案。

Scenario Wrapper 不得自動綁定固定角色；先決定這課需要什麼角色關係，再從 Character Registry 撈候選。

---

## 文體提示

### 童詩
保留節奏、意象與留白；優先感官進場、意象變形、重複節奏、內在情緒、語言工具與仿作。可檢查 `WF-05 導演／影像製作`；若動作性強也可檢查 `WF-01 現場報導`。不得硬拆成逐段摘要。

### 故事／記敘文
保留因果、轉折、高潮與資訊揭露順序。優先檢查 `WF-04 故事／連載`、`WF-01 現場報導`；若核心是找證據／人物推論可檢查 `WF-02`。

### 寫景文
保留遠近、上下、移步換景、時間推移等觀看路徑。優先檢查 `WF-05 導演／影像製作`、`WF-06 野外探索`、`WF-07 策展／畫廊`。

### 說明文
先建結構模型，再進細節；圖解與關係優先於氣氛圖。優先檢查 `WF-08 研究分析`、`WF-06 探索`、`WF-07 策展`、`WF-09 編輯部`。

### 人物文
從行動／語言／事件證據推論人物特質，不先公布標籤。依任務可檢查 `WF-02 調查`、`WF-04 故事`、`WF-09 編輯部`。

### 議論／說理
優先檢查 `WF-11 提案／辯論`；若重點是驗證證據，可局部借用 `WF-02 調查`。

### 古文／文化文本
優先檢查 `WF-07 博物館／展覽`、`WF-04 說書／傳說`；若重點為場景意象可檢查 `WF-05`。

---

## Regression Gate

若出現任一情況，必須重排：

- 為平台批次限制改變課程弧線
- 所有段落使用相同頁型
- 過早揭露學生應自行發現的結論
- 角色高頻但沒有教學功能
- 整課沒有節奏差異
- 語文知識被抽離文本脈絡
- 新版理解路徑比舊版更碎
- 因為包裝很有趣而改變教材重點
- Wrapper 只是 UI 換皮，學生行動沒有改變
- 同一課同時存在多個互相競爭的節目世界

---

## Teacher Sovereignty

AI 可以推薦、補充、提醒；不能擅自改變教師的教學意圖。

教師明確指定的核心焦點、保留內容、課堂策略、角色、情境包裝與評量需求，優先於 Director Engine 的自動建議。
