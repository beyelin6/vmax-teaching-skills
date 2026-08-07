# Visual Sequence｜序列式圖像規格

## 目的

將包含「發展、變化、因果、時間、轉折、動作、比較前後」的知識轉成連續畫面，讓學生透過圖像順序建立理解，而不是只看單張插圖。

## 核心原則

- Sequence 是理解工具，不是裝飾漫畫。
- 是否使用序列圖像，先看概念結構，再看美術風格。
- 序列長度依認知負荷決定，不固定四格。
- 每格只處理一個主要動作或理解節點。
- 文字必須少而準，畫面關係應能自行傳達大部分意義。
- 學生若需要推論，可保留一格或一句不直接揭曉答案。

## 推薦型態

- `single_frame`：單張核心意象。
- `two_frame_compare`：前後、真實/想像、原因/結果。
- `three_step_sequence`：簡短流程、三段變化。
- `four_panel_comic`：成語、事件轉折、生活情境。
- `six_panel_story`：短篇故事、課文事件濃縮。
- `timeline_sequence`：時間推移。
- `cinematic_storyboard`：情緒、視角、鏡頭節奏重要的內容。
- `wide_to_close_sequence`：遠景→中景→近景。
- `before_after`：改變、成長、修正、結果。
- `parallel_sequence`：兩條事件線同步比較。

## 適用判斷

優先推薦序列式圖像：

- 成語故事本身含事件發展。
- 課文有清楚事件順序或轉折。
- 動作描寫需要拆成連續步驟。
- 因果關係若只用箭頭會過度抽象。
- 修辭需要呈現「原畫面→想像畫面」。
- 字義本身包含動作或狀態改變。
- 說明文包含製作、循環、運作流程。
- 寫景文有移步換景、視線推近或時間推移。

不優先使用：

- 靜態分類。
- 單一概念定義。
- 人物關係網。
- 並列特徵比較且無時間順序。

## 成語模式

成語頁先判斷是否有「故事性」。有故事性時優先推薦四格或六格漫畫。

每格需標示：

1. `event_node`
2. `visual_action`
3. `key_clue`
4. `student_inference_target`

成語教學流程可採：

```text
看漫畫猜故事
→ 找出轉折
→ 推測成語意思
→ 正式解釋
→ 易誤用
→ 近義成語
→ 情境練習
```

## 與 Director Intent 的關係

Sequence Designer 不自行決定全部鏡頭語言，需讀取 Director Intent：

- 第一個畫面先讓學生看到什麼？
- 哪一格需要停格？
- 哪一格要隱藏關鍵資訊？
- 哪一格揭曉？
- 最後一格希望留下什麼理解？

## 標準輸出

```yaml
visual_sequence:
  target:
  purpose:
  recommended_type:
  panel_count:
  reason:
  sequence:
    - panel: 1
      event_node:
      visual_action:
      focus:
      text_overlay:
      guide_role:
  reveal_strategy:
  student_task:
  visual_consistency:
```

## Renderer 規則

- 所有格必須維持角色 DNA、場景連續性與視覺風格一致。
- 同一角色衣著、髮型、比例不可無故改變。
- 畫面閱讀方向需清楚。
- 不可用大量文字補救不清楚的分鏡。
- 可輸出為一張多格頁，或拆成逐頁連續畫面。
