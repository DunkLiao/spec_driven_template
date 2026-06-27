# 訂單履約狀態機整合測試範例 (Order Fulfillment Test Example)

```typescript
import { processFulfillment } from "../Phase_3_Implementation/order_fulfillment_service";

describe("訂單狀態機整合測試", () => {
  test("撿貨中訂單出貨後狀態轉為 SHIPPED", async () => {
    const order = { id: "o1", status: "PROCESSING" };
    const updated = await processFulfillment(order.id, "SHIP");
    expect(updated.status).toBe("SHIPPED");
  });

  test("已出貨訂單禁止直接退款", async () => {
    await expect(processFulfillment("o1", "REFUND")).rejects.toThrow("CANNOT_REFUND_SHIPPED_ORDER");
  });
});
```
