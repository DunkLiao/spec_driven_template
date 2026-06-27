# 退款處理流程與審核狀態規格書 (Refund Process Spec)

## 1. 功能概述
處理用戶的退款申請，並進行後台自動與手動審查。

## 2. 審查狀態流轉
- `SUBMITTED` -> `AUTO_CHECKING` (系統自動驗證)
- `AUTO_CHECKING` -> `PENDING_HUMAN` (待人工審核)
- `PENDING_HUMAN` -> `APPROVED` 或 `REJECTED`
- 交易金額低於 $500 且無異常紀錄者，跳過人工審核直接 `APPROVED`。