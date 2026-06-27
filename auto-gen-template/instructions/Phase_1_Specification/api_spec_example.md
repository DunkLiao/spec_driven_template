# API 規格範例

說明：示範 REST API 規格格式，包括路由、方法、參數、回應與範例。

`yaml
path: /api/v1/cart
method: POST
request:
  body: { userId: string, items: [{ sku: string, qty: number }] }
responses:
  200: { total: number }
`
"@},
    @{path=Join-Path D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_1_Specification D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_2_Test_Generation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_3_Implementation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_4_Verification_Loop[0] 'data_model.md'; content=@"
# 資料模型範例

說明：示範資料庫模型與欄位定義，包含索引與關聯說明。

`sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL
);
`
"@},
    @{path=Join-Path D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_1_Specification D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_2_Test_Generation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_3_Implementation D:\VIbeCoding\spec_driven_template\auto-gen-template\instructions\Phase_4_Verification_Loop[0] 'ux_flow.md'; content=@"
# 使用者流程（UX Flow）範例

說明：以步驟化流程圖描述使用者互動，列出各步驟的前置條件與成功條件。

- 登入 -> 加入購物車 -> 結帳 -> 付款成功