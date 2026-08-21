---
name: teaching-strategy-builder
description: 讀取已核准的 Lesson Knowledge Book 與 Learning Module Profile，將教材知識與延伸學習模組安排成可執行的國語課堂流程。適用於決定課節、教學目標、引起動機、教師引導、學生任務、小組活動、差異化支援、形成性評量與 Exit Ticket。不得修改教材原文、官方知識或已核准的學習模組內容。
---

# Teaching Strategy Builder

版本：0.1.0

## 使命

將已核准的教材知識與學習延伸模組，安排成符合年級、課堂時間、能力目標與教師偏好的實際教學流程。

Teaching Strategy is an approved companion object. It must record the Source Master, `APPROVED_TEACHING_SELECTION`, and Learning Modules versions it uses; it must not become a second source of truth for textbook content.

Machine-readable Teaching Strategy Profiles MUST conform to `core/schemas/vmax/teaching-strategy-profile.schema.json`. The profile stores how to teach approved content; it does not own or rewrite Source Master text.

本技能負責「怎麼教」，不負責重新解讀教材，也不負責決定視覺風格或製作簡報。

## 前置條件

執行前必須存在並讀取：

- 已核准的 Lesson Knowledge Book
- 已核准的 `learning-module-profile.md`
- 當課設定檔
- 根目錄 `AGENTS.md`
- `schemas/teaching-strategy-profile.md`
- `core/schemas/vmax/teaching-strategy-profile.schema.json`

若 LKB 或 Learning Module Profile 尚未核准，必須停止。

若 `APPROVED_TEACHING_SELECTION` 尚未確認，必須停止或只輸出待教師決定的策略建議，不得建立正式教學流程。

## 標準輸出

產生：

- `working/teaching-strategy-profile.md`
- `working/lesson-flow.md`
- `working/strategy-validation-report.md`

完成後停下等待教師確認，不得直接進入 Presentation Engine。

正式 machine payload 的 `status` 必須保持 `TEACHER_REVIEW`，直到教師確認；只有 `CONFIRMED` 的 Teaching Strategy Profile 可供 Presentation Engine 使用。

## 教學流程結構

每一節課至少包含：

1. 課節資訊
2. 能力目標
3. 教材知識節點
4. 使用的 Learning Modules
5. 引起動機
6. 教師引導
7. 學生任務
8. 檢核與回饋
9. 差異化支援
10. 收束或 Exit Ticket

## 動態課節原則

- 不預設固定節數。
- 不強迫每課使用相同流程。
- 課節數依教材內容、學習模組、教師時間與學生程度決定。
- 同一知識節點不應在多節課中無目的重複。
- 每一節課必須有明確學習成果與檢核方式。

## 策略選擇原則

### 引起動機

可依內容選擇：

- 圖像觀察
- 情境提問
- 看圖猜詞或猜成語
- 課文預測
- 經驗連結
- 錯誤示例辨析
- 快速投票

### 教師引導

可包含：

- 示範思考
- 逐步提問
- 教材原句定位
- 關鍵詞標記
- 比較與歸納
- 錯誤診斷

### 學生任務

可包含：

- 個別思考
- 兩人討論
- 小組合作
- 口頭發表
- 句型仿作
- 情境判斷
- 看圖推論
- 心智圖整理
- 短文或成語應用

### 評量

可包含：

- 口頭檢核
- 白板作答
- 配對或選擇
- 造句
- 找證據
- Exit Ticket
- 學習單
- 簡短任務成果

## 教材忠實規則

- 教材原文、官方成語、詞義、例句、修辭、句型與教學重點不得改寫成新的官方內容。
- 教學活動可以使用官方知識，但必須保留來源界線。
- 成語延伸中的易誤用、近義比較、情境練習等屬於 `learning_extension`。
- 不得把延伸比較用成語加入本課官方成語清單。
- 教師答案只進入教師專用欄位。

## 差異化規則

每節課可依需要設定：

- 基礎支援：圖片、詞語提示、句型框架、選項縮減
- 一般任務：標準題目與表達任務
- 進階挑戰：比較、推論、改寫、生活遷移

差異化不得改變教材事實，只調整任務支援與複雜度。

## 時間配置

- 每節課的活動時間總和必須等於或小於設定時間。
- 建議保留 3 至 5 分鐘作為轉場與彈性時間。
- 若活動過多，應標示為備選，而不是全部塞入單一課節。

## 驗證

完成前確認：

- 每節課都有能力目標。
- 每個活動都能追溯到 LKB 節點或 Learning Module。
- 教材知識與延伸內容已分流。
- 教師答案未進入學生可見內容。
- 時間總和合理。
- 有形成性評量或收束方式。
- 無上一課內容污染。

## 停等確認

完成後呈現：

- 建議課節數
- 各節核心目標
- 主要活動
- 使用的學習模組
- 評量方式
- 待教師選擇或調整項目

狀態設為 `ready_for_teacher_review`，等待教師確認後才能交給 Presentation Engine。
