# ?拇????祥??蝞祕雿?靘?(Shipping Calculator Example)

```typescript
export function calculateShipping(weight: number, zipcode: string) {
  let fee = 80;
  if (zipcode === "880") { fee += 120; }
  return fee;
}
```