# 摨怠?鞈?銵券?靽?蝝Ｗ?撽?皜祈岫蝭? (Inventory DB Migration Test Example)

```typescript
import { verifyInventoryIndexes } from "../Phase_3_Implementation/inventory_repository";

describe("鞈?摨?Schema ?揣撘??湔扳葫閰?, () => {
  test("鞈?銵典??遣蝡澈甈?蝝Ｗ?", async () => {
    const indexes = await verifyInventoryIndexes();
    expect(indexes).toContain("idx_warehouse");
  });
});
```