---
name: slide-script-generator
description: 從已核准的內容母檔與視覺意圖直接建立逐頁教學腳本。當已有 CP_LESSON_CONTENT_MASTER 或相容 artifact，且需要單課或批次產生 CP_SLIDE_SCRIPT、不中途重跑教材分析時使用。
---

# V-MAX Slide Script Generator

版本：1.0

## 目的
從已核准的內容母檔與視覺意圖直接建立逐頁教學腳本，不要求重跑教材分析。

```yaml
skill_io_contract:
  can_run_standalone: true
  minimum_checkpoint: CP_LESSON_CONTENT_MASTER
  accepted_artifacts:
    - CP_LESSON_CONTENT_MASTER
    - CP_VISUAL_INTENT
    - CP_TEACHING_ANALYSIS
  required_fields:
    - lesson_id
    - lesson_content_master
    - teacher_intent
  optional_fields:
    - lesson_map
    - session_map
    - scenario_wrapper
    - character_topology
    - visual_style
  produces_artifacts:
    - CP_SLIDE_SCRIPT
  batch_capable: true
  may_recompute_upstream: false
```

## 每頁最低欄位
- slide_id
- lesson_stage
- source_nodes
- student_visible_content
- teacher_notes
- primary_grammar
- primary_pattern
- first_focus
- discovery_relation
- visual_evidence
- visual_sequence
- text_integration_plan
- answer_visibility

## 規則
- 原文、語詞、句型、修辭、成語必須追溯到內容母檔。
- Visual Grammar → Gold Page Pattern → Visual Sequence，不得直接退化成固定版型。
- 若 CP_VISUAL_INTENT 尚未存在，可只建立內容腳本草稿並標記 `VISUAL_INTENT_REQUIRED`；不得自行偽造已核准視覺決策。
- Batch 可一次產多課腳本，但每課獨立驗證與命名。

## 核心金句
> 逐頁腳本是可重用的中間產物，不是一定要在同一個對話裡接著做完簡報。
