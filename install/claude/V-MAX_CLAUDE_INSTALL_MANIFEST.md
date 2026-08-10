# V-MAX Claude Install Manifest 1.0

## 安裝定位

本檔定義 Claude 第一批 V-MAX portable install bundle 的內容。Claude 端為執行副本；GitHub canonical 不分叉。

## Target

```yaml
platform: CLAUDE
bundle_mode: CORE_PLUS_HIGH_FREQUENCY
runtime_status: NOT_YET_FULLY_TESTED
```

## 必帶共同核心

- `BUNDLE_MANIFEST.md`
- `V-MAX_UNIVERSAL_BOOTSTRAP.md`
- `V-MAX_MANIFEST.md`
- `adapters/claude.md`
- `core/governance/skill-io-registry.md`
- `core/governance/platform-capability-matrix.md`
- `core/governance/modular-checkpoint-execution-policy.md`
- `core/governance/universal-skill-packaging-standard.md`
- `core/governance/portable-install-bundle-standard.md`
- `core/governance/artifact-migration-policy.md`

## 第一批高頻 Skills

1. `skills/lesson-content-master-builder/`
2. `skills/prestudy-worksheet/`
3. `skills/vmax-chinese-preview-worksheet/`
4. `skills/postlesson-short-writing-worksheet/`
5. `skills/slide-script-generator/`
6. `skills/notebooklm-renderer-script/`
7. `skills/infographic-pdf-lesson-deck/`
8. `skills/google-drive-lesson-archive/`
9. `skills/vmax-checkpoint-resume/`

## Dependency Closure 特別項目

`vmax-chinese-preview-worksheet` 必須額外帶入：

- `core/export/infographic-pdf-output-contract.md`
- `core/renderer/image-first-hybrid-renderer.md`
- Skill 自身 `references/`
- Skill 自身 `assets/`

approved reference PNG 必須原 byte / blob 帶入。

其他 Skill 依各自 `SKILL.md` 明確引用補齊 dependencies。

## Claude 安裝後啟動

1. 讀 `BUNDLE_MANIFEST.md`。
2. 讀 `V-MAX_UNIVERSAL_BOOTSTRAP.md`。
3. 讀 `adapters/claude.md`。
4. 偵測當前 capability。
5. 判斷 `FULL_GOLDEN_PATH` 或 `CHECKPOINT_RESUME`。
6. 讀 Registry 與 target Skill。

## 不允許

- 不把 Claude Project / memory 當 canonical。
- 不因 Claude 缺 Drive/GitHub tool 就重算教材。
- 不在 Claude 端直接改 Teacher Intent 後視為全域規則。
- 不宣稱 Drive / GitHub 寫入成功，除非實際 capability 與驗證存在。

## 第一輪 runtime 測試

- Fixture A：同一 `PRESTUDY_WORKSHEET_SOURCE` → 預習單內容／Renderer 邊界與 A/B mode。
- Fixture B：同一 `CP_LESSON_CONTENT_MASTER` → 課後短文單。
- 回報 C-01～C-09。

## 狀態

`INSTALL_MANIFEST_READY / BUNDLE_BYTES_NOT_YET_EXPORTED / CLAUDE_RUNTIME_NOT_YET_TESTED`
