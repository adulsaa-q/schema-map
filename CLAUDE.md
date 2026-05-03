# Schema Map — Project Brief

## Problem

- The database has many tables, making relationships hard to understand
- It is unclear which tables are connected and through which columns
- Need to open diagrams or ask a DBA every time
- Too manual and inefficient

---

## Core Idea

Create a script that reads the database schema and dumps it into `.md` files per table,  
then open them in **Obsidian** to use Graph View → visualize connections between tables

No need to build a production system — only use terminal + VS Code + Obsidian

---

## Workflow

Run python schema_to_obsidian.py
Get /vault/ folder with .md files per table
Open that folder in Obsidian
Press Ctrl+G → instantly see Graph View
Query Claude directly in VS Code / Terminal
Ask in natural language

---

## Current Status

- [x] `schema_to_obsidian.py` — runs successfully and passed security review
- [x] Obsidian Graph View — nodes and relationships are visible
- [x] Query schema via Claude Code directly (no separate API required)
- [ ] Auto-detect implicit FK
- [ ] Improve .md format readability

---

## Stack

- Python 3, SQLAlchemy, psycopg2
- PostgreSQL — Pagila database (localhost)
- Obsidian — Graph View viewer
- Claude Code — query schema directly without separate API

---

## Paths


vault: /Users/qdull/Documents/Vault/schema-map/schema_filemd/
script: schema_to_obsidian.py


---

## Database


DB: pagila (PostgreSQL localhost:5432)
User: postgres

---

## Components

| Part | Tool | Responsibility |
|------|------|---------------|
| Schema extractor | Python + SQLAlchemy | Read DB → columns, FK, row count |
| Relationship detector | FK + column naming | Detect implicit links (_id suffix) |
| MD generator | Python | Convert → .md files with [[wikilinks]] |
| Viewer | Obsidian Graph View | Visualize schema map |
| AI Query | Claude Code | Natural language querying |

---

## Next Steps (Priority)

### 1. Auto-detect implicit FK in schema_to_obsidian.py

- Columns ending with `_id` but without actual FK constraints in the database
- Match names with existing tables, e.g. `customer_id` → `customer`
- If matched → add `[[link]]` in .md and mark as `(implicit)`

### 2. Improve .md format readability

- Make relationship direction clearer (one-to-many / many-to-many)
- Clearly identify junction tables as many-to-many between related tables

---

## Example Queries to Support

- "Which tables are connected to customer_id?"
- "How to join film with actor?"
- "What is the path between customer and film?"
- "How is rental connected to payment?"

---

## Design Rules

Every feature must satisfy all three:

| Goal | How |
|------|-----|
| **Fast** | `.md` files are pre-generated snapshots — no DB query at question time |
| **Accurate** | Explicit FK + implicit FK (`_id` suffix) + correct relation types |
| **Token-efficient** | Read only the relevant subgraph, not all tables at once |

---

## Known Quirks (Pagila)

- `payment` is partitioned → actual data lives in `payment_p2022_01` through `_07`
- Views are not included in `.md` output
- `film.fulltext` is `TSVECTOR` — not a relation, ignore it

---

## Key Principles

- Not a production system — runs locally on a single machine
- `.md` = snapshot of schema at runtime — if schema changes, rerun the script
- Query Claude Code directly — no need to send schema via a separate API
- Override DB path: `DB_URL=postgresql://user@host/db python3 schema_to_obsidian.py`