# V-MAX Workflow Gates

## Gate 1：Official Knowledge Review

必要檔案：

- `knowledge/01_official-knowledge.md`
- `knowledge/source-map.md`
- `knowledge/official-knowledge-validation.md`

必須確認：

- 課文完整
- 生字與認讀字分流
- 全部核心詞語完整
- 官方成語名稱、詞義與例句完整
- 官方修辭、句型與寫作特色完整
- 習作、閱讀理解、答案與教學引導完整
- 未混入教師補充或系統延伸

核准結果：`approved_official_knowledge`

## Gate 2：LKB Review

必要檔案：

- `lkb/{課次}_{課名}_lesson-knowledge-book.md`
- `lkb/lkb-validation-report.md`

必須確認：

- 重複知識已整合
- 所有節點可追溯來源
- 官方原文沒有被改寫
- Teacher Knowledge 清楚分流
- 尚未提前產生學習延伸或教學策略

核准結果：`approved_lkb`

## Gate 3：Learning Modules Review

必要檔案：

- `knowledge/03_learning-expansion.md`

必須確認：

- 模組只掛載已核准的 LKB 節點
- 成語延伸只針對來源教材中的成語
- 易誤用、近義辨析與情境練習標示為學習延伸
- 未把延伸成語混入官方成語清單

核准結果：`approved_learning_modules`

## Gate 4：Teaching Strategy Review

必要檔案：

- `knowledge/04_teaching-strategy.md`

必須確認：

- 課節與時間合理
- 活動對應 LKB 與 Learning Modules
- 每節有檢核方式
- 教材內容未被策略層改寫

核准結果：`approved_teaching_strategy`

## Gate 5：Role Review

必要檔案：

- `project/role-selection-profile.md`

必須確認：

- 角色依教材內容推薦
- Bee 老師列為可選方案
- 角色功能、語氣與出現頻率明確
- 教師已選定唯一主引導角色或決定不使用角色

核准結果：`approved_role`

## Gate 6：Style Review

必要檔案：

- `project/style-selection-profile.md`

必須確認：

- 風格符合教材、年級與角色
- 配色、插圖、材質與版型方向明確
- 教師已選定最終風格或混合方案

核准結果：`approved_style`

## Gate 7：Output Profile Review

必要檔案：

- `project/output-profile.md`

必須確認：

- 輸出格式
- 教師版／學生版分流
- 答案位置
- NotebookLM、簡報、學習單與評量選項

核准結果：`approved_output_profile`

## Gate 8：Final Review

必要檔案：

- 所有已選輸出
- `output/output-manifest.md`
- 最終驗證報告

必須確認：

- 所有輸出可追溯版本
- 學生版無答案外洩
- 無未替換變數
- 無重複 slides 節點
- 角色與風格一致
- 未混入其他課次內容

核准結果：`completed`
