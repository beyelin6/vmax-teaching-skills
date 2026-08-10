# V-MAX Visual Grammar 2.1

## 定位

Visual Grammar 定義「學生應該怎麼看，才能理解這個知識」。它不是美術風格庫，也不是版型庫，更不是插圖 Prompt 集合。

它負責把課文中的空間、時間、動作、比較、關係、修辭、觀點與知識結構，轉譯成學生看得見的視覺結構。

> 視覺呈現不只要畫對內容，還要看對方式。

> 風格可以改變，視覺語言不能改變。

---

## 系統位置

```text
Text DNA / Lesson Knowledge Book
        ↓
Structure DNA / Knowledge Relationship
        ↓
Director Intent
        ↓
Visual Grammar
        ↓
Gold Page Pattern
        ↓
Visual Sequence / Slide Architecture
        ↓
World / Style Recipe / Character DNA / Text UI
        ↓
Renderer
```

### 核心分工

- **Director Intent**：決定孩子先看什麼、再發現什麼。
- **Visual Grammar**：決定這個理解關係應該怎麼被看見。
- **Gold Page Pattern**：決定這個認知關係在學生眼前如何成為一個可觀看、可發現的教學事件。
- **Visual Sequence**：決定需要一張、兩張、四格或整段畫面。
- **Layout / Slide Architecture**：決定元素如何同框、如何排列與推進。
- **Style Recipe**：決定畫面的媒材、色彩、質感與氣氛。
- **Renderer**：負責忠實生成與排版，不重新決定教學關係。

**Visual Grammar ≠ Gold Page Pattern ≠ Layout。**
例如「比較」是一種 Grammar；`DUAL_WORLD_COMPARE` 或 `CHARACTER_MEANING_FIELD` 是可能的 Gold Pattern；左右雙欄、上下對照、同景切換才是 Layout 選擇。

Gold Page Pattern 依 `core/visual/gold-page-pattern-library.md`。不得從 Visual Grammar 直接跳到 Layout / Renderer。

---

# Bee Visual Grammar Core

## VG-01 Spatial Depth｜空間景深

適用：寫景、自然觀察、遊記、場景描寫。

模式：
- `far_to_near`
- `near_to_far`
- `high_to_low`
- `low_to_high`
- `inside_to_outside`
- `outside_to_inside`
- `whole_to_detail`
- `detail_to_whole`

視覺要求：
- 必須看得出前景、中景、背景或整體／局部層次。
- 文字與焦點依作者視線順序出現。
- 不得把有觀看順序的景物改成普通資訊卡。

---

## VG-02 Moving Viewpoint｜移動視點

適用：遊記、參觀、步行觀察、移步換景。

模式：
- `route_sequence`
- `turn_and_reveal`
- `stop_and_observe`
- `enter_and_explore`

視覺要求：
- 學生要知道「我現在在哪裡、正在看哪裡」。
- 優先使用路線、連續場景、視角切換，不使用無空間關係的卡片堆疊。

---

## VG-03 Temporal Progression｜時間推移

適用：事件發展、成長、季節、清晨至夜晚、狀態變化。

模式：
- `time_of_day`
- `seasonal_change`
- `before_after`
- `gradual_change`
- `event_progression`

視覺要求：
- 畫面本身必須呈現變化，不能只靠時間軸文字。
- 光線、姿態、環境、尺度或狀態至少有一項隨時間改變。

---

## VG-04 Comparison Field｜同場比較

適用：形近字、同音字、多音字、近反義詞、人物比較、觀點比較、概念辨析。

模式：
- `same_frame_compare`
- `similarity_difference`
- `shared_part_vs_unique_part`
- `context_compare`
- `scale_compare`

視覺要求：
- 比較對象必須能在同一視野快速來回對照。
- 共同點與差異點要有一致視覺位置。
- 字形、注音、詞義等正式資訊必須以已核准文字為真值。若教師鎖定 `IMAGE_INTEGRATED_VERIFIED_TEXT`，可與圖像同步生成，但必須逐字驗證並以局部重生修正；否則使用真實文字層。
- 不採「一個字一頁」造成工作記憶中斷。

核心原則：
> 一個字群不是多張字卡，而是一個可比較的視覺關係場。

---

## VG-05 Motion Grammar｜動態語法

適用：動作描寫、運動、擬人、連續事件。

模式：
- `action_sequence`
- `freeze_frame`
- `motion_path`
- `before_during_after`
- `pose_contrast`

視覺要求：
- 關鍵動詞必須有可見動作證據。
- 可使用連續分鏡、運動軌跡、時空定格。
- 禁止人物站著配一段描述動作的文字。

---

## VG-06 Sequential Narrative｜連續敘事

