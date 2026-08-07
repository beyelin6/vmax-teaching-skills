# V-MAX Micro-Regeneration / Adaptive Patch Core

> 來源：Omni Architect 單頁重繪引擎
> 狀態：Bee Original／升級為平台中立 Patch 規格

## 核心理念

局部問題應局部修正，不因一頁、一道題或一個圖像不理想就重做整套教材。

## 舊系統已具備的能力

- 修改 `displayText`
- 修改 `guideTalk`
- 保留 `layout`
- 保留 `lens`
- NotebookLM 單頁 Precision Revise

## 新版標準 Patch Operation

```yaml
patch:
  target:
    lesson_id: ""
    component_id: ""
    slide_id: ""
  reason: ""
  operations:
    - simplify_text
    - simplify_question
    - add_scaffold
    - add_visual_explanation
    - replace_visual
    - revise_guide_talk
    - add_slide
    - remove_slide
    - reflow
  preserve:
    official_knowledge: true
    theme: true
    character_dna: true
    layout: optional
    structure: optional
  regenerate:
    only_affected_outputs: true
```

## 自然語言例子

> 第三段學生看不懂，增加三格圖片整理，問題改成填空；維持原本自然探險風和 Bee 老師角色。

應解析為：

- `target = paragraph_3`
- `add_visual_explanation = three_panel`
- `simplify_question = fill_in_blank`
- `preserve.theme = true`
- `preserve.character_dna = true`
- 只讓受影響簡報頁與相關教師備註 stale

## 影響分析原則

1. 改文字但不改知識：不回溯 LKB。
2. 改圖片：通常只重生該頁視覺。
3. 改問題難度：同步教師答案／評量規準。
4. 新增教學模組：檢查 Teaching Flow 與時間。
5. 改官方知識：不是 Patch，必須回到 LKB 上游。
6. Classroom Variant 的 Patch 不覆蓋 Baseline。

## Visual Evolvability

Patch 後新增或替換的頁面必須維持：

- Theme World
- Art Style
- UI Language
- Character / Host DNA
- 字級與資訊密度原則
- 圖像語意對位

目標不是只「改對」，而是讓修改後的內容看起來原本就屬於這套教材。
