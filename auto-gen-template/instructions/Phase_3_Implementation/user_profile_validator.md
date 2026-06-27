# ?冽閮剖?瑼?Schema 撽??典祕雿?靘?(User Profile Validator Example)

```typescript
export function validateProfile(data: any) {
  if (!data.nickname) {
    return { isValid: false, errors: ["nickname is required"] };
  }
  return { isValid: true, errors: [] };
}
```