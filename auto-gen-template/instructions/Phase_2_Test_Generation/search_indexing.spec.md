# ??蝝Ｗ??郊?閰Ｘ葫閰衣?靘?(Search Indexing Test Example)

```typescript
import { searchProducts } from "../Phase_3_Implementation/search_indexer";

describe("???冽?瑼Ｙ揣皜祈岫", () => {
  test("頛詨?摮璅∠?????", async () => {
    const results = await searchProducts("iphne"); // ?澆神?航炊
    expect(results.length).toBeGreaterThan(0);
    expect(results[0].name).toContain("iPhone");
  });
});
```