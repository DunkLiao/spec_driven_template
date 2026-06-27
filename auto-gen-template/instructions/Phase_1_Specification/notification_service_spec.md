# 非同步通知發送規格書 (Notification Service Spec)

## 1. 功能概述
非同步發送 Email 與 SMS 通知，支援佇列重試機制與發送狀態追蹤。

## 2. 重試與退避規則 (Retry & Backoff)
- 當發送失敗時，必須重試最多 3 次。
- 重試退避演算法：`delay = base_delay * (2 ^ attempt)`，其中 `base_delay` 為 10 秒。
- 3 次失敗後，標記狀態為 `DEAD_LETTER`。
