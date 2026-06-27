# ??甇仿?潮祕雿?靘?(Notification Sender Implementation Example)

```typescript
export async function sendNotificationWithRetry(
  notification: { type: string; to: string },
  sender: () => Promise<void>
) {
  let attempt = 0;
  while (attempt <= 3) {
    try {
      await sender();
      return;
    } catch (err) {
      attempt++;
      if (attempt > 3) {
        throw new Error('DEAD_LETTER');
      }
      const delay = 10000 * Math.pow(2, attempt);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

```
