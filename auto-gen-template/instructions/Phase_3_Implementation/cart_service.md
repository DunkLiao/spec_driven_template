# 鞈潛頠?蝞???摩撖虫?蝭? (Cart Service Implementation Example)

```typescript
export interface CartItem {
  productId: string;
  quantity: number;
  unitPrice: number;
}

export function calculateTotal(items: CartItem[]) {
  const originalTotal = items.reduce((sum, item) => sum + item.quantity * item.unitPrice, 0);
  
  // 1. 滿額折抵
  let discount = 0;
  if (originalTotal >= 2000) {
    discount = 200;
  }

  // 2. 運費計算
  const shippingFee = originalTotal >= 1000 ? 0 : 80;

  return {
    originalPrice: originalTotal,
    discountedPrice: originalTotal - discount,
    shippingFee,
    finalPayable: originalTotal - discount + shippingFee
  };
}

```
