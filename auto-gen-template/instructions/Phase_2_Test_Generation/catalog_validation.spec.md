# ???桅? API ??⊿?皜祈岫隞?Ⅳ蝭? (Catalog Query Validation Test Example)

```typescript
import { validateQueryParams } from '../Phase_3_Implementation/catalog_repository';

describe('商品目錄 API Query 參數驗證測試', () => {
  test('頁碼小於 1 應拋出校驗錯誤', () => {
    expect(() => validateQueryParams(0, 20)).toThrow('INVALID_PAGE');
  });

  test('筆數超過 100 應自動限制在 100', () => {
    const params = validateQueryParams(1, 150);
    expect(params.limit).toBe(100);
  });
});

```
