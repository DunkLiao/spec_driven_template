# 驗收與部署要分清楚


請不要把「程式完成」等同於「產品完成」。

完成前請協助我確認：

* TypeScript 是否通過
* build 是否通過
* 本機是否正常
* Preview 是否正常
* Production 是否真的部署到最新版本
* 使用者流程是否走得通
* 資料是否正確出現
* UI 是否符合實際操作情境

如果正式站看不到新功能，請先提醒我檢查：

1. main 是否真的包含最新 commit
2. Vercel 是否建立 Production Deployment
3. Production domain 是否指向最新 deployment
4. 是否已做 smoke test

不要第一時間假設是程式錯。
