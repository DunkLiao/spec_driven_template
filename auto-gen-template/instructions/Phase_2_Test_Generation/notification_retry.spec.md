# ??岫???賊?踵??嗆葫閰虫誨蝣潛?靘?(Notification Retry Test Example)

```typescript
import { sendNotificationWithRetry } from '../Phase_3_Implementation/notification_sender';

describe('非同步通知重試退避機制測試', () => {
  test('發送失敗時應進行指數退避重試', async () => {
    jest.useFakeTimers();
    const failSender = jest.fn().mockRejectedValue(new Error('NETWORK_TIMEOUT'));

    const promise = sendNotificationWithRetry({ type: 'SMS', to: '0912345678' }, failSender);

    // 第一次重試延遲: 10 * 2^1 = 20 秒
    jest.advanceTimersByTime(20000);
    // 第二次重試延遲: 10 * 2^2 = 40 秒
    jest.advanceTimersByTime(40000);

    await expect(promise).rejects.toThrow('DEAD_LETTER');
    expect(failSender).toHaveBeenCalledTimes(4); // 1次首發 + 3次重試
  });
});

```
