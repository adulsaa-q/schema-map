# customer

> **Rows:** 599

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| customer_id | INTEGER |  | PK 🔑 |  |
| store_id | INTEGER |  | FK 🔗 | → [[store]].store_id (many-to-one) |
| first_name | TEXT |  |  |  |
| last_name | TEXT |  |  |  |
| email | TEXT | ✓ |  |  |
| address_id | INTEGER |  | FK 🔗 | → [[address]].address_id (many-to-one) |
| activebool | BOOLEAN |  |  |  |
| create_date | DATE |  |  |  |
| last_update | TIMESTAMP | ✓ |  |  |
| active | INTEGER | ✓ |  |  |

## Relations (outgoing)

- `address_id` → [[address]].`address_id` — **many-to-one**
- `store_id` → [[store]].`store_id` — **many-to-one**

## Relations (incoming)

- [[payment_p2022_06]].`customer_id` → `customer_id` — **one-to-many**
- [[rental]].`customer_id` → `customer_id` — **one-to-many**
- [[payment_p2022_03]].`customer_id` → `customer_id` — **one-to-many**
- [[payment_p2022_04]].`customer_id` → `customer_id` — **one-to-many**
- [[payment_p2022_05]].`customer_id` → `customer_id` — **one-to-many**
- [[payment_p2022_01]].`customer_id` → `customer_id` — **one-to-many**
- [[payment_p2022_02]].`customer_id` → `customer_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_fk_address_id | address_id |  |
| idx_fk_store_id | store_id |  |
| idx_last_name | last_name |  |
