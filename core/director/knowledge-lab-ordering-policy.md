# V-MAX Knowledge Lab Ordering Policy 1.6

## 定位

本政策定義閱讀課中獨立 Knowledge Lab 與 `STEP 2.5 語文輻射` 的排序、分組、教師確認、AI 教學價值判讀，以及「課前預習單語文選擇」原則。

Knowledge Lab 不是附錄，也不是把所有字詞逐項講完；它只處理需要獨立建立辨識、比較、語意或遷移關係的內容。

核心原則：

> 先忠實讀取教材已提供的知識項目，再完成形近字／多音字的語文分析，再由 AI 做「教學價值判讀」，最後由教師篩選、替換與補充深教範圍。

> STEP 2.5 不只決定正式教學內容，也要同步決定哪些形近字／多音字值得先進入預習單。

> 預習單可以精選，正式教學不能被預習單的容量上限反向裁切。

> 教材原有 ≠ 一定深教；AI 推薦 ≠ 已決定。

> STEP 2.5 首要輸出是「教師可讀、可快速決策的分析推薦卡」，機器 JSON 只屬資料層，不得取代教師介面。

---

## A. 預設內容範圍

Knowledge Lab 原則上處理：

- 生字
- 形近字／字群
- 多音字
- 成語

語詞不列為固定 Knowledge Lab 項目。語詞跟著課文處理，而且只教教師選定或確認的重點語詞。

正式教學層可整理為：

- `CORE`：配合課文理解／生字辨析正式處理
- `FLEX`：可短處理、可依班級時間調整
- `BONUS`：學生自選挑戰／延伸，不要求全部完成
- `LOW_PRIORITY`：教學價值較低或疑似雞肋，可由教師刪除

這些層級屬 AI 判讀與教學調度，不是教材來源標籤。

### A1. 生字完整性

- 教材正式生字必須全部保留在本課資料層與正式教學規劃中。
- 不因預習單容量、頁數、Renderer 或「3–5 組」規則刪減教材生字。
- 並非每個生字都需要做完整形近字深究，但每個教材生字都必須有其應有的識寫／形音義教學位置。
- 形近字深教數量由實際教學價值決定，不設固定 `3–5 組` 上限。
- 多音字若屬教材正式學習內容，亦不受預習單 `3–5 組` 限制。

核心：

> 「3–5 組」是預習單的精選容量，不是簡報的教學上限。

---

## B. 教材優先與教師篩選流程

生成 Knowledge Lab 前，系統先從教材／結構化轉錄來源完整讀取：

- 本課完整生字清單
- 教材已列出的形近字／字形辨析
- 本課多音字
- 教材已列出的成語
- 同冊前課已確認的預習單形近字／多音字覆蓋紀錄

接著必須將四個層次分開呈現：

### B1. 教材原有
忠實列出來源，不因 AI 判斷而靜默刪除。

### B2. 形近字／多音字語文分析
先整理可供教師判斷與後續教材生成的語文資料，不得直接跳到推薦結論。

### B3. AI 教學價值判讀
對每一個「形近字群／多音字／成語／其他語文活動」提供：

- `recommendation_index`：1–5
- `recommendation_level`
- `reason`：具體理由
- `suggested_action`：深教／短辨析／Bonus／低優先

### B4. 預習單選擇判讀
只對需要進預習單容量判斷的形近字群與多音字額外提供：

- `prestudy_recommendation`
- `volume_duplication_status`
- `volume_history`
- `prestudy_reason`

AI 必須主動判斷「值不值得先放進預習單」以及「同一冊是否已正式出現過」，不把查重工作交給教師。

---

## C. 形近字分析整理｜Shape-near Analysis

形近字分析是 STEP 2.5 的必經資料層與教師可見資訊，不得因為新增推薦指數、快速決策代號或預習單判讀而消失。

### C1. 每一組至少包含

- `target_character`：本課目標生字
- `target_zhuyin`
- `target_radical`
- `comparison_characters`：比較字群
- 每個比較字的 `zhuyin`
- 每個比較字的 `radical`
- `common_words`：常用詞／教材可理解詞語
- `core_meaning`：學生可理解的核心字義
- `component_analysis`：共同部件與差異部件
- `confusion_point`：學生容易混淆的位置
- `discrimination_cue`：如何辨認
- `mnemonic`：可用則提供簡短記憶提示；不可硬湊

### C2. 顯示原則

教師端不需要看到冗長字典式資料，但必須能看出「為什麼這些字值得放在一起比較」。

建議格式：

