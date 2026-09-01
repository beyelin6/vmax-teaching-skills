# Example Routing｜Golden / Negative Examples 路由指南

本檔案只負責「何時讀哪個案例」。不要把所有案例同時載入。

## 核心原則
案例不是模板。

Golden Example 用來回答：這類內容為什麼可以這樣組織？什麼比例、節奏、資訊層級值得學？哪些設計決策可以抽象成規則？

Negative Example 用來回答：這個頁面為什麼難讀、難寫或像 PPT？失敗是內容、功能、版型、文字、插圖還是輸出問題？哪個問題需要避免，而不是「整種風格禁止使用」？

優先順序永遠是：
**當前使用者指示 → 來源內容 → K01 功能安全 → K02 視覺字形 → 案例證據**

## 路由方法
先看四個欄位：
1. artifact_type
2. use_context
3. density
4. design_problem / design_goal

一般只讀：
- 1 個最接近的 Golden Example
- 必要時再讀 1 個最相關的 Negative Example

若沒有真正接近的案例，不要硬套。

## Golden Example 索引
### GE01｜親師手冊・溫馨教育資訊頁
檔案：`examples/golden/GE01_parent_handbook_warm_information.md`

tags: information-handbook, parent-handbook, A4-portrait, warm-education-handbook, medium-high-density, long-text-plus-parallel-cards, functional-illustration, mixed-layout, parent-readability

適用：親師手冊、班級手冊、家長日資料、教師理念＋班級願景＋學期重點、同頁同時存在長文與數個平行資訊單元。

不要用於：大量學生作答頁、考卷、長篇連續課文、計算演算頁、真正時間軸／流程頁、單一大圖解。

## Negative Example 路由
### NE01｜PPT 貼字感
讀：`examples/negative/NE01_ppt_pasted_text.md`
觸發：固定左文右圖、圖片與文字各做各的、滿版底圖＋白框文字、標題像最後才打上去、每頁像簡報模板複製。

### NE02｜過度格子化／卡片化
讀：`examples/negative/NE02_over_gridification.md`
觸發：每段都框、2×2 / 3×2 卡片被強迫使用、卡片等大導致內容擠壓、留白被切碎、Bento 被當預設模板。

### NE03｜插圖搶內容與作答空間
讀：`examples/negative/NE03_illustration_competes_with_content.md`
觸發：圖太滿、插圖遮文字、學生寫不下、為留插圖而縮字、裝飾比教學內容更醒目。

### NE04｜高密度靠縮字硬塞
讀：`examples/negative/NE04_density_by_shrinking.md`
觸發：字小、行距過密、作答區縮水、全頁整體縮放、同頁內容已超過安全容量。

### NE05｜圖片生成中文字
讀：`examples/negative/NE05_generated_chinese_text.md`
觸發：中文模糊、假字／錯字／簡體、注音不穩、圖片放大仍不清楚、重複局部修字失敗。

## 新增案例時
每個案例至少包含：metadata、why_it_matters、content_structure、layout_logic、typography_logic、illustration_logic、density、what_to_learn、what_not_to_copy、suitable_for、unsuitable_for、tags。

不要只有圖片而沒有分析檔。
