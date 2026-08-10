# V-MAX Teaching Skills

V-MAX 是一套平台中立的臺灣國小國語教材工作流與可攜 Skill 系統，可由 ChatGPT、Claude、Codex、Gemini Spark 等相容執行器載入同一套 canonical 規格。

## 核心原則

- GitHub 保存 canonical Skill、policy、schema、adapter 與 quality rule。
- Google Drive 保存教師跨裝置需要查找、續作與交付的 checkpoint、來源與成品。
- Skill 保存方法與工作流；Library 保存可重用的風格、角色、版型與教學資源。
- 已核准資料不重算；Golden Path 定義完整課程如何形成，Checkpoint Resume 定義已形成資料如何被重用。
- 每課內容、頁數與教學模組都必須動態判斷，不使用固定頁數模板。
- 正式課堂視覺成品預設為 16:9 圖文資訊圖表 PDF；PPTX 僅在教師明確要求時選配。

## 跨平台入口

新的執行器先讀：

1. `V-MAX_UNIVERSAL_BOOTSTRAP.md`
2. 對應 `adapters/` platform adapter
3. `V-MAX_BOOTSTRAP.md`
4. `V-MAX_MANIFEST.md`
5. `runtime/lesson-state.md`
6. 目標 `skills/<name>/SKILL.md`

Skill 的通用封裝規則見：

`core/governance/universal-skill-packaging-standard.md`

## 主要 Skill 路由

### 教材與知識層
- `chinese-textbook-transcriber`
- `chinese-lesson-knowledge-builder`
- `lesson-content-master-builder`
- `learning-module-builder`
- `teaching-strategy-builder`

### 教學執行與續跑
- `vmax-golden-path-executor`
- `vmax-checkpoint-resume`
- `digital-interaction-planner`
- `four-learning-open-class-planner`

### 學生教材
- `prestudy-worksheet`：預習單內容選擇與題目設計層
- `vmax-chinese-preview-worksheet`：A／B 雙版本視覺 Renderer、300 dpi PNG／PDF／Drive 交付層
- `postlesson-short-writing-worksheet`：課後短文／童詩 Bonus 學習單

預習單標準鏈：

`CP_PRESTUDY_INPUT → prestudy-worksheet → PRESTUDY_WORKSHEET_SOURCE → vmax-chinese-preview-worksheet → PNG / PDF / Drive`

### 簡報與圖文輸出
- `slide-script-generator`
- `notebooklm-renderer-script`
- `presentation-engine`
- `infographic-pdf-lesson-deck`

### 品質、歸檔與演化
- `vqs-quality-validator`
- `lesson-package-delivery`
- `google-drive-lesson-archive`
- `teaching-memory-recorder`

## 平台 Adapter

- `adapters/chatgpt.md`
- `adapters/claude.md`
- `adapters/codex.md`
- `adapters/gemini-spark.md`

平台只負責載入與執行，不得各自複製或改寫 V-MAX Core。

## 核心金句

> V-MAX 是教學作業系統；AI 平台只是不同的執行器。
