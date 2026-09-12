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
      aspect_ratio: null  # 僅承接教師核准的 canvas_lock；允許值為 "4:3" 或 "16:9"
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

## 教師選擇時點

完成 Lesson Map、Session Map、角色／引導角色候選、Visual Grammar 與 Slide Architecture 後，才進入風格選擇確認。系統此時依本課教材與教學需求提出 **3–5 種風格庫方案**，可包含單一風格與依頁面類型混搭方案，並說明主風格、可用頁型變體、共同字體／畫布／留白與限制。

教師在此 HOLD 選擇主風格、頁型混搭、風格庫中的其他 `style_id`，或要求重新推薦。教師選擇前不得建立代表頁、PAGE_DETAIL_CONFIRMATION、正式 Slide Script 或 Renderer 批次。

## 強制規則

- `selected_style_id` 不得在教師核准前自動填入。
- 系統只能推薦 3–5 組候選或混搭方案；推薦不等於選定，Renderer 不得替教師決定。
- 批次施工只能消費 `status: approved`／機器檔 `status: CONFIRMED` 且 `teacher_confirmation_status: CONFIRMED` 的 Style Selection Profile。
- `lesson_specific_adaptations` 必須依本課內容重建。
- 混合風格時需指定主風格與輔助風格，不得把多套規則無限制堆疊。
- 角色辨識色只能作為輔助色，不得覆蓋教材主題色。
- 學生可見文字對比與字級優先於裝飾效果。
- 簡報風格的 `presentation_canvas` 必須承接教師核准的 `canvas_lock`，僅允許 `4:3` 或 `16:9` 橫式；不得由風格推薦自行選擇、切換或改成其他比例。非簡報輸出依自己的 Output Profile。
