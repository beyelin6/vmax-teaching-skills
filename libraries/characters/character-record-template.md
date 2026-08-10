# V-MAX Character Library Record Template 1.0

## 用途

本模板用來逐步累積 V-MAX 角色庫。只有經教師確認、且在代表頁或正式課程中驗證通過的角色，才建立正式角色檔。

不要求每課沿用同一引導角色；角色庫的功能是讓「曾被確認值得重複使用的角色」在未來課次中保持身份連續。

---

## Character Record

```yaml
character_record:
  character_id:
  display_name:
  status: CANDIDATE | APPROVED_RECURRING | RETIRED
  character_type: GUIDE_CHARACTER | STORY_CHARACTER | LEARNING_PARTNER | OTHER

  identity:
    role_identity:
    age_band:
    gender_presentation:
    species_or_type:
    personality_tone:

  visual_dna:
    face_shape_logic:
    facial_feature_signature:
    hair_signature:
    body_proportion:
    outfit_logic:
    signature_accessories: []
    color_logic:
    must_keep_features: []

  variation_rules:
    allowed_variations: []
    style_translation_notes:
    contextual_costume_rules:
    forbidden_drift: []

  teaching_role:
    allowed_functions:
      - LOOK
      - HINT
      - QUESTION
      - REVEAL
      - COACH
      - REFLECT
      - TRANSITION
    role_boundaries:

  reference_assets:
    canonical_reference_assets: []
    lesson_specific_reference_assets: []

  provenance:
    first_approved_lesson:
    first_approved_style:
    approved_by_teacher: false
    approval_notes:
    last_verified_lesson:
    last_verified_style:

  history:
    appearances: []
    approved_style_translations: []
    rejected_variants: []
```

---

## 累積方式

### A. 首次出現

角色第一次在某課出現時，先視為 `CANDIDATE`，只需要服務當課。

### B. 同課驗證

代表頁至少確認：
- 正面／主要視角是否可辨識
- 不同動作與表情是否仍是同一人
- Character DNA 是否足以支撐後續頁面
- 與其他角色是否容易混淆

### C. 升格為常駐角色

只有教師明確決定「這個角色之後還想用」，才改為：

`APPROVED_RECURRING`

並建立至少一個 canonical reference asset。

### D. 跨課再次使用

先讀 Character Record，再依新課 Style Recipe 做 Style Translation。

不得從角色名稱重新猜外觀。

### E. 新畫風核准

若某角色第一次進入新的畫風，先做代表角色圖／代表頁驗證；通過後才將該版本加入 `approved_style_translations`。

---

## 角色庫設計原則

1. 少量高品質角色優於大量未驗證角色。
2. 每課可以有全新的專屬角色，不必為了角色庫硬套常駐角色。
3. 常駐角色的核心 DNA 穩定，但造型可以隨世界觀合理變化。
4. Reference Asset 是辨識依據，不是要求每次複製同一姿勢。
5. 被教師淘汰的角色保留歷史紀錄但設為 `RETIRED`，避免未來 Renderer 誤調用。

---

## 建議角色檔命名

```text
libraries/characters/
  character-record-template.md
  bee-teacher.md
  xiaole.md
  <future-character-id>.md
```

尚未經教師確認的角色，不建立正式命名檔。

---

## 核心金句

> 角色庫不是先把角色填滿，而是把真正好用、已被教師認可的角色慢慢留下來。
