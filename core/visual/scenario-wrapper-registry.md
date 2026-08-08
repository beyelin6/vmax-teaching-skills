# V-MAX Scenario Wrapper Registry 1.0

## 定位

Scenario Wrapper 是 V-MAX 的「情境包裝層」。它不是美術風格，也不是角色設定，而是回答：

> 這一課，要讓學生像進入哪一個有情境、有角色功能、有任務感的學習世界？

核心原則：

> 情境包裝不是為了可愛，而是為了讓這篇課文用更自然、更有吸引力的方式被理解。

> 包裝可以換，課文與學習目標不能被包裝吃掉。

---

## A. 與其他層的區別

```text
Text DNA / Teacher Intent
        ↓
Learning Task / Director Intent
        ↓
Scenario Wrapper（情境包裝）
        ↓
Character Topology（誰上場）
        ↓
Visual Grammar（怎麼看）
        ↓
Style Recipe（畫成什麼媒材／美術感）
        ↓
Renderer
```

- Scenario Wrapper = 課堂世界／節目感／任務隱喻
- Character = 誰在這個世界裡陪學生學
- Visual Grammar = 學生如何看出認知關係
- Style Recipe = 水彩、手繪動畫、漫畫、清晰圖解等美術媒材

禁止把四層重新混成一個「風格名稱」。

---

## B. 來源考古與遷移原則

V-MAX 舊版 `content-style-library-spark.md` 曾收錄 76 種視覺風格，並包含 ESM S-01～S-23 的 Scenario / Metaphor 設計。舊資料的價值保留，但需拆層：

- 舊「場景標籤／隱喻」→ Scenario Wrapper
- 舊「角色設定」→ Character Registry
- 舊「文本結構／語氣」→ Director / Session
- 舊「視覺構成／色彩／材質」→ Style Recipe
- 舊「適用文體／情境」→ Registry retrieval tags

不得因為舊庫已有某包裝，就強迫新課套用。

---

## C. Wrapper Status

```yaml
wrapper_status:
  OFF
  SUGGESTED
  TEACHER_SELECTED
  REUSABLE_CONFIRMED
```

預設 `OFF`。

只有當包裝能讓學生更容易進入文本、理解任務或提高合理投入時才啟用。

---

## D. Registry Schema

```yaml
scenario_wrapper:
  id:
  name:
  aliases: []
  provenance: OLD_SYSTEM | TEACHER_DISCUSSION | LESSON_DISCOVERY | AI_SUGGESTION
  status:

  metaphor:
  world_logic:
  student_role:
  possible_guide_roles: []

  fit:
    genres: []
    topics: []
    learning_tasks: []
    reading_moves: []
    language_modes: []
    emotional_tone: []

  signature_moves: []
  wrapper_language_examples: []
  visual_motifs: []

  avoid_when: []
  overuse_risk:
  recent_use_penalty: true

  compatible_visual_grammars: []
  compatible_style_families: []
  compatible_character_tags: []

  successful_lessons: []
  student_feedback_notes: []
  teacher_notes: []
```

---

## E. 既有系統遷移種子

以下來自舊 ESM / Style Library 的「隱喻」智慧，先保留為可檢索種子；這些名稱不等於最終學生版標題。

### SW-OLD-01｜戰場挑戰
- provenance: OLD_SYSTEM
- source_seed: S-01 熱血少年戰鬥
- metaphor: 戰場／挑戰賽
- 適合：困難概念、複習衝刺、破關式練習
- signature_moves: 敵人出現、弱點分析、解法、挑戰完成
- 風險：容易把一般課程過度競賽化；不宜用於需要安靜感受的文本

### SW-OLD-02｜直播間／高互動節目
- provenance: OLD_SYSTEM
- source_seed: S-02 Vtuber 學院
- metaphor: 直播間
- 適合：即時互動、口語表達、投票、觀點回應
- 風險：不能只做成表面直播 UI

### SW-OLD-03｜連載漫畫世界
- provenance: OLD_SYSTEM
- source_seed: S-03 學習漫畫風
- metaphor: 連載漫畫
- 適合：科普、歷史故事、事件序列、因果
- signature_moves: 分鏡、角色對話、轉折、下一格揭曉

