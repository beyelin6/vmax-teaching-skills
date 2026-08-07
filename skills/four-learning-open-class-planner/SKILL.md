---
name: four-learning-open-class-planner
description: 將既有 V-MAX Baseline 或 Classroom Variant 轉換為符合平板公開課需求的四學模式版本，整合學生自學、組內共學、組間互學、教師導學、五大學習平台候選、學習證據、觀課可視性與數位備案。不得為了形式硬湊四學或平台，必須保留 Lesson Flow、教材忠實、Theme、Visual DNA 與引導者敘事。
---

# V-MAX Four Learning Open Class Planner

版本：0.1.0

## 使命

把一堂已完成的 V-MAX 課程轉換為可公開觀課的平板教學版本，讓觀課者看見：

- 學生先自己思考
- 小組內比較與修正
- 小組間互相學習
- 教師根據學生證據進行導學
- 數位工具留下可觀察的學習歷程

此技能不是重新設計一堂課，而是在既有 Lesson Flow 上加上一層「四學公開課策略」。

## 前置條件

必須讀取：

- 已核准 Baseline Version
- 已核准 Classroom Variant 或 Teaching Flow
- 已核准 Learning Modules
- 已核准 Digital Interaction Profile
- `schemas/four-learning-open-class-profile.md`
- `libraries/digital-platforms/four-learning-open-class.md`
- Theme／Visual DNA／Guide Character Profile（若存在）

## 工作流程

### Step 1｜找出公開課核心學習目標

只選 1 個主要學習主軸，必要時加 1 個形成性檢核。避免 40 分鐘內同時展示過多知識點與平台。

優先選擇：

- 有可比較答案的課文理解
- 字群／形近字辨析
- 成語情境判斷
- 段落結構整理
- 修辭發現與仿寫
- 句型應用
- 短文構思或修改

### Step 2｜建立四學責任鏈

為核心任務安排：

1. `student_self_learning`
2. `intra_group_learning`
3. `inter_group_learning`
4. `teacher_guided_learning`

每一學都必須回答：

- 學生／教師要做什麼？
- 為什麼要這樣做？
- 留下什麼學習證據？
- 下一階段如何使用前一階段成果？

### Step 3｜平台映射

先建立平台中立活動，再選平台。

平台候選：

- 學習吧
- 因材網
- 均一教育平台
- PaGamO
- Cool English

選擇平台時檢查：

- 是否符合本學科？
- 是否能降低蒐集或回饋成本？
- 是否有學生熟悉的登入方式？
- 是否能留下學習證據？
- 是否會造成過度切換？

若平台功能不確定，標記 `PLATFORM_CAPABILITY_CHECK_REQUIRED`。

### Step 4｜設計觀課可見證據

至少建立：

- 個人原始答案
- 小組修正或共識
- 組間比較／回饋
- 教師導學所引用的學生證據
- 導學後的二次作答或修正

公開課不能只讓觀課者看到「學生在使用平板」，而必須看到學習前後差異。

### Step 5｜整合 V-MAX 視覺與敘事

四學頁面必須沿用本課 Theme、Visual DNA 與角色。

Bee 老師可依情境切換：

- 自學：`ROLE-COACH`
- 共學：任務提醒與合作規則
- 互學：主持比較與提問
- 導學：統整、澄清、Meaningful Quote

不得因公開課而退回純文字投影片。

### Step 6｜建立數位備案

每個平台活動必須有：

- no-device fallback
- network failure fallback
- login failure fallback
- reduced-time fallback

備案要能維持同一學習目標，不可只是取消活動。

## 建議輸出

`planning/four-learning-open-class-profile.md`

並更新 Classroom Variant：

```yaml
classroom_conditions:
  teaching_mode: open_class_four_learning
```

Presentation Engine 應另外產生或重排：

- 四學任務總覽頁
- 平板操作頁
- 組內共學頁
- 組間比較頁
- 教師導學統整頁
- 導學後 Exit Ticket／二次作答頁

## 國語課範例：字群探索

### 學生自學

學生看情境圖與候選字，個人判斷「愉／偷／輸／喻」，並寫下偏旁或字義理由。

### 組內共學

四人比較答案，必須先說理由，再決定小組答案。

### 組間互學

展示兩組不同理由，其他組以「字義證據／偏旁線索」補充或質疑。

### 教師導學

教師使用學生錯誤與正確理由進行統整，最後由 Bee 老師留下金句：

> 偏旁像路標，會悄悄告訴我們字義的方向。

再以新的情境題完成二次檢核。

## 品質檢查

不得通過的情況：

- 自學只有看影片，沒有任務與產出。
- 共學只是坐在一起，沒有比較、理由或修正。
- 互學只是輪流報告，沒有跨組回應。
- 教師導學沒有引用學生前面產生的證據。
- 平台只為展示科技而存在。
- 四學每段時間被僵化為固定比例。
- 為了五大平台而硬塞不適合國語課的平台。
- 公開課版破壞原本圖片式美感與角色一致性。
