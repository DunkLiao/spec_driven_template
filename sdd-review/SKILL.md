---
name: sdd-review
description: |
  規格審查 (Spec-Driven Development review)。審查一套既有的規格驅動文件
  （憲章 / 規格 spec / 設計 design / 任務 tasks），逐條檢查驗收標準 (AC) 是否
  從規格 → 設計 → 任務 → 實作一路可追溯，找出缺口、未填的 [方括號] 佔位、杜撰
  事實、範圍蔓延與設計違反憲章之處，並產出可追溯矩陣與審查清單。
  Use when the user asks to "審查我的規格", "做規格審查", "檢查 spec/design/tasks",
  "驗收標準有沒有對齊", "AC 有沒有都對應到任務", "規格跟設計有沒有兜起來",
  "/sdd-review", "review my spec", "check AC coverage", "規格驗收", or wants to
  verify an existing spec-driven document set before或during 實作.
  Do NOT use for：佈建/建立規格範本或開新功能（用 sdd）、實際產出文件檔
  Word/PDF/PPT/Excel（用 docx/pdf/pptx/xlsx）、建立或管理「個人技能」本身（用
  skills）、一般程式碼審查 (code review) 而非規格審查、或寄送 email / Teams 訊息。
cowork:
  category: analysis
  icon: ClipboardCheckmark
---

# 規格審查 (SDD Review)

審查一套既有的規格驅動文件，確認「規格 → 設計 → 任務」一路對得起來、沒有缺口、沒有杜撰，並把問題列清楚讓使用者修。搭配 `sdd` 技能（佈建與引導）使用 —— 那個負責「寫」，這個負責「驗」。

## When NOT to Use

- 使用者要的是**佈建範本或開新功能** → 用 `sdd`。
- 要產出**實際文件檔**（Word / PDF / 簡報 / 試算表）→ 用 docx / pdf / pptx / xlsx。
- 要審查**程式碼正確性** (code review) 而非規格 → 這個技能只審規格文件，不審程式邏輯。
- 還沒有任何規格檔可審 → 先用 `sdd` 佈建並填寫，再回來審查。

## 審查的四個面向

| # | 面向 | 在問什麼 |
|---|------|----------|
| 1 | **可追溯性 (Traceability)** | 每條驗收標準 AC，在設計裡有對應處理、在任務裡有對應任務嗎？反向：每個任務都對得到某條 AC 嗎？ |
| 2 | **完整性 (Completeness)** | 還有沒有 `[待確認]` / `[方括號]` 佔位沒填？必填段落（問題、AC、契約）有沒有空著？ |
| 3 | **一致性 (Consistency)** | 設計有沒有違反憲章的技術選型或禁止事項？任務順序與相依有沒有矛盾？ |
| 4 | **真實性 (Faithfulness)** | 有沒有看起來像被杜撰的具體事實（人名、數字、欄位）？範圍有沒有偷偷超出規格的「非目標」？ |

## 工作流程

每個步驟都指名工具 (each step names its tool — Glob, Read, render_ui)。

1. **定位檔案**：用 **Glob** tool 找出該功能的 SDD 檔（例 `**/0[0-3]-*.md`、`**/sdd-template/**/*.md`、或使用者指定的資料夾）。找不到就請使用者指出位置，don't 假設路徑。
2. **讀取**：用 **Read** tool 讀齊憲章 / 規格 / 設計 / 任務四份（缺哪份就在報告標明 missing）。
3. **抽出 AC**：從 `01-spec*.md` 抽出每條驗收標準（AC-x.y）。
4. **建可追溯矩陣**：逐條比對 —— 該 AC 在設計的契約/決策有對應嗎？在任務清單有任務標到它嗎？標記 ✅對齊 / ⚠️部分 / ❌缺口。
5. **掃完整性與一致性**：列出所有未填 `[方括號]`、空白必填段、設計違反憲章處、任務相依矛盾。
6. **掃真實性**：標出疑似杜撰的具體事實、超出「非目標」的範圍蔓延。
7. **產出報告**：用 markdown table 呈現可追溯矩陣，再用 bullet 條列問題清單（依嚴重度排序），最後給 1～3 個最該先修的建議。必要時用 **render_ui** tool 出一張對齊度卡片。

## 輸出格式 (Output format)

回覆用 markdown：**先一句總評**（綠燈可往下實作 / 黃燈有缺口要補 / 紅燈規格未就緒），再附下列兩塊。

- **可追溯矩陣 (table)**：欄位 `AC 編號 | 規格 | 設計對應 | 任務對應 | 狀態`，一條 AC 一列。
- **問題清單 (bullet)**：依「缺口 / 未填 / 違反憲章 / 疑似杜撰 / 範圍蔓延」分類，每條指出檔案與位置。
- **下一步**：1～3 個優先修正建議。
- 全部基於讀到的檔案內容，don't 評論讀不到的東西；缺檔就標 missing。

## Guardrails

- **只審不改 / review only, never edit**：這個技能 never 自動改使用者的規格檔；只產出審查結果，由使用者決定怎麼修。
- **基於檔案、不臆測 / ground in files**：所有結論 always 對應到具體檔案與位置；don't 評論沒讀到的檔案，缺檔一律標 missing。
- **不杜撰 / never fabricate**：報告裡的 AC 編號、引用內容 always 取自原檔；if 某段讀不到或不確定 (cannot tell)，標「需人工確認」而非編造。
- **缺檔處理 / failure handling**：if 找不到規格檔 (not found)，先用 Glob 換關鍵字再找；仍 not found 就請使用者指出位置，don't 假裝審過。
- **不替使用者拍板 / don't decide**：發現規格有歧義時，列出選項與影響供使用者判斷，don't 逕自選一個當定論。
- **保護隱私 / privacy**：審查報告若需引用機敏內容，以 `[redact]` 佔位，never 把機敏資料原樣寫進可下載檔案。
- **嚴重度誠實 / honest severity**：紅燈就說紅燈；don't 為了好看把缺口淡化成「小問題」。confirm before 給出「可以開始實作」的綠燈結論。
