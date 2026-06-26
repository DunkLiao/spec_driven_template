# 技術設計：授信戶風險分級查詢

> 階段二：講「怎麼做」。對應規格：`01-spec-borrower-lookup.md`。
> 動筆前已讀 `00-constitution.md`，設計不違反憲章。

- 狀態：已定案
- 最後更新：2026-06-26

---

## 1. 設計概述 (Overview)

單頁 Web 工具。前端純 HTML 表單，呼叫 FastAPI 的查詢 API；
API 經邏輯層驗證統編後，向資料層（SQLite）查詢，回傳分級與更新日。
邏輯層不直接寫 SQL，符合「邏輯與 I/O 分離」原則。

## 2. 架構與資料流 (Architecture)

```
[瀏覽器表單] ──HTTP──▶ [FastAPI 介面層] ──▶ [查詢邏輯層] ──▶ [資料層 SQLite]
   (index.html)          (api.py)            (service.py)       (repository.py)
        ▲                                                            │
        └──────────────── JSON 結果 ◀───────────────────────────────┘
```

- 介面層 `api.py`：定義路由、接收輸入、回傳 JSON / 錯誤碼。
- 邏輯層 `service.py`：驗證統編、組裝回傳資料、處理「查無資料」。
- 資料層 `repository.py`：唯一碰 SQL 的地方，依統編查單筆。

## 3. 模組與檔案規劃 (Modules)

| 檔案 / 模組 | 職責 | 對外提供 |
|-------------|------|----------|
| `app/api.py` | 路由與 HTTP 處理 | `GET /api/borrower/{id}` |
| `app/service.py` | 統編驗證、商業邏輯 | `lookup_borrower(id) -> BorrowerResult` |
| `app/repository.py` | SQLite 存取 | `find_by_id(id) -> Row \| None` |
| `app/models.py` | 資料結構定義 | `BorrowerResult` |
| `static/index.html` | 查詢前端頁 | — |
| `tests/` | pytest 測試 | — |

## 4. 資料模型 (Data Model)

```
資料表 borrower
  - tax_id：TEXT (PK)   // 統一編號，8 碼數字
  - risk_level：INTEGER // 風險分級 1~5
  - updated_at：TEXT    // 最後更新日 YYYY-MM-DD

回傳物件 BorrowerResult
  - tax_id：str
  - risk_level：int     // 1~5
  - updated_at：str
```

## 5. 介面 / API 契約 (Contract)

```
GET /api/borrower/{tax_id}

輸入：
  tax_id — 路徑參數，需為 8 碼數字

輸出 (200)：
  { "tax_id": "12345678", "risk_level": 3, "updated_at": "2026-05-30" }

錯誤：
  400 —— 統編格式錯誤   { "detail": "統編須為 8 碼數字" }
  404 —— 查無資料        { "detail": "查無此授信戶資料" }
  500 —— 系統錯誤        { "detail": "系統忙碌，請稍後再試" }
```

## 6. 關鍵決策與取捨 (Decisions)

- **決策 1**：用 SQLite 而非連線正式資料庫，因為這是唯讀的小型內部工具、資料量小；放棄直連核心系統，避免權限與連線複雜度。
- **決策 2**：統編驗證放在邏輯層而非只靠前端，因為前端驗證可被繞過，後端須再驗一次。
- **決策 3**：錯誤訊息對使用者一律白話，不回傳技術細節，符合憲章禁止事項。

## 7. 風險與對策 (Risks)

| 風險 | 影響 | 對策 |
|------|------|------|
| SQLite 資料未即時同步正式系統 | 分級可能落後 | 畫面標示「最後更新日」，由使用者判讀 |
| 內網無權限控管 | 任何內網者可查 | 列為非目標、後續評估；先限部署於部門內網段 |

## 8. 測試策略 (Testing)

- 單元測試：`service.lookup_borrower` 的正常、查無、格式錯誤三路徑。
- 邊界測試：空字串、7 碼、9 碼、含英文。
- 對應 AC：AC-1.1 / AC-2.1 / AC-2.2 各至少一個測試。
