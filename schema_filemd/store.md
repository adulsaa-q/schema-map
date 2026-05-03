# store

> **Rows:** 500

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| store_id | INTEGER |  | PK 🔑 |  |
| manager_staff_id | INTEGER |  |  |  |
| address_id | INTEGER |  | FK 🔗 | → [[address]].address_id (many-to-one) |
| last_update | TIMESTAMP |  |  |  |

## Relations (outgoing)

- `address_id` → [[address]].`address_id` — **many-to-one**

## Relations (incoming)

- [[inventory]].`store_id` → `store_id` — **one-to-many**
- [[customer]].`store_id` → `store_id` — **one-to-many**
- [[staff]].`store_id` → `store_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_unq_manager_staff_id | manager_staff_id | ✓ |
