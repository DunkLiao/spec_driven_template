# Debug 診斷報告：金流密等性失效

## 1. 失敗測試
- **Test Case**: `相同 Idempotency-Key 重複請求不應重複扣款`
- **錯誤訊息**: `Expected mockPaymentCall to have been called 1 time, but called 2 times.`

## 2. 根本原因分析 (RCA)
在 `payment_handler.ts` 中，內存中的 `processedKeys` 集合未被正確宣告為全域變數，而是被宣告在函數內部，導致每次執行 `processPayment` 時，集合都被重新初始化為空，導致冪等性過濾失效。

## 3. 修復方案
將 `processedKeys` 的宣告移至函數外部（或使用持久化 Redis 快取鎖定）。
```diff
- export async function processPayment(...) {
-   const processedKeys = new Set<string>();
+ const processedKeys = new Set<string>();
+ export async function processPayment(...) {
```
