# category

> **Rows:** 16

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| category_id | INTEGER |  | PK 🔑 |  |
| name | TEXT |  |  |  |
| last_update | TIMESTAMP |  |  |  |

## Relations (incoming)

- [[film_category]].`category_id` → `category_id` — **one-to-many**
