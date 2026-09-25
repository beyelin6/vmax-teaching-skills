# V-MAX STEP 1 Source Anchor Policy 1.8

## 定位

STEP 1 是「教材定錨」，目的只有一個：先把教材真值、範圍與來源確認清楚，再進入教學判讀。

核心原則：

> STEP 1 只回答「教材裡有什麼」，不提前回答「要怎麼演、怎麼畫、怎麼分頁」。

來源取得另遵循：

- `core/governance/source-library-policy.md`
- `core/governance/recognition-only-character-policy.md`
- `core/schemas/vmax/source-ingestion-record.schema.json`

---

## A. STEP 1 必做

教師可讀確認卡應整理：

- Source Ingestion Record 狀態與掃描範圍
- 課名
- 作者
- 年級／冊別
- 文體
- 課文原文或可核對的段落／詩節結構
- 完整教材正式生字／我會寫字
- **認讀字 presence check，且必須完成「課文頁下方小字 × 課後獨立生字表」雙來源核對**
- 完整教材詞語聯集／教材重要語詞
- 教材成語
- 教材正式語文活動
- 教材明列修辭／句型／文體焦點（若來源有）
- source provenance / 不確定處

### A2. Source Ingestion Record 先於教材判讀

STEP 1 先建立 `SOURCE_INGESTION_RECORD`，逐頁記錄正文、底欄、側欄、圖表、圖片下方小字與教材框線區塊的掃描結果。至少要明確標示：

- `main_text`
- `bottom_margin`
- `small_text_area`
- `radical_markup`
- `vocabulary_box`
- `sentence_pattern_box`
- `publisher_note`

每個 `FOUND` 區塊中屬於本次擷取清單的內容，必須保存完整文字與 `pdf_page`、`printed_page`、`region_ref`；`crop_ref` 無獨立裁切時填 null，原始頁面可回看且區域定位清楚即足夠；`UNCERTAIN` 區塊必須保存原因與證據位置。`NOT_FOUND` 只表示該區塊已被檢查且未發現，不能由 Agent 用推測補成內容。

Source Ingestion Record 是「掃描與證據記錄」，不包含教學取捨、角色、風格、頁數或答案裁決。它完成後才可組裝 Source Master；Source Master 以 `ingestion_record_refs` 回指本記錄。

可加入「初步教材觀察」，但必須明確標示為 AI observation，不得冒充教材來源。

### A1. 認讀字必須雙來源核對

STEP 1 必須依 `core/governance/recognition-only-character-policy.md` 檢查：

1. 課文頁下方的小字生字標示
2. 課文後方獨立生字表／生字教學頁

然後交叉核對，才可判定正式生字／認讀字身分。

```yaml
recognition_only_characters:
  status: PRESENT | N/A_SOURCE_NOT_PRESENT | UNCERTAIN_SOURCE_LABEL | SOURCE_CONFLICT
  source_label:
  items: []
  textbook_footer_evidence: []
  posttext_character_table_evidence: []
  cross_check_status: MATCH | PARTIAL_MATCH | CONFLICT | NOT_APPLICABLE
  provenance:
```

規則：
- 認讀字不是「無方格字」的同義詞；無方格只能作為版面辨識線索。
- 教材明確列為識讀、但非正式書寫生字時，才判定為認讀字。
- 課文中一般字、形近補充字、比較字、偏旁識字示例，不得因此被判為認讀字。
- 兩處來源一致：正常定錨。
- 兩處來源不一致：標記 `SOURCE_CONFLICT`，完整列出差異，建立 STEP 1 內的來源裁決 HOLD，依 HOLD policy 的確認範圍處理；裁決後回 STEP 1 重驗，不直接進 STEP 2。
- 來源沒有：明確顯示 `N/A_SOURCE_NOT_PRESENT`，不得整欄消失。
- 不得以年級經驗取代來源判定。

---

## B. STEP 1 禁止提前決定

STEP 1 不得鎖定或預設：

- Mode A / Drama / Field Trip 等情境模式
- Scenario Wrapper
- 角色或卡司
- Style Recipe / 畫風
- Visual Grammar
- 具體頁型或 slide count
- `visualStructureRecommendation` 之類後段視覺方案
- Session 數
- Lesson Visual Map 模式

