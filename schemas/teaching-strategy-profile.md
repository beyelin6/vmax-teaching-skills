# Teaching Strategy Profile

版本：1.0.0

## 目的

將已選定的 Learning Modules 編排為實際課堂流程。此設定不修改教材知識，只決定教學順序、活動方式、時間與評量。

```yaml
teaching_strategy:
  lesson_duration_minutes: 40
  lesson_count: 1

  phases:
    - phase: motivation
      minutes: 5
      module_refs: []
      grouping: whole_class

    - phase: instruction
      minutes: 10
      module_refs: []
      grouping: whole_class

    - phase: guided_practice
      minutes: 10
      module_refs: []
      grouping: pairs

    - phase: independent_practice
      minutes: 10
      module_refs: []
      grouping: individual

    - phase: assessment
      minutes: 5
      module_refs: []
      grouping: individual

  differentiation:
    support_level: standard
    struggling_learners: true
    advanced_learners: false

  assessment:
    formative: true
    exit_ticket: true
    answers_location: teacher_only
```

## 可用階段

- `motivation`：引起動機
- `review`：複習先備知識
- `instruction`：教師講解與示範
- `guided_practice`：引導練習
- `collaborative_learning`：小組或同儕活動
- `independent_practice`：個別練習
- `application`：生活或寫作應用
- `assessment`：形成性評量
- `reflection`：反思與統整

## 編排規則

- 教學時間依課程實際需求動態設定。
- 不要求每課使用全部階段。
- 每個階段只能引用已建立的 Learning Module。
- 教材官方內容與延伸活動在畫面與講稿中要能區分。
- 學生評量頁不得顯示答案。
- 教師答案放於講者備註或教師專用輸出。
