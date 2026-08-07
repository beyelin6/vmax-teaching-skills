---
name: digital-interaction-planner
description: 將已核准的 Learning Modules 與 Teaching Strategy 轉換為適合平板操作的互動活動規格。適用於每生一機、兩人共用或小組共用情境，可規畫點選、拖曳、標示、排序、錄音、短答、合作白板與 Exit Ticket；若為公開觀課，可進一步映射四學模式與五大學習平台候選。不得改寫官方教材內容，所有互動都必須追溯至 LKB 節點並提供離線替代方案。
---

# Digital Interaction Planner

版本：0.2.0

## 前置條件

必須讀取：

- 已核准的 Lesson Knowledge Book
- 已核准的 Learning Module Profile
- 已核准的 Teaching Strategy Profile
- `schemas/tablet-interaction-profile.md`
- `libraries/learning-modules/digital-interaction/index.md`

若 `teaching_mode: open_class_four_learning`，另讀取：

- `schemas/four-learning-open-class-profile.md`
- `libraries/digital-platforms/four-learning-open-class.md`
- `skills/four-learning-open-class-planner/SKILL.md`

## 職責

1. 判斷哪些學習模組適合轉為平板互動。
2. 選擇合適的互動形式與裝置模式。
3. 產生平台中立的活動規格。
4. 安排活動時間、教師控制點與回饋方式。
5. 提供無網路或裝置故障時的替代方案。
6. 將活動映射給 Presentation Engine、學習單或外部平台。
7. 公開課模式下，建立四學活動與學習證據鏈。
8. 公開課模式下，只在有學習價值時映射數位平台。

## 適配原則

優先推薦平板活動的情況：

- 需要標示課文證據
- 需要拖曳排序或配對
- 需要看圖判斷
- 需要即時蒐集全班答案
- 需要錄音或口語表達
- 需要合作整理想法
- 需要快速形成性評量
- 需要留下個人→小組→跨組→導學後的學習歷程

不建議使用平板的情況：

- 單純閱讀短段落即可完成
- 手寫比輸入更符合學習目標
- 活動只增加點擊，沒有認知價值
- 網路或登入流程會占用過多教學時間
- 只是為了公開課展示科技

## 平台中立輸出

標準輸出：

`knowledge/03_learning-expansion-tablet.md`

每個活動包含：

- 活動 ID 與名稱
- 對應 LKB 節點
- 對應 Learning Module
- 學習目標
- 操作形式
- 學生畫面內容
- 學生操作步驟
- 教師引導與控制點
- 正確答案或評量規準
- 預估時間
- 無障礙注意事項
- 離線替代方案
- 可映射平台類型
- 學習證據
- 若屬四學：four_learning_phase

## 公開課四學模式

當 `teaching_mode: open_class_four_learning` 時，Digital Interaction Planner 不得只產生單點平板活動，而必須與 `four-learning-open-class-planner` 協作，形成：

```text
學生自學：個人原始答案／標記／短答
        ↓
組內共學：比較、說理由、修正
        ↓
組間互學：展示差異、提問、補充
        ↓
教師導學：引用學生證據統整與澄清
        ↓
二次檢核：修正答案／Exit Ticket
```

四學是整堂課的責任鏈，不是固定時間切割。

## 五大學習平台候選

公開課可從以下平台候選中映射：

- 學習吧
- 因材網
- 均一教育平台
- PaGamO
- Cool English

規則：

- 先設計平台中立任務，再選平台。
- 不要求一堂課五個平台全部使用。
- 國語課若無跨語言任務，Cool English 預設不適用。
- 若無法確認平台目前功能，標記 `PLATFORM_CAPABILITY_CHECK_REQUIRED`。
- 若登入、切換、操作成本過高，優先改用單一平台或紙本替代。

## 與簡報的關係

簡報中若安排平板活動，需清楚呈現：

- QR Code／短連結預留區
- 活動目的
- 學生操作步驟
- 完成時間
- 完成後回到全班討論的提示

公開課模式另外應呈現：

- 四學目前階段（不必做成制式標籤，可融入 Theme）
- 小組合作規則
- 組間比較方式
- 教師導學統整頁
- 二次檢核頁

實際連結尚未建立時，使用 `LINK_PENDING`，不得虛構網址。

## 美感與角色規則

平板活動頁不得退化為純文字操作說明。應沿用本課 Theme、Visual DNA 與引導角色。

Bee 老師可在公開課中擔任：

- 自學：任務教練
- 共學：合作提醒者
- 互學：比較主持者
- 導學：概念統整者

## 教師確認關卡

產出後必須停下，讓教師確認：

- 哪些活動真的使用平板
- 每節課活動數量
- 裝置分配方式
- 網路與帳號條件
- 是否需要指定平台
- 是否保留紙本替代方案
- 公開課四學是否可觀察
- 教師導學是否真的使用學生證據

確認前不得把平台或連結寫入最終簡報。
