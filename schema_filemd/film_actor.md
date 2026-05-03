# film_actor

> **Rows:** 5,462
> **Type:** Junction table (many-to-many)

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| actor_id | INTEGER |  | PK 🔑 FK 🔗 | → [[actor]].actor_id (one-to-one) |
| film_id | INTEGER |  | PK 🔑 FK 🔗 | → [[film]].film_id (one-to-one) |
| last_update | TIMESTAMP |  |  |  |

## Relations (outgoing)

- `actor_id` → [[actor]].`actor_id` — **one-to-one**
- `film_id` → [[film]].`film_id` — **one-to-one**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_fk_film_id | film_id |  |
