# V-MAX Teacher Review View Contract 1.1

## 定位

本契約定義 ChatGPT、Codex、Gemini 與其他執行器在教師需要閱讀、核准或修正時的共同顯示層。完整 JSON／YAML／schema 是 Machine Payload；Teacher Review View 是人類決策介面，兩者必須分開。

核心原則：

> 先讓老師看懂結論、證據、缺口與這次唯一決定，再把完整結構化資料留給系統。

## A. 雙層輸出

每個正式 stage 可同時產生：

1. `Machine Payload`：完整、可續跑、可回寫的結構化母檔，保存於指定 artifact／Drive 文件。
2. `Teacher Review View`：對話中預設顯示的教師審核卡。

除非教師明確要求查看 JSON／YAML 或正在除錯 schema，對話不得展開完整 Machine Payload。不得把程式欄位名稱、內部狀態欄位、巢狀陣列、大段 code block 或空白程式碼框當作審核卡。需要另存 JSON／YAML 時才產生檔案，對話只提供檔名或連結。

## B. 審核卡固定順序

```text
{目前階段}｜{這次確認主題}

結論摘要（3–7 點）
教材證據／判讀依據
知識層標記
缺口、衝突或風險
AI 建議與理由
本次只需決定
⏸ {目前 HOLD}｜確認後唯一下一步：{合法下一階段}
```

- 第一屏先出現結論與阻塞狀態，不先貼資料表。
- 長清單只顯示教師判斷所需的分組摘要；完整內容保存於母檔並提供路徑或名稱。
- 不得為了縮短畫面刪除教材內容；只調整顯示層級。
- 教師可要求「展開證據」「查看完整母檔」「顯示 JSON」。

## C. 知識層標記

教師畫面中的重要項目必須標示至少一種：

- `[教材明載]`：有教材來源與頁碼／區塊。
- `[教師補充]`：來自教師明確決定。
- `[AI 延伸]`：教學建議，不是教材事實。
- `[待核對]`：來源不足、OCR 不確定或來源衝突。

字典、網頁或一般常識只能支援讀音、詞義等外部查核；不能因此把項目標成教材明載。

## D. 來源狀態標示

教師審核表中的每個字、詞、讀音、例詞、口訣或教材焦點，至少標示一個可見狀態：

- `[教材已確認]`：課本／教冊的本課來源與頁碼或區塊已核對。
- `[教育部辭典已核對]`：讀音、詞義或例詞已逐項由教育部辭典核對；這不等於教材收錄。
- `[AI 建議，待教師確認]`：教學延伸候選，尚未成為 locked decision。
- `[尚待教材來源核對]`：教材身分、課內讀音或來源仍不完整。

可同時顯示兩個狀態，例如 `[教材已確認] [教育部辭典已核對]`。未完成教材來源核對的項目不得使用「已鎖定／教材正式內容／確認完成」等字樣。

## E. STEP 1 完整性阻擋

若完整正式生字、認讀字雙來源、教材詞語聯集、課文結構或 provenance 等必要來源仍未核對：

- 顯示 `STEP1_INCOMPLETE`。
- 清楚列出已完成與缺少部分。
- 本輪只要求補來源或處理衝突，不得要求教師核准完整 STEP 1。
- 不得進入 STEP 2、STEP 2.5 或任何設計階段。

STEP 1 不得出現 Mode、Scenario、角色、視覺、頁數、固定每段教學迴圈或已鎖定的教學主軸。

## F. 階段與下一步

前段合法鏈固定為：

```text
STEP 1 → HOLD 1 → STEP 2 → HOLD 2 → STEP 2.5 → HOLD 2.5 → STEP 2.6 → HOLD 2.6 → Teacher Intent Lock
```

- `STEP 2.75` 不存在，出現即標記 `LEGACY_STAGE_ALIAS`。
- 教師一次「確認」只解鎖一個正式 stage，完成後停在緊接的 HOLD。
- 審核卡最後只能列一個 `next_allowed_stage`，且須與 Runtime State 一致。

## G. STEP 2.5 停等畫面

STEP 2.5 完成後只呈現：

1. 形近字審核表。
2. 多音字審核表。
3. 教材詞語／成語候選審核表。
4. 尚待來源核對或教師決定的項目。
5. `⏸ HOLD 2.5｜請回覆「確認」或指出要修改的項目；確認後唯一下一步為 STEP 2.6。`

審核表建議欄位：`項目｜來源狀態｜教材證據｜字形／讀音核對｜AI 建議與理由｜教師決定`。不得在同一回覆展開詩節教學、宣布新階段或預告 `STEP 2.75`。

## H. 不合格條件

任一成立即不得前進：

- `RAW_SCHEMA_DUMP`
- `TEACHER_INTERFACE_OVERLOAD`
- `SOURCE_ANCHOR_INCOMPLETE`
- `KNOWLEDGE_LAYER_MIXED`
- `PREMATURE_DESIGN_LOCK`
- `TEMPLATE_FLATTENING`
- `STAGE_LEAP / SKIPPED_HOLD`
- `LEGACY_STAGE_ALIAS`
- `WRONG_NEXT_STAGE_POINTER`

## I. 最小完成紀錄

```yaml
teacher_review_view:
  stage:
  hold:
  machine_payload_path:
  summary_rendered: true
  source_evidence_rendered: true
  knowledge_layers_labeled: true
  gaps_rendered: true
  decision_scope_single: true
  next_stage_pointer_valid: true
  raw_payload_hidden_by_default: true
  internal_state_fields_hidden: true
  source_status_visible: true
  unverified_items_not_locked: true
  status: PASS | BLOCKED
  failure_codes: []
```

## 核心金句

> 母檔要完整；畫面要好讀；教師一次只決定一件事。
