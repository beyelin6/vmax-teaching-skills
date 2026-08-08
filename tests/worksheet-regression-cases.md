# V-MAX Worksheet Regression Cases 1.1

## 用途

檢查課前預習單與課後短文／Bonus 寫作單是否保留 V-MAX 的中年級閱讀、書寫、語文聚焦與版面原則。

共同硬規格：

> A4 100% 實際列印時，任何學生需要閱讀、辨認、勾選或作答依據的文字不得小於 12 pt。

若內容放不下，應刪減、縮短或重排；不得用縮字解決。

---

## CASE WS-01｜預習單不得變縮小版講義

### PASS
- A4 橫式
- 任務式分區
- 左／上短任務 + 右側較大閱讀理解區 + 開放思考區
- 書寫空間足夠
- 文字適合三、四年級
- 學生可見文字全部 >= 12 pt（A4 100% 實際列印）

### BLOCKER
- 滿版小字
- 把整份 Source Master 塞進一頁
- 沒有學生實際操作空間
- 任一必要閱讀文字 < 12 pt

分類：`PRESTUDY_LAYOUT_FAIL / PRESTUDY_OVERLOAD / WORKSHEET_FONT_TOO_SMALL`

---

## CASE WS-02｜三、四年級預習語文聚焦

### PASS
- 正式生字完整保留在資料層
- 預習單主要生字任務聚焦高價值形近字與多音字
- 一般生字不平均做同規格深教
- AI 不自行新增單一生字詳解；單字詳解只由教師指定
- 3–5 組為軟性精選容量
- 同冊去重已檢查

### BLOCKER
- 每個生字都做一格
- AI 因易錯／複雜／字源有趣自行新增單字詳解
- 為湊數加入低價值形近字
- 把未進預習單解讀成正式教學刪除

分類：`PRESTUDY_SCOPE_DRIFT / CHARACTER_TEACHING_FLATTENED / SINGLE_CHARACTER_AUTO_DEEPENED`

---

## CASE WS-03｜預習單不得提前講完

### PASS
- 閱讀題可回到課文找線索
- 保留推論／發現空間
- 學生版無答案

### BLOCKER
- 題目直接把課文主旨、修辭結論或教師答案寫出
- 預習單取代正式課堂發現

分類：`PRESTUDY_SPOILER / PRESTUDY_ANSWER_LEAK`

---

## CASE WS-04｜短文單必須有三段式鷹架

### PASS
1. 素材／畫面啟動
2. 語文 Bonus 工具箱
3. 最大面積正式創作區

### BLOCKER
- 只有作文格
- 只有工具清單沒有創作空間
- 正式書寫區小於整體可寫面積約一半

分類：`WRITING_SCAFFOLD_FAIL / WRITING_WORKSHEET_LAYOUT_FAIL`

---

## CASE WS-05｜Bonus 必須真的是可選工具

### PASS
- 明示不用全部使用
- 語詞、四字語詞／成語、句型、修辭只選與本課寫作任務有遷移價值的內容
- 學生可自主勾選
- 工具太多時優先刪減，不縮到 12 pt 以下

### BLOCKER
- 要求全部使用
- 變成檢核表式作文
- 所有學生被迫用同一句型、同一成語
- 為塞更多 Bonus 而縮小字體

分類：`BONUS_OVERLOAD / FORMULAIC_WRITING / WORKSHEET_FONT_TOO_SMALL`

---

## CASE WS-06｜成語寫作遷移不可漂移

### PASS
- 短文單中的成語來自已確認範圍
- 使用語意符合 STEP 2.6
- 不需要教典故才能完成

### BLOCKER
- 加入未確認成語
- 例句／使用方式與已確認語意衝突
- 把典故故事當成寫作使用義

分類：`WRITING_TOOL_DRIFT / IDIOM_VISUAL_DRIFT`

---

## CASE WS-07｜同一視覺家族，不同任務功能

### PASS
- 預習單與短文單可共享紙張、框線、角色與主題視覺語彙
- 預習單功能是探索／理解／預備
- 短文單功能是輸出／遷移／創作

### BLOCKER
- 兩份只換標題、內容骨架完全相同
- 為追求視覺一致犧牲任務差異

分類：`WORKSHEET_FUNCTION_DRIFT`

---

## CASE WS-08｜學習單字級不得低於 12 pt

### PASS
- 預習單與短文單均以 A4 100% 實際列印尺寸檢查
- 所有學生必要閱讀文字 >= 12 pt
- 正文／題幹建議 12–14 pt 以上
- 區塊標題建議 14–18 pt 以上
- 主標題建議 20 pt 以上
- 班級／座號／姓名、勾選項、提示語、角色台詞、圖說等只要學生需要辨讀，也 >= 12 pt
- 圖片式輸出依實際列印尺寸檢查等效字級，不以設計畫布數值自欺

### BLOCKER
- 任何必要閱讀文字 < 12 pt
- 匯出／縮放後實際尺寸低於 12 pt
- 因內容過多而縮字
- 只放大標題，正文／勾選項仍過小

分類：`WORKSHEET_FONT_TOO_SMALL / WORKSHEET_EXPORT_SCALE_FAIL`

---

## 整體 PASS

```yaml
worksheet_regression:
  prestudy_task_layout: PASS
  prestudy_grade34_language_focus: PASS
  prestudy_no_spoiler: PASS
  writing_three_stage_scaffold: PASS
  bonus_is_optional: PASS
  idiom_transfer_preserved: PASS
  shared_visual_family_distinct_function: PASS
  writing_space_sufficient: PASS
  min_student_visible_font_12pt: PASS
  export_scale_preserves_font_size: PASS
  student_answer_leak: PASS
```
