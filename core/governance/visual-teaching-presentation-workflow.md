# V-MAX Visual Teaching Presentation Workflow

Version: 1.1
Status: REVIEW
Scope: Cross-subject
Mode ID: VISUAL_TEACHING_PRESENTATION

---

## 0. Purpose｜目的

本 Workflow 用於將教師已完成的：

- Google Slides
- PPTX
- 既有教學簡報
- 自學簡報
- 教學活動簡報

轉譯為「V-MAX 圖片式教學簡報」。

本模式的核心不是重新設計課程，
也不是單純美化既有投影片。

核心任務為：

SOURCE PRESENTATION
→ 理解既有教學功能
→ 分析頁面內容
→ 選擇適合的視覺結構
→ 圖片式教學轉譯
→ QA
→ 可實際教學的成品

---

### 0.1 Intent Gate｜先辨認轉檔或視覺轉譯

「把簡報變成 PNG」可能指兩種不同工作，必須先按教師明確意圖分流：

#### A. 原樣匯出

教師要求「原樣匯出」「不改版面」「直接把每頁轉成 PNG」時：

- 保留來源每頁的文字、圖片、版面、配色與順序。
- 只做格式轉換，逐頁輸出完整 PNG。
- 不進入本 Workflow 的視覺分析、重新構圖或代表頁製作流程。
- 匯出 QA 必須核對 PNG 數量與來源投影片頁數一致、頁序一致、比例與版面未被裁切；任何轉換失敗頁面需明確列出，不得以代表頁預覽代替整份匯出。

#### B. 圖片式視覺轉譯

教師要求「圖片式視覺簡報」「重新視覺化」「依參考圖製作」或提供新的視覺設計方向時：

- 進入本 Workflow，依下列 Stage 轉譯。
- `CONTENT_LOCK = TRUE`：保留來源的教學內容、要求與頁序；允許依教學功能調整構圖、插圖與資訊層級。
- 教師提供參考圖並說「像這樣」時，將其作為視覺語言依據，辨識色彩、插畫質感、字級層級、資訊密度與圖文關係；各頁仍依教學功能變化構圖，不複製固定版型。
- 正式交付格式為逐頁完整 PNG。可編輯 PPTX 只能作為教師另行要求的附加格式，不能代替 PNG。

附件圖片依教師描述判定用途：稱為來源頁、要求照原樣輸出時，歸入 A；稱為參考圖、要求「像這樣」製作新頁時，歸入 B。不得只因附件外觀經過設計，就自行推定教師授權重新美編。

若指令不足以判斷 A 或 B，或同時出現互相矛盾的要求，只問一次：「要保留原版面直接匯出 PNG，還是依視覺方向重新轉譯成 PNG？」得到答覆後按選定路徑執行，不把 `PNG` 一詞單獨當成美編授權。

# 1. Core Principle｜核心原則

## 1.1 既有 Slides 轉譯 ≠ 重新規劃課程

當來源簡報已具備完整：

- 教學順序
- 教學內容
- 提問
- 活動
- 範例
- 練習
- 統整

不得自行重新執行完整課程設計。

應以來源簡報為 CONTENT SOURCE OF TRUTH。

允許：

- 重新構圖
- 視覺化
- 圖文化
- 調整資訊層級
- 將文字轉換為情境
- 將流程轉換為圖像路徑
- 將比較轉換為視覺對照
- 將人物特質轉換為人物＋證據

禁止：

- 因為畫面不好看而刪除重要內容
- 擅自改變原本教學目標
- 擅自新增答案
- 擅自重新安排整套課程
- 未經教師確認自行大量拆頁或合頁

---

# 2. Trigger｜觸發條件

當教師提供既有 Google Slides / PPTX，
並提出下列需求或同義需求時啟動：

- 圖片式教學簡報
- 圖片式文字組件
- 圖片引擎渲染文字
- 把這份簡報重新做成圖片式
- 把這份 Slides 視覺化
- 重新製作成學生上課版本
- 做成 ChatGPT 可直接編輯的圖片
- 依 V-MAX 圖片式簡報製作

