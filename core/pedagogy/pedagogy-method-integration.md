# V-MAX Pedagogy Method Integration 1.0

## 定位

Pedagogy Method Integration 負責處理「教學法與載具如何改變一課的學習流程」。

核心原則：

> 教學法不是最後多加一張活動頁；如果它真的被採用，就應該改變學生怎麼進入、互動、蒐集、討論、產出與回望。

本層位於 Lesson / Session 設計之間，提供可選模組，不預設每課都要使用。

---

## A. 可選教學法模組

至少支援：

- 四學：學生自學、組內共學、組間互學、教師導學
- 平板／數位載具整合
- PBL / Project-Based Learning
- 合作學習
- 探究式學習
- 任務導向學習
- 差異化學習
- 媒體／資訊素養活動
- 跨領域整合
- 教師自訂教學法

教學法可單獨使用，也可組合，但不得為了看起來創新而堆疊多種方法。

---

## B. 教學法啟用條件

每課 Lesson Map 完成後，系統可提出 0–3 個「適合但非必要」的教學法候選，由教師決定是否啟用。

每個候選必須說明：

```yaml
pedagogy_candidate:
  method:
  why_fit_this_lesson:
  suitable_session:
  student_action_change:
  teacher_role_change:
  required_resources: []
  expected_output:
  time_cost:
  risk_or_tradeoff:
  status: PROPOSED | CONFIRMED | OFF
```

若無法明確說出「學生行動會因此怎麼不同」，不得只因教學法名稱流行就推薦。

---

## C. 四學整合

四學不是固定四步驟頁面模板，而是角色與學習責任的轉換。

### 學生自學
適合：先讀、先找線索、先做個人判斷、先蒐集證據。

### 組內共學
適合：比較答案、整合證據、共同標記、協作解題。

### 組間互學
適合：不同觀點交換、成果巡覽、互評、補充證據。

### 教師導學
適合：統整關鍵概念、處理迷思、命名規則、深化推論。

規則：
- 不要求每堂課四學四階段全部出現。
- 可以只採其中 1–2 個階段。
- 教師導學不是最後固定講解，而應根據學生前面產出的證據介入。

---

## D. 平板／數位載具整合

平板使用必須有明確功能，不得只把紙本題目搬到螢幕。

允許用途：
- 圈選／標記文本證據
- 拍照蒐集生活語料或環境例子
- 即時投票與預測
- 協作白板／共編
- 錄音朗讀與自評
- 圖像、影片、地圖、時間軸探索
- 查證背景資料或時事
- 數位作品產出
- 同儕互評／回饋

每次平板活動必須定義：

```yaml
device_activity:
  purpose:
  student_task:
  tool_type:
  artifact:
  teacher_view:
  offline_fallback:
  privacy_or_safety_note:
```

重要：
- 工具品牌不是核心。優先描述功能，平台可替換。
- 必須有 `offline_fallback`，避免載具故障讓教學崩潰。
- 若查網路資訊，需考慮來源判讀與適齡性。

---

## E. PBL 整合

PBL 只在課文有足夠真實問題、跨資料需求、持續探究或可公開成果時啟用。

不得把一個普通練習包裝成 PBL。

PBL 最少需要：

```yaml
pbl:
  driving_question:
  authentic_context:
  inquiry_tasks: []
  knowledge_connections: []
  student_choices: []
  checkpoints: []
  final_product:
  audience:
  reflection:
```

PBL 可跨一課、多課甚至跨領域，因此不必強迫塞進單一 Lesson。

---

## F. 與 Session Director 的關係

啟用教學法後，Session Director 必須重新檢查：
- 堂數是否需要增加
- 哪一堂需要蒐集／討論／產出
- natural_stop_point 是否改變
- 是否需要課外或跨堂任務
- CORE / FLEX / BONUS 是否重新配置

因此流程為：

```text
Text DNA
→ Lesson Map
→ Contextual Enrichment
→ Pedagogy Method Candidates
→ Teacher Confirmation
→ Session Map
→ Slide Architecture
```

若教師在後期才加入 PBL／四學／平板活動，系統不得只附加一頁，而要重新檢查 Session Map。

---

## G. 投影片與教學法的關係

不是每個教學活動都需要投影片。

投影片可扮演：
- 任務啟動
- 時間／步驟提示
- 問題展示
- 證據比較
- 成果投影
- 回饋規準
- 反思收束

若學生主要在平板、白板、實作或小組中工作，投影片可以刻意減少。

核心原則：

> V-MAX 設計的是學習流程，不是讓每一分鐘都被簡報佔滿。

---

## H. 教師選擇權與 Intent Lock

教學法屬於高層教學決策。

AI 可以：
- 提出候選
- 說明利弊
- 幫忙拆 Session
- 產生任務支架與評量規準

AI 不可以：
- 未經確認自動把整課改成 PBL
- 因為有平板就預設全部數位化
- 把四學固定成每堂標準流程
- 讓教學法名稱凌駕課文本身

教師確認後可標記：

```yaml
pedagogy_lock:
  selected_methods: []
  must_keep: []
  optional: []
  forbidden: []
```

---

## I. Quality Gate

每次啟用教學法前檢查：
- 這個方法真的比一般教學更適合這一課嗎？
- 學生的認知行動因此變得更好，還是只是多一道操作？
- 是否增加不必要的時間與管理成本？
- 平板活動若沒有網路或設備是否仍可教？
- PBL 是否真的有 driving question 與成果，而不是包裝名稱？
- 四學是否根據學習需要使用，而非四步全套？
- 投影片是否退到適當位置，而不是搶走學生互動？

---

## 核心金句

> 先決定學生要怎麼學，再決定要不要用平板、四學或 PBL；工具與方法都應該服務理解，而不是讓理解服務工具。
