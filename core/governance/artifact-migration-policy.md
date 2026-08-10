# V-MAX Artifact Migration Policy 1.0

## 定位

本規則處理舊版 checkpoint / portable artifact 在新版 V-MAX 或不同平台重新使用時的 schema 相容問題。

核心原則：

> Schema 舊，不等於教材要重做。

> 能無損升級就 migration；缺欄位只補缺欄位；只有會改變教師決策時才重新確認。

## Migration 流程

1. 讀 artifact 的 `artifact_type / schema_version / vmax_version / teacher_approved`。
2. 讀目前 target skill 的 `skill_io_contract`。
3. 比較 required fields。
4. 分類：
   - `COMPATIBLE_AS_IS`：直接使用。
   - `MIGRATE_LOSSLESS`：只做 schema rename / metadata 補齊。
   - `FILL_MISSING_FIELDS`：只補新技能真正要求的欄位。
   - `TEACHER_RECONFIRM_REQUIRED`：新欄位會改變 Teacher Intent / HOLD / 教學決策。
   - `INCOMPATIBLE_ARTIFACT`：內容本質不足以供目標技能使用。
5. migration 後建立新 artifact version，保留 upstream provenance。

## 禁止事項

- 不得因 `schema_version` 舊就重跑教材轉錄／教學分析。
- 不得把 migration 當成重新解讀 Teacher Intent 的機會。
- 不得丟失原 artifact ID、來源、核准狀態與上游鏈。
- 不得靜默改寫教材正式文字。

## 建議 Metadata

```yaml
migration:
  source_artifact_id:
  source_schema_version:
  target_schema_version:
  migration_type: COMPATIBLE_AS_IS | MIGRATE_LOSSLESS | FILL_MISSING_FIELDS | TEACHER_RECONFIRM_REQUIRED
  changed_fields: []
  preserved_teacher_decisions: []
  migrated_at:
```

## 失敗分類

`ARTIFACT_SCHEMA_UNKNOWN / LOSSY_MIGRATION / MIGRATION_RECOMPUTED_UPSTREAM / MIGRATION_DROPPED_TEACHER_DECISION / MIGRATION_RECONFIRMATION_SKIPPED`

## 核心金句

> 舊資料應該被升級，不應該被遺忘；老師確認過的內容更不應因換平台而重算。
