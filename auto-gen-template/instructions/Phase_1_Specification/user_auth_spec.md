# 使用者身分驗證與授權模組規格書 (User Auth Spec)

## 1. 功能概述
負責使用者註冊、密碼雜湊儲存、使用者登入、JWT 發行與 Token 驗證。

## 2. 介面定義
### 函數：`registerUser(email: string, passwordPlain: string) -> UserResult`
*   **輸入參數**：
    - `email`: 合法的 Email 格式。
    - `passwordPlain`: 最少 8 個字元，須包含英文與數字。
*   **異常處理**：
    - 若 Email 已被使用，拋出 `USER_ALREADY_EXISTS`。
    - 若密碼不符強度限制，拋出 `WEAK_PASSWORD`。

### 函數：`loginUser(email: string, passwordPlain: string) -> AuthToken`
*   **輸入參數**：
    - 帳號與密碼。
*   **輸出**：
    - `accessToken`: 效期 1 小時的 JWT。
*   **異常處理**：
    - 帳密不符時，拋出 `UNAUTHORIZED_CREDENTIALS`。

## 3. 安全規則
- 密碼存入 DB 前，必須使用 `bcrypt` 進行雜湊，工作因子 (Salt Rounds) 設為 10。
- JWT 簽章演算法必須使用 `HS256`。