### SW-OLD-04｜RPG 任務地圖
- provenance: OLD_SYSTEM
- source_seed: S-04 遊戲化任務地圖
- metaphor: 任務地圖／旅程
- 適合：單元導覽、長文本、多站任務、進度總覽
- 風險：不可為了任務感硬切頁數

### SW-OLD-05｜精裝立體故事書
- provenance: OLD_SYSTEM
- source_seed: S-05 虛擬立體書
- metaphor: 精裝故事書
- 適合：記敘文、繪本、故事性文本
- signature_moves: 翻頁、場景展開、故事節點

### SW-OLD-10｜博物館微縮模型
- provenance: OLD_SYSTEM
- source_seed: S-10 等距微縮世界
- metaphor: 博物館模型／展示櫃
- 適合：生態、系統、空間關係、結構說明

### SW-OLD-12｜陪伴式讀書室
- provenance: OLD_SYSTEM
- source_seed: S-12 Lo-Fi 讀書室
- metaphor: 深夜書房／伴讀空間
- 適合：自學、閱讀、安靜整理
- 風險：情境氛圍不可壓過教材可讀性

### SW-OLD-13｜特刊編輯部
- provenance: OLD_SYSTEM
- source_seed: S-13 拼貼誌手作感
- metaphor: 手作雜誌／特刊
- 適合：人文、創意寫作、多觀點整理
- possible_guide_roles: 編輯、小記者

### SW-OLD-15｜未來儀表板
- provenance: OLD_SYSTEM
- source_seed: S-15 玻璃擬態 UI
- metaphor: 未來控制台／儀表板
- 適合：資訊分類、數據、系統整理
- 風險：不適合情感主導文本

### SW-OLD-16｜自然野外旅程
- provenance: OLD_SYSTEM
- source_seed: S-16 吉卜力式自然風
- metaphor: 野外探索
- 適合：自然、生態、散文、觀察
- 注意：此項舊資料同時混有美術風格，遷移時僅保留「野外探索」情境隱喻；美術感另交 Style Recipe。

### SW-OLD-20｜交換日記
- provenance: OLD_SYSTEM
- source_seed: S-20 溫暖色鉛筆
- metaphor: 交換日記
- 適合：情緒、輔導、第一人稱、生活反思

### SW-OLD-21｜畫廊導覽
- provenance: OLD_SYSTEM
- source_seed: S-21 夢幻水彩渲染
- metaphor: 畫廊
- 適合：抒情、寫景、美感、意象欣賞
- 注意：夢幻水彩是 Style，不是 Wrapper；只保留「畫廊／作品導覽」情境。

### SW-OLD-22｜卷軸／古典展卷
- provenance: OLD_SYSTEM
- source_seed: S-22 東方水墨留白
- metaphor: 展卷／古典閱讀現場
- 適合：古文、古典詩詞、歷史文化

### SW-OLD-23｜電影現場／電影旁白
- provenance: OLD_SYSTEM
- source_seed: S-23 新海誠光影風
- metaphor: 電影
- 適合：回憶性文本、情感引導、寫景、視角移動
- 注意：電影光影屬 Style；「電影／鏡頭」屬 Wrapper / Visual Grammar。

---

## F. 教師近期確認的高價值 Wrapper 候選

以下來自教師實際偏好與課堂經驗，優先納入候選庫。

### SW-BEE-01｜偵探辦案所
- provenance: TEACHER_DISCUSSION
- metaphor: 偵探辦案／線索室
- student_role: 小偵探、證據分析員
- fit.learning_tasks: 找線索、推論、字詞辨析、閱讀理解、證據判斷
- compatible_visual_grammars: Evidence Lens, Comparison Field, Relationship Network
- signature_moves: 線索出現 → 找證據 → 提出推論 → 驗證
- wrapper_language_examples: 「哪一條線索最關鍵？」、「證據在哪一句？」
- avoid_when: 純抒情停格、需要沉浸而非破解的文本

### SW-BEE-02｜運動播報中心
- provenance: TEACHER_DISCUSSION
- metaphor: 現場轉播／精彩回放
- student_role: 現場觀察員、小主播、動作分析員
- fit.learning_tasks: 動作描寫、速度、節奏、過程、情緒轉折、順序
- compatible_visual_grammars: Motion Grammar, Temporal Progression, Sequential Narrative
- signature_moves: 現場進入 → 關鍵動作 → 慢動作回放 → 賽後分析
- avoid_when: 靜態說理、情緒需留白的頁面

