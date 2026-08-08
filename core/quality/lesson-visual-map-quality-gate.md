# V-MAX Lesson Visual Map Quality Gate 1.0

## 定位

本 Gate 是 `core/quality/quality-gate-2.md` 的必要子檢查。只要本課 `lesson_visual_map.status != OFF`，正式交付前必須通過。

## A. LVM-OPEN 檢查

- 能否在短時間內看出整課大方向？
- 圖像是否比文字更先承擔結構理解？
- 是否只使用關鍵詞／短語，而非把整課摘要塞入？
- 是否保留需要學生自行推論的發現空間？
- 是否誤把完整主旨、人物特質、修辭答案提前揭露？

任何核心爆雷 → `BLOCKER`。

## B. LVM-CLOSE 檢查

- 是否真正串起整課內容，而不是把各頁縮小拼貼？
- 主旨、結構、語文焦點是否都來自已確認內容？
- 是否能作為快速回想／複習入口？
- 是否因內容過多而縮字、塞框、拉大量裝飾線？

若需要縮小核心文字才能塞入 → `REVISE`，應刪減節點或拆圖，不得縮字硬塞。

## C. 結構與視覺

- 結構形式是否來自文本關係，而非固定樹狀心智圖？
- 線、箭頭、區域與分支是否代表真實關係？
- key scenes / key nodes 是否真的幫助記憶？
- Visual Grammar 是否合理？
- 是否與該課 Style Recipe / Scenario / Character 世界相容，但不被 Wrapper 搶走理解重點？

## D. 文字正確性

Lesson Visual Map 中學生會閱讀到的：
- 課文詞句
- 主旨／結構標籤
- 語文焦點
- 人名／地名／專有名詞

均屬正式教學文字，必須進 Strange Chinese Character Scan。關鍵文字優先 Native Text / Hybrid。

## E. 5-Second Grasp Test

LVM 必做快速掌握測試：

> 不讀所有小字，只看主圖、節點與少量標籤，學生是否能說出「這課大概在學什麼／怎麼走」？

結果：
- `PASS`：能抓到核心與主線。
- `REVISE`：看得出有很多內容，但抓不到主線。
- `BLOCKER`：圖像關係與課文理解矛盾或造成誤解。

## F. Output

```yaml
lesson_visual_map_gate:
  status: PASS | REVISE | BLOCKER
  mode: OPEN | CLOSE | BOTH
  quick_grasp: PASS | REVISE | BLOCKER
  spoiler_check: PASS | BLOCKER
  structure_check: PASS | REVISE | BLOCKER
  text_check: PASS | REVISE | BLOCKER
  overload_check: PASS | REVISE
  issues: []
  fixes_applied: []
```

只要 `BLOCKER` 未歸零，不得正式交付。

## 核心金句

> 一張整課圖的價值，不是塞進多少內容，而是孩子能不能更快看懂整課。
