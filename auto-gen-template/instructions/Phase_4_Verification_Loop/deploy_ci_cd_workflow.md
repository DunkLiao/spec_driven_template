# SDD 自動化發佈與部署 CD 配置範例 (CD Pipeline Configuration Example)

```yaml
name: Spec-Driven Deployment CD
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Deploy to Production
      run: echo "Deploying compliant code..."
```
