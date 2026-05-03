# inventory

> **Rows:** 4,581

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| inventory_id | INTEGER |  | PK 🔑 |  |
| film_id | INTEGER |  | FK 🔗 | → [[film]].film_id (many-to-one) |
| store_id | INTEGER |  | FK 🔗 | → [[store]].store_id (many-to-one) |
| last_update | TIMESTAMP |  |  |  |

## Relations (outgoing)

- `film_id` → [[film]].`film_id` — **many-to-one**
- `store_id` → [[store]].`store_id` — **many-to-one**

## Relations (incoming)

- [[rental]].`inventory_id` → `inventory_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_store_id_film_id | store_id, film_id |  |
