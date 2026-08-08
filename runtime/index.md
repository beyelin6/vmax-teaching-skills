# V-MAX Runtime Index 1.0

## 目的

本檔是 V-MAX 多課並行的 Runtime 總索引。任何 AI 在開始或續跑課程前，先讀本檔，再讀對應課程的獨立 state。

核心原則：

> 一課一個 Runtime State；切換課程不覆蓋其他課的進度。

---

## Runtime Registry

```yaml
runtime_registry_version: 1.0
active_lesson_id: zh-4a-l01-water-land-athletes
lessons:
  zh-4a-l01-water-land-athletes:
    grade_volume: 四上
    lesson_number: 第一課
    title: 水陸小高手
    state_file: runtime/lessons/zh-4a-l01-water-land-athletes.md
    status: IN_PROGRESS
    current_stage: HOLD_2
    next_allowed_stage:
      - STEP_2_5
```

---

## Lesson ID 規則

建議採穩定、平台中立 ID：

`{subject}-{grade_volume}-{lesson_number}-{short-slug}`

例如：

- `zh-4a-l01-water-land-athletes`
- `zh-4a-l02-after-school`
- `zh-4a-l03-basketball-dream`

顯示名稱可改，Lesson ID 不應因課名微調而變動。

---

## 啟動／切換規則

### 續跑既有課
1. 依教師指定的冊別／課次／課名，在本 Index 找 lesson_id。
2. 讀取該 `state_file`。
3. 依該課 `next_allowed_stage` 繼續。
4. 不得讀另一課的 state 來推測本課進度。

### 開始新課
1. 建立新的 lesson_id。
2. 建立新的 `runtime/lessons/{lesson_id}.md`。
3. 在本 Index 新增 registry entry。
4. 只有教師正在操作的課可設為 `active_lesson_id`。
5. 不得覆寫既有課的 state。

### 切換課程
切換 `active_lesson_id` 只改目前工作焦點，不刪除、不重設其他 lesson state。

---

## 狀態值

建議 lesson `status`：

- `NOT_STARTED`
- `IN_PROGRESS`
- `WAITING_CONFIRMATION`
- `BLOCKED`
- `RENDERING`
- `DELIVERY_PENDING`
- `COMPLETED`
- `ARCHIVED`

---

## 核心金句

> 對話可以同時談很多課；Runtime 必須知道每一課各自停在哪裡。