不得要求教師額外說：

「像社會簡報」

本 Workflow 為跨科共用模式。

---

# 3. Source Fidelity｜來源忠實

開始製作前必須先完整理解來源。

至少辨識：

1. 原始頁序
2. 每頁標題
3. 每頁主要內容
4. 每頁教學功能
5. 學生需要完成的任務
6. 範例／答案／教師提示
7. 是否存在不可任意改寫的原文

來源內容優先級：

SOURCE
> 已確認教師要求
> V-MAX 共用規則
> 視覺美術需求

視覺美術不得凌駕來源內容。

---

# 4. Page Function Analysis｜頁面功能判讀

每一頁在製作前必須回答：

### A. SEE
學生這一頁需要「看見什麼」？

### B. THINK
學生這一頁需要「思考什麼」？

### C. DO
學生這一頁需要「做什麼」？

完成以上判讀後，
才可選擇視覺構圖。

不得：

SOURCE SLIDE
→ 直接 IMAGE GENERATION

必須：

SOURCE SLIDE
→ TEACHING FUNCTION
→ VISUAL STRUCTURE
→ IMAGE GENERATION

---

# 5. Visual Translation Router｜視覺轉譯路由

視覺構圖必須依教學功能選擇。

## STORY

適用：

- 故事發展
- 敘事順序
- 起承轉合

優先：

- 故事山
- 故事路徑
- 情境連續圖
- 漫畫式連拍

---

## PROCESS

適用：

- 步驟
- 操作流程
- 事件發展

優先：

- 箭頭流程
- 路徑
- 1 → 2 → 3
- 連續情境

---

## TIME

適用：

- 歷史
- 人物生平
- 事件先後

優先：

- 時間軸
- 時間道路
- 年代節點

---

## CAUSE / EFFECT

適用：

- 因果
- 原因與結果
- 問題與影響

優先：

- 因果魚骨
- 箭頭鏈
- 原因 → 現象 → 結果

---

## COMPARE

適用：

- 比較
- 異同
- 前後變化

優先：

- 左右對照
- 雙情境
- 中央比較軸

---

## SPACE

適用：

- 地理
- 空間
- 方位
- 建築配置

優先：

- 地圖
- 空間放大鏡
- 同心圓
- 平面配置圖

---

## CHARACTER

適用：

- 人物特質
- 人物行動
- 模範人物

優先：

- 人物中央
- 周圍證據卡
- 行動特寫
- 情境證據

---

## EVIDENCE

適用：

- 找證據
- 文本觀察
- 圖表觀察

優先：

- 原始材料
- 放大鏡
- 線索標記
- 證據 → 推論

學生需要自己推論時，
不得直接顯示最終答案。

---

## LANGUAGE SCAFFOLD

適用：

- 好詞
- 句型
- 修辭
- 寫作鷹架

優先：

- 詞語積木
- 句型組件
- 圖像語意
- 範例組裝

---

## SUMMARY

適用：

- 全課統整
- 段落統整
- 學習整理

優先：

- 學習地圖
- 路線圖
- 概念網
- 分支整理

---

# 6. Visual DNA｜預設視覺語言

預設 Visual DNA：

## Fresh Textbook Watercolor

特徵：

- 16:9
- 白底
- 高明度
- 足夠留白
- 清新教科書手繪
- 淡水彩
- 日系兒童教材感
- 情境式人物插圖
- 圖文融合
- 大字級
- 清楚資訊層級
- 小量貼紙／便條紙元素
- 柔和筆刷
- 統一頁碼設計

目標：

TEACHING FUNCTION
×
VISUAL DESIGN
×
CLASSROOM USABILITY

---

# 7. Visual DNA ≠ Template

Visual DNA 不是固定版型。

不得：

