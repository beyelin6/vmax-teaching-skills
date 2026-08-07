# V-MAX Strategy Engine 2.0

版本：0.1.0

## 定位

Strategy Engine 的任務不是「想一個很炫的活動」，而是根據教材、學習目標、班級學習樣貌與教師意圖，推薦最適合的教學策略，並說明為什麼值得用。

舊版 Omni Architect 已具備 `type / title / method / teachingPoint / application` 五欄策略骨架；新版保留此資產，但移除「創意優先」與「低階動詞一律封殺」的硬規則，改採學習目的優先。

## 核心原則

1. 策略服務學習目標，不服務新奇感。
2. AI 先推薦與說明理由，教師保留最終決策權。
3. 策略必須能回指課文、段落、語文知識或學生作品證據。
4. 不因為「畫線、圈選、朗讀、找證據」看似低階就禁止；若它是建立理解的必要步驟，就可使用。
5. 高階活動不等於好活動。辯論、角色扮演、解謎、遊戲化只有在符合內容與學生需求時才推薦。
6. 同一策略可以有紙本、口語、平板、Padlet、ClassSwift、Wordwall 等不同 Delivery，不把平台寫死在策略核心。
7. 每個策略都要回答「學生可能卡在哪裡」與「這個策略如何幫他跨過去」。
8. 微任務可短，但不能為了湊 1 分鐘而破壞完整理解。

## 輸入

```yaml
strategy_input:
  text_dna:
    genre:
    structure:
    key_language_features: []
    difficult_sections: []
  lesson_goal:
    primary:
    secondary: []
  learning_profile:
    reading_support:
    language_support:
    interaction_preference:
    collaboration_readiness:
    digital_access:
  teacher_intent:
    priority_focus: []
    preferred_modes: []
    avoid_modes: []
  evidence:
    source_nodes: []
    student_observations: []
  director_intent_ref:
```

## Strategy Card Schema

保留舊系統五欄，並擴充決策欄位：

```yaml
strategy:
  id:
  type:
  title:
  method:
  teaching_point:
  application:
  target:
    source_node:
    learning_goal:
    common_barrier:
  why_this_strategy:
  evidence_to_watch:
  recommended_delivery: []
  alternatives: []
  support_level:
  estimated_time:
  director_alignment:
```

## 四層策略

### A. Teaching Strategy｜教學策略

處理「怎麼讓學生理解」。

常見類型：

- 觀察與發現
- 找證據
- 比較與分類
- 因果推理
- 角色視角
- 情境模擬
- 概念命名
- 改寫與轉換
- 圖像化整理
- 口語重述
- 創作應用

### B. Visual Strategy｜視覺策略

由 Director Designer 與 Visual Grammar 協作，處理「要讓學生怎麼看」。

例如：

- 遠景 → 中景 → 近景
- 真實畫面 ↔ 想像畫面
- Before / After
- 四格漫畫
- 六格故事
- 動作分鏡
- 雙線對照
- 特寫停格

### C. Interaction Strategy｜互動策略

處理「學生在哪個階段要自己想、跟別人想、公開比較」。

可選：

- 個人先想
- 兩人互證
- 組內共學
- 組間互學
- 全班投票
- 即時診斷
- 作品互評
- 口語接龍
- 平板拖曳／分類／回應

### D. Assessment Strategy｜評量策略

處理「如何知道學生真的懂了」。

優先收集：

- 原始答案
- 修正後答案
- 課文證據
- 解釋理由
- 圖像整理
- 口語重述
- 創作遷移

## 推薦流程

```text
Text DNA
→ Lesson Goal
→ Learning Profile
→ Teacher Intent
→ Director Intent
→ Strategy Candidates
→ Why / Barrier / Evidence
→ Teacher Selection
→ Delivery Mapping
```

## 推薦而非自動決定

每個重要學習節點原則上推薦 2～4 個策略候選，而不是只輸出唯一答案。

推薦格式：

```yaml
recommendations:
  - rank: 1
    strategy_id:
    reason:
    best_for:
    tradeoff:
  - rank: 2
    strategy_id:
    reason:
    best_for:
    tradeoff:
```

## 舊版規則遷移

### 保留

- `type / title / method / teachingPoint / application`
- 策略要指出學生痛點或盲點
- 任務要具體可執行
- 可以針對單一策略重新生成
- 可以針對修辭單獨產生教學引導與互動任務
- 可避開既有策略，提供新的選項

### 改寫

舊規則：必須使用高階動詞，禁止畫線、圈出、找一找、朗讀、討論。

新版：依學習目的選動詞。必要的低負荷任務可作為發現、取證、比較前置步驟；高階活動只在它能增加理解時使用。

舊規則：Task 必須遊戲化／角色扮演；Thinking 必須哲學思辨／極端情境；Rhetoric 必須跨界改編／感官重塑。

新版：以上皆為候選策略，不是硬鎖。系統依 Text DNA、學生程度與教師意圖決定是否推薦。

舊規則：策略固定生成 3 個。

新版：依節點複雜度與教師需求推薦 1～4 個；開學快速版可只給 2 個高品質候選。

## 與 Director Designer 的關係

Strategy Engine 決定「學生怎麼學」；Director Designer 決定「學生怎麼看」。兩者互相約束。

例如寫景文採「遠景→近景」閱讀路徑時：

- Director Designer：定義鏡頭與視線推進。
- Strategy Engine：推薦先觀察遠景線索、再比較近景細節、最後用一句話說明作者觀察順序。
- Visual Sequence：必要時產生三段連續畫面。
- Renderer：負責最終美感呈現。

## 驗收

策略輸出前至少檢查：

- 是否能回指來源內容
- 是否對應明確學習目標
- 是否符合班級支援需求
- 是否說明學生可能的理解障礙
- 是否有可觀察的學習證據
- 是否把數位平台錯當學習目的
- 是否為了創意而過度設計
- 是否提供教師可選擇的替代方案
