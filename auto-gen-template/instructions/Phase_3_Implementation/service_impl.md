# 實作範例：服務層實作

說明：示範如何從測試驅動的規格逐步實作服務層，包含介面定義與錯誤處理。

`	ypescript
export function calculateTotal(items: {price:number, qty:number}[]) {
  return items.reduce((s, i) => s + i.price * i.qty, 0);
}
`
"@},
    @{path=Join-Path D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_1_Specification D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_2_Test_Generation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_3_Implementation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_4_Verification_Loop[2] 'cart_service.md'; content=@"
# 購物車服務範例

說明：購物車核心邏輯實作範例，包含加入項目、移除、計價與折扣邏輯。