- 每頁都做 Bento Box
- 每頁都做四張卡片
- 每頁都左右切半
- 每頁都放相同人物位置
- 每頁都使用同一資訊框

同一份簡報應保持：

STYLE CONSISTENCY

但允許：

LAYOUT VARIATION

頁面構圖必須依教學功能改變。

---

# 8. Image-rendered Text｜圖片式文字

適合圖片引擎整合：

- 標題
- 小標
- 關鍵詞
- 短句
- 流程節點
- 對話泡泡
- 視覺標籤
- 情境文字
- 短說明

---

## Precision Text

以下內容優先考慮文字精準度：

- 課文原文
- 完整範文
- 長篇閱讀文本
- 生字
- 注音
- 多音字
- 精確表格
- 評量題目
- 專有名詞
- 特殊字形

不得為追求圖片效果犧牲文字正確性。

---

# 9. Illustration Function｜插圖功能

插圖不得只是裝飾。

每張主要插圖至少支援：

- 情境建立
- 概念理解
- 找證據
- 比較
- 流程
- 人物特質
- 空間理解
- 時間理解
- 寫作想像

若插圖不支援教學功能，
且干擾閱讀，
應刪除。

---

# 10. Character & Object Consistency

一旦教師確認：

- 角色
- 髮型
- 制服
- 運動服
- 校名
- 配色
- 教具
- 特殊物件

即進入 LOCKED 狀態。

後續不得自行變更。

例如：

APPROVED:
一般塑膠掃把

不得後續自動變成：

竹掃把。

---

# 11. Student-facing Rules

學生可見頁面：

- 不直接放答案
- 不由角色代答
- 不提前揭露推論
- 保留思考空間
- 保留合理作答空間
- 指令簡潔
- 字級適合投影與 iPad

教師答案與提示另行處理。

---

# 12. Approval State｜確認狀態

頁面狀態：

PLANNED
→ DRAFT
→ REVIEW
→ APPROVED

當教師說：

- 通過
- 確認
- OK
- 可以
- 這版可以

該頁進入：

APPROVED

---

# 13. Approved Page Lock

APPROVED 後鎖定：

- 構圖
- Visual DNA
- 角色
- 物件
- 已確認文字
- 頁面功能
- 修正結果

後續頁面可以延續其視覺語言，

但不得擅自重新設計已確認頁。

若教師只要求：

「把竹字拿掉」

只處理指定內容。

不得趁機：

- 換人物
- 換構圖
- 改背景
- 改其他文字
- 重設整頁

---

# 14. Mandatory Approval Gate｜強制停等

本 Workflow 必須遵守以下流程。

## STAGE 1 — SOURCE

讀取來源簡報。

↓

## STAGE 2 — ANALYSIS

分析：

- 全份結構
- 頁面功能
- 視覺需求
- 特殊內容
- 可能拆頁需求

↓

## STAGE 3 — CONSTRUCTION PLAN

提出：

- 頁碼
- 教學功能
- 核心文字
- 插圖
- 視覺結構
- 版面配置

↓

## STAGE 4 — REPRESENTATIVE PAGE

只製作代表頁。

↓

# STOP

等待教師確認。

---

教師確認後：

## STAGE 5 — SMALL BATCH

只製作第一批小批次。

建議：

2～5 頁／批

↓

# STOP

等待教師確認。

---

教師確認後：

- 若仍有未完成的規劃頁面，進入 STAGE 6，只製作下一批。
- 若所有規劃頁面均已完成並進入 APPROVED，進入 STAGE 7 — QA。

## STAGE 6 — NEXT BATCH

每次只製作一個下一批小批次。

↓

# STOP

等待教師確認。

---

教師確認後：

- 若仍有未完成的規劃頁面，留在 STAGE 6，再製作下一批。
- 只有所有規劃頁面均已完成並進入 APPROVED，才能進入 STAGE 7 — QA。

↓

## STAGE 7 — QA

完成：

