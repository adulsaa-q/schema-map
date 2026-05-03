# language

> **Rows:** 6

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| language_id | INTEGER |  | PK 🔑 |  |
| name | CHAR(20) |  |  |  |
| last_update | TIMESTAMP |  |  |  |

## Relations (incoming)

- [[film]].`language_id` → `language_id` — **one-to-many**
- [[film]].`original_language_id` → `language_id` — **one-to-many**
