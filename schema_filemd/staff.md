# staff

> **Rows:** 1,500

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| staff_id | INTEGER |  | PK 🔑 |  |
| first_name | TEXT |  |  |  |
| last_name | TEXT |  |  |  |
| address_id | INTEGER |  | FK 🔗 | → [[address]].address_id (many-to-one) |
| email | TEXT | ✓ |  |  |
| store_id | INTEGER |  | FK 🔗 | → [[store]].store_id (many-to-one) |
| active | BOOLEAN |  |  |  |
| username | TEXT |  |  |  |
| password | TEXT | ✓ |  |  |
| last_update | TIMESTAMP |  |  |  |
| picture | BYTEA | ✓ |  |  |

## Relations (outgoing)

- `address_id` → [[address]].`address_id` — **many-to-one**
- `store_id` → [[store]].`store_id` — **many-to-one**

## Relations (incoming)

- [[payment_p2022_06]].`staff_id` → `staff_id` — **one-to-many**
- [[rental]].`staff_id` → `staff_id` — **one-to-many**
- [[payment_p2022_03]].`staff_id` → `staff_id` — **one-to-many**
- [[payment_p2022_04]].`staff_id` → `staff_id` — **one-to-many**
- [[payment_p2022_05]].`staff_id` → `staff_id` — **one-to-many**
- [[payment_p2022_01]].`staff_id` → `staff_id` — **one-to-many**
- [[payment_p2022_02]].`staff_id` → `staff_id` — **one-to-many**
