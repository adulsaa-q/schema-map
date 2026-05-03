# film

> **Rows:** 1,000

## Columns

| column | type | nullable | key | note |
|--------|------|----------|-----|------|
| film_id | INTEGER |  | PK 🔑 |  |
| title | TEXT |  |  |  |
| description | TEXT | ✓ |  |  |
| release_year | DOMAIN | ✓ |  |  |
| language_id | INTEGER |  | FK 🔗 | → [[language]].language_id (many-to-one) |
| original_language_id | INTEGER | ✓ | FK 🔗 | → [[language]].language_id (many-to-one) |
| rental_duration | SMALLINT |  |  |  |
| rental_rate | NUMERIC(4, 2) |  |  |  |
| length | SMALLINT | ✓ |  |  |
| replacement_cost | NUMERIC(5, 2) |  |  |  |
| rating | VARCHAR(5) | ✓ |  |  |
| last_update | TIMESTAMP |  |  |  |
| special_features | ARRAY | ✓ |  |  |
| fulltext | TSVECTOR |  |  |  |

## Relations (outgoing)

- `language_id` → [[language]].`language_id` — **many-to-one**
- `original_language_id` → [[language]].`language_id` — **many-to-one**

## Relations (incoming)

- [[inventory]].`film_id` → `film_id` — **one-to-many**
- [[film_actor]].`film_id` → `film_id` — **one-to-many**
- [[film_category]].`film_id` → `film_id` — **one-to-many**

## Indexes

| name | columns | unique |
|------|---------|--------|
| film_fulltext_idx | fulltext |  |
| idx_fk_language_id | language_id |  |
| idx_fk_original_language_id | original_language_id |  |
| idx_title | title |  |
