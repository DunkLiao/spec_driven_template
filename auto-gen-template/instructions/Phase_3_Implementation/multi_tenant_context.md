# 憭??嗡?銝??????Ｗ祕雿?靘?(Multi-Tenant Context Example)

```typescript
export function checkTenantAccess(userTenantId: string, dataTenantId: string) {
  if (userTenantId !== dataTenantId) {
    throw new Error("FORBIDDEN_TENANT_ACCESS");
  }
  return true;
}
```