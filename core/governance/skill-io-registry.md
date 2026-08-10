# V-MAX Skill I/O Registry 1.4

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
    role: CONTENT_SELECTION_AND_TASK_DESIGN
    can_run_standalone: true
    minimum_checkpoint: CP_PRESTUDY_INPUT
    accepted_artifacts: [CP_PRESTUDY_INPUT, CP_LESSON_CONTENT_MASTER, CP_TEACHING_ANALYSIS]
    produces_artifacts: [PRESTUDY_WORKSHEET_SOURCE, PRESTUDY_TEACHER_KEY]
    downstream_preferred_skill: vmax_chinese_preview_worksheet
    batch_capable: true
    may_recompute_upstream: false

  vmax_chinese_preview_worksheet:
    path: skills/vmax-chinese-preview-worksheet/SKILL.md
    role: VISUAL_RENDER_AND_PRINT_DELIVERY
    can_run_standalone: true
    minimum_checkpoint: PRESTUDY_WORKSHEET_SOURCE
    accepted_artifacts: [PRESTUDY_WORKSHEET_SOURCE]
    required_fields: [lesson_id, lesson_title, approved_worksheet_content, output_mode]
    produces_artifacts: [PRESTUDY_WORKSHEET_PNG, PRESTUDY_WORKSHEET_PDF, PRESTUDY_RENDER_VALIDATION, DRIVE_ARCHIVE_REPORT]
    output_modes: [A_CLEAR_FRAME, B_FREEHAND]
    batch_capable: true
    batch_semantics: QUEUE_MULTI_LESSON_RENDER_VALIDATE_ONE_BY_ONE
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
    accepted_artifacts: [CP_SOURCE_ANCHOR, CP_TEACHING_ANALYSIS, CP_LESSON_CONTENT_MASTER, CP_PRESTUDY_INPUT, CP_SLIDE_SCRIPT, CP_RENDER_READY, PRESTUDY_WORKSHEET_PNG, PRESTUDY_WORKSHEET_PDF, POSTLESSON_WRITING_WORKSHEET_OUTPUT, NOTEBOOKLM_SOURCE_MD, NOTEBOOKLM_INSTRUCTION_MD, INFOGRAPHIC_TEACHING_PDF]
    produces_artifacts: [DRIVE_ARCHIVE_REPORT]
    batch_capable: true
    may_recompute_upstream: false
```

## 預習單雙層分工

`prestudy-worksheet` 是內容層：決定題目、語文焦點、閱讀任務與教師答案，產出唯一正式 Renderer 輸入 `PRESTUDY_WORKSHEET_SOURCE`。

`vmax-chinese-preview-worksheet` 是 Renderer／交付層：**只接受已核准 `PRESTUDY_WORKSHEET_SOURCE`**，負責 A／B 視覺版本、300 dpi、3508×2480 px、4.5 mm 安全白邊、逐字校對、PNG／PDF 驗證與 Drive 交付，不得改寫上游教學內容。

標準鏈：

`CP_PRESTUDY_INPUT → prestudy-worksheet → PRESTUDY_WORKSHEET_SOURCE → vmax-chinese-preview-worksheet → PRESTUDY_WORKSHEET_PNG / PRESTUDY_WORKSHEET_PDF / PRESTUDY_RENDER_VALIDATION / DRIVE_ARCHIVE_REPORT`

`output_mode` 是 Renderer required field；合法值：`A_CLEAR_FRAME | B_FREEHAND`。不得同時維護 `visual_mode` 等第二套欄位名稱。

## Batch 共通規則
- 每課使用自己的 checkpoint，不混用教材內容。
- 一課缺欄位只阻塞該課。
- 可共用技能規則、版面家族、教師明確鎖定的跨課偏好。
- 不可共用生字、語詞、閱讀題、答案、Teacher Intent。
- 預習單 Renderer 的 batch 是「多課佇列、逐課渲染、逐課校字、逐課驗證」，不是一次生成未確認的多課畫面。

## User-facing Guide Synchronization

以下文件是本 Registry 的教師可讀鏡像：
- `docs/V-MAX_使用指南.md`
- `docs/V-MAX_中文指令速查表.md`
- `docs/V-MAX_跨平台安裝與執行指南.md`

若發生以下任一變更，修改者必須在同一變更批次檢查並同步更新教師指南：
- checkpoint / artifact 新增、刪除、更名、用途或 alias 改變
- `skill_io_contract` 的 minimum checkpoint、accepted artifacts、produced artifacts 改變
- standalone / batch capability 改變
- 新增、刪除或更名可直接呼叫技能
- Golden Path / Checkpoint Resume 的交界改變
- 使用者可直接要求的輸出格式改變
- 預習單內容層與 Renderer 層的責任邊界改變

**PR #3 當前狀態：`USER_GUIDE_SYNC_PASS`。**

三份指南已同步以下 Renderer 規則：
1. `PRESTUDY_WORKSHEET_SOURCE` 是 Renderer 唯一最低輸入。
2. Renderer required field 使用 `output_mode`，合法值 `A_CLEAR_FRAME | B_FREEHAND`。
3. Renderer 產出名稱統一為 `PRESTUDY_RENDER_VALIDATION`，Drive 成功歸檔後產出 `DRIVE_ARCHIVE_REPORT`。
4. PDF 共通規格引用 Core PDF Contract；worksheet skill 不維護第二套 canonical 壓縮規格。
5. AI 中文局部修復失敗時依 Core Renderer 使用 verified/native-text fallback。
6. Drive 實際 IDs 由 project/runtime artifact 或當次查詢注入，不硬編碼在 canonical Skill。

若後續任一 canonical 規則再變更而指南未同步，重新標記 `USER_GUIDE_STALE`。

## 核心金句
> Manifest 管誰是權威；I/O Registry 管積木怎麼接；使用指南把積木翻成老師自然會說的中文。
