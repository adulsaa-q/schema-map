# city

> **Rows:** 600

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| city_id | INTEGER |  | PK 🔑 |  |
| city | TEXT |  |  |  |
| country_id | INTEGER |  | FK 🔗 | → [[country]].country_id (many-to-one) |
| last_update | TIMESTAMP |  |  |  |

## Relations (outgoing)

- `country_id` → [[country]].`country_id` — **many-to-one**

## Relations (incoming)

- [[address]].`city_id` → `city_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_fk_country_id | country_id |  |
