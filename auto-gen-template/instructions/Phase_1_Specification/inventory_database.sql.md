# 摨怠?鞈?摨?DDL 閬 (Inventory Database Schema)

```sql
CREATE TABLE inventory (
    product_id VARCHAR(50) PRIMARY KEY,
    stock_quantity INT NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    warehouse_code VARCHAR(20) NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE INDEX idx_warehouse ON inventory(warehouse_code);
```