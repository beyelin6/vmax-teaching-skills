# V-MAX Infographic PDF Regression Cases 1.1

## I-01｜正式成品格式

PASS：預設交付單一 16:9 圖文資訊圖表 PDF，頁序與 Renderer Script 一致。

FAIL：預設要求可修改 PPTX，或只把整頁圖片放入 PPTX 後宣稱完成。

## I-02｜圖文一體

PASS：每頁有單一主要學習焦點，圖像、文字、提問、提示與角色形成完整閱讀路徑。

FAIL：插圖與文字割裂、固定左圖右文、背景圖上堆疊大量文字框，或為可編輯拆掉成功構圖。

## I-03｜情境敘事型

PASS：主場景／連續動作承擔理解，少量關鍵文字嵌入天然留白與資訊卡。

FAIL：圖片只裝飾，事件、聯想、因果或動作關係看不出來。

## I-04｜知識比較型

PASS：形近字採字群同框比較；多音字以讀音、語意、例詞／例句與情境對位。

FAIL：單字孤立、比較欄位錯位、注音或正式字形交給圖片模型猜測。

## I-05｜Verified Teaching Text

PASS：繁體中文、注音、原句、生字、成語與題目逐項核對，學生頁無答案。

FAIL：假字、簡體／日文異體、漏字增字、注音錯誤、答案外洩或來源文字被改寫。

## I-06｜PDF Preflight

PASS：最終 PDF 全頁重渲染為 PNG，確認頁數、順序、裁切、清晰度、色彩、重複／漏頁與邊界。

FAIL：只檢查單頁原圖，未檢查組裝後 PDF；或 PDF 有模糊、黑框、裁切與頁序錯誤。

## I-07｜可修改性位置

PASS：修改回到 Source Master、Renderer Script、Visual YAML 或單頁來源圖，再重生受影響頁與重組 PDF。

FAIL：把 PPTX 物件層當成正式內容來源，或要求教師自行搬字、遮錯字與重排。

## I-08｜Gold Pattern 必須落地

PASS：每張代表頁都有 `primary_pattern`，Visual Grammar 被具體轉譯成學生可見的理解事件；代表頁通過後才全量渲染。

FAIL：Visual Grammar 只存在 metadata，Renderer 自行退化成左文右圖、白框資訊卡或固定三欄模板。

分類：`GOLD_PATTERN_DROPPED / TEMPLATE_CARD_DRIFT / LEFT_TEXT_RIGHT_IMAGE_DRIFT`。

## I-09｜Visual Evidence

PASS：圖片實際承擔字義、句意、比較、動作、證據、結構或情緒理解；拿掉圖會明顯降低理解。

FAIL：圖片只是裝飾，移除後學生仍可只靠旁邊文字得到完全相同的理解。

分類：`VISUAL_EVIDENCE_MISSING`。

## I-10｜Discovery Before Label

PASS：需要學生發現的修辭、句型、推論、聯想與閱讀策略，先讓學生看線索／關係，再命名或收束。

FAIL：一開始就把答案、術語與分析完整列出，畫面只負責陪襯已揭露的結論。

分類：`DISCOVERY_PREEMPTED`。

## I-11｜Lesson Visual Map 不得流程框化

PASS：整課圖像心智地圖以世界、路徑、場景、空間或真正結構關係承載全文理解。

FAIL：3–6 個矩形＋箭頭、段落標題貼背景圖、或文字流程圖冒充 Lesson Visual Map。

分類：`LVM_FUNCTION_DRIFT / TEMPLATE_CARD_DRIFT`。

## I-12｜Theme 一致不等於版型一致

PASS：同課世界觀、角色、色彩、材質維持一致，但頁型依認知關係自然變化。

FAIL：因為 Style Recipe 一致，連續多頁複製同一構圖，只替換文字與插圖。

分類：`TEMPLATE_CARD_DRIFT`。

## 整體 PASS

```yaml
infographic_pdf_regression:
  default_format_pdf: PASS
  infographic_integration: PASS
  narrative_scene_pages: PASS
  comparison_pages: PASS
  verified_teaching_text: PASS
  pdf_preflight: PASS
  source_based_revision: PASS
  gold_pattern_loaded: PASS
  visual_evidence: PASS
  discovery_before_label: PASS
  lesson_visual_map_world_relation: PASS
  theme_without_template_drift: PASS
```

任一 FAIL，不得宣告 `INFOGRAPHIC_PDF_PASS`。
