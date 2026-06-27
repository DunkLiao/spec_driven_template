# 撣喳????蝝?霅祕雿?靘?(Billing Controller Example)

```typescript
export function validateBillingRequest(body: any) {
  if (!body.orderId) {
    return { status: 400 };
  }
  return { status: 201 };
}
```