# V-MAX Project Status

```yaml
project:
  course_id: ""
  title: ""
  grade: ""
  semester: ""
  created_at: ""
  updated_at: ""

workflow:
  current_stage: project_initialized
  blocked: false
  blocked_reason: null
  next_skill: null

approvals:
  official_knowledge:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  lkb:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  learning_modules:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  teaching_strategy:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  role:
    status: pending
    approved_by: null
    approved_at: null
    role_id: null
  style:
    status: pending
    approved_by: null
    approved_at: null
    style_id: null
  output_profile:
    status: pending
    approved_by: null
    approved_at: null
    version: null
  final_review:
    status: pending
    approved_by: null
    approved_at: null

artifacts:
  official_knowledge: null
  teacher_knowledge: null
  source_map: null
  official_validation: null
  lkb: null
  lkb_validation: null
  learning_expansion: null
  teaching_strategy: null
  role_selection: null
  style_selection: null
  output_profile: null
  output_manifest: null

stale_artifacts: []
errors: []
history: []
```

## 狀態更新紀錄

每次狀態變更追加：

| 時間 | 原狀態 | 新狀態 | 執行技能 | 原因或核准紀錄 |
|---|---|---|---|---|
