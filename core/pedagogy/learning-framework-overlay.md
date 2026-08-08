# V-MAX Learning Framework Overlay 1.0

## 定位

Learning Framework Overlay 是 V-MAX 的「可掛載學習框架層」。它用來承接 SEL、閱讀理解、語文理解、數位學習、PBL、四學、合作學習、探究學習、跨領域、媒體素養、教育政策方案等會持續增加或變動的教學框架。

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

若無法說明明確增益，預設 `OFF`。

---

## 核心金句

> 框架可以很多，學生的學習路徑不能因此變亂。

> V-MAX 不收藏教育名詞；V-MAX 收藏真正有效的學習行動。
