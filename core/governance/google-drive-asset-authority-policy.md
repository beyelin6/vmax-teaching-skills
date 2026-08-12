# V-MAX Google Drive Asset Authority Policy 1.0-draft

## 定位

本政策定義 V-MAX 的永久資產邊界：

> GitHub 保存規則、技能、schema、模板與可重用文字規格；Google Drive 保存所有實際成品、半成品、核准過的視覺資產與每課 Runtime。

任何不可重建、已經人工確認、或未來需要跨平台續用的資產，不得只存在於聊天、單一 AI 平台暫存或模型記憶中。

---

## 1. Authority Split

### GitHub = System Brain
保存：
- Main Workflow / Executor / Runtime schema
- Character System / Scenario / Style / Typography 規則
- Role Library 的穩定文字規格與可重用 ID
- 技能、policy、schema、regression、adapter

GitHub 不保存每課大量實際教材圖像、簡報成品與日常半成品。

### Google Drive = Persistent Workspace
保存：
- 每課 Runtime State
- Source Master / LKB 輸出
- Storyboard / Page Ledger / Renderer Script
- NotebookLM Source / Visual YAML / Curated Briefing
- 角色基準圖、表情、姿勢、服裝變體
- Lesson Visual Identity Pack
- Style reference / Book DNA reference
- 預習單、短文單、題庫、評量、Kahoot 匯出檔
- PPTX / PDF / Google Slides / 代表頁樣張
- 所有尚未完成但需要日後接續的半成品

---

## 2. Shared Visual Asset Library

固定根目錄：

```yaml
shared_visual_asset_library:
  title: 00_V-MAX_角色與視覺資產庫
  folder_id: 1rooMvBzXHTr4IRbCm5YV6x-qgl-07k2V
  parent_library_id: 1d1vCEw-BzFiR_DyGYDM1f3aovrKODIaA
```

固定子資料夾：

```text
00_V-MAX_角色與視覺資產庫/
├── 01_角色庫/
├── 02_整冊Book_DNA/
├── 03_Style_Reference/
├── 04_共用圖示與視覺語彙/
└── 05_Lesson_Visual_Identity_Packs/
```

已建立角色實例：

```text
01_角色庫/
└── ROLE-BEE-001_Bee老師/
    ├── 01_角色設定/
    ├── 02_核准基準圖/
    ├── 03_表情姿勢/
    └── 04_服裝變體/
```

---

## 3. Character Authority

角色採雙層權威：

### Stable Role Spec
GitHub Role Library 保存：
- role_id
- 角色定位
- 教學功能
- 人格／語氣
- Visual DNA 的穩定文字規格
- 使用頻率與禁則

### Approved Visual Asset
Google Drive 保存：
- canonical portrait / full-body reference
- 核准基準圖
- 表情／姿勢 sheet
- 服裝變體
- 角色視覺版本
- 可供下次生成直接引用的圖像資產

若文字規格與已核准圖像發生衝突：
- 教學功能與角色身分規則以 GitHub 為準。
- 「角色實際長相」以 Drive 最新核准基準圖與其 asset_version 為準。

不得只靠 prompt 重新猜角色長相。

---

## 4. Lesson Visual Identity Pack

每課一旦開始產生跨教材視覺，必須建立可持久引用的 `Lesson Visual Identity Pack`，存於：

`05_Lesson_Visual_Identity_Packs/`

最低欄位：

```yaml
lesson_visual_identity:
  lesson_id:
  version:
  status: PROPOSED | LOCKED
  book_dna_ref:
  scenario_ref:
  character_refs:
    - role_id:
      asset_version:
      drive_asset_ref:
  style_recipe_ref:
  lesson_skin:
  style_reference_asset_ref:
  typography_lock_ref:
  material_modes:
    prestudy:
    short_read:
    teaching_slide:
    extension:
  drift_guardrails: []
```

此 Pack 是跨平台視覺引用層；NotebookLM Visual YAML、Canva、Gemini、Renderer prompt 等都由此轉譯，不得反過來成為視覺真值。

---

## 5. Two Production Modes

### SINGLE_LESSON_BUILD

```text
完整分析
→ Teaching Direction
→ Scenario / Character / Style / Storyboard
→ 正式簡報與代表頁
→ 簡報詳細說明 / Renderer Script
→ Lesson Visual Identity Pack
→ NotebookLM Visual YAML / Source
→ 預習單 / 短文單
→ Kahoot / 題庫 / 評量 / 其他附加文件
```

原則：正式簡報是單課最完整教學母體；後續教材繼承同一 Identity Pack，但依 Material Mode 降密度或改版面。

### BATCH_PREP_BUILD

```text
多課來源分析
→ 批次確認各課重點知識與 Teaching Direction
→ 批次確認 Scenario / Character / Style 方向
→ 建立每課 Lesson Visual Identity Pack
→ 批量產出預習單 / 短文單
→ 全部寫入 Drive
→ 未來正式上課時載回該課 Runtime + Identity Pack
→ 再完成 Storyboard / 正式簡報 / NotebookLM / 題庫
```

批次模式不要求先做完整簡報，但不得在沒有 Identity Pack 或角色核准 reference 時生成需要跨期續用的視覺教材。

---

## 6. Save-on-Approval Rule

任何下列事件成立，必須寫入 Google Drive：
- 教師核准角色長相
- 教師核准 Style reference / Lesson Skin
- 代表頁通過 Gate C
- Storyboard / Page Ledger 已達可續跑狀態
- NotebookLM YAML / Source 已可使用
- 預習單／短文單／題庫已有可用版本
- 任何半成品因額度、平台、時間中斷而需要日後續跑

禁止：只在對話說「已鎖定」但 Drive 沒有可恢復的 reference。

Failure code：`CHAT_ONLY_ASSET / APPROVED_ASSET_NOT_PERSISTED / VISUAL_REFERENCE_MISSING`。

---

## 7. Lesson Folder vs Shared Library

### Shared Library 放「可重用資產」
- 核准角色基準圖
- 通用角色 DNA visual asset
- Book DNA
- Style reference
- 共用圖示語彙

### 每課資料夾放「本課使用紀錄與本課變體」
- 本課引用哪些 role_id / asset_version
- 本課 Lesson Visual Identity Pack reference
- 本課專用服裝／道具／姿勢
- 本課代表頁與樣張
- 本課全部成品與半成品

不要在每課複製同一角色原始資產；用 reference + lesson-specific variation。

---

## 8. Platform Independence

若 ChatGPT / NotebookLM / Gemini / Canva / 其他平台額度用完或更換：

```text
讀 Google Drive Runtime
→ 讀 Lesson Visual Identity Pack
→ 讀角色 reference assets
→ 讀當前半成品
→ 從合法下一步續跑
```

不得要求教師重新描述已確認過的角色與風格。

---

## 核心金句

> GitHub 保存方法；Google Drive 保存工作。

> 角色的「規則」在 GitHub，角色的「臉」在 Drive。

> 任何已確認或未來要接著做的東西，都不能只活在聊天裡。
