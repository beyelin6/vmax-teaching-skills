# V-MAX Adapter｜Claude 1.0

## 目的

本檔只定義 Claude 如何載入與執行 V-MAX；Claude 不得建立自己的 V-MAX 教學核心或以 Project / Skill 記憶取代 canonical files。

## 啟動契約

開始 V-MAX 任務前：

1. 讀 `V-MAX_UNIVERSAL_BOOTSTRAP.md`。
2. 讀 `V-MAX_MANIFEST.md`。
3. 判斷 `FULL_GOLDEN_PATH` 或 `CHECKPOINT_RESUME`。
4. 若有 portable artifact，優先讀 artifact，不重跑已確認上游。
5. 依 `skill-io-registry.md` 載入目標 Skill 的 `SKILL.md`。
6. 只讀當前任務需要的 references / assets / policy。

## Claude Skill 安裝原則

V-MAX Skill 應遵循 `universal-skill-packaging-standard.md`：

```text
<skill-name>/
├── SKILL.md
├── references/
├── assets/
└── scripts/
```

- `SKILL.md` 為 canonical 技能主檔。
- Claude 端安裝的是執行副本，不是新的規格權威。
- 同名 Skill 更新時先比對 canonical 版本；不得用較舊副本覆蓋 GitHub。

## 工具與 Artifact 邊界

若 Claude 當前環境具備 Drive / GitHub / filesystem / code 等工具，可依 capability matrix 實際使用。

若缺少某工具：
- 優先使用使用者提供檔案、portable artifact 或可下載來源。
- 不得宣稱已寫入 Drive / GitHub。
- 不得因缺 connector 就重算教材內容。

## Teacher Sovereignty

Claude 不自行改寫：
- Teacher Intent
- 已確認教材主檔
- 合法 HOLD 決策
- 角色 DNA
- Visual Grammar / Gold Pattern 的認知目的

## 輸出

可依當前 capability 產生：
- 教材分析與 portable MD artifact
- 預習單／短文單內容與腳本
- Renderer / NotebookLM MD
- 程式與驗證腳本
- 圖像／PDF（平台能力允許時）

完成後應保存為 V-MAX portable artifact；若無法持久化，標記 `PERSISTENCE_PENDING`。

## 失敗分類

`CLAUDE_SKILL_NOT_LOADED / CLAUDE_REQUIRED_CAPABILITY_MISSING / CLAUDE_CANONICAL_DRIFT / CLAUDE_PERSISTENCE_PENDING`

## 核心金句

> Claude 是 V-MAX 的相容執行器；Skill 可以安裝，Core 不在平台內分叉。
