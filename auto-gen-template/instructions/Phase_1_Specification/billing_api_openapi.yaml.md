# 撣喳?蝟餌絞 OpenAPI 閬??(Billing OpenAPI Spec)

```yaml
openapi: 3.0.0
info:
  title: Billing API
  version: 1.0.0
paths:
  /api/bills:
    post:
      summary: 撱箇?撣喳
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                orderId: { type: string }
                amount: { type: number }
              required: [orderId, amount]
      responses:
        "201":
          description: 撣喳撱箇???
```