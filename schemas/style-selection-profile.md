# Style Selection Profile

## 用途

記錄每課的風格推薦、教師選擇、角色搭配與動態適配規則。

```yaml
style_selection:
  status: pending_teacher_review
  lesson_id: ""
  selected_style_id: null
  selected_role_id: null
  mixed_style_ids: []

  recommendation_basis:
    genre: ""
    theme: ""
    emotional_tone: []
    grade: ""
    learning_modules: []
    teaching_modes: []
    required_visual_forms: []

  candidates:
    - style_id: ""
      name: ""
      rank: 1
      fit_reasons: []
      role_fit: ""
      visual_language: []
      palette: []
      background_material: []
      illustration_rules: []
      section_labels: []
      recommended_layouts: []
      suitable_slide_types: []
      limitations: []

  teacher_adjustments:
    palette_changes: []
    material_changes: []
    illustration_changes: []
    layout_changes: []
    role_changes: []
    forbidden_elements: []

  final_style:
    style_id: null
    name: ""
    version: ""
    palette: []
    background_material: []
    illustration_language: []
    section_label_system: []
    layout_ids: []
    role_integration_rules: []
    lesson_specific_adaptations: []
    presentation_canvas:
      aspect_ratio: "16:9"
      orientation: landscape

  approval:
    teacher_approved: false
    approved_at: null
    notes: []
```

## 狀態

- `pending_analysis`
- `pending_teacher_review`
- `approved`
- `needs_revision`

## 強制規則

- `selected_style_id` 不得在教師核准前自動填入。
- `lesson_specific_adaptations` 必須依本課內容重建。
- 混合風格時需指定主風格與輔助風格，不得把多套規則無限制堆疊。
- 角色辨識色只能作為輔助色，不得覆蓋教材主題色。
- 學生可見文字對比與字級優先於裝飾效果。
- 簡報風格的 `presentation_canvas` 固定為 `16:9` 橫式；不得以風格推薦改成其他比例。非簡報輸出依自己的 Output Profile。
