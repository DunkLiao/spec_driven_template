# ?甈暹?蝔?E2E ?芸??葫閰衣?靘?(Refund Workflow E2E Test Example)

```typescript
import { runRefundFlow } from "../Phase_3_Implementation/refund_manager";

describe("?甈暹?蝔?E2E ?芸??葫閰?, () => {
  test("撠??甈暹?頝喲?鈭箏極撖拇?湔??", async () => {
    const refund = await runRefundFlow("ref_001", 350); // $350 < $500
    expect(refund.status).toBe("APPROVED");
  });
});
```