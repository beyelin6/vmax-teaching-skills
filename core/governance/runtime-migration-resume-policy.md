# V-MAX Runtime Migration Resume Policy 1.0-draft

## 定位
本政策只處理 legacy Runtime 非破壞遷移後「從哪裡接回新 Golden Path」。它不得改寫一般新課的 HOLD 規則，也不得把未確認欄位當成已確認。

核心原則：

> 舊流程已被教師明確確認過的決策，可以攜帶確認證據；新流程新增、推論或缺乏證據的決策，必須在最早不確定依賴重新停下。

---

## 1. 適用條件
只有 Runtime 同時符合以下條件才啟用：

```yaml
migration:
  migration_status: REVIEWED
migration_review:
  explicitly_confirmed_legacy_fields: [...]
  recommended_reopen_point: ...
```

一般新課永遠走標準 `HOLD 1 → LKB REVIEW → HOLD 2 → HOLD 2.5 → HOLD 2.6 ...`。

---

## 2. Evidence Carry-forward
Legacy 欄位只有明確標記 `MIGRATED_CONFIRMED` / `MIGRATED_CONFIRMED_EVIDENCE` 且有 legacy evidence ref，才可視為「已在舊流程完成教師確認」。

允許 carry-forward 不等於把舊設計升格成新版 Gate/Lock。

例如：
- 舊 HOLD 2 明確確認 → 可 carry forward 教學價值判讀。
- 舊 HOLD 2.5 明確確認 → 可 carry forward 語文範圍。
- 舊 HOLD 2.6 明確確認 → 可 carry forward 成語取捨。
- 舊 Scenario 選擇雖明確確認，但新版另有 `SCENARIO LOCK` 語義時，除非 migration review 明確裁決等價，否則只作 evidence，不自動升格。
- 舊 Style 選擇不能自動等於新版 `Style Recipe → Lesson Skin Final → Typography → Gate B`。

---

## 3. Resume Algorithm
教師確認 migration 的最早 reopen checkpoint 後：

```text
1. 將該 checkpoint 寫成 confirmed / approved。
2. 依 Golden Path 往後逐節點掃描。
3. 若節點 = MIGRATED_CONFIRMED 且 evidence 完整 → 視為已完成，不重問教師。
4. 若節點 = MIGRATED_CONFIRMED_EVIDENCE 但新版語義不同 → 保留 evidence，停在新版對應 lock 前。
5. 若節點 = NEEDS_REVIEW / NOT_RUN / 缺 Drive ref → 立即停止。
6. 不得越過第一個未滿足依賴。
```

這叫 `EVIDENCE_AWARE_RESUME`，不是 `STAGE_LEAP`。

---

## 4. Mandatory HOLD Compatibility
Mandatory HOLD 不可在一般流程被刪除。

Migration 情境下，若舊 Runtime 有明確教師確認證據：
- 不要求教師為同一內容重複按一次確認。
- Runtime 必須留下 `MIGRATED_CONFIRMED` 與來源。
- 若內容因新 LKB、來源或教師意圖改變，舊確認自動失效，該 HOLD 重新開啟。

因此：

> 「不重問已確認內容」與「不准飛站」可以同時成立。

---

## 5. First Lesson Runtime 03 Resolution
對 `V-MAX_State_四上_第一課_水陸小高手_03`：
- reopen point：`LKB_REVIEW`
- HOLD 2：`MIGRATED_CONFIRMED`
- HOLD 2.5：`MIGRATED_CONFIRMED`
- HOLD 2.6：`MIGRATED_CONFIRMED`
- Teacher Intent：`MIGRATED_CONFIRMED`
- Lesson Map / Session Map / LVM：legacy confirmed evidence
- Teaching Skill Selection：`NEEDS_REVIEW`
- Lesson Budget Draft：`NEEDS_REVIEW`
- Gate A：`NOT_RUN_NEW_V1`

因此 migration LKB 核准後，若 LKB 核准內容沒有推翻舊 HOLD 2 / 2.5 / 2.6 的教師決策，合法 resume target 是：

`Teaching Skill Selection → Lesson Budget Draft → Gate A`

不是重新詢問 HOLD 2，也不是跳到 FULL_RENDERER。

---

## 6. Invalidation Rule
以下任一發生，必須重開受影響的 migrated confirmation：
- Source Truth 改變
- LKB 新版刪除／更正被舊 HOLD 引用的知識節點
- 教師明確改語文範圍
- 教師改核心成語／句型／修辭
- Teacher Intent 改變到影響舊決策

Runtime 應記：
`MIGRATED_CONFIRMATION_INVALIDATED_BY_UPSTREAM_CHANGE`。

---

## 7. Failure Codes
- `MIGRATED_CONFIRMATION_WITHOUT_EVIDENCE`
- `REASKED_ALREADY_CONFIRMED_MIGRATION_HOLD`
- `MIGRATION_STAGE_LEAP`
- `MIGRATED_EVIDENCE_PROMOTED_TO_NEW_LOCK`
- `MIGRATED_CONFIRMATION_INVALIDATED_BY_UPSTREAM_CHANGE`

---

## 核心金句
> Migration 不讓老師重做已做過的決定，也不讓系統假裝新規則以前就被確認過。

> 帶得走的是證據；需要重開的是新依賴。
