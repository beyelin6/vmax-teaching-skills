# Back-to-School Fast Track

版本：0.1.0

## 適用情境

教師已接近開學，需要先產出可直接上課的教材，不希望因完整系統建置而延誤實際備課。

Fast Track 不是降低教材正確性，而是把選配成果延後，先完成最有教學價值的核心輸出。

## 四個必要確認點

### Gate 1｜教材內容確認

確認：

- 課文與段落
- 生字、認讀字與核心語詞
- 教材成語
- 多音字與形近字
- 修辭、句型與寫作特色
- 主旨、結構與教師手冊重點

### Gate 2｜課程骨架確認

確認：

- Lesson Flow
- 全文主架構 Macro
- 必要段落副架構 Micro
- 必教 Learning Modules
- 教材內容與 Bee 老師補充的分界

### Gate 3｜呈現設計確認

一次確認：

- 引導者與課文角色關係
- Theme 與 Visual DNA
- 核心 Layout
- 圖片式簡報輸出
- 金句與 Podcast 是否啟用

### Gate 4｜最終內容與成品確認

確認：

- 學生可見內容正確
- 教師答案分流
- 圖片符合句意
- 角色與風格一致
- NotebookLM 來源與生成指令完整
- Output Manifest 可追溯

## 必做成果

開學前每課優先完成：

```text
knowledge/
  01_official-knowledge.md
lkb/
  lesson-knowledge-book.md
planning/
  lesson-flow.md
  structure-profile.md
presentation/
  slide-script.md
  notebooklm-source.md
  notebooklm-generation-instructions.md
  visual-profile.md
  guide-character-profile.md
  quote-profile.md
teacher/
  teacher-notes.md
project/
  output-manifest.md
```

## 可延後成果

若時間不足，可在 Baseline 圖片式簡報完成後追加：

- 預習單
- 短文創作單
- 其他語文應用任務
- Podcast
- 平板互動
- 紙本替代活動
- 公開觀課版
- 補救與進階版本

延後項目必須記錄為 `planned_after_baseline`，不得假裝已完成。

## 簡報最小教學序列

```text
封面與任務
→ 全課導航
→ 分段理解
→ 必要字群／成語／修辭／句型
→ 課文統整
→ 今天帶走的一句話
→ 簡短評量
```

依課文內容刪減或擴充，不設固定頁數。

## Fast Track 完成狀態

當核心輸出完成並通過內容與視覺檢查，可標記：

```yaml
status: baseline_core_ready
remaining_optional_outputs:
  - ...
```

之後再逐項補齊完整 Baseline Package。