適用：成語、故事事件、情境推理、因果變化、童詩動態意象。

模式：
- `two_step`
- `three_step`
- `four_panel`
- `six_panel`
- `cinematic_storyboard`
- `setup_turn_result`

視覺要求：
- 先判斷「一張圖能不能完成理解」。不能時才啟動序列。
- 每格只推進一個明確變化。
- 角色、場景與關鍵物件需保持連續性。
- 成語不得只做單張裝飾圖；若語意包含事件發展，優先使用分鏡。

核心問題：
> 一個概念應該用幾個畫面，孩子才真的看懂？

---

## VG-07 Process & Causality｜流程與因果

適用：說明文、程序文、事件因果、問題解決、科普流程。

模式：
- `cause_effect`
- `input_process_output`
- `step_sequence`
- `cycle`
- `branching_choice`

視覺要求：
- 箭頭只能表示真正存在的方向或因果，不作裝飾。
- 每個節點需呈現狀態改變或關係，不只是一串文字框。
- 因果與時間順序不可混為一談。

---

## VG-08 Relationship Network｜關係網絡

適用：詞彙輻射、概念群、人物關係、主題關聯、知識網絡。

模式：
- `hub_spoke`
- `semantic_cluster`
- `relationship_map`
- `category_network`

視覺要求：
- 線條必須代表可說明的關係。
- 不為了好看把所有內容畫成心智圖。
- 中心節點不一定是最大字，而是認知上的核心。

---

## VG-09 Hierarchy & Structure｜層級結構

適用：文章結構、主旨—分述、總分結構、分類、段落關係。

模式：
- `whole_part`
- `main_support`
- `nested_structure`
- `category_tree`
- `story_arc`

視覺要求：
- 要讓學生看出「誰包含誰、誰支持誰」。
- 不因為有三段就自動生成三格。
- 文章結構優先依邏輯意義單位，不依原始段落數機械切割。

---

## VG-10 Sensory Focus｜感官焦點

適用：五感描寫、寫景、飲食、童詩。

模式：
- `visual_focus`
- `sound_focus`
- `smell_focus`
- `touch_focus`
- `taste_focus`
- `multi_sensory_blend`

視覺要求：
- 呈現感官線索，而不是只貼「視覺／聽覺」標籤。
- 必要時使用局部特寫、環境反應、聲音線條、材質感。

---

## VG-11 Figurative Transformation｜修辭視覺轉化

適用：譬喻、擬人、誇飾、想像、象徵。

模式：
- `literal_then_imagined`
- `blended_metaphor`
- `personification_action`
- `exaggerated_scale`
- `symbolic_mapping`

視覺要求：
- 同時讓學生分辨「真實是什麼」與「作者想像成什麼」。
- 不得把修辭畫成新的事實。
- 若修辭包含轉化過程，可與 VG-06 Sequential Narrative 組合。

---

## VG-12 Perspective & Voice｜敘事視角與聲音

適用：第一人稱、第三人稱、自述、多觀點、對話文本。

模式：
- `first_person_view`
- `observer_view`
- `character_switch`
- `multi_perspective`
- `speaker_listener`

視覺要求：
- 要清楚知道「誰在看、誰在說」。
- 多觀點不可只靠人物姓名標籤區分。
- 可使用視線方向、鏡位、位置、色溫或畫框差異建立觀點。

---

## VG-13 Evidence Lens｜證據聚焦

適用：課文找證據、修辭判讀、關鍵詞、推論、閱讀理解。

模式：
- `quote_to_evidence`
- `highlight_detail`
- `clue_chain`
- `evidence_to_inference`

視覺要求：
- 原文證據與推論必須視覺上可區分。
- 聚焦的是「支持理解的證據」，不是把整段課文螢光標滿。
- 可使用放大鏡、局部裁切、連線等語法，但不得取代正式文字層。

---

## VG-14 Contrast & Transformation｜對照與轉變

適用：前後改變、動靜、情緒、人物成長、期待與現實、冷暖差異。

模式：
- `before_vs_after`
- `static_vs_dynamic`
- `expectation_vs_reality`
- `emotion_shift`
- `state_transformation`

視覺要求：
- 對照必須一眼可比較。
- 優先以構圖、比例、姿態、景別、光影建立差異，而非兩欄長文字。

---

# Grammar 組合規則

一張投影片可以有：
- `primary_grammar`：只能 1 個，代表這頁最重要的理解方式。
- `secondary_grammar`：0–2 個，用來輔助，不得搶走主理解。

例如：

```yaml
primary_grammar: comparison_field
secondary_grammar:
  - evidence_lens
```

表示這頁主要任務是「比較」，證據聚焦只是幫助比較。

禁止為了視覺豐富而同時套用大量 Grammar。