若 AI 覺得某課具有明顯視覺／情境潛力，只能記為：

`later_candidate_note`，不得進入 STEP 1 教師決策，也不得視為已選方案。

---

## C. STEP 1 Teacher Confirmation Card

預設呈現人類可讀格式，不顯示 raw JSON。

建議結構：

```text
STEP 1｜教材定錨

課名：
作者：
文體：
年級／冊別：

課文結構：
正式生字／我會寫字：
認讀字：有→完整列出｜無→來源未列（N/A）｜不確定→列待確認｜衝突→列兩處差異
來源核對：課文頁下方小字 ✓／課後獨立生字表 ✓
教材詞語：
教材成語：
教材語文活動：
教材明列語文焦點：

來源核對／待確認：

⏸ HOLD 1｜請確認教材定錨
```

若教師確認後才進下一步。

---

## D. Source First

STEP 1 必須優先使用教材／結構化轉錄來源；不得用舊簡報、舊腳本或模型記憶取代來源真值。

若教師已指定固定 Google Drive Source Library，預設先依 `core/governance/source-library-policy.md` 自動尋找冊別與課次：

`Drive Source Library → 找冊別／原始手冊 → 定位課次 → STEP 1 教材定錨`

只有來源庫找不到、版本衝突、檔案權限阻擋或資料不足時，才要求教師重新上傳或補充來源。

不得明明來源庫已有完整原始手冊，仍要求教師每課重新上傳相同 PDF。

舊成果只能作為後續教學設計參考，不得倒灌成 source truth。

---

## E. 與 STEP 2 / STEP 2.5 的界線

- STEP 1：教材真值與範圍，包含正式生字／認讀字身分與雙來源核對。
- STEP 2：AI 教學價值判讀／Teacher Intent 候選。
- STEP 2.5：語文輻射分析與教師選擇，包括形近字、多音字、成語教學價值與預習單候選；若來源有認讀字，才條件式處理其教學深度。

因此 STEP 1 不需要先做形近字深究、成語教學層級、認讀字頁型、預習單 3–5 組選擇；這些留給後續階段。

---

## F. 完成條件

下列條件全部成立才算擷取完整、可進 HOLD 1 審核；STEP 1 正式完成另須教師核准此完整版本：

- source_data_complete_or_gaps_named: true（只表示已建缺口記錄，不單獨構成 PASS）
- required_extraction_complete: true
- unresolved_required_gaps: 0
- page_region_and_category_cross_check_complete: true
- teacher_readable_card_rendered: true
- machine_payload_not_primary_ui: true
- source_library_checked_if_configured: true
- source_ingestion_record_created: true
- source_region_coverage_recorded: true
- source_uncertainties_named: true
- recognition_only_character_presence_checked: true
- recognition_footer_checked: true
- recognition_posttext_character_table_checked: true
- recognition_cross_check_completed: true
- recognition_only_character_source_status_explicit: true
- recognition_conflict_not_silently_resolved: true
- no_grade_assumption_override: true
- no_unnecessary_reupload_request: true
- no_scenario_lock: true
- no_character_lock: true
- no_style_lock: true
- no_slide_architecture_lock: true

否則標記 `STEP1_INCOMPLETE`，依下方完整擷取流程先完成可自行查明的工作，再集中顯示仍需教師處理的缺口與補來源行動，不得要求教師核准完整 STEP 1，也不得把「教師確認方向」當作來源完整性核准。

所有重要項目須依 `core/ui/teacher-review-view-contract.md` 標示 `[教材明載] / [教師補充] / [AI 延伸] / [待核對]`。外部字典查核不能取代教材 provenance。

---

## 核心金句

> 先把教材讀對，再談怎麼教。

> 認讀字看教材生字系統，不看方格猜。

> 課文下方小字與課後生字表都要看，兩邊核對後才定身分。

> STEP 1 是教材定錨，不是視覺提案會議。

> 原始教材放一次；之後 V-MAX 自己去來源庫找。

## G. 完整擷取、集中審核（GLOBAL_SKILL_RULE）

### 階段內連續處理

