# 閮撅亦?????蝘餃祕雿?靘?(Order Fulfillment Service Example)

```typescript
export async function processFulfillment(orderId: string, action: string) {
  if (action === "REFUND") {
    throw new Error("CANNOT_REFUND_SHIPPED_ORDER");
  }
  return { id: orderId, status: "SHIPPED" };
}
```