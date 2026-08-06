# V-MAX Knowledge Layer Naming Standard

版本：1.0.0

## 正式五層名稱

V-MAX 所有技能、模板與課程專案統一使用以下名稱：

1. `Official Knowledge`｜官方教材知識
2. `Teacher Knowledge`｜教師知識
3. `Learning Expansion`｜學習延伸
4. `Teaching Strategy`｜教學策略
5. `Presentation Mapping`｜呈現映射

## 正式檔名

```text
knowledge/
├── 01_official-knowledge.md
├── 02_teacher-knowledge.md
├── 03_learning-expansion.md
├── 04_teaching-strategy.md
├── 05_presentation-mapping.md
├── source-map.md
└── official-knowledge-validation.md

lkb/
├── {課次}_{課名}_lesson-knowledge-book.md
└── lkb-validation-report.md

project/
├── project-status.md
├── role-selection-profile.md
├── style-selection-profile.md
└── output-profile.md

output/
└── output-manifest.md
```

## 淘汰名稱

下列名稱只作為舊版遷移參考，不得在新專案中建立：

| 舊名稱 | 新名稱 |
|---|---|
| `01_fact.md` | `01_official-knowledge.md` |
| `fact-validation-report.md` | `official-knowledge-validation.md` |
| `02_analysis.md` | 視內容遷移到 Official Knowledge 或 Learning Expansion |
| `03_teaching.md` | 拆分為 Learning Expansion 與 Teaching Strategy |
| `Fact Layer` | Official Knowledge |
| `Analysis Layer` | 不再作為正式層名 |
| `Extended Knowledge` | Learning Expansion |
| `Teaching Design` | Teaching Strategy |

## 遷移判斷

### 舊 `02_analysis.md`

- 教師手冊已明示的修辭、句型、主旨、賞析：移至 Official Knowledge。
- 教師個人補充：移至 Teacher Knowledge。
- AI 新增的分析、近義辨析、易誤用：移至 Learning Expansion。

### 舊 `03_teaching.md`

- 學生練習內容：移至 Learning Expansion。
- 課節、時間、分組、教師行動與評量安排：移至 Teaching Strategy。
- 投影片、版型、角色與插圖指示：移至 Presentation Mapping。

## 禁止混用

同一份課程專案不得同時把舊檔與新檔視為有效來源。完成遷移後，舊檔須標示 `legacy` 或移入 `archive/legacy/`。

## 唯一來源規則

- Official Knowledge 是出版社教材內容的唯一正式來源。
- LKB 是課程整合知識的唯一主書。
- Learning Expansion、Teaching Strategy 與 Presentation Mapping 都是 LKB 的派生層。
- 所有最終輸出必須可追溯到核准的 LKB 版本。
