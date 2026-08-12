---
name: presentation-engine
description: V-MAX Output Mapping Helper。把 approved LKB、已鎖 Storyboard、Page Ledger、Experience refs、Style/Typography 與教師／學生分流轉成平台輸出來源。不得重新分析教材、重新決定頁數、Scenario、Character 或 Style；教學簡報正式視覺須服從 Gate B/C 與 Image-first Renderer。
---

# Presentation Engine

版本：0.2.0-compat

## Status
`OUTPUT_MAPPING_HELPER_NOT_PRESENTATION_WORKFLOW_AUTHORITY`

正式主流程與視覺 production 由：
- Main Workflow
- Golden Path Executor
- Page Ledger / Storyboard
- Style Recipe / Typography
- Image-first Renderer
- Gate C

控制。

---

## 1. Mission
Presentation Engine 只做：
- 選取
- 排序
- 教師／學生分流
- source-node mapping
- 平台輸出格式轉譯

不重新做課程設計。

---

## 2. Preconditions by Output Type

### NotebookLM / Curated Source
至少需要：
- approved LKB
- 已核准 Learning Expansion / Teacher Strategy（若要包含）
- 明確 output request

可在完整 slide production 前產生，但不得把未核准候選寫成教材真值。

### Slide Script / Teacher Notes / Student Slide Source
至少需要：
- approved LKB
- Teaching Skill Lock
- Experience locks
- Slide Architecture
- Budget Final / Page Ledger
- Storyboard / Gate B confirmed

### Final Visual Slide Package
Presentation Engine 不直接取代 Renderer；必須等 Style/Typography + Representative Visual + Gate C，再交 Image-first Renderer / platform adapter。

---

## 3. Source Authority

- Official / Teacher Knowledge → approved LKB
- Learning Expansion → approved expansion nodes
- Teaching sequence → locked Storyboard / Page Ledger
- Scenario → locked scenario ref
- Character → locked topology / cast / DNA refs
- Style → canonical Style Recipe ref
- Typography → Typography Lock

缺任何必要 source 時標 `missing_approved_source`，不得自行補造。

---

## 4. Forbidden Decisions

不得：
- 新增未核准成語、句型、修辭、知識
- 改寫課文原文／官方詞義
- 重新決定主旨、文體或段落結構
- 重新估頁數
- 重新選 Scenario / Character / Style
- 以 Layout Library 反推教學內容
- 在 Gate C 前宣告 final visual approved

---

## 5. Optional Outputs

依 request 產生一種或多種：
- `lesson_knowledge_book_reference`
- `curated_briefing`
- `notebooklm_source`
- `notebooklm_instruction`
- `teacher_markdown`
- `student_markdown`
- `slide_source`
- `slide_script`
- `speaker_notes`
- `worksheet_source`
- `assessment_source`
- `output_manifest`

不自動全產。

---

## 6. Slide Mapping Contract

每個 slide node 至少記錄：

```yaml
slide_id:
section:
lesson_stage:
cognitive_scene:
learning_gain:
teaching_skill: []
text_anchor:
student_visible_content:
teacher_notes:
source_nodes: []
experience_refs:
layout_intent:
illustration_requirement:
answer_visibility:
```

這些欄位必須引用已鎖 Page Ledger / Storyboard，不由 Presentation Engine 自己發明。

---

## 7. Teacher / Student Separation

學生可見輸出不得包含：答案、source metadata、internal IDs、教師講解提示、validation message。

教師輸出可保留：source nodes、答案、教學提示、差異化、speaker notes。

---

## 8. NotebookLM
NotebookLM 目前沿用 adapter / output contract。Presentation Engine 可整理 source / instruction，但：
- approved LKB 是唯一知識底座
- 不建立分叉 Source Truth
- 未來 Visual Source Pack / Audio Source Pack 規格另行討論，不阻塞 v1

---

## 9. Visual Mapping

- Style 只能引用 Style Recipe Families 已選結果。
- Character 只能引用 locked Character DNA。
- Typography 交 Typography Bridge。
- Final visual composition 交 Image-first Renderer。

Presentation Engine 可以寫 `visual_intent`，不能自行改畫風或角色身份。

---

## 10. Quality Checks

- source trace 完整
- student / teacher 分流正確
- slide order 與 Storyboard 一致
- page count 與 Page Ledger 一致
- locked Scenario / Character / Style 未漂移
- 未混入其他課次
- 未把未核准 Extension 當 Core

Failure codes：
`PRESENTATION_ENGINE_REDESIGNS_LESSON / PAGE_LEDGER_DRIFT / EXPERIENCE_LOCK_DRIFT / UNAPPROVED_SOURCE_IN_OUTPUT / GATE_C_BYPASS`

---

## 核心金句
> Presentation Engine 負責把已鎖設計翻譯成輸出，不再偷偷重新設計一課。
