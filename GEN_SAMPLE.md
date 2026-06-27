任務:在資料夾 ./auto-gen-template/instructions 底下的每個Phase資料夾，建立5組範例md檔案，需依照下列規則

# Spec-Driven Development (SDD) 架構建置規範

本文件定義了專案中 SDD 提示詞模板與範例檔案的目錄結構、命名規則與格式規範，以供後續 AI 助理（Agents）與開發者遵循。

---

## 1. 目錄結構與分類 (Phases)

所有 SDD 相關檔案均應分類存放於 `instructions/` 目錄下的四個生命週期階段資料夾中：

1.  📁 **`Phase_1_Specification`**：規格定義與設計。
2.  📁 **`Phase_2_Test_Generation`**：測試案例自動生成。
3.  📁 **`Phase_3_Implementation`**：測試驅動實作與重構。
4.  📁 **`Phase_4_Verification_Loop`**：自動驗證、除錯與防禦。

---

## 2. 扁平化與同層級規範 (Flat Same-Level Layout)

*   **禁止使用子資料夾**：各 Phase 資料夾下**不得**建立 `examples/` 或其他子資料夾。
*   **同層平鋪**：該階段的所有「提示詞模板」與「範例檔案」必須平鋪在同一個目錄層級下，便於檢索與直接讀取。

---

## 3. 命名與格式規範 (Naming & Format)

*   **去除流水號**：所有檔案名稱必須移除數字流水號前綴（例如：`01_prd_to_spec.md` 應命名為 `prd_to_spec.md`）。
*   **全 Markdown 格式化**：
    *   專案內所有範例與模板檔案，其副檔名一律必須為 **`.md`**。
    *   如果是程式碼範例（例如 TypeScript 實作或測試、YAML 配置、SQL DDL 等），必須在 `.md` 檔案中使用對應語法的 Markdown 代碼區塊進行封裝：
        *   TypeScript：使用 ` ```typescript `
        *   YAML：使用 ` ```yaml `
        *   SQL：使用 ` ```sql `
    *   範例檔案開頭必須包含一個清晰的 Markdown 一級大標題描述該範例。

---

## 4. 範例檔案關聯與參照路徑 (Import Paths)

由於檔案被平鋪在各個 Phase 的根目錄中，範例檔案之間的跨階段參照必須使用正確的相對路徑。例如：

*   在 `Phase_2_Test_Generation` 中的測試範例導入 `Phase_3` 的實作代碼時，Import 路徑應修正為：
    ```typescript
    import { calculateTotal } from '../Phase_3_Implementation/cart_service';
    ```
*   **嚴禁**使用已棄用的 `../.../examples/` 等深層路徑。

---

## 5. 重要事項

- 需使用繁體中文建立內容，使用CP950編碼
