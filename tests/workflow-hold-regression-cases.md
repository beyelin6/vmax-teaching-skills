# V-MAX Workflow HOLD Regression Cases 1.0

## 用途

本檔用真實工作流失敗案例檢查 V-MAX 在新對話／重跑時是否仍遵守 Teacher UI、STEP 1 邊界與 STEP 2.5 語文分析規格。

---

## CASE W-01｜STEP 1 不得提前進視覺／情境

### 輸入情境
教師要求：重新開始、從 STEP 1 跑、完成後停等確認。

### PASS 必須包含
- 教師可讀 `STEP 1｜教材定錨` 卡
- 課名／作者／年級冊別／文體
- 課文結構或詩節
- 完整教材生字
- 教材詞語
- 教材成語
- 教材語文活動
- 來源或待確認處
- `HOLD 1`

### BLOCKER
- raw JSON 作為主要確認畫面
- `Mode A (Drama)` / Field Trip / RPG 等情境模式
- `visualStructureRecommendation`
- Scenario Wrapper 已選定
- Character 已選定
- Style Recipe 已選定
- 頁數／版型已決定

### 預期分類
出現上述任一項：`PREMATURE_DESIGN_DECISION` 或 `MISSING_INTERFACE`

---

## CASE W-02｜STEP 2.5 必須先做形近字分析，再推薦

### 輸入情境
HOLD 1 已確認，進入 `STEP 2.5 語文輻射`。

### PASS｜形近字
每一組教師可見資訊至少包含：
- 目標字／比較字
- 注音
- 部首
- 常用詞
- 核心字義
- 共同／差異部件
- 易混淆點
- 辨認提示
- 記憶提示（適合才給）
- 推薦指數 1–5
- 詳細理由
- A/B/C/D/E 教學建議
- P1/P2/P3/PX 預習單建議
- 同冊紀錄

### PASS｜多音字
- 各讀音
- 語意
- 教材／生活情境
- 推薦指數與理由
- 教學建議
- 預習單建議與同冊去重

### PASS｜成語
- 推薦指數與理由
- 教學層級
- 理解需求
- 定義／例句等資料可存在，但不能取代推薦判讀
- 不在此鎖死漫畫格數或頁型

### BLOCKER
- 只輸出 `vocabulary[]` raw JSON
- 形近字只有字群＋推薦，沒有分析
- 多音字只有讀音表，沒有教學價值判讀
- 成語只有 definition/context/example，沒有推薦與教學層級
- 直接進 Slide Architecture

### 預期分類
`MISSING_INTERFACE / INCOMPLETE_ANALYSIS / PREMATURE_SLIDE_DECISION`

---

## CASE W-03｜預習單 3–5 組不得裁切正式教學

### PASS
- 正式教材生字完整保留
- 正式 Knowledge Lab 無 3–5 組硬上限
- 預習單從形近字／多音字中精選約 3–5 組
- P3/PX 只表示預習單不放，不等於正式教學刪除
- 同冊預習單重複字群預設 PX

### BLOCKER
- 因預習單空間刪掉正式生字
- 把 P3 當 D
- 為湊 3–5 組加入低價值內容

---

## CASE W-04｜所有 HOLD 教師介面優先

### PASS
1. Teacher Confirmation Card
2. 明確 HOLD
3. 簡短決策方式
4. machine payload 預設隱藏

### BLOCKER
- JSON/YAML 先於教師卡
- 只有 machine payload
- 要教師自己讀 schema 才能決定

---

## CASE W-05｜STEP 2.5 與 Knowledge Lab 不可合併

### PASS
- STEP 2.5：分析、推薦、教師選擇、預習單選擇
- 後段 Knowledge Lab：在 Lesson/Session/Scenario/Character 已確認後，才分 Chunk、決定位置、視覺關係與頁面

### BLOCKER
- STEP 2.5 直接決定頁數／漫畫格／Layout
- 後段 Knowledge Lab 再次推翻 STEP 2.5 已確認教學範圍

---

## 整體 PASS 條件

```yaml
workflow_hold_regression:
  step1_teacher_ui: PASS
  no_premature_visual_decision: PASS
  step2_5_analysis_preserved: PASS
  step2_5_recommendation_interface: PASS
  prestudy_scope_separated: PASS
  hold_teacher_ui_global: PASS
  selection_vs_orchestration_separated: PASS
```

只要其中一項 FAIL，不應宣告「工作流回歸測試完成」。