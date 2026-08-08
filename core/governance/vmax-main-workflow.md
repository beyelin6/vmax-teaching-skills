# V-MAX Main Workflow 1.1

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
→ Lesson Visual Map Strategy
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
7. Lesson Visual Map Strategy：判斷 `OPEN / CLOSE / BOTH / OFF`、用途、整體結構與 Reveal Guardrails。此階段只決定整課理解圖策略，不先畫頁面；正式視覺化在 Visual Grammar / Slide Architecture 階段完成。
8. Scenario Wrapper：由 AI 看懂課文後提出最多 1–3 個候選，可 OFF。
9. Character Topology / Cast：先角色功能再選角色，Wrapper 不綁固定卡司。
10. Knowledge Lab：來源先行、教師選擇、AI 組織比較與視覺化。
11. Visual Grammar / Slide Architecture：先認知關係，再決定畫面序列與頁面；若 Lesson Visual Map 已啟用，在此轉成實際學生版頁面。
12. Style Recipe：最後決定媒材與美術語言，不反推教學。
13. 代表頁驗證：先驗證關鍵頁型、Lesson Visual Map、角色、文字與視覺一致性。
14. 全量 Renderer：依已鎖定設計生成，不擅自改課程。
15. Quality Gate：教學正確、視覺理解、Lesson Visual Map、Visual Drift、中文字、Regression、Teacher Effort 均需過關。
16. Lesson Learning：每課必跑，區分 lesson-specific、global candidate、one-off exception；任何全域升級需教師批准。

## Lesson Visual Map 決策原則

- Lesson Visual Map 是學生可見的整課理解圖，不取代 Lesson Map。
- 不因「每課都要有心智圖」而強制啟用。
- `OPEN` 不得提前揭露需要學生推論的結論。
- `CLOSE` 可整理已確認的主旨、結構與高價值語文焦點。
- 圖像結構依文體與理解關係產生，不固定樹狀心智圖。

## 教師主權

教師不需要每一步都被詢問；只有會改變教學方向、課堂節奏、情境世界、角色卡司、知識取捨或正式輸出的決策才進確認點。

AI 的任務是減少決策疲勞：先分析、縮小候選、說明差異，再讓教師決定。

## 禁止反向依賴

- 不因 NotebookLM 批次限制切 Lesson / Session。
- 不因現成角色改 Scenario Wrapper。
- 不因畫風漂亮改 Text DNA 或 Teacher Intent。
- 不因 Renderer 做不到而刪掉已 LOCKED 教學重點。
- 不因舊 76 種風格庫而讓教師重新面對大型選單。
- 不因 Lesson Visual Map 是高價值頁型就每課固定生成。

## 核心金句

> 先把教學設計對，再交給當下最會呈現的 AI。

> V-MAX 的主流程由學習邏輯決定，不由平台能力決定。
