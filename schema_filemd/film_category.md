# film_category

> **Rows:** 2,367
> **Type:** Junction table (many-to-many)

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| film_id | INTEGER |  | PK 🔑 FK 🔗 | → [[film]].film_id (one-to-one) |
| category_id | INTEGER |  | PK 🔑 FK 🔗 | → [[category]].category_id (one-to-one) |
| last_update | TIMESTAMP |  |  |  |

## Relations (outgoing)

- `category_id` → [[category]].`category_id` — **one-to-one**
- `film_id` → [[film]].`film_id` — **one-to-one**
