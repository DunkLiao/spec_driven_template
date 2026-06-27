# 單元測試範例

說明：展示單元測試範例（使用 TypeScript / Jest）。

`	ypescript
import { sum } from '../Phase_3_Implementation/cart_service';

test('sum 計算正確', () => {
  expect(sum([1,2,3])).toBe(6);
});
`
"@},
    @{path=Join-Path D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_1_Specification D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_2_Test_Generation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_3_Implementation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_4_Verification_Loop[1] 'property_test.md'; content=@"
# 屬性測試（Property Testing）範例

說明：示範如何使用屬性測試工具來驗證不變性與邊界條件。

- 範例：排序結果長度不變且為遞增序列