```text
01｜泳／永／詠

分析整理：
- 泳 ㄩㄥˇ｜水部｜游泳、泳池｜在水中游動。
- 永 ㄩㄥˇ｜水部｜永遠、永久｜長久、持續。
- 詠 ㄩㄥˇ｜言部｜歌詠、吟詠｜用詩文或聲音吟唱。

構形辨析：三字共享「永」的字形核心；「泳」加水部連結水中活動，「詠」加言部連結吟唱。
易混淆點：三字同音且外形接近，學生容易只憑右半部認字。
辨認提示：先看部首，再連到字義。
記憶提示：水中游泳，言語歌詠。

★★★★★ 5/5｜強烈推薦
理由：本課生字直接相關，同音形近，部首與語意又能形成清楚辨析。
教學建議：A 深教｜CORE
預習單：P1 預習核心
冊內紀錄：本冊尚未出現
```

### C3. 禁止

- 只列 `泳／永／詠｜5/5｜A` 而省略分析。
- 只列部首與例詞，卻沒有說明共同部件、差異部件與混淆點。
- 為了縮短 Teacher Selection Card，把分析全部藏進 machine JSON。
- 用不可靠的自造字源／牽強聯想取代真正的構形辨析。
- 把記憶提示當作正式字源解釋。

---

## D. 推薦指數｜Recommendation Index

`STEP 2.5 語文輻射` 中，推薦指數為必填欄位，不得省略。

### 量尺

- `5｜強烈推薦`：與本課課文、學生高混淆點、考評或高遷移價值高度相關，值得正式深教。
- `4｜推薦`：有明確辨析／理解價值，適合核心或短辨析。
- `3｜可選`：有學習價值，但非本課必要，可依班級／時間處理。
- `2｜低優先`：來源雖有，但教學增益有限，適合 Bonus 或簡短帶過。
- `1｜疑似雞肋`：與本課理解、常見錯誤或遷移關聯弱，AI 應主動提醒教師可刪除。

### 指數判斷至少考慮

```yaml
recommendation_dimensions:
  text_relevance: 0-2
  confusion_risk: 0-2
  transfer_value: 0-2
  assessment_value: 0-1
  cognitive_cost: 0 to -2
  redundancy_penalty: 0 to -1
```

最終不需要把計分細節全部展示給教師；教師端需看到 `1–5 + 具體理由`。

### 禁止

- 因教材有列就全部給 4–5。
- 因被分到 `CORE` 就不顯示推薦指數。
- 因被分到 `BONUS` 就不做價值判讀。
- 用推薦指數取代 Teacher Decision。

---

## E. 快速教師決策代號｜Decision Codes

### 教學決策

- `A｜深教`
- `B｜短辨析`
- `C｜Bonus`
- `D｜刪除`
- `E｜調整`

### 預習單決策

- `P1｜預習核心`
- `P2｜預習短看`
- `P3｜本課不放`
- `PX｜冊內已出現`
- `PE｜調整`

### 快速回覆

若 AI 推薦都可接受：

```text
R
```

若只微調例外：

```text
R 2C/P2 5PE：補「坨」
```

注意：`P3/PX` 只代表預習單不放，不等於正式教學 `D 刪除`。

---

## F. 預習單 3–5 組規則

完整細則以 `core/worksheet/prestudy-language-selection-policy.md` 為準。

### 核心規則

1. `3–5 組` 只適用於預習單形近字／多音字主要練習區。
2. 正式簡報／Knowledge Lab 不設 3–5 組上限。
3. 教材生字完整保留；需要教的字仍需有正式教學位置。
4. 形近字是否深教看教學價值，不看預習單還有沒有空位。
5. 預習單可以只挑 3–5 組最值得「先看」的內容，其餘標 `P3`，但仍可在簡報 A/B/C 層教學。
6. 同冊去重只限制預習單正式占位，不禁止簡報必要複習或再教。
7. 若本課真正值得預習的只有 2 組，不硬湊 3 組；若教師指定或特殊課次需要超過 5 組，可例外調整。

---

## G. 同冊去重｜Volume-level Deduplication

1. 同一字群在同一冊原則上只在預習單正式出現一次。
2. 字群比對採正規化，不因順序不同而視為不同群。
3. 後課若只是前課完整字群的子集合，視為已覆蓋，除非新增了重要比較關係。
4. 多音字以「字 + 讀音／語意對比」查重，不只看單一字。
5. `PX` 不等於永不再教；可在簡報、口頭、考前整理中快速喚回。
6. 只有教師確認的 `P1/P2` 才寫入本冊正式覆蓋紀錄。

---

## H. STEP 2.5 教師端顯示格式

### H1. 教師決策卡是第一輸出

當狀態為 `WAITING_CONFIRMATION` 時，AI 必須先輸出人類可讀的 Teacher Selection Card，不得只回 JSON、YAML、資料陣列或 `vocabulary[]`。

對形近字，每一項的順序固定為：

```text
編號＋字群
→ 分析整理
→ 構形辨析／混淆點／辨認提示
→ 推薦指數＋詳細理由
→ 教學建議 A–E
→ 預習單建議 P1/P2/P3/PX
→ 冊內紀錄
```

若需要保留機器資料，可在教師決策卡之後附上 machine-readable payload；但該資料層不能取代分析推薦卡。