STEP 1 的執行規則只有一條：來源可讀且仍有可做項目，就在當前回合持續整理，完成整份後再請教師審核。`STEP1_INCOMPLETE` 表示尚未完成，`next_allowed_stage: []` 表示不能跨階段；兩者都不是停止目前擷取的理由。翻頁、存檔與 checkpoint 後接著做下一個未完成項目，不以進度回報結束回合。只有完整稿待審、剩餘工作確實需要教師提供資料／裁決，或工具失敗使其餘工作無法繼續時才停；教師要求停止時立即停止。

1. 載入本政策、Transcriber 的收錄清單及當課已確認擷取範圍，形成「來源檔／課次頁範圍 × 頁面區塊 × 內容類別」工作清單。教師不必重新指定已有的收錄項目。來源範圍以本課為界，另查明確跨頁引用的補充，不延伸到整冊無關課文。
2. 先核對已有轉錄的來源版本／fingerprint、完整性與核准紀錄；相同來源的已驗證內容可沿用，補齊未掃描或不完整部分。重製簡報不等於丟棄已確認來源及教師決定；來源變更、證據矛盾或教師指定重查時才重新擷取受影響部分。舊摘要、舊簡報或未核准草稿不能冒充完整轉錄。
3. 在目前可用且已授權來源中，連續完成搜尋、文字層擷取與必要的原頁影像／局部放大核對。OCR 與清楚原圖不同時，依原圖修正轉錄並保存證據，這是擷取修正，不是教師選教決定。兩份原始來源真正矛盾時保留兩者，不自行裁決。
4. 遇到局部疑點先登錄，繼續同 stage 其餘獨立可查項目；完成可用來源核對後，才把無法辨識、缺頁、權限不足或真正來源衝突集中成一份缺口表。來源完全不可用或後續工作都依賴該缺口時才立即停止，避免盲目重試。缺口表分開列「AI 尚未完成」與「需要教師處理」，並列已查位置、具體缺什麼及影響；不能把只剩一個教師決定說成只剩一項工作。工具阻塞須說明失敗操作、已嘗試方法及無法繼續的原因，不以籠統待核對代替。未有可驗證處理速度時不估剩餘分鐘數，結束回合後不宣稱會在背景自行完成。

### 頁區與內容交叉防漏

逐頁檢查正文、側欄、底欄、框線補充、表格、圖說、圖下小字及跨頁續表；再依 Transcriber 收錄類別核對課文、完整生字與認讀字、部首／筆畫／字義／書寫提醒、詞語詞義、教材成語及例句、形近／音近／多音字、修辭句型、主旨結構、教學引導、活動／習作／答案與出版社補充。清單內內容完整保存；頁區掃描用於找出目標資料，不等於全頁逐字抄錄。教學引導中與本課字詞用法、理解題、例句或教材重點有關的內容仍須擷取，不因它位於教師欄而省略。

多音字不能只記字名或課文讀音：同頁旁欄、補充框及明確續頁中的所有教材讀音／注音、詞義、例詞、例句、辨析提醒須逐項擷取。保留主欄與補充欄的來源身分；這是教材既有資料，不能誤判為 AI 新增讀音。STEP 2.5 才決定教學範圍；完成擷取不代表自動選教所有補充。

每個必要頁區須有掃描結果與證據定位；FOUND 的目標內容須有完整文字；同區清單外內容只記來源位置及未擷取範圍。原始 PDF 頁碼＋區域描述可定位時，不必逐區另做裁切檔；小字辨識或欄位歧義才按需放大／裁切。圖片／表格的原頁即可作為圖像證據，仍須實際核對其內容。缺少獨立 crop 檔不算教材缺漏。來源未列和「尚未查／尚未讀清」分開，後者不得標成 NOT_FOUND 或 N/A。已命名缺口不等於已完成；「可辨識重點摘要」不等於完整來源。使用現有 ingestion schema 的 page_regions、extracted_segments、coverage_check、uncertainties／conflicts 保存，不另造不相容欄位。

### 完成與教師畫面

