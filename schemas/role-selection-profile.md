# Role Selection Profile

## 定位

角色不得先於教材分析固定套用。系統必須根據已核准的 Lesson Knowledge Book、Learning Module Profile、Teaching Strategy Profile 與目標年級，提出 3 至 5 個角色建議，再停下等待教師確認。

## 角色選擇流程

1. 讀取教材文體、主題、場景、情緒、敘事視角與主要能力目標。
2. 判斷角色功能需求：引導、陪伴、提問、示範、挑戰、統整。
3. 從 Role Library 篩選適合角色。
4. 產生推薦排序與理由。
5. 教師可選擇：
   - 採用推薦角色
   - 改選 Bee 老師
   - 選擇其他角色
   - 關閉角色
6. 未確認前不得生成角色插圖或定稿簡報。

## 推薦依據

```yaml
role_selection:
  mode: content_driven
  recommendation_count: 3
  allow_teacher_override: true
  allow_no_role: true
  require_teacher_approval: true

  evidence:
    genre: ""
    topic: ""
    setting: []
    emotional_tone: []
    learning_goals: []
    activity_types: []
    age_group: ""
```

## 建議評分

每個角色可依下列項目評分 1 至 5：

- `content_fit`：與教材主題及場景契合度
- `pedagogical_fit`：與教學策略及活動契合度
- `age_fit`：與年級閱讀及情緒需求契合度
- `visual_fit`：與候選視覺風格契合度
- `continuity_fit`：是否適合貫穿整課

## 推薦輸出

```yaml
recommendations:
  - role_id: ""
    rank: 1
    scores:
      content_fit: 0
      pedagogical_fit: 0
      age_fit: 0
      visual_fit: 0
      continuity_fit: 0
    reasons: []
    suggested_functions: []
    cautions: []
```

## 教材類型與角色功能示例

- 童詩、感官描寫：溫暖陪伴型、觀察型角色。
- 記敘文、人物成長：教練型、夢想引導型角色。
- 探索、自然觀察：探險家、研究員、觀察員。
- 推理、法律與規則：偵探、記者、案件分析員。
- 說明文、步驟教學：研究員、工程師、整理型教師。

以上只作為篩選提示，不得以文體直接指定唯一角色。

## 角色使用規則

- 一套簡報預設只有一個主要引導角色。
- 配角只能在教材情境確有需要時出現。
- 角色不得遮擋課文、題目或學生任務。
- 角色出現頻率依內容決定，不要求每頁出現。
- 角色台詞必須服務教學，不加入無關口頭禪。
- 角色外觀、服裝、比例與色彩需保持一致。
