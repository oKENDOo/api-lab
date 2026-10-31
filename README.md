| Characteristic | Blocks | Test values |
|---|---|---|
| C1 Value of stars | below 1, 1–5, above 5 | `0`, `3`, `6` |
| C2 Type of stars | whole number, decimal, text, missing | `3`, `3.5`, `"3"`, ไม่มี field |
| C3 Pizza | exists, does not exist | `pizza_id`, `99999999` |
| C4 Token | own token, none, malformed | `auth`, ไม่มี header, token สั้น |