# ?刻撘?瞍?瘜?頛舀葫閰衣?靘?(Recommendation Algorithm Test Example)

```typescript
import { getRecommendations } from "../Phase_3_Implementation/recommendation_engine";

describe("?刻撘?甈?????蝞葫閰?, () => {
  test("??憿???行????? 20%", () => {
    const recs = getRecommendations("user_01", ["prod_shampoo"]);
    expect(recs[0].scoreBoost).toBe(1.2);
  });
});
```