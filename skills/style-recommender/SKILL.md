---
name: style-recommender
description: 根據已核准的 Lesson Knowledge Book、Learning Modules、Teaching Strategy、角色設定與年級，推薦適合當課教材的 3 至 5 種視覺風格方案。每個方案必須說明適用理由、視覺 DNA、配色、紙張材質、插圖語言、章節標籤、版型方向與限制，並在教師確認前停止。不得固定套用上一課風格，也不得以風格壓過教材內容。
---

# Style Recommender

Machine-readable style selections MUST conform to `core/schemas/vmax/style-selection-profile.schema.json`. `style_core` is the reusable locked visual system; `page_variants` may adjust page-family composition but may not silently replace the core palette, typography, ratio, safe boundary, or character rules.

## 頁面類型風格矩陣

風格可以混搭，但混搭必須以「頁面類型」為單位，不得逐頁隨意漂移。推薦結果必須另外輸出一份 page-family matrix，至少列出：

- `page_family`：課文閱讀、語文知識、成語／四字詞語、情境漫畫、總結遷移等。
- `style_variant`：該頁型使用的插圖媒材、筆觸、色彩與構圖語言。
- `character_policy`：該頁型的人物使用策略，使用 `CANONICAL_REQUIRED`、`CANONICAL_OPTIONAL`、`SUPPORTING_FIGURE_ALLOWED`、`CHARACTER_DISCOURAGED` 或 `NO_CHARACTER`。
- `shared_invariants`：整課共用的字體、畫布比例、章節標籤、角色 DNA、留白與安全邊界。
- `consistency_rule`：同一 `page_family` 的所有頁面必須沿用同一 `style_variant`，除非教師明確核准例外。

水彩插圖、韓風漫畫等僅是示意，不是固定配方或預設答案。實際方案可依教材內容、教學功能與教師偏好推薦不同媒材、畫風、構圖與版型；只要同一頁面家族內保持一致即可。混搭的是頁面家族，不是未經說明的單頁風格。

## 使命

依每一課教材內容與教學需求，推薦最合適的視覺風格組合，並提供可供教師比較與確認的具體方案。

## 前置條件

必須讀取：

- 已核准的 Lesson Knowledge Book
- 已核准的 Learning Module Profile
- 已核准的 Teaching Strategy Profile
- 已確認或候選中的 Role Selection Profile
- `libraries/styles/index.md`
- `schemas/style-selection-profile.md`

若角色尚未確認，可以提供角色與風格的配對建議，但不得直接鎖定最終風格。

## 分析維度

至少分析：

- 文體與篇章結構
- 課文主題與核心情緒
- 故事場景或知識領域
- 年級與閱讀習慣
- 學習模組類型
- 教學活動形式
- 引導角色功能與外觀
- 圖文密度
- 是否需要流程圖、比較表、情境漫畫、心智圖或任務卡

## 推薦數量

預設推薦 3 至 5 組方案。

每組方案必須包含：

- style_id
- 方案名稱
- 適用理由
- 主要視覺語言
- 配色方向
- 背景與紙張材質
- 插圖筆觸與情境規則
- 章節標籤方式
- 頁碼系統：位置、格式、字體角色、顏色與特殊頁顯示規則
- 推薦版型
- 與角色的協調方式
- 適合的投影片類型
- 可能限制

風格推薦不得決定簡報畫布比例。方案必須承接教師已核准的 `canvas_lock`，僅允許 `4:3` 或 `16:9` 橫式；推薦方案可以改變頁面構圖與頁型變體，但不得推薦 `9:16`、A4、3:2 或其他比例，也不得在缺少或衝突的 `canvas_lock` 時繼續，應停在 `CANVAS_SPEC_BLOCKED`。

## 推薦原則

- 風格必須服務教材，不得只因熱門或美觀而推薦。
- 同一風格須能依課文類型動態調整。
- 不得沿用上一課的背景、情境、圖像符號或章節命名。
- 同一份教材可推薦不同方向，例如溫暖敘事、探險任務、清楚資訊圖，但必須說明差異。
- 風格方案可包含多個頁面家族變體；必須明確區分「課級共用 DNA」與「頁型專屬變體」。
- 頁型專屬變體只能改變插圖媒材、情境語言與局部構圖，不得破壞整課共用的字體、畫布、角色、章節標籤、留白與文字可讀性。
- Bee 老師可搭配多種風格，但其蜜蜂元素只能作為識別，不得主導整套教材視覺。
- 學生可見文字必須清楚、大字、繁體中文。
- 插圖須依內容重新生成，不以教材截圖代替情境插圖。

## 風格與角色配對

角色確認後，需檢查：

- 角色服裝與主色是否衝突
- 角色辨識色是否過度搶焦
- 角色出現頻率是否符合版面密度
- 角色是否適合該課情緒與教學功能
- 是否需要為該課調整角色配件，但不得改變核心角色 DNA

## 輸出

建立：

- `working/style-recommendation.md`
- `working/style-selection-profile.md`
- `working/page-family-style-matrix.md`

推薦完成後必須停止，等待教師：

1. 選擇推薦方案
2. 混合兩個方案
3. 指定其他風格
4. 關閉角色
5. 調整配色、材質或插圖方向

未確認前，不得啟動 Presentation Engine 的最終產出。

Only a `CONFIRMED` Style Selection Profile may be consumed by Presentation Engine or Image Renderer. A recommendation remains `TEACHER_REVIEW`／`WAITING_TEACHER`.
