# V-MAX Character Teaching Regression Cases 1.3

## 用途

防止三、四年級生字教學再次從「形近字＋多音字」擴張成 AI 自動逐字深教。

---

## CASE C-01｜生字表不等於生字教學清單

### PASS
- 教材正式生字完整保留於 Source / 基礎識寫層。
- AI 不逐字建立獨立生字教學頁。
- 一般生字預設為 `BASIC_LITERACY_ONLY`。

### BLOCKER
- 因教材列為正式生字就自動獨立成頁。
- 每個生字固定套字義／字源／部件／造詞／遊戲。

---

## CASE C-02｜AI 主動深教只有形近字與多音字

### PASS
AI 可主動推薦的生字深教入口只有：
- `SHAPE_NEAR`
- `POLYPHONIC`

### BLOCKER
- AI 以「容易寫錯」自動建立單字深教頁。
- AI 以「字形複雜、字源有趣、評量重要、語義特殊」自動建立單字深教頁。

### 預期分類
`CHARACTER_SCOPE_EXPANSION`

---

## CASE C-03｜單一生字詳解必須由教師指定

### PASS
若教師明確指定某字需要額外講解，可標記：

`TEACHER_ADDED_SINGLE_CHARACTER`

並依教師需求處理字義、字源／構形、部件、易錯點、筆順、造詞或課文特殊語意。

### BLOCKER
- 沒有教師明確指定卻產生單字詳解頁。
- AI 提醒某字可能難寫後，直接視為已確認深教。

### 預期分類
`SINGLE_CHARACTER_WITHOUT_TEACHER_OVERRIDE`

---

## CASE C-04｜易錯字不是第三個 AI 自動入口

### PASS
AI 若發現某正式生字可能容易寫錯，只能提出：

`AI_SUGGESTION_SINGLE_CHARACTER`

教師確認後才轉為：

`TEACHER_ADDED_SINGLE_CHARACTER`

### BLOCKER
- `ERROR_PRONE_WRITING` 被當成與形近字、多音字並列的 AI 自動深教類別。

---

## CASE C-05｜多音字來源仍受 Polyphonic Source Policy 控制

### PASS
- 教材明列 → `TEXTBOOK_POLYPHONIC`
- AI 推薦 → 只能從本課正式生字
- 教師指定 → `TEACHER_ADDED_POLYPHONIC`
- 形近補充字即使有多音，不可因 AI 自動升級

## CASE C-06｜字形口訣不得為押韻犧牲正確性

### PASS
- 部首、偏旁、部件與筆畫位置逐字核對。
- 口訣標示為 AI 建議並等待教師確認。
- 有疑點時停在當前 STEP。

### BLOCKER
- 為押韻編造錯誤部首、構形或字義關係。
- 未核對就將口訣標成已確認。

分類：`CHARACTER_FORM_UNVERIFIED / MNEMONIC_ACCURACY_RISK`

## CASE C-07｜多音字例詞必須逐詞核對

### PASS
- 課本生字欄／課文注音是本課讀音第一來源。
- 教育部《國語辭典簡編本》補充驗證各讀音、詞義與每一個例詞。
- 每個例詞留下獨立核對紀錄。

### BLOCKER
- 只查單字後自行類推例詞讀音。
- 教材與辭典衝突仍自行選一邊。
- 未核對例詞卻標成已鎖定。

分類：`PRONUNCIATION_SOURCE_CONFLICT / EXAMPLE_WORD_UNVERIFIED / PRONUNCIATION_INFERENCE_DRIFT`

## CASE C-08｜教材未列讀音不得由 AI 自行擴張

### PASS
- 先以教冊／課本生字欄／課文注音確認本課正式讀音集合與呈現列數。
- AI 發現教材未列的其他讀音時，只能列為 `AI_SUGGESTED_READING` 延伸候選。
- 延伸候選必須以教育部《國語辭典簡編本》或指定權威來源驗證，並標示「教材未列／待教師確認」。
- 延伸候選必須出現在教師確認單，附上來源證據與 `downstream_impact`。
- 未經教師確認，不得放入正式多音字列數、預習單、簡報或學生可見頁面。

### BLOCKER
- AI 只因模型記憶或查到字典，就把教材列兩個讀音的多音字直接做成三列。
- AI 用字典的完整讀音清單取代本課教冊標示。
- 未查證教材來源就把新增讀音標為 `CONFIRMED / LOCKED`。
- 教材與字典數量或讀法不一致時，AI 自行選擇其中一方繼續生成。

分類：`UNVERIFIED_AI_READING_EXPANSION / PRONUNCIATION_SOURCE_CONFLICT`

## CASE C-09｜多音字讀音證據必須可追溯

### PASS
- 每個讀音保存來源檔名、PDF 頁碼、印刷頁碼、區塊、擷取原文、擷取方式、信心等級與核對狀態。
- 預習單、簡報腳本與學生頁引用既有 evidence，不因下游製作重新掃描整份 PDF。

### BLOCKER
- 只保存「來自教冊」而沒有頁碼、區塊或原文。
- 讀音進入正式輸出前沒有 `verification_status`。
- 下游找不到證據就自行重建或猜測讀音。

分類：`PRONUNCIATION_EVIDENCE_MISSING / SOURCE_TRACEABILITY_FAIL`

---

## 整體 PASS

```yaml
character_teaching_regression:
  source_characters_complete: PASS
  ai_deep_focus_only_shape_near_polyphonic: PASS
  single_character_requires_teacher: PASS
  error_prone_not_auto_entry: PASS
  polyphonic_source_gate_preserved: PASS
  textbook_reading_count_not_expanded: PASS
  pronunciation_evidence_traceable: PASS
  character_form_verified: PASS
  mnemonic_accuracy_verified: PASS
  example_words_individually_verified: PASS
```

只要其中一項 FAIL，不得宣告生字教學規則通過。

---

## 核心金句

> 生字表 ≠ 生字教學清單。

> AI 主動教形近字與多音字；單一生字詳解由老師指定。
