# V-MAX Output Profile

每一課可透過設定檔選擇輸出格式，不需修改 Skill 本體。

## 可選格式

```yaml
output_profile:
  formats:
    - lesson_knowledge_book
    - curated_briefing
    - notebooklm_source
    - teacher_markdown
    - student_markdown
    - slide_source
    - worksheet_source
    - assessment_source
  language: zh-TW
  include_source_metadata: true
  include_teacher_answers: true
  include_system_extensions: true
  include_idiom_teaching: true
```

## 格式說明

- `lesson_knowledge_book`：完整 LKB 主書。
- `curated_briefing`：接近 NotebookLM Curated Briefing 的連續結構化 MD。
- `notebooklm_source`：刪除過多內部欄位、保留完整知識內容的 NotebookLM 來源檔。
- `teacher_markdown`：保留答案、教學引導、來源與備課提示。
- `student_markdown`：移除教師答案與內部標記。
- `slide_source`：提供簡報技能使用的頁面內容來源。
- `worksheet_source`：提供預習單、學習單或仿作單使用。
- `assessment_source`：題目、評量規準與教師答案分流。

## 原則

1. LKB 是唯一知識來源。
2. 所有格式均由同一版 LKB 派生。
3. 修改知識時先修改 LKB，再重新輸出。
4. 不同格式不得各自保存互相矛盾的教材內容。
5. 教師答案在學生版中必須移除。
