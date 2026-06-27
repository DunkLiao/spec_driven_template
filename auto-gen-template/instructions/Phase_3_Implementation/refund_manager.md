# 撠??甈曇?祟?詨祕雿?靘?(Refund Manager Example)

```typescript
export async function runRefundFlow(refundId: string, amount: number) {
  if (amount < 500) {
    return { id: refundId, status: "APPROVED" };
  }
  return { id: refundId, status: "PENDING_HUMAN" };
}
```