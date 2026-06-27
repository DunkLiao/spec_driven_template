# 鞈潛頠?蝞?葫閰虫誨蝣潛?靘?(Cart Integration Test Example)

```typescript
import { calculateTotal } from '../Phase_3_Implementation/cart_service';

describe('購物車計算整合測試', () => {
  test('滿 2000 折 200 且滿 1000 免運費', () => {
    const items = [
      { productId: 'p1', quantity: 2, unitPrice: 1100 } // 總共 2200 元
    ];
    const result = calculateTotal(items);
    // 運費: 0 (滿1000)
    // 扣折: 2200 - 200 = 2000 元
    expect(result.finalPayable).toBe(2000);
    expect(result.shippingFee).toBe(0);
  });

  test('未滿 1000 需付運費且無折扣', () => {
    const items = [
      { productId: 'p2', quantity: 1, unitPrice: 500 }
    ];
    const result = calculateTotal(items);
    expect(result.finalPayable).toBe(580); // 500 + 80 元運費
  });
});

```
