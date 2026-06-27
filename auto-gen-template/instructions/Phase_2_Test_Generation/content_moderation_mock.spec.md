# ?批捆撖拇?? Mock 皜祈岫蝭? (Content Moderation Mock Test Example)

```typescript
import { moderateContent } from "../Phase_3_Implementation/content_moderator";

describe("?批捆?蕪 Mock ?游?皜祈岫", () => {
  test("?菜葫?唳???敶??芸??脰??踵?", async () => {
    const cleanText = await moderateContent("?銝蝭??瘜陪????");
    expect(cleanText).toBe("?銝蝭??**??蝡?);
  });
});
```