# 商品搜尋與索引建立規格書 (Search Indexing Spec)

## 1. 功能概述
同步資料庫商品異動至 Elasticsearch，並提供多維度全文檢索 API。

## 2. 搜尋語法限制
- 支援關鍵字模糊搜尋 (Fuzzy Search)，編輯距離 (Levenshtein Distance) 預設為 2。
- 篩選條件：價格區間、分類 ID、庫存狀態 (必須大於 0)。