### H2. 多音字分析也不得只剩結論

每個多音字至少顯示：
- 各讀音
- 對應詞語
- 詞義／使用情境
- 課文使用
- 易混淆點
- 推薦指數與理由
- 教學建議
- 預習單建議與冊內查重

### H3. 成語也必須先做推薦判讀

成語在 STEP 2.5 不應只輸出 `definition / context / relatives / example`。每個成語必須先顯示：

```text
09｜躍躍欲試　★★★★★ 5/5｜強烈推薦
理由：與本課運動、挑戰與想嘗試的情境高度相連，生活與寫作遷移價值高。
教學建議：A 深教｜CORE
理解需求：動作＋心理狀態；適合生活例句與句意插圖。
```

其 `definition / context / relatives / example` 屬後續內容資料，不是教師確認介面的替代品。

### H4. 生字完整清單與形近字深究分開

`生字檢查數` 只能做 audit，不代表生字教學已完成。STEP 2.5 必須能證明：

- 教材生字完整清單仍在資料層與正式教學規劃中。
- 形近字推薦只是「哪些生字值得額外做字群辨析」。
- 未被選入形近字群的教材生字不得因此消失。

---

## I. STEP 2.5 必填資料格式

```yaml
step_2_5_language_radiation:
  status: WAITING_CONFIRMATION
  volume_id:

  teaching_scope:
    source_characters_complete: true
    formal_teaching_group_cap: NONE

  prestudy_scope:
    preferred_group_range: 3-5
    hard_cap: false

  teacher_selection_card:
    required: true
    rendered_before_machine_payload: true
    shape_near_analysis_required: true

  items:
    - id:
      category: CHARACTER | SHAPE_NEAR | POLYPHONIC | IDIOM | OTHER
      item:
      provenance:
      analysis:
        target_character:
        target_zhuyin:
        target_radical:
        comparison_characters: []
        common_words: []
        core_meanings: []
        component_analysis:
        confusion_point:
        discrimination_cue:
        mnemonic:
      recommendation_index:
      recommendation_level:
      ai_suggested_decision:
      reason:
      teacher_decision: PENDING
      prestudy:
        applicable: true | false
        ai_recommendation: P1 | P2 | P3 | PX
        volume_duplication_status: NEW | COVERED | PARTIAL_OVERLAP | NEW_RELATION
        volume_history: []
        reason:
        teacher_decision: PENDING
```

若資料層沒有完整教材生字，或系統用 `3–5 組` 規則刪掉正式教學內容，STEP 2.5 視為 `INCOMPLETE`。

若 `WAITING_CONFIRMATION` 只輸出 raw JSON / YAML 而沒有教師分析推薦卡，STEP 2.5 同樣視為 `INCOMPLETE`，不得進入下一個 HOLD。

若形近字只顯示字群＋推薦結果，卻沒有分析整理／構形辨析／混淆點，STEP 2.5 亦視為 `INCOMPLETE`。

---

## J. AI 的責任

AI 必須同時做到：

- 保留完整教材生字
- 先完成形近字／多音字分析整理，再做推薦
- 判斷哪些字需要一般識寫、哪些值得形近字深究
- 對正式教學內容給完整推薦，不受預習單容量限制
- 再從中精選適合預習單先看的 3–5 組左右高價值項目
- 比較本冊前課已確認的字群／多音字紀錄
- 判斷重複、部分重疊或新關係
- 說明為什麼某項「要教但不放預習單」
- 在等待教師確認時先呈現完整分析、推薦理由與快速決策代號，不把結構化資料直接丟給教師自己判讀

教師主要看分析與推薦後微調例外，不需要自己重做形近字判讀。

---

## K. Director Engine 接軌

1. 讀取完整教材生字／形近字／多音字／成語資料。
2. **先完成形近字與多音字語文分析整理。**
3. 再完成正式教學價值判讀，不設 3–5 組上限。
4. 再讀取同冊 `Volume Language Coverage`。
5. 從正式候選中精選預習單約 3–5 組形近字／多音字。
6. **先輸出 Teacher Selection Card：完整分析、推薦指數、理由、A–E、P1/P2/P3/PX。**
7. 若有 machine payload，再於教師卡後輸出；不得反過來。
8. 教師主要採 `R` 沿用，僅微調例外。
9. AI 依確認內容分 Knowledge Chunk，並同步輸出預習單語文項目。
10. 教師確認的 P1/P2 寫回本冊 Coverage Registry。
11. 才進入預習單版面與完整 Slide Architecture。

---

## 核心金句

> 教材告訴我們「有什麼」，分析告訴老師「這些字之間到底有什麼關係」，AI 再告訴老師「該教到什麼深度」。

> 推薦不能取代分析；代號不能取代語文判斷。

> 預習單要精選；正式教學要完整。

> 結構化資料是給系統讀的；STEP 2.5 的確認畫面是給老師做決策的。