# 頨怠?撽??桀?皜祈岫隞?Ⅳ蝭? (Auth Unit Test Example)

```typescript
import { registerUser } from '../Phase_3_Implementation/auth_controller';

describe('身分驗證模組單元測試', () => {
  test('正常註冊與雜湊確認', async () => {
    const user = await registerUser('test@example.com', 'SecurePass123');
    expect(user.id).toBeDefined();
    expect(user.passwordHash).not.toBe('SecurePass123'); // 不能儲存明文
  });

  test('無效的密碼格式應拋出異常', async () => {
    await expect(registerUser('test@example.com', '123')).rejects.toThrow('WEAK_PASSWORD');
  });

  test('重複註冊相同 Email 應拋出異常', async () => {
    await registerUser('dup@example.com', 'Password123');
    await expect(registerUser('dup@example.com', 'Password123')).rejects.toThrow('USER_ALREADY_EXISTS');
  });
});

```
