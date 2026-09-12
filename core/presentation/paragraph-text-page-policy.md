# Paragraph Text Page Policy 1.0

這是課文閱讀頁與段落語詞頁的硬性施工規則，優先於頁數、模板、圖片模型與批次方便性。

## 預設頁面單位

- 預設 **一個自然段一頁**，同頁附上該段已核准、需要教學的語詞解釋。
- 不得為了湊頁數、套模板或節省圖片，把兩個自然段合在同一頁。
- 若單一自然段在核准畫布與投影可讀字級下放不下，才可拆成連續頁；必須以完整句子邊界拆分，保留同一 `split_group_id`、`part_index`、`part_count` 與明確 `split_reason`。
- 拆頁是同一段的連續閱讀頁，不是摘錄代表句；所有分頁合起來必須還原該段完整原文。

## 完整內容要求

每個課文閱讀頁的逐頁確認稿必須記錄：

- `source_unit_type: NATURAL_PARAGRAPH`（詩歌使用 `POETRY_STANZA`；教師明確核准的意義段才可使用 `MEANING_UNIT`）。
- `source_unit_ids` 與完整原文來源回指。
- `text_integrity: COMPLETE_UNEDITED`。
- `student_visible_text.body` 的完整課文文字；不得只放代表句、摘要、改寫或省略句子。
- `vocabulary_coverage.required_refs`：該段已核准、必須在段落教學處理的全部語詞。
- `vocabulary_coverage.placement: INLINE_ADJACENT` 或 `SIDE_BY_SIDE_ADJACENT`；若因字數拆頁，可用 `CONTINUATION_ADJACENT`，但仍須在同一段連續頁旁回指同一段與同一詞語覆蓋表。
- `projection_typography.profile: CLASSROOM_PROJECTOR`，並以最終學生可見文字層記錄 `effective_pt_verified: true`。
- 課文正文投影目標為 36–40 pt 等效字級，硬下限為 32 pt；段落旁語詞解釋目標為 30–34 pt，硬下限為 28 pt。
- 字級必須以最終畫布、字型、行距與文字區量測後的實際文字層為準，不得以圖片解析度、提示詞或預設模板字級代替證據。

語詞解釋必須緊跟在該段完整課文旁，採同頁內嵌、左右相鄰或同一段連續頁相鄰的方式呈現，讓學生在上下文中理解。不得把該段語詞移成脫離課文的清單頁、獨立卡片牆或無法辨認所屬段落的角落。若解釋太多，先拆成同段連續頁或刪除未核准／低價值補充，不得刪掉已核准的段落語詞。課後統整頁可以再次整理語詞，但不能取代段落旁的即時解釋。

## 禁止情況

- 只呈現一兩句「代表句」並宣稱段落已完成。
- 用摘要、教師講稿或 AI 改寫取代學生可見的完整原文。
- 課文完整，但把該段語詞解釋漏掉、移到別段、另成脫離上下文的清單頁或混入不相關頁。
- 為了不拆頁而縮小正文、縮成背景圖文字或壓到無法投影閱讀。
- 未提供 `CLASSROOM_PROJECTOR` 的有效字級證據，或正文低於 32 pt、語詞低於 28 pt。

Failure codes：`PARAGRAPH_TEXT_INCOMPLETE / PARAGRAPH_TEXT_REWRITTEN / PARAGRAPH_VOCABULARY_DROPPED / PARAGRAPH_VOCABULARY_DETACHED / PARAGRAPH_SPLIT_UNJUSTIFIED / PARAGRAPH_SOURCE_UNIT_DRIFT / CLASSROOM_FONT_SIZE_UNVERIFIED / CLASSROOM_FONT_TOO_SMALL`。
