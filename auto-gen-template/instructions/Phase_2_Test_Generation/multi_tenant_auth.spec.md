# 蝘甈?????冽葫閰衣?靘?(Multi-Tenant Auth Test Example)

```typescript
import { checkTenantAccess } from "../Phase_3_Implementation/multi_tenant_context";

describe("憭??嗉????Ｗ??冽葫閰?, () => {
  test("摮???撅祉??嗡?鞈????箸???蝯?, () => {
    expect(() => checkTenantAccess("tenant_A", "data_of_tenant_B")).toThrow("FORBIDDEN_TENANT_ACCESS");
  });
});
```