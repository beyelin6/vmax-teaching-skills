# V-MAX STEP 1 Source Anchor Policy 1.4

## 定位

STEP 1 是「教材定錨」，目的只有一個：先把教材真值、範圍與來源確認清楚，再進入教學判讀。

核心原則：

> STEP 1 只回答「教材裡有什麼」，不提前回答「要怎麼演、怎麼畫、怎麼分頁」。

來源取得另遵循：

- `core/governance/source-library-policy.md`
- `core/governance/recognition-only-character-policy.md`

---

## A. STEP 1 必做

教師可讀確認卡應整理：

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
- 兩處來源不一致：標記 `SOURCE_CONFLICT`，完整列出差異，進 HOLD 1。
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

只有下列條件成立才算 STEP 1 PASS：

- source_data_complete_or_gaps_named: true
- teacher_readable_card_rendered: true
- machine_payload_not_primary_ui: true
- source_library_checked_if_configured: true
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

否則標記 `STEP1_INCOMPLETE`，只顯示缺口與補來源行動，不得要求教師核准完整 STEP 1，也不得把「教師確認方向」當作來源完整性核准。

所有重要項目須依 `core/ui/teacher-review-view-contract.md` 標示 `[教材明載] / [教師補充] / [AI 延伸] / [待核對]`。外部字典查核不能取代教材 provenance。

---

## 核心金句

> 先把教材讀對，再談怎麼教。

> 認讀字看教材生字系統，不看方格猜。

> 課文下方小字與課後生字表都要看，兩邊核對後才定身分。

> STEP 1 是教材定錨，不是視覺提案會議。

> 原始教材放一次；之後 V-MAX 自己去來源庫找。