- 文字 QA
- 視覺 QA
- 頁碼 QA
- 角色 QA
- 尺寸 QA
- 來源忠實 QA

↓

## STAGE 8 — DELIVERY

圖片式視覺轉譯的正式交付：

- 每頁一張完整 PNG，頁碼與來源／核准頁面對應。
- 先直接呈現已核准批次的 PNG 預覽，再提供可取得的檔案。

教師另有要求時，可附加：

- PPTX
- PDF
- Google Slides
- Google Drive

附加格式不得取代逐頁 PNG。若選擇的是「原樣匯出」，依 Intent Gate 直接輸出來源各頁 PNG，不執行本 Workflow 的視覺轉譯 Stage。

---

# 15. Hard Gate｜禁止跳步

禁止：

- 未分析來源就開始生圖
- 未提供施工規劃就大量生圖
- 未確認代表頁就完成整份
- 一次生成全部頁面後才詢問教師
- 每一批完成後都必須 STOP 等待教師確認（`EVERY_BATCH_REQUIRES_APPROVAL`）。
- 教師說「繼續」只授權製作下一批，不授權自動完成所有剩餘批次。
- 所有規劃頁面均完成並進入 `APPROVED` 前，不得進入 QA。
- 圖片式視覺轉譯要求 PNG 時，所有核准頁面均須有對應的完整 PNG 才算交付完成；PPTX 或其他可編輯檔不得替代。
- 教師明確要求原樣匯出時，保持來源視覺與頁面內容不變，不把格式轉換擴大成視覺改版。
- 因過去做過相似教材而跳過確認
- 自行修改 APPROVED 頁
- 自行更換已確認角色
- 自行更換已確認 Visual DNA

「繼續」

代表：

只進入下一個已定義 Stage。

不代表：

授權自動完成所有剩餘 Stage。

---

# 16. Existing Presentation Protection

若教師提供的是已完成 Slides / PPTX：

預設：

CONTENT_LOCK = TRUE

表示：

內容本身視為已規劃完成。

Workflow 的主要工作是：

VISUAL TRANSLATION

而非：

CURRICULUM REDESIGN

若發現：

- 明顯缺頁
- 前後矛盾
- 文字不足
- 教學功能無法判讀

應先標示問題，
不得自行補寫後直接製作。

---

# 17. QA Checklist

每頁交付前檢查：

### TEXT
- 繁體中文
- 臺灣用語
- 無錯別字
- 無亂碼
- 標點正確
- 字級清楚
- 無文字溢位

### VISUAL
- 16:9
- 圖片未錯切
- 留白合理
- 視覺焦點清楚
- 圖文不互相遮擋

### CHARACTER
- 人物一致
- 服裝一致
- 校名一致
- 教具一致

### TEACHING
- 教學功能明確
- 學生知道要看什麼
- 學生知道要想什麼
- 學生知道要做什麼
- 不提前洩漏答案

### SOURCE
- 未遺漏重要內容
- 未擅自增加內容
- 頁序正確

---

# 18. Default User Invocation

教師可以使用：

「@V-MAX 圖片式教學簡報，
轉譯這份 Google Slides。」

或：

「把這份 PPTX 做成圖片式教學簡報。」

系統應自動進入：

VISUAL_TEACHING_PRESENTATION

不要求教師另外指定：

「像社會簡報」。

---

# 19. Minimal Launcher Route

Launcher 僅需辨識需求並路由：

VISUAL_TEACHING_PRESENTATION

Launcher 不應複製本 Workflow 全文。

完整規則由：

visual-teaching-presentation-workflow.md

負責。

---

# 20. Design Philosophy

圖片式教學簡報不是：

漂亮的投影片。

而是：

「把學生原本必須閱讀大量文字才能理解的內容，
轉換成能看、能想、能操作的教學畫面。」

因此所有視覺決策皆遵循：

TEACHING FIRST.
VISUAL SUPPORTS THINKING.
CONTENT REMAINS TRUSTWORTHY.
