# V-MAX Lesson Visual Map 1.1

## 定位

Lesson Visual Map（圖像式課文心智圖）是 V-MAX 的高價值「整課理解視覺」。

它不是傳統密集心智圖，也不是把整課文字縮小塞進一張圖，而是：

> 用一張有結構、有畫面感的整體圖像，加上少量關鍵文字，讓學生快速掌握「這一課在教什麼、各部分怎麼連起來、重點在哪裡」。

核心原則：

> Lesson Visual Map 不是把內容縮小，而是把整課變成學生一眼能看懂、之後也能回想的理解地圖。

> 一旦教師已選定／偏好整課圖像心智地圖，它就是 downstream invariant，不得在簡報大綱、Slide Architecture 或 Renderer 階段靜默消失。

---

## A. 系統位置

```text
Text DNA / Teacher Intent
        ↓
Lesson Map / Director Intent
        ↓
Lesson Visual Map Strategy
        ↓
Slide Outline 明確占位
        ↓
Visual Grammar / Slide Architecture
        ↓
Style Recipe / Renderer
```

Lesson Visual Map 不取代 Lesson Map；Lesson Map 是教師／系統的教學結構，Lesson Visual Map 是學生可見的整課理解視覺。

全文導航頁回答「這課有哪些站、怎麼走」；Lesson Visual Map 回答「這整趟旅程到底在學什麼、這些內容彼此怎麼連起來」。

---

## B. 模式

### LVM-OPEN｜開課版
用途：在細部教學前建立整體感。

- 先看整課全貌
- 看見段落／詩節／事件／場景關係
- 預告核心閱讀焦點，但不提前爆雷
- 圖像多、文字少

### LVM-CLOSE｜收束版
用途：學完後整理、複習、遷移。

- 回顧整課結構
- 串起主旨、重要內容、語文焦點
- 建立考前快速回想索引
- 可呈現已經透過教學確認的主旨與結構

### LVM-BOTH
若一課同時需要「先建立全貌」與「學後重整」，可以開課版＋收束版各一張；兩張不得只是同圖複製。

---

## C. 教師偏好／選定後的持續性規則

### C1. 尚未選定時
Lesson Visual Map 可由 AI 依文本結構與理解增益提出 `OPEN / CLOSE / BOTH / OFF` 建議。

### C2. 教師已選定或明確表達偏好時
若教師已確認本課需要整課圖像心智地圖，或已把它列為穩定教材偏好：

- 狀態不得自動改回 `OFF`
- 簡報大綱必須出現明確項目：`整課圖像心智地圖`／`Lesson Visual Map`
- 必須標記位置：開課、收束或兩者
- Slide Architecture 必須保留其 `stable_id`
- 頁數估算必須計入
- Renderer 不得因頁數、風格、版面或批次限制刪除
- 若平台能力受限，只能改呈現方式，不得刪除教學功能

只有教師明確取消，才可移除。

### C3. 大綱可見性
禁止把已選定 LVM 只藏在：
- `Lesson Visual Map Strategy`
- Visual Grammar metadata
- YAML / machine payload
- Renderer note

教師查看簡報大綱時，必須直接看得到它。

建議大綱格式：

```text
整課圖像心智地圖｜OPEN
目的：先看見全文／詩節／事件的整體關係
位置：正式細讀前

或

整課圖像心智地圖｜CLOSE
目的：把主旨、結構與語文焦點串回同一張理解地圖
位置：單課收束
```

---

## D. 啟用建議

優先考慮 Lesson Visual Map，當：
- 學生需要先建立全文全貌，否則容易陷入細節。
- 課文有清楚場景、事件、段落、詩節、觀點或結構路徑。
- 本課有多個語文焦點，需要一張圖重新串回文本。
- 課文適合用整體視覺模型幫助記憶。
- 教師希望學生在複習時有一張可快速回看的整課地圖。

若教師尚未選定，且課文本身極短、總圖會提前揭露關鍵推論，AI 才可建議 OFF；不得因「想省頁數」而關閉。

---

## E. 必要內容欄位

不是全部塞入，但至少選 3–5 類真正重要元素：

```yaml
lesson_visual_map:
  status: OFF | OPEN | CLOSE | BOTH
  selection_source: AI_RECOMMENDATION | TEACHER_CONFIRMED | TEACHER_STABLE_PREFERENCE
  stable_id:
  outline_slot_required: true | false
  purpose:
  central_message:
  structure_path: []
  key_scenes_or_images: []
  key_language_focus: []
  main_idea_or_feeling:
  transfer_or_extension:
  reveal_guardrails: []
```

若 `selection_source` 為 `TEACHER_CONFIRMED` 或 `TEACHER_STABLE_PREFERENCE`：

```yaml
outline_slot_required: true
silent_removal_allowed: false
```

---

## F. 文體與視覺結構

- 童詩／新詩：意象旅程圖、畫面串聯圖、雙軌對照圖、節奏／情感路徑。
- 記敘文／故事：事件歷程、情緒轉折、起因—經過—結果、證據—人物特質。
- 寫景文／遊記：遠近景、移步換景、觀看路徑、感官地圖。
- 說明文：概念模型、分類結構、流程因果、整體—部分。
- 人物文：事件證據—人物特質、行動／語言／選擇關係圖。
- 議論／說理：觀點—理由—證據—結論。

禁止每課固定同一棵樹、同一放射圖。

---

## G. 圖像設計原則

1. 圖像先行，文字輔助；不得變成摘要表。
2. 5–10 秒內能抓到整課主軸。
3. 每條線／每個區塊都代表真正的文本關係。
4. 插圖必須參與理解，不是裝飾。
5. 不把所有生字、成語、修辭硬塞進同一張。
6. 正式中文字以可靠文字層呈現。
7. 資訊過多時刪減或拆成 OPEN／CLOSE，不以縮小字體解決。

---

## H. Reveal Policy

```yaml
reveal_policy:
  open_map: preview_without_spoiler
  close_map: confirmed_learning_summary
```

開課版保護學生發現空間；收束版可以呈現已確認的主旨、結構與語文發現。

---

## I. Outline / Renderer Quality Gate

若本課 LVM 已確認，出稿前必查：

- `outline_contains_lesson_visual_map: true`
- `stable_id_preserved: true`
- `page_estimate_includes_lvm: true`
- `renderer_contains_lvm: true`
- `visual_relation_matches_lesson_structure: true`
- `not_reduced_to_text_summary: true`

任一失敗，標記：

- `LVM_OUTLINE_DROPPED`
- `LVM_DOWNSTREAM_DROPPED`
- `LVM_FUNCTION_DRIFT`
- `LVM_TEXT_WALL_FAIL`

不得宣告簡報大綱或完整簡報 PASS。

---

## J. 與預習單的關係

Lesson Visual Map 不等於預習單。

- 預習單：學生先讀、先找、先寫、先想。
- Lesson Visual Map：建立整課整體理解與回想索引。

預習單可放簡化版，但不能因此刪掉已確認的簡報整課圖像心智地圖。

---

## 核心金句

> 一張好的整課圖，不是把每個重點都塞進去，而是讓孩子知道這些重點彼此怎麼連在一起。

> 全文導航告訴孩子「要走哪些站」；Lesson Visual Map 告訴孩子「這整趟旅程到底在學什麼」。

> 教師已選定的整課圖像心智地圖，必須在大綱裡看得見，也必須一路活到最後成品。