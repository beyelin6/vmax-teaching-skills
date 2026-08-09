# V-MAX NotebookLM / Renderer Script Skill

版本：1.0

## 目的
把已核准的逐頁腳本轉成 NotebookLM 可讀的來源 MD、生成指令 MD 與 Renderer 詳細腳本，不重跑教材分析。

```yaml
skill_io_contract:
  can_run_standalone: true
  minimum_checkpoint: CP_SLIDE_SCRIPT
  accepted_artifacts:
    - CP_SLIDE_SCRIPT
    - CP_VISUAL_INTENT
    - CP_RENDER_READY
  required_fields:
    - lesson_id
    - slide_script
  optional_fields:
    - visual_intent
    - character_dna
    - style_recipe
    - gold_page_patterns
  produces_artifacts:
    - NOTEBOOKLM_SOURCE_MD
    - NOTEBOOKLM_INSTRUCTION_MD
    - RENDERER_DETAILED_SCRIPT_MD
  batch_capable: true
  may_recompute_upstream: false
```

## 輸出分工
- `NOTEBOOKLM_SOURCE_MD`：完整內容、逐頁教學資訊、來源證據與必要教師資料。
- `NOTEBOOKLM_INSTRUCTION_MD`：只保留生成操作、視覺、學生／教師分流與輸出限制，不重貼完整教材。
- `RENDERER_DETAILED_SCRIPT_MD`：逐頁 `primary_grammar / primary_pattern / first_focus / discovery_relation / visual_evidence / text_integration_plan / character refs / style refs`。

## 規則
- NotebookLM 不依賴 YAML 副檔名；需要結構資料時以 Markdown code block 保存。
- 不建立重複 `slides` 節點。
- 角色 DNA 變數不得未替換。
- 若逐頁腳本缺少 Gold Pattern 或文字真值，只標記缺口，不重跑上游。
- Batch 時每課輸出獨立檔案，不混用來源。

## 核心金句
> 同一份已核准逐頁腳本，可以換平台，不需要重新做一次教學設計。
