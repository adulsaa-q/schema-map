# payment_p2022_06

> **Rows:** 2,654

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| payment_id | INTEGER |  | PK 🔑 |  |
| customer_id | INTEGER |  | FK 🔗 | → [[customer]].customer_id (many-to-one) |
| staff_id | INTEGER |  | FK 🔗 | → [[staff]].staff_id (many-to-one) |
| rental_id | INTEGER |  | FK 🔗 | → [[rental]].rental_id (many-to-one) |
| amount | NUMERIC(5, 2) |  |  |  |
| payment_date | TIMESTAMP |  | PK 🔑 |  |

## Relations (outgoing)

- `customer_id` → [[customer]].`customer_id` — **many-to-one**
- `rental_id` → [[rental]].`rental_id` — **many-to-one**
- `staff_id` → [[staff]].`staff_id` — **many-to-one**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_fk_payment_p2022_06_customer_id | customer_id |  |
| idx_fk_payment_p2022_06_staff_id | staff_id |  |
| payment_p2022_06_customer_id_idx | customer_id |  |
