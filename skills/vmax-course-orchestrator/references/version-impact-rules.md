# Version and Impact Rules

## 目的

協助 Orchestrator 判斷一次修改應建立 Patch、Classroom Variant，還是回到上游重建 Baseline。

## 先判斷修改性質

### 回到上游重建 Baseline

遇到以下情況，不得只建立 Patch：

- 課文、生字、認讀字、核心詞語或官方成語擷取錯誤
- 教師手冊中的修辭、句型、主旨或寫作特色漏列或誤列
- LKB 節點結構或來源關聯錯誤
- 整課主要 Learning Path 或教學結構全面改變
- 出版社教材版本更新

建議版本：Major，例如 `1.x.x → 2.0.0`。

### 建立 Adaptive Patch

適用：

- 新增特殊任務、節慶或議題融入
- 新增成語易誤用、近義辨析、情境練習
- 增加補救教學或進階挑戰內容
- 新增平板互動或紙本替代活動
- 替換特定活動、投影片或問題
- 對既有流程作可重用的局部增修

建議版本：Minor，例如 `1.0.0 → 1.1.0`。

### 建立 Classroom Variant

適用：

- 同一教材因班級、日期或時間條件而調整
- 四十分鐘縮短為二十五分鐘
- 公開觀課、高互動、複習或無平板模式
- 只挑選 Baseline 的部分頁面上課
- 對特定班級套用已存在的 Support 或 Challenge Patch

Variant 不一定提升 Baseline 版本；應建立獨立 Variant ID 與輸出版本。

### Patch Release

適用：

- 修正錯字
- 修正答案標示
- 修正連結或 QR Code
- 修正版面溢出
- 修正未替換變數

建議版本：Patch，例如 `1.1.0 → 1.1.1`。

## 影響矩陣

| 修改項目 | LKB | Learning Modules | Teaching Flow | Role／Style | Presentation |
|---|---:|---:|---:|---:|---:|
| 官方教材知識 | 重建 | 重建 | 重建 | 重檢 | 重建 |
| Teacher Knowledge | 視內容 | 視內容 | 視內容 | 視內容 | 視內容 |
| 成語延伸 | 不變 | 修改 | 視活動 | 通常不變 | 修改 |
| 特殊任務 | 通常不變 | 可能新增 | 修改 | 視情境 | 修改 |
| 平板活動 | 不變 | 視內容 | 修改 | 視畫面需求 | 修改 |
| 課堂時間 | 不變 | 不變 | 重排 | 通常不變 | 重排 |
| 角色 | 不變 | 不變 | 通常不變 | 修改 | 修改 |
| 風格 | 不變 | 不變 | 不變 | 修改 | 修改 |
| 錯字／連結 | 不變 | 不變 | 不變 | 不變 | 小修 |

## 差異化標籤

Patch 可依用途標記：

- `core`：全班核心內容
- `support`：學習支援
- `challenge`：進階挑戰
- `mission`：特殊任務

同一 Patch 可以包含多個標籤，但必須說明目標學生與使用時機。

## 防止過度重跑

Orchestrator 應採最小影響原則：

1. 先判斷修改觸及哪一層。
2. 只將真正受影響的成果標記 stale。
3. 不因新增一張活動頁而重建 LKB。
4. 不因縮短上課時間而重做官方教材轉錄。
5. 不因更換平板工具而改寫 Learning Module 的學習目標。

## 版本記錄必要欄位

每次產出必須記錄：

- Baseline Version
- Source LKB Version
- Patch ID 與 Patch Version
- Classroom Variant ID
- Active Classroom Version
- Output Manifest Path
- Generated At
- Teacher Approval
