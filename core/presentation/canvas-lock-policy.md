# V-MAX Presentation Canvas Lock Policy 1.0

## 定位

本政策是教師口述用圖片式國語簡報的畫布與輸出規格唯一來源。它只管理簡報；預習單、課後短文單、A4 講義與其他成果使用各自的 Output Profile。

核心原則：

> 每個簡報專案第一次啟動時先由教師選擇 `4:3` 或 `16:9`；選定後鎖定，續跑、換 AI、換平台與批次製作都不得自行切換。

## 1. 畫布選擇 Gate

在尚未存在已確認的 `canvas_lock` 時，只能向教師提出一個選擇：

```text
本次簡報畫面要使用哪一種比例？
A. 16:9 橫式（建議，適合現代投影與寬螢幕）
B. 4:3 橫式（若教室設備或既有教材要求）
```

不得詢問 3:2、9:16 或「讓 AI 自己判斷」。教師選定後，建立 `canvas_lock` 並持續沿用；未選定時標記 `CANVAS_SPEC_BLOCKED`，不得建立代表頁、圖片或批次成果。

若 Runtime State、既有已確認成果或教師先前決定已包含 `canvas_lock`，續跑時直接讀取並沿用，不得重新詢問或改選。只有教師明確要求變更比例，才建立新的 Output Profile 版本，並列出受影響下游。

## 2. 唯一核准 profiles

```yaml
profiles:
  lesson_presentation_16_9_v1:
    canvas_ratio: 16:9
    orientation: LANDSCAPE
    default_width_px: 2560
    default_height_px: 1440
  lesson_presentation_4_3_v1:
    canvas_ratio: 4:3
    orientation: LANDSCAPE
    default_width_px: 2048
    default_height_px: 1536
```

選定的 profile 使用其固定預設像素；若教師另指定解析度，寬高比仍須精確維持該 profile，並在 Render Request 與 Output Manifest 留存實際寬高。不得讓 provider／平台自動決定尺寸。

以下不得默默使用：`3:2`、`9:16`、A4、Letter、未知比例或只寫「高清」但沒有像素的尺寸。

## 3. 渲染前必鎖定

每一份 `SLIDE_SCRIPT`、`Render Request`、Runtime State 與 Output Manifest 都必須能追溯同一個設定，至少包含：

```yaml
canvas_lock:
  profile: lesson_presentation_16_9_v1 | lesson_presentation_4_3_v1
  ratio: 16:9 | 4:3
  width_px: 2560
  height_px: 1440
  orientation: LANDSCAPE
  safe_area: locked_reference
  fit_mode: PRESERVE_ASPECT_CONTAIN_OR_APPROVED_CROP
  output_formats: [PNG, PDF]
  teacher_decision_ref:
```

缺少必要欄位、不同母檔設定不一致，或同一任務出現多個未決畫布設定時，標記 `CANVAS_SPEC_BLOCKED`，列出受影響頁面與下游成果，停止圖片生成與批次製作。

## 4. 頁面與素材規則

- 同一份簡報所有頁面共用同一 `canvas_profile`；頁型可以改變構圖，不得改變畫布比例。
- 原始插圖、角色圖或外部樣張可以是其他比例，但只能以 `CONTAIN`、等比縮放或教師核准的 `CROP` 放入畫布。
- 禁止拉伸、壓扁、非等比變形或以變形修正留白。
- 使用裁切時必須記錄 `crop_mode`、裁切方向與是否影響角色／關鍵教材細節；未核准的裁切視為 `ASSET_CROP_UNAUDITED`。
- 不得為了填滿畫布而擴寫課文、增加無來源情節、放大裝飾或壓縮正文。

## 5. 實際成品驗證

生成後必須讀取實際 PNG／PDF 尺寸，不可只看 prompt、腳本或平台預覽。驗證至少包括：

1. 實際寬高是否等於 Render Request。
2. 寬高比是否精確符合已選定的 `4:3` 或 `16:9`。
3. 是否有任何頁面混入另一種比例、`3:2`、`9:16` 或平台預設比例。
4. 角色、插圖與文字元件是否保持比例，沒有拉伸或錯誤裁切。
5. PDF 每頁是否與 PNG 使用同一畫布。

任一頁不符合即標記 `CANVAS_DRIFT`，整批停在驗證失敗，不得混入交付包。若輸出格式或實際尺寸與鎖定設定不一致，標記 `OUTPUT_PROFILE_MISMATCH`。

## 失敗碼

- `CANVAS_SPEC_BLOCKED`
- `CANVAS_DRIFT`
- `OUTPUT_PROFILE_MISMATCH`
- `ASSET_STRETCH_DETECTED`
- `ASSET_CROP_UNAUDITED`

