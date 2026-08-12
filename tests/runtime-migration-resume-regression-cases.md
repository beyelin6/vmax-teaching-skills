# V-MAX Runtime Migration Resume Regression Cases 1.0-draft

## Purpose
驗證 legacy Runtime 遷移後不會逼教師重複確認已明確確認過的內容，也不會把舊 evidence 偷升格成新版 lock。

## M1｜Confirmed Legacy HOLD Carry-forward
Given：HOLD 2 / 2.5 / 2.6 在 legacy Runtime 有明確 teacher confirmation，migration review 標 `MIGRATED_CONFIRMED`。
When：migration LKB 被核准。
Then：不得再次停 HOLD 2 / 2.5 / 2.6；逐節點掃描到第一個 `NEEDS_REVIEW / NOT_RUN`。
Fail：`REASKED_ALREADY_CONFIRMED_MIGRATION_HOLD`

## M2｜Evidence Is Not New Lock
Given：legacy Scenario / Character / Style 曾確認。
Then：若新版另有 Scenario Lock / Character visual asset / Style Recipe→Lesson Skin→Typography→Gate B 語義，legacy evidence 只能保存為 evidence，不自動標新版 lock confirmed。
Fail：`MIGRATED_EVIDENCE_PROMOTED_TO_NEW_LOCK`

## M3｜Upstream Invalidation
Given：legacy HOLD confirmation 已 carry forward。
When：新 LKB 修改／刪除該 HOLD 引用的知識節點，或教師改變語文範圍／成語／Teacher Intent。
Then：受影響 migrated confirmation 必須失效並重開。
Fail：`MIGRATED_CONFIRMATION_INVALIDATED_BY_UPSTREAM_CHANGE`

## M4｜First Lesson Runtime 03 Resume Target
Runtime：`V-MAX_State_四上_第一課_水陸小高手_03`
Current：`LKB_REVIEW`
Evidence：HOLD 2 / 2.5 / 2.6 / Teacher Intent = `MIGRATED_CONFIRMED`；Teaching Skill Selection / Budget Draft = `NEEDS_REVIEW`；Gate A = `NOT_RUN_NEW_V1`。

Expected after LKB approval, provided LKB does not invalidate migrated decisions：

`Teaching Skill Selection → Lesson Budget Draft → Gate A`

Forbidden：
- 回問相同 HOLD 2 / 2.5 / 2.6
- 跳 Scenario Lock
- 跳 FULL_RENDERER

## PASS
M1–M4 contract inspection PASS when `core/governance/runtime-migration-resume-policy.md` and Executor E2 agree with Runtime 03 fields.
