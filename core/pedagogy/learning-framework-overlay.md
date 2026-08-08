# V-MAX Learning Framework Overlay 1.1

## 定位

Learning Framework Overlay 是 V-MAX 的「可掛載學習框架層」。它用來承接 SEL、閱讀理解、語文理解、數位學習、PBL、四學、合作學習、探究學習、跨領域、媒體素養、教育政策方案，以及各式討論法、提問法與閱讀分類系統。

核心原則：

> 先讓課文與學習任務成立，再決定需要掛上哪些框架；框架服務學習，不讓學習服務框架。

---

## A. 為什麼需要 Overlay，而不是一直改核心

教育現場會持續出現新的方案、倡議、政策名詞與教學框架。V-MAX 不應每新增一個名詞就重寫主流程。

因此採用：

```text
Text / Lesson Core
      ↓
Director + Session
      ↓
Learning Framework Overlay（0..n）
      ↓
Activity / Interaction / Assessment
```

每一個 Overlay 都可：
- `OFF`
- `SUGGESTED`
- `TEACHER_SELECTED`
- `REQUIRED`

預設 `OFF`，不得為了「看起來完整」自動全部套用。

---

## B. Framework Families｜框架家族

### 1. Language & Literacy｜語文與閱讀理解

適用於真正需要提升閱讀與語言理解的課次。

可包含但不限於：
- 字詞理解
- 詞義推論
- 句義理解
- 指涉／連貫
- 段落關係
- 文本結構
- 摘要
- 主旨
- 推論
- 觀點與證據
- 閱讀監控
- 提問策略
- 預測
- 連結先備知識
- 圖文整合
- 多文本比較
- 語用與情境理解
- 寫作遷移

規則：不得把「閱讀策略名稱」當成教學成果。學生真正要做的是理解、推論、比較、監控與表達。

#### 1A. Reading Taxonomy｜閱讀分類子層

閱讀分類不是單一固定表，而是一個可掛載的分類槽，用來回答：

> 這一個閱讀任務，學生究竟在做哪一種理解工作？

可容納：
- 擷取明示訊息
- 直接理解
- 推論訊息
- 統整與解釋
- 評估與批判
- 比較文本／觀點
- 監控理解
- 應用／遷移

亦可掛載教師指定或官方／研究框架，例如：
- PIRLS 類閱讀歷程分類
- QAR 類問題來源分類
- 教材或縣市採用的閱讀理解分類
- 學校自訂閱讀層次

規則：
- 分類用來幫助設計題目與檢查覆蓋，不得反過來硬逼每課湊滿所有類別。
- 同一題可有主要分類與次要分類，但需指定主要認知動作。
- 若某分類名稱屬政策／版本化框架，使用前應依需要查證其現行定義。
- V-MAX 內部可保留平台中立的核心動作，例如 `retrieve / infer / integrate / evaluate / transfer`，外部再映射到各框架名稱。

建議欄位：

```yaml
reading_task:
  primary_move: RETRIEVE | INFER | INTEGRATE | EVALUATE | MONITOR | TRANSFER
  framework_mapping: []
  text_evidence:
  expected_student_action:
  evidence_of_understanding:
```

### 2. SEL｜社會情緒學習

僅在課文情節、人物、情緒、選擇、關係或真實生活連結自然支持時啟用。

可聚焦：
- 自我覺察
- 自我管理
- 社會覺察
- 人際互動
- 負責任的決定
- 情緒辨識與表達
- 同理與觀點取替
- 衝突處理
- 韌性／挫折調節

禁止把任何故事硬轉成品德訓話或貼 SEL 標籤。

### 3. Inquiry / PBL / Problem Solving｜探究與問題導向

可包含：
- 驅動問題
- 問題拆解
- 蒐證
- 查證
- 假設
- 方案設計
- 作品迭代
- 公開成果

若沒有持續探究與真實產出，不標示為 PBL。

### 4. Collaborative Learning｜合作與互學

可包含：
- 個人思考
- 組內共學
- 組間互學
- 教師導學
- 同儕回饋
- 角色分工
- 共編／共創

四學可視為此家族中的一種可選結構，不強迫四階段每次完整出現。

#### 4A. Discussion Protocol｜討論／提問流程子層

Discussion Protocol 用來定義「討論怎麼走」，而不是定義「學生最後要學會什麼」。

可掛載：
- ORID 焦點討論法
- Think-Pair-Share
- Socratic questioning
- 六何法
- 教師自訂提問階梯
- 其他結構化討論流程

##### ORID 焦點討論法

ORID 可作為一種可選討論流程：

- `O｜Objective`：先看見／回想具體事實、訊息、現象
- `R｜Reflective`：說出感受、直覺、聯想、印象
- `I｜Interpretive`：解釋意義、關係、原因、觀點
- `D｜Decisional`：形成選擇、行動、判斷、遷移

