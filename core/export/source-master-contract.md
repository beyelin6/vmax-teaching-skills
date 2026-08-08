# V-MAX Source Master Contract 1.0

## 定位

Source Master 是 V-MAX 提供給 NotebookLM、Gemini、ChatGPT、Canva 或未來 Renderer Adapter 的平台中立來源文件契約。

核心原則：

> 完整教學設計放在 Source Master；平台生成指令只負責操作，不重新發明教學內容。

NotebookLM 可使用 `.md` / `.txt` 表示此契約；不得因平台不支援 YAML 副檔名而改變資料結構本身。

## A. 必備頂層區塊

```yaml
source_master:
  metadata:
  source_anchor:
  teacher_intent:
  lesson_map:
  contextual_enrichment:
  learning_frameworks:
  session_map:
  lesson_visual_map:
  scenario_wrapper:
  character_cast:
  knowledge_lab:
  visual_grammar_plan:
  slide_architecture:
  style_recipe:
  renderer_constraints:
  teacher_notes_policy:
  quality_requirements:
  lesson_learning_hooks:
```

未啟用的模組明確標 `OFF`，不要整段消失造成 Adapter 猜測。

## B. Lesson Visual Map Schema

```yaml
lesson_visual_map:
  status: OFF | OPEN | CLOSE | BOTH
  purpose:
  central_message:
  structure_type:
  structure_path: []
  key_nodes:
    - id:
      label:
      visual_meaning:
      source_evidence:
  key_scenes_or_images: []
  key_language_focus: []
  main_idea_or_feeling:
  transfer_or_extension:
  reveal_policy:
    open_map: preview_without_spoiler
    close_map: confirmed_learning_summary
  reveal_guardrails: []
  primary_visual_grammar:
  secondary_visual_grammars: []
  visual_intent:
  native_text_required: []
  renderer_must_preserve: []
```

### Adapter 不得自行補寫

若 `status: OFF`，平台不得因為「心智圖很好看」自行新增。
若 `OPEN`，不得把 CLOSE 才能出現的答案提前生成。
若來源未提供某個主旨／語文焦點，Adapter 不得自己補成教材事實。

## C. Provenance

來源內容、教師決策、AI 建議與外部補充需保留來源標記：

```yaml
provenance: TEXTBOOK | TEACHER | AI_SUGGESTION | EXTERNAL_SOURCE
```

平台轉譯不得把 `AI_SUGGESTION` 改寫成教材原有內容。

## D. NotebookLM / Renderer Adapter 規則

Adapter 只負責：
- 把 Source Master 映射成平台能理解的格式。
- 保留段落、Reveal、Visual Intent、Character、Style、Native Text 要求。
- 依平台能力選擇 Image-first / Hybrid / Native，但不能改 Teacher Intent。

Adapter 不負責：
- 重新挑教學重點。
- 新增未確認角色或 Wrapper。
- 重排 Session 以符合批次限制。
- 把 Lesson Visual Map 改成固定樹狀心智圖。
- 因文字放不下而縮小學生核心文字。

## E. 完整內容與生成指令分離

建議交付組合：

```text
Lesson_Source_Master.md
+ Renderer_Instruction.md / .txt
```

`Lesson_Source_Master.md`：保存完整教材、教學結構、頁面意圖與限制。
`Renderer_Instruction`：只保存平台操作規則、批次方式、讀取順序與輸出格式。

## F. Contract Gate

交付 Adapter 前必查：
- Lesson Visual Map 狀態與欄位是否完整。
- Teacher Intent LOCKED 項是否可追蹤。
- Session Map 是否完整傳遞。
- Character / Wrapper 是否保留 OFF 可能。
- Native Text / Zero-Tolerance Text 是否標示。
- Renderer 是否能知道哪些元素不可改。

若 Adapter 需要「猜」核心教學設計，代表 Source Master Contract 不完整。

## 核心金句

> 核心設計只做一次；不同平台只負責翻譯，不負責重新當老師。
