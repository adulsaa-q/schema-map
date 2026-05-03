# rental

> **Rows:** 16,044

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| rental_id | INTEGER |  | PK 🔑 |  |
| rental_date | TIMESTAMP |  |  |  |
| inventory_id | INTEGER |  | FK 🔗 | → [[inventory]].inventory_id (many-to-one) |
| customer_id | INTEGER |  | FK 🔗 | → [[customer]].customer_id (many-to-one) |
| return_date | TIMESTAMP | ✓ |  |  |
| staff_id | INTEGER |  | FK 🔗 | → [[staff]].staff_id (many-to-one) |
| last_update | TIMESTAMP |  |  |  |

## Relations (outgoing)

- `customer_id` → [[customer]].`customer_id` — **many-to-one**
- `inventory_id` → [[inventory]].`inventory_id` — **many-to-one**
- `staff_id` → [[staff]].`staff_id` — **many-to-one**

## Relations (incoming)

- [[payment_p2022_06]].`rental_id` → `rental_id` — **one-to-many**
- [[payment_p2022_03]].`rental_id` → `rental_id` — **one-to-many**
- [[payment_p2022_04]].`rental_id` → `rental_id` — **one-to-many**
- [[payment_p2022_05]].`rental_id` → `rental_id` — **one-to-many**
- [[payment_p2022_01]].`rental_id` → `rental_id` — **one-to-many**
- [[payment_p2022_02]].`rental_id` → `rental_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_fk_inventory_id | inventory_id |  |
| idx_unq_rental_rental_date_inventory_id_customer_id | rental_date, inventory_id, customer_id | ✓ |
