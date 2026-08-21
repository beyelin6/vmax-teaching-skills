# NotebookLM Output Contract

版本：0.2.0（開學可用版）

## 定位

NotebookLM 是 V-MAX 的渲染器之一，主要負責：

- 圖片式教學簡報
- Podcast 式課文導讀
- 語文知識音訊
- 寫作教練音訊

NotebookLM 不作為唯一知識來源，也不得自行改變已核准的教材內容、Lesson Flow、角色功能與教學順序。

## 歷史脈絡與設計原因

V-MAX 早期曾直接由 AI 生成簡報，但當時常出現：

- 版面過度文字化
- 圖像與文字割裂
- 視覺風格不一致
- 新增頁面後整體美感下降
- 可編輯 PPT 雖方便修改，但難以穩定維持整套視覺品質

因此，Bee 老師把「教材內容與教學設計」和「最終視覺渲染」分開：先由 V-MAX 決定內容、結構、角色、版型與圖片意圖，再交給 NotebookLM 產生高一致性的圖片式簡報。

此設計不是對 NotebookLM 的永久綁定，而是 V-MAX 的 Renderer-Agnostic 原則：

> 先保證教學內容與視覺規格正確，再交給當下最擅長呈現的渲染器。

NotebookLM 是目前偏好的圖片式簡報與 Podcast Renderer，但未來可被其他具備更佳視覺一致性、排版、美感或音訊能力的平台替換。

## Renderer-Agnostic Pipeline

```text
Lesson Knowledge / Lesson DNA
        ↓
Teaching Flow / Structure / Layout
        ↓
Theme / Visual DNA / Character DNA
        ↓
Slide Script / Visual Intent
        ↓
Renderer Adapter
        ├─ NotebookLM
        ├─ ChatGPT
        ├─ Gemini
        ├─ Canva
        └─ Future Renderer
        ↓
Rendered Presentation / Audio
```

Core 層不得依賴 NotebookLM 專屬語法。NotebookLM 特有操作、限制與提示規則只存在本 Adapter。

## 必要輸入

NotebookLM 輸入分成兩種用途，不得把兩者混成單一來源：

### A. Knowledge Source Package

負責讓 NotebookLM 讀取完整、可追溯的教材與核准知識：

- `source-master.md`：符合 `core/schemas/vmax/source-master.schema.json` 的來源主檔。
- `approved-teaching-selection`：教師已確認的選教結果與版本。
- `learning-modules`／`teaching-strategy`：已核准 companion objects 及其版本。
- 來源層、證據位置、provenance 與教師／AI 分層。

### B. Slide／Audio Package

負責 NotebookLM 簡報工作室與語音／音訊流程：

- `slide-script.md`：符合 `core/schemas/vmax/slide-script.schema.json` 的逐頁簡報內容主檔。
- `visual-profile.md`：Theme、配色、插圖、角色、卡片、留白與字級。
- `guide-character-profile.md`：引導者角色 DNA、出場功能與禁止事項。
- `output-manifest.md`：來源版本、衍生關係與輸出追溯。
- Renderer Script／Visual YAML：僅作執行衍生物，不得反向修改 Slide Script。

生成指令只描述如何使用對應輸入包，不得重新決定課程順序、學生文字或教學焦點。

## 圖片式簡報規則

- 最終頁面可以不可逐項編輯。
- 內容來源必須可修改並保留版本。
- 一頁只處理一個主要學習焦點。
- 每頁需有明確視覺焦點；插圖應服務理解。
- 學生可見區不得出現答案、來源標記、內部節點或英文系統字樣。
- 官方教材、Bee 老師補充與學習延伸必須清楚區分。
- 長課文只擷取當頁需要的關鍵句，不以縮小字體塞滿頁面。
- 不得為湊頁數反向改變 Teaching Flow。

## 引導者規則

引導者可使用：

- `HOST`：開場與任務主持
- `COACH`：策略提示
- `INTERVIEW`：與課文角色對話
- `TRANSITION`：章節轉場
- `REFLECT`：課末統整
- `OFF`：詩意大圖、沉浸頁或不需角色的頁面

不得要求「每頁都加入角色」。角色只在有教學功能時出現，並維持外觀、服裝、比例、表情與說話風格一致。

## 金句規則

每課可選用：

- `課文金句`
- `Bee老師想一想`
- `學習策略句`
- `我們的金句`
- `今天帶走的一句話`

每句原則上 12～28 個中文字，一句只承載一個觀點，不使用空泛勵志語，不把 AI 詮釋冒充為作者原文。

## 結構圖規則

生成前必須指定：

```yaml
structure:
  macro:
    id:
    reason:
  micro:
    - id:
      target:
      reason:
```

全文主架構與段落副架構必須依文體、內容與學生理解需求選擇，不得所有課程都使用放射狀心智圖。

## 視覺一致性

每套簡報必須固定：

- Theme 世界觀
- 主配色與輔助色
- 背景材質
- 插圖風格
- 引導角色 DNA
- 標題框與章節標籤
- 內容卡片系統
- Icon 系統
- 留白與邊界

新增或重生頁面時，必須沿用同一套 Visual Profile。

## Podcast 輸出

音訊可選：

- `lesson_preview`：課文導讀
- `language_focus`：字群、成語、修辭與句型
- `writing_coach`：短文或作文鷹架

每段需標示功能：

```text
HOOK / EXPLAIN / MODEL / PAUSE / CHALLENGE
```

Podcast 不逐字朗讀整份簡報，而應補充聽覺理解、想像、口語示範與停頓任務。

## 圖片式成品修改方式

教師提出修改後：

1. 回到 Source Package 修改對應節點。
2. 建立 Change Request 與 Patch ID。
3. 只重建受影響的腳本、頁面或音訊。
4. 重新執行內容與視覺檢查。
5. 產生新版本，不覆蓋既有 Baseline。

## 生成後檢查

至少檢查：

- 內容是否忠於核准來源
- 是否漏字、錯字或誤植
- 學生版是否出現答案
- 引導角色是否一致
- 插圖是否符合句意
- 金句是否標示正確來源類型
- 頁面是否過度文字化
- 是否出現重複 `slides` 節點
- 是否仍符合核准 Teaching Flow

## Renderer 選擇原則

當未來有多個可用 Renderer 時，優先比較：

1. 視覺一致性
2. 圖文整合能力
3. 中文文字正確率
4. 角色一致性
5. 長簡報整套一致性
6. 圖片式簡報品質
7. 音訊／Podcast 品質
8. 局部重生成能力
9. 成本與處理時間

Renderer 可更換；Lesson DNA、Visual DNA 與 Bee Teaching DNA 不隨平台更換而重寫。
