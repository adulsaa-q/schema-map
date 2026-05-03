# address

> **Rows:** 603

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| address_id | INTEGER |  | PK 🔑 |  |
| address | TEXT |  |  |  |
| address2 | TEXT | ✓ |  |  |
| district | TEXT |  |  |  |
| city_id | INTEGER |  | FK 🔗 | → [[city]].city_id (many-to-one) |
| postal_code | TEXT | ✓ |  |  |
| phone | TEXT |  |  |  |
| last_update | TIMESTAMP |  |  |  |

## Relations (outgoing)

- `city_id` → [[city]].`city_id` — **many-to-one**

## Relations (incoming)

- [[customer]].`address_id` → `address_id` — **one-to-many**
- [[staff]].`address_id` → `address_id` — **one-to-many**
- [[store]].`address_id` → `address_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_fk_city_id | city_id |  |
