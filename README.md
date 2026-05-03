# schema-map

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-compatible-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Turn a PostgreSQL database schema into an interactive Obsidian Graph View — then query it in natural language with Claude.

```
python3 schema_to_obsidian.py  →  vault/*.md  →  Obsidian Graph  →  Ask Claude
```

---

## Problem

Large databases are hard to navigate. Which table connects to which? Through what column? This tool makes the answer visual and queryable — without building a production system.

---

## How it works

`schema_to_obsidian.py` inspects the database and writes one `.md` file per table:

- **Columns** with types, nullable flags, PK/FK markers
- **Relations** (outgoing + incoming) as Obsidian `[[wikilinks]]`
- **Indexes** for query planning
- **`_index.md`** — a single manifest listing every table and its connections

Open the output folder in Obsidian → press `Cmd+G` (Mac) / `Ctrl+G` (Windows/Linux) → see the schema graph.  
Ask questions directly in Claude Code — it reads only the relevant files, not the whole schema.

---

## Screenshot

> _Obsidian Graph View — each node is a table, each edge is a FK relationship_

![Obsidian Graph View](image/Obsidian_Graph_View.png)

---

## Quickstart

**1. Install dependencies**
```bash
pip install sqlalchemy psycopg2-binary
```

**2. Run against your database**
```bash
python3 schema_to_obsidian.py

# custom DB
DB_URL=postgresql://user:pass@host/dbname python3 schema_to_obsidian.py

# custom output folder
VAULT_DIR=/path/to/vault python3 schema_to_obsidian.py
```

**3. Open vault in Obsidian**
- Open Obsidian → `Open folder as vault` → select `schema_filemd/`
- Press `Cmd+G` (Mac) / `Ctrl+G` (Windows/Linux) to open Graph View

**4. Ask Claude**

Open the project in VS Code with Claude Code, then ask naturally:

```
"How do I join film with actor?"
"Which tables connect to customer_id?"
"What is the path between customer and payment?"
```

---

## Output format

Each table becomes a `.md` file:

```markdown
# rental

> **Rows:** 16,044

## Columns

| column       | type      | nullable | key   | note                                       |
|--------------|-----------|----------|-------|--------------------------------------------|
| rental_id    | INTEGER   |          | PK 🔑 |                                            |
| inventory_id | INTEGER   |          | FK 🔗 | → [[inventory]].inventory_id (many-to-one) |
| customer_id  | INTEGER   |          | FK 🔗 | → [[customer]].customer_id (many-to-one)   |
| return_date  | TIMESTAMP | ✓        |       |                                            |

## Relations (outgoing)

- `customer_id` → [[customer]].`customer_id` — **many-to-one**

## Relations (incoming)

- [[payment_p2022_01]].`rental_id` → `rental_id` — **one-to-many**

## Indexes

| name                 | columns      | unique |
|----------------------|--------------|--------|
| idx_rental_customer  | customer_id  |        |
```

---

## Design goals

| Goal | Approach |
|------|----------|
| **Fast** | Pre-generated snapshots — no DB query at question time |
| **Accurate** | Explicit FK + nullable flags + index info |
| **Token-efficient** | Claude reads only the relevant subgraph |

---

## Environment variables

| Variable | Default | Description |
|----------|---------|-------------|
| `DB_URL` | `postgresql://postgres@localhost/pagila` | SQLAlchemy connection string |
| `VAULT_DIR` | `schema_filemd/` | Output folder for `.md` files |

---

## Limitations

- `.md` files are snapshots — re-run script after schema changes
- FK detection requires explicit constraints in the database

---

## Requirements

- Python 3.9+
- PostgreSQL (tested with [Pagila](https://github.com/devrimgunduz/pagila) sample DB)
- [Obsidian](https://obsidian.md) for graph visualization
- [Claude Code](https://claude.ai/code) for natural language queries

---

## Example queries (Pagila)

```sql
-- "How do I join film with actor?"
SELECT f.title, a.first_name, a.last_name
FROM film f
JOIN film_actor fa ON f.film_id   = fa.film_id
JOIN actor a       ON fa.actor_id = a.actor_id;

-- "Which country has the most customers and what category do they prefer?"
WITH top_country AS (
    SELECT co.country_id, co.country
    FROM customer c
    JOIN address a  ON c.address_id  = a.address_id
    JOIN city    ci ON a.city_id     = ci.city_id
    JOIN country co ON ci.country_id = co.country_id
    GROUP BY co.country_id, co.country
    ORDER BY COUNT(*) DESC
    LIMIT 1
),
country_customers AS (
    SELECT c.customer_id
    FROM customer c
    JOIN address a  ON c.address_id  = a.address_id
    JOIN city    ci ON a.city_id     = ci.city_id
    JOIN top_country tc ON ci.country_id = tc.country_id
)
SELECT
    tc.country,
    cat.name        AS category,
    COUNT(DISTINCT r.rental_id) AS rental_count
FROM country_customers cc
JOIN rental        r   ON cc.customer_id = r.customer_id
JOIN inventory     i   ON r.inventory_id = i.inventory_id
JOIN film_category fc  ON i.film_id      = fc.film_id
JOIN category      cat ON fc.category_id = cat.category_id
JOIN top_country   tc  ON 1=1
GROUP BY tc.country, cat.name
ORDER BY rental_count DESC
LIMIT 5;
```

---

## License

MIT