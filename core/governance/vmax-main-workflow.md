# V-MAX Main Workflow 1.0

## 定位

本檔定義 V-MAX 教材製作的正式主流程與教師確認點。平台、Renderer、NotebookLM、Gemini、ChatGPT、Canva 等都不得反向改寫此核心順序。

## 正式主流程

```text
教材定錨
→ AI 教學價值判讀
→ Teacher Intent Lock
→ Lesson Map
→ 補充內容／學習框架候選
→ Session Map
→ Scenario Wrapper
→ Character Topology / Cast
→ Knowledge Lab
→ Visual Grammar / Slide Architecture
→ Style Recipe
→ 代表頁驗證
→ 全量 Renderer
→ Quality Gate
→ Lesson Learning
```

## 各階段要點

1. 教材定錨：來源真值、課文、字詞、教材活動先確認。
2. AI 教學價值判讀：教材原有與 AI 判讀分欄，教師最後決策。
3. Teacher Intent Lock：採 `PROPOSED → CONFIRMED → LOCKED`。
4. Lesson Map：先決定整課理解旅程，不先切頁。
5. 補充內容／學習框架候選：可選，不強制；外部補充要保留 provenance。
6. Session Map：AI 依內容自然切堂，教師確認後才進完整 Slide Architecture。
7. Scenario Wrapper：由 AI 看懂課文後提出最多 1–3 個候選，可 OFF。
8. Character Topology / Cast：先角色功能再選角色，Wrapper 不綁固定卡司。
9. Knowledge Lab：來源先行、教師選擇、AI 組織比較與視覺化。
10. Visual Grammar / Slide Architecture：先認知關係，再決定畫面序列與頁面。
11. Style Recipe：最後決定媒材與美術語言，不反推教學。
12. 代表頁驗證：先驗證關鍵頁型與角色／文字／視覺一致性。
13. 全量 Renderer：依已鎖定設計生成，不擅自改課程。
14. Quality Gate：教學正確、視覺理解、中文字、Regression、Teacher Effort 均需過關。
15. Lesson Learning：每課必跑，區分 lesson-specific、global candidate、one-off exception；任何全域升級需教師批准。

## 教師主權

教師不需要每一步都被詢問；只有會改變教學方向、課堂節奏、情境世界、角色卡司、知識取捨或正式輸出的決策才進確認點。

AI 的任務是減少決策疲勞：先分析、縮小候選、說明差異，再讓教師決定。

## 禁止反向依賴

- 不因 NotebookLM 批次限制切 Lesson / Session。
- 不因現成角色改 Scenario Wrapper。
- 不因畫風漂亮改 Text DNA 或 Teacher Intent。
- 不因 Renderer 做不到而刪掉已 LOCKED 教學重點。
- 不因舊 76 種風格庫而讓教師重新面對大型選單。

## 核心金句

> 先把教學設計對，再交給當下最會呈現的 AI。

> V-MAX 的主流程由學習邏輯決定，不由平台能力決定。
