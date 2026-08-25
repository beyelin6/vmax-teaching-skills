# V-MAX Layout Library

## 定位

Layout Library 保存可重用的教學版型。版型依知識類型與學習任務選擇，不依課次固定套用。

簡報版型不得自行決定畫布比例。首次建立簡報時，必須沿用教師選定的 `canvas_lock`（僅可為 `4:3` 或 `16:9` 橫式）；選定後，Layout 只能調整區域配置、文字／圖片方向、留白與視線路徑，不得改變比例。學習單與短文單使用各自的非簡報 Output Profile。詳見 `core/presentation/canvas-lock-policy.md`。

## 初始版型索引

| Layout ID | 名稱 | 主要用途 |
|---|---|---|
| `LAYOUT-COVER-001` | 課程封面 | 課名、主題情境、角色開場 |
| `LAYOUT-TEXT-FOCUS-002` | 課文焦點 | 原文短段、重點標記、情境插圖 |
| `LAYOUT-VOCABULARY-003` | 字詞教學卡 | 生字、認讀字、詞義、語境 |
| `LAYOUT-IDIOM-SOURCE-004` | 成語教材卡 | 官方成語、教材詞義、教材例句、對應生字 |
| `LAYOUT-IDIOM-CONTEXT-005` | 成語情境理解 | 情境插圖、判斷、理由表達 |
| `LAYOUT-IDIOM-MISUSE-006` | 成語易誤用 | 正誤例句、錯誤診斷、教師揭示 |
| `LAYOUT-IDIOM-COMPARE-007` | 成語近義辨析 | 官方成語與延伸比較詞的語境差異 |
| `LAYOUT-IMAGE-REASONING-008` | 看圖判斷 | 多圖選擇、推理、證據說明 |
| `LAYOUT-RHETORIC-009` | 修辭辨認與效果 | 原句、手法、效果、改寫 |
| `LAYOUT-SENTENCE-010` | 句型學習 | 官方句型、結構拆解、補句與造句 |
| `LAYOUT-MINDMAP-011` | 結構心智圖 | 主旨、段落關係、事件或概念結構 |
| `LAYOUT-DOK-012` | 深度提問 | 問題、課文證據、思考或討論任務 |
| `LAYOUT-ACTIVITY-013` | 課堂活動 | 任務步驟、分組方式、時間與成果 |
| `LAYOUT-EXIT-014` | Exit Ticket | 課末短答、自評或應用題 |

## 選擇原則

1. 先確認 LKB 知識節點。
2. 再確認 Learning Module 的學習任務。
3. 根據年級與資訊量選擇 Layout。
4. 最後才套用角色與 Style DNA。

不得因偏好某個風格，而強迫所有內容使用相同版型。

## 成語版型規則

### 官方成語教材卡

只呈現來源教材已有的：

- 成語
- 對應生字
- 教材詞義
- 教材例句
- 教材教學提醒（有則保留）

### 學習延伸版型

可引用已核准 Learning Modules 中的：

- 情境理解
- 易誤用
- 近義或反義辨析
- 看圖判斷
- 造句應用
- 生活連結

延伸比較詞不得混入本課官方成語清單。

## 下一步

每一個 Layout ID 後續需建立獨立檔案，並依 `schemas/layout-dna.md` 補齊：

- 區域配置
- 文字上限
- 插圖比例
- 適用年級
- Learning Module 映射
- Style／Role 相容性
- 禁止事項
