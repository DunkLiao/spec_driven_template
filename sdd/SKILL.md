---
name: sdd
description: |
  規格驅動開發 (Spec-Driven Development) 工作流程，給 vibe coding 用。一鍵把一套
  可重複使用的規格範本（憲章 / 規格 / 設計 / 任務 / CLAUDE.md / 提示詞）佈建到任何
  新功能或新專案，並引導使用者「先寫規格、再讓 AI 照規格寫程式」，避免 AI 腦補需求、
  越改越歪。也能引導逐項實作與規格審查。
  Use when the user asks to "用 SDD / 規格驅動開發開一個新功能", "建立 spec/design/tasks
  範本", "幫我把這個專案做成規格驅動", "scaffold spec-driven development", "set up a
  spec/design/tasks workflow", "寫一份功能規格再讓 AI 實作", "spec-driven 起手式",
  "幫我開一個新功能的規格", or wants a repeatable spec-first workflow for vibe coding.
  Do NOT use for：實際產出文件檔 Word/PDF/PPT/Excel（用 docx/pdf/pptx/xlsx）、
  建立或管理「個人技能」本身（用 skills）、純品牌主題或配色（用 bot-brand-*）、
  領域驅動設計 DDD 的程式架構骨架（這是規格流程，不是 DDD 類別骨架）、
  或寄送 email / Teams 訊息。
cowork:
  category: productivity
  icon: ClipboardTaskListLtr
---

# 規格驅動開發 (Spec-Driven Development, SDD)

把「先寫規格、再讓 AI 照規格寫程式」變成可重複使用的起手式。核心理念：
**規格文件是唯一事實來源，AI 寫出來的東西好不好，取決於規格寫得清不清楚。**

## When NOT to Use

- 使用者要的是**實際文件檔**（Word / PDF / 簡報 / 試算表）→ 用 docx / pdf / pptx / xlsx。
- 使用者要**建立或調整「技能」本身** → 用 skills。
- 使用者只是要**一段程式碼**、不需要規格流程 → 直接寫，不必佈建範本。
- 領域驅動設計 (DDD) 的**程式類別骨架**（Entity / Aggregate / Repository 程式碼）→ 這個技能是規格流程，不是 DDD 程式骨架產生器。

## 四個階段、四份文件

| 順序 | 檔案 | 階段 | 回答 |
|------|------|------|------|
| 0 | `00-constitution.md` | 憲章 | 這專案永遠遵守的規矩（技術選型、風格、禁止事項）。一次寫、長期用。 |
| 1 | `01-spec.md` | 規格 | 做什麼：問題、使用者故事、可勾稽的驗收標準 (AC)。 |
| 2 | `02-design.md` | 設計 | 怎麼做：架構、資料模型、API 契約、關鍵決策取捨。 |
| 3 | `03-tasks.md` | 任務 | 照什麼順序做：拆成可逐項打勾的小任務，每項標完成定義＋對應 AC。 |

> 另有 `CLAUDE.md`（放專案根目錄讓 AI 自動讀）、`prompts.md`（各階段可貼的提示詞）、`README.md`（流程說明）。

## 工作流程

### A. 佈建範本（起手式）

當使用者要開新功能或新專案時，每個步驟都指名工具 (each step names its tool — Bash, Glob, Write)。用 **Bash** tool 跑佈建腳本：

```bash
python scripts/scaffold.py --dest output/sdd-template
# 需要附上完整範例示範時：
python scripts/scaffold.py --dest output/sdd-template --with-example
```

佈建後用 **Glob** tool（`output/**/*`）確認檔案存在，再告訴使用者位置（OneDrive 的 Documents/Cowork 1）。

**失敗處理 (Failure handling)：**
- **If** the scaffolded files are **not found** in `output/`：用 `Glob **/*` 找出實際寫到哪、`mv` 搬回 `output/`，再重新確認；確認存在前 never 告訴使用者「已完成」。
- **If** the scaffold script **fails**（找不到 templates 來源）：fallback —— 改用 **Write** tool 依 `references/templates/` 的內容手動建立四份核心檔，不要讓使用者空手而回。
- **If** the destination folder already exists（已有同名範本）：ask 使用者要覆蓋還是換新資料夾名，never 逕自覆蓋使用者既有規格。

### B. 引導寫規格 → 設計 → 任務（一次只往前一步）

依使用者目前所在階段，引導對應產出，**規格未定案不碰設計、設計未定案不碰程式**：

1. **規格**：問清楚「要解決什麼問題、誰用、怎樣算做完」。把驗收標準寫成可勾稽的「假設／當／則」。不確定處標 `[待確認]`，不要腦補。
2. **設計**：先讀憲章，確認不違反技術選型。每個關鍵決策寫「為什麼選它、放棄什麼」。逐條對應規格的 AC。
3. **任務**：把設計拆成 15～30 分鐘可完成、可獨立驗證的小任務，標明完成定義與對應 AC，照相依順序排列。

每個階段產出後，請使用者審查再往下。`references/templates/prompts.md` 有每階段可直接複製的提示詞。

### C. 逐項實作

引導 AI（或使用者的 AI 工具）照 `03-tasks.md`：**一次只做一個未打勾任務**，做完打勾、簡述改動、說明如何驗證，然後停下來等確認。實作中發現規格不對 → 先停手回去改規格，再改程式。

## 輸出格式 (Output format)

回覆一律用 markdown：短摘要（bullet 條列）＋必要時一個 table，不要長篇大論。

- **佈建範本時** (bullet summary)：簡述佈建了哪些檔、放哪裡、下一步做什麼（先填憲章）。
- **引導產出時**：直接照範本結構產出該階段內容（憲章 / 規格 / 設計 / 任務其一），保留 `[方括號]` 待填處，**不要填入杜撰的事實**（人名、數字、欄位資料）。
- **回報健康度/比對時**：用一個 markdown table（檔案 / 狀態 / 對應 AC）呈現，不要把細節塞進一段文字。
- 需要完整示範時，指向 `references/templates/範例-borrower-lookup/`（授信戶風險查詢的整套填寫範例）。

## Guardrails

- **不杜撰事實 / never fabricate**：規格 / 設計裡的人名、數字、資料欄位若未知 (missing)，標 `[待確認]` 或 `[請填寫]`，never 編造。
- **一次只往前一步 / always one step**：always 等當前階段定案再往下；don't 在規格還沒定案時就跳去寫設計或程式。
- **保留待填處 / don't auto-fill**：佈建的是空白範本，方括號是給使用者填的，don't 自作主張填滿。
- **AI 動工前先讀規格 / always read specs first**：always 提醒使用者把 `CLAUDE.md` 放專案根目錄，或每個新對話先叫 AI 讀相關 `.md` 再動程式。
- **檔案一律寫到 `output/`**：佈建與產出的檔案 always 放 `output/`；佈建後用 Glob confirm before 回報「已完成」—— 確認檔案存在前 never 宣稱完成。
- **不覆蓋既有規格 / ask before overwrite**：目的地若已有同名範本，ask 使用者；fallback 是另開新資料夾，don't 蓋掉既有內容。
- **規格優先於程式 / spec over code**：實作中發現規格不對，don't 只改程式 —— always 先回去改規格、取得確認，再改程式。
- **保護隱私 / privacy**：範本內容不含使用者真實機敏資料；若使用者貼入機敏資訊，提醒以 `[redact]` 佔位，don't 原樣寫進可下載檔案。
