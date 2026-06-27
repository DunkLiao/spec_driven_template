# ??璅⊥?蝑扳葫閰虫誨蝣潛?靘?(Payment Mock Test Example)

```typescript
import { processPayment } from '../Phase_3_Implementation/payment_handler';

describe('金流模擬與冪等性測試', () => {
  test('相同 Idempotency-Key 的重複請求應返回相同結果且只扣款一次', async () => {
    const key = 'unique-transaction-1234';
    const mockPaymentCall = jest.fn().mockResolvedValue({ status: 'SUCCESS', transactionId: 'tx_999' });

    const call1 = await processPayment(key, 1500, mockPaymentCall);
    const call2 = await processPayment(key, 1500, mockPaymentCall);

    expect(call1.status).toBe('SUCCESS');
    expect(call2.transactionId).toBe(call1.transactionId);
    expect(mockPaymentCall).toHaveBeenCalledTimes(1); // 僅被扣款一次
  });
});

```
