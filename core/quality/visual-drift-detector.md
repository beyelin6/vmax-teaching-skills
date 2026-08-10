# V-MAX Visual Drift Detector 1.0

## 定位

Visual Drift Detector 用來檢查長篇教材在全量生成後是否逐頁偏離已確認的視覺世界、角色 DNA、構圖語言與教學視覺意圖。

核心原則：

> 一套簡報可以有節奏變化，但不能像每五頁換了一個 AI。

> 允許變化的是畫面任務；不允許漂移的是已鎖定的視覺身份。

## A. 建立 Baseline

在「代表頁驗證」通過後，建立 Visual Baseline：

```yaml
visual_baseline:
  lesson_id:
  world_theme:
  style_recipe:
  palette_logic:
  material_language:
  line_and_texture:
  character_dna_refs: []
  typography_logic:
  text_integration_mode: NATIVE_OVERLAY | IMAGE_INTEGRATED_VERIFIED_TEXT
  background_value_anchor:
  ui_motifs: []
  visual_grammar_constraints: []
  lesson_visual_map_signature:
  protected_visual_moments: []
```

Baseline 是一致性參考，不是固定版型。

## B. Drift 維度

逐頁／逐批檢查：

1. `WORLD_DRIFT`：世界觀或場景語彙突然換世界。
2. `STYLE_DRIFT`：水彩、手繪、3D、漫畫等媒材無理由切換。
3. `PALETTE_DRIFT`：主配色邏輯失控，不是正常情緒變奏。
4. `CHARACTER_DRIFT`：臉型、髮型、服裝識別、比例、年齡感或角色關係變形。
5. `TYPOGRAPHY_DRIFT`：學生可見字體層級、標籤邏輯、文字密度突然失衡。
6. `UI_DRIFT`：木牌、徽章、卡片、手帳等介面語彙無理由換套。
7. `COMPOSITION_DRIFT`：整套從圖像式觀看突然退化成機械模板，或反之。
8. `PEDAGOGICAL_VISUAL_DRIFT`：畫面仍好看，但已不再服務原本的 Visual Grammar / Director Intent。
9. `LVM_DRIFT`：Lesson Visual Map 與整課視覺世界、結構關係或 Reveal Policy 不一致。
10. `CHARACTER_IDENTITY_SPLIT`：同一角色在不同頁被生成成不同年齡、臉型、髮型、服裝或物種；例如教師化身與昆蟲吉祥物被誤當成同一角色。
11. `BACKGROUND_VALUE_DRIFT`：已確認的明度方向漂移；例如偏白象牙紙面逐頁變成黃褐舊紙。
12. `UI_MOTIF_TEMPLATE_DRIFT`：木牌、紙卡、彩帶等候選載體被 Renderer 無視內容地重複套版。
13. `TEXT_INTEGRATION_DRIFT`：教師已鎖定圖文同步生成，後續卻退回機械疊字；或生成文字雖美觀但未通過逐字核對。

## C. 允許的變奏

下列不算 Drift，只要有教學理由：
- 高潮頁增加對比或鏡頭張力。
- Knowledge Lab 使用更精準的 Native Analytic Slide。
- 不同 Act 使用不同 Visual Grammar。
- 文字載體隨內容改成水波、輪跡、雲層、物件或其他場景元素，只要閱讀層級與整課媒材一致。
- 情緒轉折造成明暗、景別、留白變化。
- Lesson Visual Map 使用較高層級的整體視角。

判斷問題不是「是不是一模一樣」，而是：

> 這個變化是因為學生要看懂不同關係，還是 Renderer 自己走鐘？

## D. 風險分級

- `PASS`：屬合理變奏，身份一致。
- `REVISE`：局部漂移，可用小範圍修正。
- `BLOCKER`：角色辨識、整課世界、核心視覺語法或學生理解明顯被破壞。

## E. 修正順序

1. 修正局部角色／物件／材質。
2. 修正局部配色、UI 或文字層。
3. 以代表頁 Baseline 重新生成該區塊。
4. 必要時重做單頁。
5. 不因一頁漂移而整套重畫。

## F. 批次檢查

全量生成時至少在：
- 代表頁後
- 每一 Session 或生成批次結束
- 最終 Quality Gate 前

執行 Drift Check。

```yaml
visual_drift_check:
  status: PASS | REVISE | BLOCKER
  baseline_ref:
  pages_checked: []
  drift_items:
    - page:
      type:
      severity:
      evidence:
      fix:
  unresolved_blockers: []
```

## G. 與 Quality Gate 的關係

Visual Drift Detector 是 Quality Gate 的必要輸入之一。任何 `unresolved_blockers` 不為空時，不得正式交付。

## 核心金句

> 一致不是每頁長一樣，而是每頁都像同一位導演拍的、同一個世界裡發生的事。

