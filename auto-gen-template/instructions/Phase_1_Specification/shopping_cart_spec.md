# 購物車管理模組規格書 (Shopping Cart Spec)

## 1. 功能概述
管理用戶購物車內容物，包含商品的新增、修改、刪除，以及結算總額（包含多個促銷折扣計算）。

## 2. 資料結構
```typescript
interface CartItem {
  productId: string;
  quantity: number;
  unitPrice: number;
}
```

## 3. 折扣規則
- **滿額折**：購物車原價總額滿 $2,000，現折 $200。
- **免運折**：滿 $1,000 免運費（運費預設為 $80）。
- 折扣計算順序：原價加總 -> 滿額折抵 -> 免運判定 -> 最終應付金額。
