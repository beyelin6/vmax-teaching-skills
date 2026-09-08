# Codex V-MAX Skill 自動同步

## 目的

讓 `beyelin6/vmax-teaching-skills` GitHub Repository 的 `skills/` 成為 Codex 本機 V-MAX Skill 清單的唯一來源。

解決兩種情況：

1. GitHub 更新既有 Skill，但 Codex 本機仍停留在舊版。
2. GitHub 新增 Skill，但 `~/.codex/skills/` 因為本機原本沒有該資料夾而完全看不到。

## 安裝模式互斥

本文件只適用於同步模式。若 repository 已透過 `.codex-plugin/plugin.json` 被 Codex Plugin discovery 載入，請不要再執行同步腳本；Plugin 與同步目錄會暴露相同 skill name，造成來源與版本優先順序不明。若要使用同步模式，先停用另一個來源，再重新啟動 Codex。

ChatGPT Work 的 Launcher 是第三種平台專用方式，只保存一個 Launcher，不批次保存 repository `skills/` 模組；它不與 Codex Plugin 或同步模式互相替代。

## 核心腳本

### `scripts/sync_codex_skills.ps1`

功能：

- 建立或更新本機 GitHub cache。
- 掃描 Repository 內所有 `skills/*/SKILL.md`。
- 新 Skill：自動建立到 `~/.codex/skills/<skill-name>/`。
- 舊 Skill：鏡像更新整個目錄。
- Skill 內 GitHub 已刪除的舊檔：本機對應 V-MAX Skill 目錄同步移除。
- 非 V-MAX 的其他 Codex Skill：不碰。
- 產生 `~/.codex/skills/.vmax-managed-skills.json` 作為同步回條。

手動執行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\sync_codex_skills.ps1
```

預覽、不寫入：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\sync_codex_skills.ps1 -DryRun
```

## Windows 登入自動同步

### `scripts/enable_codex_skill_auto_sync.ps1`

一次性執行：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\enable_codex_skill_auto_sync.ps1
```

完成後，會在目前使用者的 Windows Startup 建立：

`V-MAX-Codex-Skill-Sync.cmd`

每次登入 Windows 時：

1. 從官方 V-MAX GitHub main branch 取得最新版 `sync_codex_skills.ps1`。
2. 更新本機 V-MAX repository cache。
3. 重新掃描 GitHub `skills/`。
4. 將所有 V-MAX Skills 鏡像到 `~/.codex/skills/`。

因此 GitHub 未來新增 Skill，不需要人工逐一重新安裝。

## 停用自動同步

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\enable_codex_skill_auto_sync.ps1 -Disable
```

只會移除 V-MAX 的 Windows Startup entry，不會刪除已安裝 Skills。

## 驗證

同步後檢查：

```powershell
Get-Content "$HOME\.codex\skills\.vmax-managed-skills.json"
```

或檢查指定 Skill：

```powershell
Get-Content "$HOME\.codex\skills\traditional-chinese-font-safety\SKILL.md" | Select-String "版本"
```

目前 `traditional-chinese-font-safety` 應顯示 `1.2.0` 或之後的最新版。

## 安全邊界

- 只同步 Repository `skills/` 下、且含 `SKILL.md` 的資料夾。
- 不會對 `~/.codex/skills/` 根目錄做整體 `/MIR`，因此不會刪除其他來源的 Codex Skills。
- `/MIR` 只作用在單一已識別的 V-MAX Skill 目錄，使該 Skill 內容與 GitHub 一致。
- 每個 Skill 先同步到暫存目錄，再以備份／替換方式更新；替換失敗會嘗試恢復上一版。
- 首次使用 `-DryRun` 會建立暫存 cache 預覽，不會要求本機先存在 cache，也不會留下暫存目錄。
- 自動同步會優先選用 `pwsh.exe`，找不到時才使用 `powershell.exe`。
- GitHub cache 更新採 `fetch + reset --hard origin/main + clean -fd`，cache 僅作同步來源，不應存放私人修改。
- 自動啟用器只從 `https://raw.githubusercontent.com/beyelin6/vmax-teaching-skills/main/` 取得同步腳本。

## 故障排除

### 找不到 `git`

安裝 Git for Windows，重新開啟終端機後再執行同步。

### GitHub 暫時無法連線

同步會失敗，但既有 `~/.codex/skills/` 不會被整體刪除。下次登入或手動重新執行即可。

### Codex 還看不到剛新增的 Skill

1. 先檢查 `.vmax-managed-skills.json` 是否列出該 Skill。
2. 確認 `~/.codex/skills/<skill-name>/SKILL.md` 存在。
3. 若檔案已存在但目前 Codex session 仍看不到，開啟新的 Codex session，讓 Skill discovery 重新載入。

## 建議操作原則

- GitHub 是規格與 Skill Source of Truth。
- `~/.codex/skills/` 是執行快取／安裝層，不在本機直接維護 V-MAX Skill 正式版本。
- 要修改 Skill：改 GitHub，再同步。
- 不要在 Codex Skill 目錄直接做長期手動修補，避免下次鏡像同步被覆蓋。

## 簡報驗證器的安裝後使用

使用已載入 vmax-image-renderer 技能內 `scripts/validate_presentation.py` 的絕對路徑。它讀取 Skills 根目錄的 `.vmax-managed-skills.json`，從 cache_dir 找到同次同步的完整 scripts/core；不依賴課程目前目錄。Plugin 模式直接從 checkout 找到 canonical。自訂 CacheDir 同樣可用。

Python 依賴只需在選定環境安裝一次：`python -m pip install "jsonschema>=4.18,<5"`。缺依賴會顯示設定錯誤，不得把錯誤當作 QA PASS。若只是單獨複製技能而沒有完整 Repository，可用 `--repo-root` 指定完整最新 checkout。詳細操作依 Renderer 的 Render Request Schema。
