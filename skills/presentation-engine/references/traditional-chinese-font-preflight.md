# Traditional Chinese Font Preflight Integration

本規則把 `skills/traditional-chinese-font-safety` 接入 V-MAX 簡報渲染流程。

## 何時必須執行

凡 `presentation-engine` 的輸出包含下列任一項，在代表頁渲染前必須執行字型 preflight：

- image-first PNG / PDF
- 含繁體中文的 PPTX
- 生字、形近字、課文、詞語、注音頁
- 任何由 Python / Pillow / SVG / Canvas / ReportLab 合成學生可見文字的頁面

## 強制讀取

進入代表頁施工前，renderer 必須讀取：

1. `skills/traditional-chinese-font-safety/SKILL.md`
2. `skills/traditional-chinese-font-safety/font-registry.yaml`
3. `skills/traditional-chinese-font-safety/scripts/check_fonts.py`

## Gate 1｜代表頁前

1. 依頁面功能決定 `selected_font_role`。
2. 優先尋找專案工作區 `assets/fonts/` 或 renderer 已知可定位的字型檔。
3. 不得只以 family name 判斷字型可用。
4. 執行 `check_fonts.py`，至少檢查標準繁中字串。
5. 若頁面包含注音，加上 `--require-bopomofo`。
6. 若頁面為生字／形近字，將當課所有目標字放入 `--extra-text`。
7. preflight status 不為 `pass` 時，不得渲染代表頁。

範例：

```bash
python skills/traditional-chinese-font-safety/scripts/check_fonts.py \
  --font assets/fonts/SourceHanSansTW-Regular.otf \
  --extra-text "奉獻良方衛生捐錢食宿" \
  --require-bopomofo \
  --report working/font-preflight-report.json
```

## Gate 2｜批次輸出前

代表頁通過不代表整課可直接批次輸出。正式批次前必須再次確認：

- 本批所有實際使用字型檔仍可載入。
- 新增頁面若出現代表頁沒有的生字，必須把新字加入測試。
- 若有注音頁，Bopomofo test 必須為 `pass`。
- fallback 若被啟用，必須記錄實際字型檔，不得只記 family 名稱。
- 最終輸出後仍要檢視 PNG/PDF，不得以 script exit code 0 取代視覺 QA。

## 必留紀錄

在當課 `00_施工中_接續區` 或對應 working 區保存：

```yaml
FONT_PREFLIGHT:
  selected_font_role: body_sans
  selected_font_file: assets/fonts/SourceHanSansTW-Regular.otf
  fallback_used: false
  traditional_chinese_test: pass
  bopomofo_test: not_required
  missing_glyphs: []
  report_ref: working/font-preflight-report.json
  final_render_QA: pending
```

## STOP 條件

任一情況成立即停止批次輸出：

- 找不到實際字型檔
- renderer 無法載入字型
- 標準繁中字串有缺字
- 當課目標生字有缺字
- 需要注音但 Bopomofo test fail
- 系統自行換成未登錄 fallback
- 最終 PNG/PDF 出現方框、亂碼、明顯錯誤字形或字型漂移

禁止以「先輸出再說」或「工作區預覽看起來正常」繞過本 gate。