必要內容完整、頁區與類別交叉核對通過、必要 UNCERTAIN／來源衝突已解決，才設 EXTRACTION_VERIFIED，呈現一份整合的 STEP 1 教材審核稿並進 HOLD 1。三份內容輸出與 ingestion 記錄按既有格式分存，但教師只看一個目前審核入口；完整文字、來源表及差異可由該入口展開，不能只給多張檔案卡片或以摘要取代全文。

有未解必要缺口時維持 STEP1_INCOMPLETE／NEEDS_REVIEW。此時可請教師針對缺口補來源或裁決，不能要求「確認這份不完整摘錄即可往下」。教師回覆只解決本次指定缺口；AI 接著完成其餘核對，完整後才開放 HOLD 1 核准。單字裁定、同意方向或一般「繼續」不等於核准整份來源。

教師改字須另存原文、調整後文字、原頁證據及明確裁定事件；不把模糊的「是」擴張成未被詢問的其他改字，也不覆寫原始來源真值。

階段內 checkpoint 可保存細部進度與版本，但它不是 HOLD，不推進 next_allowed_stage。完成 stage／正式 HOLD 時仍依既有政策更新並驗證 Drive Runtime State、Index 與施工接續區。若環境中斷，記錄已完成範圍與下一個未完成項目；恢復後補齊同一清單，不重新詢問擷取範圍。

### 僅套用目前階段的前置條件

SOURCE 0／STEP 1 只要求當課身分、可用來源及適用的 State Sync。尚未產生的 LKB 核准、STEP 2.5 生字延伸成語覆蓋、風格、角色、畫布、頁數帳本、PAGE_DETAIL、Slide Script、P01 或代表頁，記錄 not_yet_produced／預期階段；不列為 STEP 1 缺口，也不提前執行。教材本來附的生字成語及多音字補充仍須在 STEP 1 完整擷取。到相應後段 stage 時，既有確認與施工門檻照常適用。

### 擷取效率：清單決定範圍，一次讀取，疑點回看

先沿用教師已指定的擷取清單；未另指定時，必抓本課資訊、完整課文、生字／認讀字及字音字義、全部核心詞語及詞義、教材成語（含生字補充）及例句、形近／多音字的全部教材補充、主旨／段意／結構／寫作特色、修辭句型與例句、語文活動／閱讀理解及其答案。教師欄中承載上述內容的段落也在清單內。這份清單決定完整性，不以「整頁每一字都已轉錄」作為完成條件。

通用授課操作（如請學生分組、請教師板書）、跨課重複行政說明、版權／裝飾文字及筆順圖逐筆重描，預設只保留原頁引用，不逐字轉錄、不作為完成阻塞；字形易錯提醒、實際筆畫資料與辨析重點仍必抓。教師已要求的其他內容保留在清單內，明確要求全文轉錄時才逐字擷取全範圍。清單外未擷取範圍在整合稿註明，不標為來源不存在，不把清單內難辨內容改列清單外。

1. 依已知 Drive file ID／目前進度直接讀取當課檔案；只有找不到、版本衝突或教師要求換源才重搜來源庫。核對來源版本與既有紀錄後，讀回完整且已驗證的擷取結果，只補缺項，不重做全課。
2. 工具支援時一次取得本課頁範圍的文字層；有限制時分段連續讀取，累積到同一份工作資料。先用同一份資料按清單擷取，再做頁區／類別覆蓋核對，不為每個類別重讀整份 PDF。
3. 文字層完整、閱讀順序可靠且已做必要頁區檢查時直接使用；只對缺字、OCR 疑點、多欄順序或表格對應不明的頁區回看影像。已驗證且來源未變的區域不反覆 OCR／截圖。必要影像工具不可用時保留具體缺口，不用猜測取代。
4. 同一工作資料產生教材全文、來源索引、擷取紀錄及驗證摘要，避免四份各自重寫。以一段連續擷取成果合併保存，完成 stage／HOLD、教師決策、實際阻塞或交接時依原政策同步並驗證；不每讀一頁就重寫所有文件、重列整個 Drive 或建立新的教師確認點。

效率驗收看本次讀取是否只針對缺項、已驗證頁區是否重用，以及每次回看是否有具體疑點；不以犧牲教材清單完整性換取速度，也不在未實測前宣稱節省多少分鐘。
