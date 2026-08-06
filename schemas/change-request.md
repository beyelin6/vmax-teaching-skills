# V-MAX Change Request

版本：0.1.0

## 目的

將教師的自然語言修改需求轉成跨平台、可追蹤、可驗證的教材修改單。教師不需要指定技術檔案或頁面路徑，只需描述學生反應與想調整的方向。

## 標準格式

```yaml
change_request:
  id: CR-{日期}-{流水號}
  lesson_id:
  requested_by: teacher
  requested_at:

  observation:
    student_response:
    identified_need:
    urgency: normal | before_next_class | immediate

  based_on:
    baseline_version:
    classroom_variant:
    applied_patch_ids: []

  requests:
    - target:
      operation: add | replace | remove | simplify | deepen | reflow | regenerate
      component:
      instruction:
      source_type: official | teacher_supplement | learning_expansion

  constraints:
    preserve_official_content: true
    preserve_theme: true
    preserve_visual_dna: true
    preserve_guide_character_dna: true
    preserve_approved_learning_flow: true
    student_answers_hidden: true

  output_scope:
    slide_script: auto
    rendered_deck: auto
    teacher_notes: auto
    notebooklm_source: auto
    notebooklm_instructions: auto
    worksheet: auto
    podcast: auto
    tablet_activity: auto

  impact_analysis:
    lkb_changed: false
    learning_modules_changed: false
    teaching_flow_changed: false
    structure_changed: false
    role_changed: false
    style_changed: false
    outputs_to_regenerate: []

  approval:
    scope_status: pending
    final_status: pending
```

## 自然語言範例

教師輸入：

> 第三段太難，學生搞不懂原因和結果。增加一頁三格圖解，把問題改成填空；維持原本自然探險風。Podcast 多加一個生活例子。

轉換結果：

```yaml
requests:
  - target: paragraph_3
    operation: add
    component: three_panel_cause_effect_visual
    instruction: 用三格情境圖呈現原因、行動與結果
    source_type: learning_expansion

  - target: paragraph_3_comprehension
    operation: simplify
    component: question
    instruction: 將開放題改為具提示的段落大意填空
    source_type: learning_expansion

  - target: audio.lesson_preview.paragraph_3
    operation: add
    component: life_example
    instruction: 增加一個四年級學生熟悉的生活因果例子
    source_type: learning_expansion

constraints:
  preserve_theme: true
  preserve_visual_dna: true
```

## 判斷規則

### 必須回到 Official Knowledge／LKB

- 課文、字詞、成語、修辭或句型轉錄有誤。
- 教師手冊內容漏列。
- 出版社教材改版。

### 適合建立 Adaptive Patch

- 增加圖解、提示、生活例子或補充練習。
- 新增 Bee 老師補充形近字或成語。
- 調整問題難度。
- 新增 Podcast 或平板活動。

### 適合建立 Classroom Variant

- 縮短或延長教學時間。
- 改成高互動、公開觀課、補救或進階版本。
- 本班不使用平板。

## 自動同步原則

Agent 必須先做影響分析，不得無條件重跑全部成果。

例如新增一頁段落圖解，通常需要更新：

- Slide Script
- NotebookLM Source 或生成指令
- 教師備註
- Rendered Deck
- Output Manifest

若不影響預習單、短文單或 LKB，則不得強制重建。

## 教師確認

緊急修改可先提供簡短摘要：

```text
將修改：第三段圖解、問題難度、Podcast 生活例子。
不修改：官方教材、字群、成語、全課 Theme。
需重生：3 張簡報頁與 1 段音訊。
```

教師核准範圍後再執行正式修改。
