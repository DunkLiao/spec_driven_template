# ???桅?????瞈曉祕雿?靘?(Catalog Repository Implementation Example)

```typescript
export function validateQueryParams(page: number, limit: number) {
  if (page < 1) {
    throw new Error('INVALID_PAGE');
  }

  const verifiedLimit = limit > 100 ? 100 : limit;
  return {
    page,
    limit: verifiedLimit
  };
}

```
