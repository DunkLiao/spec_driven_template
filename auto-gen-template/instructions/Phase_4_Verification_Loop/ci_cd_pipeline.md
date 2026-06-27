# ?芸???CI/CD 瘚偌蝺?蝵桃?靘?(CI/CD Pipeline Configuration Example)

```yaml
name: Spec-Driven Development CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  sdd-validation:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: 18

    - name: Install dependencies
      run: npm install

    - name: Run Spec Compliance Tests
      run: npm run test:coverage

```
