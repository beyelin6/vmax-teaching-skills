# Installation Mode Regression Cases

1. Plugin mode only：由 `.codex-plugin/plugin.json` 發現 repository `skills/`，不執行同步腳本。
2. Sync mode only：停用 Plugin discovery 後執行同步，其他 Codex skill 不受影響。
3. 雙重安裝：若 Plugin 與同步副本同時存在，文件要求擇一並重新啟動 Codex。
4. ChatGPT Work：只保存 Launcher，不批次保存 `skills/` 下的模組。
5. 切換模式：確認同名 skill 只出現一個來源，並以 GitHub current revision 為準。
