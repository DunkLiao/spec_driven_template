# ?????蝑扳?嗅祕雿?靘?(Payment Handler Implementation Example)

```typescript
const processedKeys = new Set<string>();

export async function processPayment(
  idempotencyKey: string,
  amount: number,
  gatewayCall: () => Promise<{ status: string; transactionId: string }>
) {
  if (processedKeys.has(idempotencyKey)) {
    return { status: 'SUCCESS', transactionId: 'tx_dup_' + idempotencyKey };
  }

  const result = await gatewayCall();
  if (result.status === 'SUCCESS') {
    processedKeys.add(idempotencyKey);
  }
  return result;
}

```
