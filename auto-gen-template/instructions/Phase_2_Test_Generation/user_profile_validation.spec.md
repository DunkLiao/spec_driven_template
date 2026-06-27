# ?冽閮剖?瑼?Schema 撽?皜祈岫蝭? (User Profile Validation Test Example)

```typescript
import { validateProfile } from "../Phase_3_Implementation/user_profile_validator";

describe("閮剖?瑼?JSON Schema ?⊿?皜祈岫", () => {
  test("?芸‵撖急蝔望???⊿?憭望?", () => {
    const result = validateProfile({ gender: "MALE" });
    expect(result.isValid).toBe(false);
    expect(result.errors).toContain("nickname is required");
  });
});
```