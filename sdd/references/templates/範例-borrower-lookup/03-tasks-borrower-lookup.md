# 任務拆解：授信戶風險分級查詢

> 階段三：把 `02-design-borrower-lookup.md` 拆成可逐項打勾的小任務。
> AI 一次只做一個未打勾任務，做完停下來等確認。

- 狀態：進行中
- 對應設計：`02-design-borrower-lookup.md`
- 最後更新：2026-06-26

---

## 任務清單

### 階段 A：地基與資料層
- [x] **T1**　建立專案骨架（`uv` 初始化、安裝 FastAPI / pytest、目錄結構）
  - Done：`uv run pytest` 可執行（即使 0 測試）。
- [x] **T2**　定義 `models.py` 的 `BorrowerResult`
  - Done：物件含 tax_id / risk_level / updated_at 三欄位。
- [ ] **T3**　建立 SQLite 與 `repository.find_by_id`（相依：T1）
  - Done：能對測試用 DB 依統編查到 / 查不到單筆。

### 階段 B：核心邏輯
- [ ] **T4**　實作 `service.lookup_borrower`：統編驗證 + 查詢 + 查無處理
  - Done：通過三路徑測試 —— 對應 AC-1.1、AC-2.1、AC-2.2。
- [ ] **T5**　補 `service` 邊界測試（空、7 碼、9 碼、含英文）
  - Done：邊界案例全綠。

### 階段 C：介面與前端
- [ ] **T6**　實作 `api.py` 的 `GET /api/borrower/{tax_id}`，對應 400/404/500
  - Done：用 TestClient 驗證各狀態碼回傳正確 —— 對應 AC-1.1、AC-2.2。
- [ ] **T7**　做 `static/index.html` 查詢頁（即時格式提示、顯示統編＋分級＋更新日）
  - Done：手動操作符合規格畫面 —— 對應 AC-1.2、AC-2.1。

### 階段 D：收尾
- [ ] **T8**　補齊測試，確認每條 AC 都有對應測試且通過
- [ ] **T9**　跑 ruff format / lint，整理 docstring
- [ ] **T10**　對照 `01-spec` 逐條驗收，更新各檔狀態為「已完成」

---

## 進度筆記 (Log)

- 2026-06-26　T1～T2 完成，骨架就緒。下一步 T3 建資料層。
