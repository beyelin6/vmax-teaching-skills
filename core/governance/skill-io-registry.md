# V-MAX Skill I/O Registry 1.0

## 定位

本檔只管理「技能如何從 checkpoint / artifact 啟動、產出什麼、是否可批次」。
Manifest 繼續管理 canonical authority；本檔不得取代 Manifest。

核心原則：
> 已核准資料不重算；技能只吃自己真正需要的資料。

```yaml
skills:
  lesson_content_master_builder:
    path: skills/lesson-content-master-builder/SKILL.md
    can_run_standalone: true
    minimum_checkpoint: CP_TEACHING_ANALYSIS
    accepted_artifacts: [CP_SOURCE_ANCHOR, CP_TEACHING_ANALYSIS]
    produces_artifacts: [CP_LESSON_CONTENT_MASTER]
    batch_capable: true
    may_recompute_upstream: false

  prestudy_worksheet:
    path: skills/prestudy-worksheet/SKILL.md
    can_run_standalone: true
    minimum_checkpoint: CP_PRESTUDY_INPUT
    accepted_artifacts: [CP_PRESTUDY_INPUT, CP_LESSON_CONTENT_MASTER, CP_TEACHING_ANALYSIS]
    produces_artifacts: [PRESTUDY_WORKSHEET_SOURCE, PRESTUDY_WORKSHEET_OUTPUT]
    batch_capable: true
    may_recompute_upstream: false

  postlesson_short_writing_worksheet:
    path: skills/postlesson-short-writing-worksheet/SKILL.md
    can_run_standalone: true
    minimum_checkpoint: CP_LESSON_CONTENT_MASTER
    accepted_artifacts: [CP_LESSON_CONTENT_MASTER, CP_TEACHING_ANALYSIS, CP_PRESTUDY_INPUT]
    produces_artifacts: [POSTLESSON_WRITING_WORKSHEET_SOURCE, POSTLESSON_WRITING_WORKSHEET_OUTPUT]
    batch_capable: true
    may_recompute_upstream: false

  slide_script_generator:
    path: skills/slide-script-generator/SKILL.md
    can_run_standalone: true
    minimum_checkpoint: CP_LESSON_CONTENT_MASTER
    accepted_artifacts: [CP_LESSON_CONTENT_MASTER, CP_VISUAL_INTENT, CP_TEACHING_ANALYSIS]
    produces_artifacts: [CP_SLIDE_SCRIPT]
    batch_capable: true
    may_recompute_upstream: false

  notebooklm_renderer_script:
    path: skills/notebooklm-renderer-script/SKILL.md
    can_run_standalone: true
    minimum_checkpoint: CP_SLIDE_SCRIPT
    accepted_artifacts: [CP_SLIDE_SCRIPT, CP_VISUAL_INTENT, CP_RENDER_READY]
    produces_artifacts: [NOTEBOOKLM_SOURCE_MD, NOTEBOOKLM_INSTRUCTION_MD, RENDERER_DETAILED_SCRIPT_MD]
    batch_capable: true
    may_recompute_upstream: false

  infographic_pdf_lesson_deck:
    path: skills/infographic-pdf-lesson-deck/SKILL.md
    can_run_standalone: true
    minimum_checkpoint: CP_RENDER_READY
    accepted_artifacts: [CP_RENDER_READY, CP_SLIDE_SCRIPT, CP_VISUAL_INTENT]
    produces_artifacts: [INFOGRAPHIC_PAGE_PNGS, INFOGRAPHIC_TEACHING_PDF, PAGE_PREFLIGHT_REPORT]
    batch_capable: false
    may_recompute_upstream: false

  google_drive_lesson_archive:
    path: skills/google-drive-lesson-archive/SKILL.md
    can_run_standalone: true
    minimum_checkpoint: ANY_DELIVERABLE_READY
    accepted_artifacts: [CP_SOURCE_ANCHOR, CP_TEACHING_ANALYSIS, CP_LESSON_CONTENT_MASTER, CP_PRESTUDY_INPUT, CP_SLIDE_SCRIPT, CP_RENDER_READY, PRESTUDY_WORKSHEET_OUTPUT, POSTLESSON_WRITING_WORKSHEET_OUTPUT, NOTEBOOKLM_SOURCE_MD, NOTEBOOKLM_INSTRUCTION_MD, INFOGRAPHIC_TEACHING_PDF]
    produces_artifacts: [DRIVE_ARCHIVE_REPORT]
    batch_capable: true
    may_recompute_upstream: false
```

## Batch 共通規則
- 每課使用自己的 checkpoint，不混用教材內容。
- 一課缺欄位只阻塞該課。
- 可共用技能規則、版面家族、教師明確鎖定的跨課偏好。
- 不可共用生字、語詞、閱讀題、答案、Teacher Intent。

## 核心金句
> Manifest 管誰是權威；I/O Registry 管積木怎麼接。
