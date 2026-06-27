# 商品目錄查詢模組規格書 (Product Catalog Spec)

## 1. 功能概述
提供使用者查詢商品列表，支援關鍵字搜尋、分類過濾與分頁功能。

## 2. API 定義
### `GET /api/products`
*   **Query 參數**：
    - `page` (number): 頁碼，預設為 1，必須大於 0。
    - `limit` (number): 每頁筆數，預設 20，最大 100。
    - `search` (string): 關鍵字。
*   **Response**：
    ```json
    {
      "products": [],
      "totalCount": 120,
      "page": 1,
      "limit": 20
    }
    ```
