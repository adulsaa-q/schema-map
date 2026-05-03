# actor

> **Rows:** 200

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| actor_id | INTEGER |  | PK 🔑 |  |
| first_name | TEXT |  |  |  |
| last_name | TEXT |  |  |  |
| last_update | TIMESTAMP |  |  |  |

## Relations (incoming)

- [[film_actor]].`actor_id` → `actor_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| idx_actor_last_name | last_name |  |
