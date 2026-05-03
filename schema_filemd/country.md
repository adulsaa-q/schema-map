# country

> **Rows:** 109

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| country_id | INTEGER |  | PK 🔑 |  |
| country | TEXT |  |  |  |
| last_update | TIMESTAMP |  |  |  |

## Relations (incoming)

- [[city]].`country_id` → `country_id` — **one-to-many**
