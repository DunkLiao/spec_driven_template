# 頨怠?撽???甈芋蝯祕雿?靘?(Auth Controller Implementation Example)

```typescript
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';

export interface UserResult {
  id: string;
  passwordHash: string;
}

const JWT_SECRET = process.env.JWT_SECRET || 'dev_secret';

export async function registerUser(email: string, passwordPlain: string): Promise<UserResult> {
  if (passwordPlain.length < 8) {
    throw new Error('WEAK_PASSWORD');
  }

  const passwordHash = await bcrypt.hash(passwordPlain, 10);
  return {
    id: 'user_' + Date.now(),
    passwordHash
  };
}

export function generateToken(userId: string): string {
  return jwt.sign({ userId }, JWT_SECRET, { algorithm: 'HS256', expiresIn: '1h' });
}

```
