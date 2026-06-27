# 驗證：API 偏移檢查 範例

示範如何自動檢測 API 行為偏移（contracts drift）並回報。

```typescript
// pseudo: 比對現行 API schema 與合約檔案
import { compareSchemas } from '../../tools/schema_diff';
const diffs = compareSchemas(currentSchema, contractSchema);
```