使用原則：
- 不要求每一課、每一次討論都完整跑 O→R→I→D。
- 可依文本與課堂任務取其中部分步驟。
- O 不等於低階、D 也不必然等於高階；仍須看實際提問內容。
- ORID 只是一條討論路徑，不能取代文本證據、閱讀理解層次與語文學習目標。
- 若套用 ORID 會讓原本自然的對話變得僵化，預設不用。

建議欄位：

```yaml
discussion_protocol:
  protocol: ORID | TPS | SOCRATIC | SIX_WH | CUSTOM
  selected_moves: []
  purpose:
  anchor_text_or_evidence:
  expected_student_talk:
  teacher_moves:
```

### 5. Digital Learning｜數位／平板學習

平板與平台屬載具，不是目的。

只有當數位工具真正改變學生行動時才啟用，例如：
- 圈選／標註文本證據
- 即時投票／診斷
- 協作白板
- 錄音朗讀
- 查詢與查證
- 多媒體閱讀
- 拍攝生活證據
- 數位創作
- 同儕回饋

### 6. Cross-Curricular & Real-World｜跨領域與真實世界

可包含：
- 社會
- 自然
- 藝術
- 健體
- 科技
- 媒體與資訊素養
- 時勢／時事
- 生活議題

必須與課文理解或遷移有自然關係，不為跨領域而跨領域。

### 7. Policy / Initiative Overlay｜政策／方案層

用來承接會隨時間變動的教育政策、專案名稱、學校推動方案。

規則：
- 政策名稱與正式內涵若可能變動，使用前需查證最新官方資料。
- 核心教學不可依賴某個政策名稱存在。
- 政策改名或退場時，只需更新 Overlay Registry，不需改 Lesson Core。

---

## C. Overlay Selection Workflow

每課 Lesson Map 完成後，AI 只能提出「少量且有理由」的候選：

```yaml
framework_candidates:
  - framework:
    status: SUGGESTED
    why_fit_this_text:
    student_action:
    learning_gain:
    session_impact:
    evidence_of_learning:
    cost_or_risk:
```

教師可：
- 接受
- 拒絕
- 改寫
- 補充自己的框架

未經教師確認，不得因為教材談到情緒就自動新增 SEL 活動，也不得因為有平板就自動加入數位任務。

---

## D. 語文課的優先順位

國語課中，Overlay 必須服從以下順位：

```text
文本理解／語文學習
    > 教師本課意圖
    > 學習框架帶來的增益
    > 政策或活動名稱的完整呈現
```

如果套用某框架會讓學生離開文本太遠、壓縮必要語文練習、或增加大量無效流程，應降低或關閉該 Overlay。

---

## E. 同一活動可以同時服務多個框架

禁止為了每個框架各加一個活動。

例如：
「小組比較兩段文本證據，平板共編後向全班說明」
可能同時服務：
- 閱讀推論
- 合作學習
- 數位學習
- 口語表達

系統應優先設計一個高品質學習行動，而不是四個貼標籤活動。

---

## F. 與 Session Director 的關係

Framework Overlay 會影響 Session，但不得反過來支配整課。

若教師啟用某 Overlay，Session Director 需重新檢查：
- 是否增加活動時間
- 是否需要新的自然停點
- 是否需要學生作品
- 是否需要設備／網路／分組
- 是否需要前置任務
- 是否需要多一堂課
- 是否應標為 CORE / FLEX / BONUS

因此 3–5 堂只是常見區間，加入深度探究、PBL、數位創作或跨領域後，可自然延伸。

---

## G. Framework Registry｜可演化登錄表

V-MAX 不把所有框架寫死在程式邏輯，而以 Registry 管理：

```yaml
framework_registry:
  id:
  family:
  official_name:
  aliases: []
  source_type: STABLE_PRACTICE | RESEARCH_FRAMEWORK | POLICY | SCHOOL_CUSTOM
  current_status:
  last_verified:
  core_moves: []
  misuse_warnings: []
```

新的教育政策或教學法加入時，優先新增 Registry 條目，不修改核心架構。

---

## H. Quality Gate

啟用任何 Overlay 前檢查：
- 它真的讓這篇課文學得更好嗎？
- 學生實際會多做哪一個有意義的認知／互動行動？
- 如果拿掉框架名稱，這個活動本身仍然值得做嗎？
- 是否只是為了交差、觀課或政策名詞而加入？
- 是否擠壓核心語文理解？
- 是否造成工具負擔大於學習增益？
- 是否可與其他框架共用同一高品質活動？
- 討論流程是否僵化了原本自然的閱讀對話？
- 閱讀分類是否只是為了湊類別，而沒有真實認知需求？

若無法說明明確增益，預設 `OFF`。

---

## 核心金句

> 框架可以很多，學生的學習路徑不能因此變亂。

> V-MAX 不收藏教育名詞；V-MAX 收藏真正有效的學習行動。

> 討論法決定怎麼談，閱讀分類決定在做哪一種理解；兩者都不能取代真正的文本學習。
