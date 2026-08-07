# V-MAX Visual Grammar

## 定位

Visual Grammar 定義「課文中的觀看方式、空間關係、時間推移、敘事視角與修辭動態」如何被轉譯成簡報畫面。它不是美術風格庫，也不是插圖提示詞集合；它負責把作者的表達方式轉成學生看得見的視覺結構。

核心原則：

> 視覺呈現不只要畫對內容，還要看對方式。

例如寫景文若使用由遠而近、由高而低、移步換景或時間推移，畫面本身也應呈現相同的觀看路徑，而不是把所有景物平鋪成普通資訊卡。

## 與其他模組的關係

```text
Text DNA / Lesson Knowledge Book
        ↓
Structure DNA
        ↓
Visual Grammar
        ↓
Layout / Visual Intent
        ↓
Theme / Art Style / Character DNA
        ↓
Renderer（NotebookLM / ChatGPT / Gemini / Canva / 未來平台）
```

Visual Grammar 先決定「應該怎麼看」，Theme 才決定「看起來是什麼風格」。

## 主要視覺語法

### 1. Spatial Depth｜空間景深

適用：寫景、自然觀察、遊記、場景描寫。

可辨識模式：

- `far_to_near`：遠景 → 中景 → 近景
- `near_to_far`：近景 → 中景 → 遠景
- `high_to_low`：由高處視線向下
- `low_to_high`：由低處仰望
- `inside_to_outside`：由室內／核心向外
- `outside_to_inside`：由環境進入核心

視覺要求：

- 畫面需有明確前景、中景、背景層次。
- 文字標籤跟隨視線順序，不任意打散。
- 若課文透過焦點推進，投影片序列也應配合 zoom-in / zoom-out 的理解節奏。

### 2. Moving Viewpoint｜移動視點

適用：遊記、參觀、步行觀察、移步換景。

可辨識模式：

- `route_sequence`：依行進路線逐站觀看
- `turn_and_reveal`：轉彎／跨越後出現新景物
- `stop_and_observe`：移動 → 停留 → 細看

視覺要求：

- 優先使用路線、連續場景、視角切換，而非靜態並列卡片。
- 需要保留「我目前站在哪裡、正在看哪裡」的空間感。

### 3. Temporal Progression｜時間推移

適用：清晨到夜晚、四季、成長、事件發展。

可辨識模式：

- `time_of_day`
- `seasonal_change`
- `before_after`
- `gradual_change`

視覺要求：

- 光線、色溫、天空、人物狀態或環境細節應隨時間變化。
- 不只用時間軸文字標示，畫面本身也必須呈現變化。

### 4. Contrast｜對照

適用：遠近、大小、動靜、冷暖、前後變化、人物選擇。

模式：

- `before_vs_after`
- `static_vs_dynamic`
- `large_vs_small`
- `light_vs_dark`
- `expectation_vs_reality`

視覺要求：

- 對照必須一眼可比較。
- 避免只用兩欄文字；優先以構圖、比例、姿態、景別或光影建立差異。

### 5. Motion Grammar｜動態語法

適用：動作描寫、運動、擬人、連續事件。

模式：

- `action_sequence`
- `freeze_frame`
- `motion_path`
- `before_during_after`

視覺要求：

- 關鍵動詞要有可見動作證據。
- 可用連續分鏡、運動軌跡、時空定格，而非人物站著配文字。

### 6. Sensory Focus｜感官焦點

適用：五感描寫、寫景、飲食、童詩。

模式：

- `visual_focus`
- `sound_focus`
- `smell_focus`
- `touch_focus`
- `taste_focus`

視覺要求：

- 圖像呈現感官線索，而非只標示「視覺／聽覺」。
- 必要時以局部特寫、環境反應、聲音線條或材質感協助理解。

### 7. Figurative Transformation｜修辭視覺轉化

適用：譬喻、擬人、誇飾、想像。

模式：

- `literal_then_imagined`：真實畫面 → 聯想畫面
- `blended_metaphor`：兩個意象視覺融合
- `personification_action`：非人事物做出人的動作／情緒
- `exaggerated_scale`：誇張比例呈現語意

視覺要求：

- 必須同時讓學生分辨「現實是什麼」與「作者想像成什麼」。
- 不得把修辭插圖畫成新的事實，造成文意誤解。

### 8. Perspective / Voice｜敘事視角

適用：第一人稱、第三人稱、角色自述、多觀點文章。

模式：

- `first_person_view`
- `observer_view`
- `character_switch`
- `multi_perspective`

視覺要求：

- 第一人稱可使用視線式構圖或角色視角。
- 多觀點要清楚區別誰正在看、誰正在說。

## Visual Intent 標準欄位

每張需要主要視覺設計的投影片，Visual Designer 至少輸出：

```yaml
visual_intent:
  teaching_goal:
  text_evidence:
  visual_grammar:
    primary:
    secondary: []
  viewpoint:
  depth_layers:
    foreground:
    midground:
    background:
  focal_subject:
  student_attention_path: []
  literal_content:
  imagined_content:
  layout_hint:
  guide_character_role:
  quote_role:
  renderer_notes:
```

不適用的欄位可留空，不得為填表而強行加入視覺效果。

## 寫景文專用判斷

遇到寫景文時，生成簡報前必須先回答：

1. 作者的觀察位置在哪裡？
2. 視線是固定還是移動？
3. 景物出現順序是遠近、上下、內外、左右，還是依行進路線？
4. 是否有時間、光線或季節變化？
5. 哪些景物是背景，哪些是作者真正聚焦的主體？
6. 有沒有由整體到局部／局部到整體的焦點變化？

若答案顯示存在清楚觀看順序，投影片構圖與頁面序列必須反映該順序。

## Renderer 原則

Renderer 負責美術完成度，但不得改變 Visual Grammar。

例如：

```text
Text DNA：寫景文，由遠而近
Visual Grammar：far_to_near
Visual Intent：山脈遠景 → 河岸中景 → 花朵近景
Theme：溫暖水彩自然探險
Renderer：NotebookLM / ChatGPT / Gemini
```

換 Renderer 時，觀看邏輯必須一致，只允許美術語言與實際渲染方式不同。

## 禁止事項

- 不得把所有文章都轉成資訊卡或普通心智圖。
- 不得只因版面漂亮而破壞作者觀看順序。
- 不得讓插圖和文字各講各的。
- 不得只靠標題寫「遠景／近景」，畫面卻沒有景深差異。
- 不得因 Theme 世界觀過強而遮蔽課文本身的空間、時間與情緒。

## 核心金句

> AI 真正有價值的，不只是把文字變成圖片，而是把老師腦中的學習畫面變成可以實行的教學現場。
