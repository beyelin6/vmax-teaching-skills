# V-MAX Cross-platform Skill Sync Policy 1.0

## 定位

本規則定義 GitHub canonical Skill 如何同步到 ChatGPT、Claude、Codex、Gemini Spark 等執行平台，避免每個平台各自長成不同版本。

核心原則：

> GitHub canonical → 平台執行副本；平台副本不得反向靜默覆蓋 canonical。

## 1. Source of Truth

- GitHub：Skill / policy / adapter / schema 的 canonical source。
- Google Drive：教師 artifact、checkpoint、指南與可攜工作成果。
- 平台 Skill Manager：執行副本，不是 canonical source。

## 2. 安裝

安裝 Skill 前：

1. 讀 canonical `SKILL.md`。
2. 檢查 skill name 是否已存在。
3. 若不存在，建立平台副本。
4. 若存在，先比對版本／內容，不直接覆蓋。
5. 記錄來源 commit / canonical path（若平台可記錄）。

## 3. 更新

canonical Skill 更新時：

- 同名且平台副本未有本地客製 → 可更新。
- 平台副本已有本地客製 → 先做三方比較：canonical old / canonical new / platform local。
- 可無衝突合併 → 更新副本。
- 會改變 Teacher Intent、HOLD、artifact schema 或教學決策 → 不自動合併，標記 `SKILL_SYNC_REVIEW_REQUIRED`。

## 4. 平台端改動

平台內臨時調整分三類：

- `SESSION_ONLY`：只限當次執行，不回寫。
- `PLATFORM_LOCAL_PREFERENCE`：只屬平台介面，不進 Core。
- `CANDIDATE_CANONICAL_CHANGE`：可能值得全平台共用，需建立 proposed change 回 GitHub 審核。

不得把 Spark / Claude / ChatGPT 某次對話中的新規則直接視為全域 V-MAX 規則。

## 5. 停用與刪除

- 平台停用 Skill：只影響該平台。
- 平台刪除 Skill：只刪執行副本。
- canonical Skill 只有 GitHub 明確刪除／退役才算系統移除。

## 6. Sync Metadata

建議平台副本附帶：

```yaml
vmax_skill_sync:
  canonical_path:
  canonical_commit:
  canonical_name:
  installed_at:
  last_synced_at:
  local_customization: NONE | PRESENT
  sync_status: CURRENT | STALE | REVIEW_REQUIRED
```

平台不支援 metadata 時，可改用對應管理文件保存。

## 7. Guide Sync

以下改動發生時，除了平台 Skill 副本，也要同步：
- `docs/V-MAX_使用指南.md`
- `docs/V-MAX_中文指令速查表.md`
- Google Drive 現行指南副本

尤其包含：新平台、adapter、Skill 安裝方式、capability、checkpoint、儲存規則與中文別名。

## 失敗分類

`SKILL_SYNC_STALE / SKILL_SYNC_REVIEW_REQUIRED / PLATFORM_LOCAL_OVERRIDE_CANONICAL / CANONICAL_SOURCE_UNKNOWN / USER_GUIDE_STALE / USER_GUIDE_DRIVE_STALE`

## 核心金句

> 平台可以有不同操作介面，但 V-MAX Skill 的教學邏輯只能有一個 canonical 版本。