---

# Grammar → Gold Pattern 選擇器

AI 在選 Visual Grammar 與 Gold Page Pattern 時，依序回答：

1. 學生這一頁真正要建立的是哪一種**認知關係**？
2. 這個關係是一眼比較、逐步變化、空間觀看、時間發展、因果、層級、網絡，還是觀點？
3. 先選 `primary_grammar`，再依 `core/visual/gold-page-pattern-library.md` 選 `primary_pattern`；不得直接跳到 Layout。
4. 一張畫面能完成理解嗎？若不能，交給 Visual Sequence 決定幀數。
5. 是否有課文證據需要被看見？若有，可加入 Evidence Lens，並確認 Pattern 中保留 evidence layer。
6. 是否存在「作者的觀看方式」？若有，優先保留作者的視角／時序／空間語法。
7. 最後才選 Layout、Style Recipe、Character 與 Text Integration Mode。

---

# Knowledge Type → Grammar 建議映射

| 教學內容 | 優先 Grammar |
|---|---|
| 形近字／同音字／多音字 | VG-04 Comparison Field |
| 成語事件／情境變化 | VG-06 Sequential Narrative |
| 寫景遠近／上下 | VG-01 Spatial Depth |
| 遊記／移步換景 | VG-02 Moving Viewpoint |
| 動作描寫／運動 | VG-05 Motion Grammar |
| 程序／步驟 | VG-07 Process & Causality |
| 詞語輻射／人物關係 | VG-08 Relationship Network |
| 課文結構／主旨分述 | VG-09 Hierarchy & Structure |
| 五感／童詩感官 | VG-10 Sensory Focus |
| 譬喻／擬人／誇飾 | VG-11 Figurative Transformation |
| 第一人稱／多觀點 | VG-12 Perspective & Voice |
| 找證據／推論 | VG-13 Evidence Lens |
| 前後改變／情緒成長 | VG-14 Contrast & Transformation |

這只是推薦，不是硬性綁定。Teacher Intent 與文本證據優先。

---

# Visual Intent 標準欄位

```yaml
visual_intent:
  teaching_goal:
  cognitive_relationship:
  text_evidence:
  primary_grammar:
  secondary_grammar: []
  primary_pattern:
  secondary_pattern: []
  first_focus:
  discovery_relation:
  visual_evidence:
  sequence_requirement:
    frames: 1
    reason:
  viewpoint:
  student_attention_path: []
  focal_subject:
  literal_content:
  imagined_content:
  comparison_targets: []
  evidence_focus: []
  layout_hint:
  guide_character_role:
  text_integration_plan:
  renderer_notes:
```

不適用欄位留空，不得為填表而強加效果。

---

# Renderer 原則

Renderer 可以改變媒材與美術完成方式，但不得改變 Visual Grammar 或已核准的 Gold Page Pattern。

```text
Text DNA：寫景，由遠而近
Director Intent：讓學生跟著作者視線走近主景
Visual Grammar：VG-01 far_to_near
Gold Page Pattern：依理解事件選擇
Visual Sequence：3 個連續焦距
Style Recipe：溫暖自然探險
Renderer：ChatGPT / NotebookLM / Gemini / Canva / 未來平台
```

換 Renderer 後，學生的觀看路徑與發現關係仍必須一致。若最終頁已無法辨識 `primary_pattern`，標記 `GOLD_PATTERN_DROPPED`。

---

# 禁止事項

- 不得把所有文章轉成資訊卡或心智圖。
- 不得把 Grammar 或 Gold Pattern 當成固定版型代碼。
- 不得從 Grammar 直接跳到 Layout / Renderer。
- 不得因為有三個項目就自動 grid-3。
- 不得因為有四個事件就自動四格漫畫；先判斷是否需要序列理解。
- 不得只因畫面漂亮而破壞作者的觀看順序。
- 不得讓插圖和文字各講各的。
- 不得用 Theme 世界觀遮蔽課文本身的空間、時間、情緒與語言證據。
- 不得讓圖片模型自行決定、改寫或未經驗證地輸出正式中文字形、注音或關鍵教學文字。教師明確選擇圖文同步生成時，仍須以核准文字為真值並完成逐字驗證。
- 不得讓引導角色為了出場而占據主要視覺焦點。

---

# 核心金句

> AI 真正有價值的，不只是把文字變成圖片，而是把老師腦中的學習畫面變成可以實行的教學現場。

> Visual Grammar 決定「怎麼看」；Gold Page Pattern 決定「這個理解如何在眼前發生」。

> 有些知識，不是一張圖就能理解，而是一連串畫面才能真正看懂。

> 好的教材，不是因為畫得漂亮，而是因為學生看懂了。
