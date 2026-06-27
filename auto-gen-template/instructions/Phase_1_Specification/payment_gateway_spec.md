# 金流閘道介接規格書 (Payment Gateway Spec)

## 1. 功能概述
介接第三方金流 API 處理信用卡扣款，保證交易之冪等性 (Idempotency) 與狀態流轉之一致性。

## 2. 狀態機定義
```text
[CREATED] --> (扣款中) --> [SUCCESS]
                     --> [FAILED]
```

## 3. 冪等性控制
- 每次請求必須攜帶 `Idempotency-Key` (UUIDv4)。
- 若金流閘道收到重複的 `Idempotency-Key` 且狀態為 `SUCCESS`，直接傳回上次的交易結果，不可重複扣款。
