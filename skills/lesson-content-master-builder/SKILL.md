# V-MAX Lesson Content Master Builder

版本：1.0

## 目的
把已核准的教材定錨與教學分析整理成可被預習單、短文單、逐頁腳本、NotebookLM 與 Renderer 重複使用的內容母檔。

```yaml
skill_io_contract:
  can_run_standalone: true
  minimum_checkpoint: CP_TEACHING_ANALYSIS
  accepted_artifacts:
    - CP_SOURCE_ANCHOR
    - CP_TEACHING_ANALYSIS
  required_fields:
    - lesson_id
    - source_anchor
    - approved_teaching_analysis
  optional_fields:
    - idiom_expression_decision
    - teacher_added_notes
    - supplementary_frameworks
  produces_artifacts:
    - CP_LESSON_CONTENT_MASTER
  batch_capable: true
  may_recompute_upstream: false
```

## 母檔最低內容
- lesson metadata
- verified source text / paragraphs
- source characters / recognition-only characters
- approved shape-near / polyphonic / teacher-added writing focus
- vocabulary / sentence patterns / rhetoric with source evidence
- idioms and approved expression direction
- paragraph / structure / reading understanding
- teacher decisions and provenance
- downstream eligibility

## 規則
- 不重新分析已核准內容。
- 不補寫來源不存在的官方資訊。
- 缺少欄位只標記缺口，不重跑上游。
- Batch 時每課獨立產生母檔，禁止跨課污染。

## 核心金句
> 先把一課整理成可重用的內容母檔，後面的教材就不必一直重新讀教材。
