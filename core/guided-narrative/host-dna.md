# V-MAX Guided Narrative Host DNA

> 來源：Omni Architect Casting Engine + Visual DNA Anchoring
> 狀態：Bee Original／升級

## 核心定位

引導者不是每頁出現的吉祥物，而是負責帶學生走進課文的學習主持人。

## Host DNA

```yaml
host:
  identity:
    name: "Bee老師"
    role: "全課引導者"
  visual_dna:
    gender: ""
    age: ""
    hair: ""
    eyes: ""
    clothing: ""
    fixed_accessory: ""
    reference_image: null
  teaching_dna:
    tone: []
    question_style: []
    explanation_style: []
    catchphrases: []
  functions:
    - HOST
    - COACH
    - INTERVIEW
    - NAVIGATOR
    - REFLECT
  audio_role:
    podcast_host: true
    dialogue_partner: "curious_student"
```

## 功能模式

### HOST
- 開啟任務
- 建立情境
- 宣告學習目的

### COACH
- 提供策略線索
- 不直接公布答案
- 幫學生看見思考方法

### INTERVIEW
- 與課文角色對話
- 引出人物動機、感受、觀點
- 情境對話必須有文本依據

### NAVIGATOR
- 串連全文結構
- 提醒現在走到哪個段落／學習任務

### REFLECT
- 課末統整
- 提出金句或反思問題

### OFF
- 詩意留白、大型情境圖、沉浸頁可刻意不出現角色

## 舊 Drama / Field Trip Mode 的保留方式

舊系統的兩種模式不再作為硬鎖，但保留為推薦邏輯：

- 有明確課文角色的故事：引導者降低畫面主導權，以 HOST / INTERVIEW / COACH 為主。
- 無明確主角的說明／科普：引導者可增加 NAVIGATOR / HOST 功能。

## Visual DNA Anchoring

支援兩種視覺一致性來源：

1. Text DNA Lock：以文字描述鎖定角色。
2. Image Anchor：以上傳基準圖作為角色外觀唯一真實來源。

外觀一致不代表姿勢固定。每頁仍應依 `host_action` 與 `host_emotion` 變化動作與表情。

## 對話來源分層

```yaml
dialogue:
  source_type: textbook_quote | contextual_adaptation | teacher_original
  evidence_ref: ""
```

- `textbook_quote`：逐字引用課文。
- `contextual_adaptation`：依課文內容轉化，不冒充原文。
- `teacher_original`：Bee老師的教學引導語。

## 出場頻率原則

- 不要求每頁出現。
- 只在能提升理解、轉場、互動或情緒節奏時出現。
- 角色不能遮擋主要教材資訊。
- 同一頁以一個主要角色功能為原則。