### SW-BEE-03｜美食節目製作室
- provenance: TEACHER_DISCUSSION
- metaphor: 美食節目／試吃現場／料理特輯
- student_role: 小主持人、美食評論員、料理觀察員
- fit.learning_tasks: 五感描寫、順序、介紹、詞語運用、口語表達
- compatible_visual_grammars: Sensory Focus, Process & Causality, Comparison
- signature_moves: 開場介紹 → 觀察色香味 → 描述證據 → 評論／推薦
- avoid_when: 與食物／感官完全無關時不得硬套

### SW-BEE-04｜大導演拍片現場
- provenance: TEACHER_DISCUSSION
- metaphor: 電影拍攝現場
- student_role: 導演、攝影師、場記、取景員
- fit.learning_tasks: 寫景、視角移動、遠近景、感官描寫、畫面順序、童詩意象
- compatible_visual_grammars: Moving Viewpoint, Spatial Depth, Sensory Focus, Sequential Narrative
- signature_moves: 勘景 → 選鏡頭 → 遠景／中景／近景 → 定格 → 剪接／回看
- wrapper_language_examples: 「第一個鏡頭你想拍哪裡？」、「作者把焦點推近了嗎？」
- avoid_when: 概念型知識頁不應硬用電影語彙

---

## G. Retrieval Logic｜怎麼撈包裝

新課分析時，系統依下列訊號找候選，不從 76 種全量丟給教師選：

1. 文體與文本結構
2. 本課核心理解任務
3. Director Intent / Visual Grammar
4. 學生要執行的認知行動
5. 情緒氛圍
6. 是否已有成功使用的 Wrapper
7. 最近是否使用太頻繁
8. 教師偏好與班級反應

輸出最多 1–3 個候選：

```yaml
wrapper_candidates:
  - id:
    why_fit:
    what_students_will_do_differently:
    possible_character_topology:
    visual_opportunity:
    risk:
    provenance:
```

教師可：接受／拒絕／改寫／混搭。

---

## H. 混搭規則

允許主包裝 + 局部語彙，但不得一課變成多個互相競爭的節目。

```yaml
wrapper_mix:
  primary:
  secondary_accent:
  secondary_scope:
```

例：
- 主：大導演拍片現場
- 局部：偵探「找證據」只用在一個閱讀任務

不允許：每個 Act 都換一個完全不同的節目世界。

---

## I. 驚喜感保護

班級對「今天誰上場／今天是什麼世界」的期待，本身是投入的一部分。

因此：
- 不固定每課同一 Wrapper。
- 不固定每課 Bee 老師。
- 相同 Wrapper 連續使用需有充分理由。
- `recent_use_penalty: true` 預設啟用。
- 若新角色／新 Wrapper 與文本高度契合，可優先提案。
- 驚喜不能凌駕理解；最適合的課有時就是 `OFF`。

---

## J. Quality Gate

啟用 Scenario Wrapper 前檢查：

- 拿掉包裝後，學習任務是否仍成立？若不成立，代表教學設計本身有問題。
- 加上包裝後，學生是否更容易理解要做什麼？
- 包裝是否與課文自然相連，而不是硬套？
- 是否產生更清楚的角色功能？
- 是否讓 Visual Grammar 更自然，而不是只多裝飾？
- 是否因追求節目感而改寫教材事實？
- 是否太像上一課，失去驚喜？
- 是否可在學生畫面使用繁體中文自然表達，而不靠大量英文 UI 標籤？

若增益不明確，`OFF`。

---

## K. Lesson Learning

完成一課後記錄：

```yaml
wrapper_learning:
  wrapper_id:
  lesson:
  teacher_rating:
  student_engagement_signal:
  student_visual_feedback:
  helped_understanding:
  overused_or_distracting:
  reusable_update:
```

高品質且多次成功的包裝可升級為 `REUSABLE_CONFIRMED`。

---

## 核心金句

> 同一篇課文可以有很多漂亮的畫法，但只有少數情境能真正讓孩子更想走進去。

> V-MAX 不替每一課換皮；V-MAX 替每一課找到最自然的「進場方式」。

> 今天誰上場、今天進哪個世界，可以是驚喜；但孩子最後帶走的，仍然要是課文與能力。
