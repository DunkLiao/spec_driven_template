# ?冽閮剖?瑼?JSON Schema (User Profile Schema)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "UserProfile",
  "type": "object",
  "properties": {
    "nickname": { "type": "string", "maxLength": 50 },
    "avatarUrl": { "type": "string", "format": "uri" },
    "gender": { "type": "string", "enum": ["MALE", "FEMALE", "OTHER"] }
  },
  "required": ["nickname"]
}
```