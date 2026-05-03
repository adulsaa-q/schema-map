import logging
import os
from sqlalchemy import create_engine, inspect, Table, MetaData, func, select

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# === CONFIG ===
DB_URL    = os.environ.get("DB_URL", "postgresql://postgres@localhost/pagila")
VAULT_DIR = os.environ.get("VAULT_DIR", os.path.join(os.path.dirname(__file__), "schema_filemd"))


def get_row_count(table_name: str, valid_tables: set[str]) -> int:
    if table_name not in valid_tables:
        raise ValueError(f"Unknown table: {table_name!r}")
    meta = MetaData()
    tbl = Table(table_name, meta, autoload_with=engine, schema="public")
    with engine.connect() as conn:
        result = conn.execute(select(func.count()).select_from(tbl))
        return result.scalar()


def detect_relation_type(fk_cols: set[str], pk_cols: set[str]) -> str:
    if fk_cols.issubset(pk_cols):
        return "one-to-one"
    return "many-to-one"

def main() -> None:
    global engine
    try:
        engine = create_engine(DB_URL)
        insp = inspect(engine)
    except Exception as exc:
        raise SystemExit(f"Failed to connect to database: {exc}") from exc

    os.makedirs(VAULT_DIR, exist_ok=True)

    tables = insp.get_table_names(schema="public")
    valid_tables = set(tables)

    # Build reverse FK index once — O(N) instead of O(N²)
    incoming_map: dict[str, list[tuple[str, list[str], list[str]]]] = {t: [] for t in tables}
    for other in tables:
        for fk in insp.get_foreign_keys(other):
            ref = fk["referred_table"]
            if ref in incoming_map:
                incoming_map[ref].append((other, fk["constrained_columns"], fk["referred_columns"]))

    index_entries: list[dict] = []

    for table in tables:
        columns  = insp.get_columns(table)
        pk_info  = insp.get_pk_constraint(table)
        fks      = insp.get_foreign_keys(table)
        db_indexes = insp.get_indexes(table)
        pk_cols  = set(pk_info.get("constrained_columns", []))
        fk_map   = {col: fk for fk in fks for col in fk["constrained_columns"]}
        incoming = incoming_map[table]

        is_junction = (
            len(fks) == 2 and
            len(columns) <= len(fks) + 1
        )

        try:
            row_count = get_row_count(table, valid_tables)
        except Exception as exc:
            logger.error("Could not count rows for %s: %s", table, exc)
            row_count = 0

        lines = []
        lines.append(f"# {table}")
        lines.append(f"\n> **Rows:** {row_count:,}")
        if is_junction:
            lines.append("> **Type:** Junction table (many-to-many)")
        lines.append("")

        lines.append("## Columns\n")
        lines.append("| column | type | nullable | key | note |")
        lines.append("|--------|------|----------|-----|------|")

        for col in columns:
            name     = col["name"]
            dtype    = str(col["type"])
            nullable = "✓" if col.get("nullable") else ""
            key      = ""
            note     = ""

            if name in pk_cols:
                key = "PK 🔑"
            if name in fk_map:
                fk    = fk_map[name]
                ref_t = fk["referred_table"]
                ref_c = fk["referred_columns"][0]
                rel   = detect_relation_type(set(fk["constrained_columns"]), pk_cols)
                key   = key + " FK 🔗" if key else "FK 🔗"
                note  = f"→ [[{ref_t}]].{ref_c} ({rel})"

            lines.append(f"| {name} | {dtype} | {nullable} | {key} | {note} |")

        if fks:
            lines.append("\n## Relations (outgoing)\n")
            for fk in fks:
                cols  = ", ".join(fk["constrained_columns"])
                ref_t = fk["referred_table"]
                ref_c = ", ".join(fk["referred_columns"])
                rel   = detect_relation_type(set(fk["constrained_columns"]), pk_cols)
                lines.append(f"- `{cols}` → [[{ref_t}]].`{ref_c}` — **{rel}**")

        if incoming:
            lines.append("\n## Relations (incoming)\n")
            for other_table, in_cols, in_ref_cols in incoming:
                c = ", ".join(in_cols)
                r = ", ".join(in_ref_cols)
                lines.append(f"- [[{other_table}]].`{c}` → `{r}` — **one-to-many**")

        if db_indexes:
            lines.append("\n## Indexes\n")
            lines.append("| name | columns | unique |")
            lines.append("|------|---------|--------|")
            for idx in db_indexes:
                idx_cols = ", ".join(idx["column_names"])
                unique   = "✓" if idx["unique"] else ""
                lines.append(f"| {idx['name']} | {idx_cols} | {unique} |")

        filepath = os.path.join(VAULT_DIR, f"{table}.md")
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("\n".join(lines) + "\n")
        except OSError as exc:
            logger.error("Could not write %s: %s", filepath, exc)
            continue

        logger.info("✅ %s.md (%s rows)", table, f"{row_count:,}")

        index_entries.append({
            "table":       table,
            "rows":        row_count,
            "is_junction": is_junction,
            "outgoing":    [fk["referred_table"] for fk in fks],
            "incoming":    [t for t, _, _ in incoming],
        })

    _write_index(index_entries)
    logger.info("\nDone — %d files → %s", len(tables), VAULT_DIR)


def _write_index(entries: list[dict]) -> None:
    from datetime import date
    lines = []
    lines.append("# Schema Index")
    lines.append(f"\n> Generated: {date.today()}\n")
    lines.append("| table | rows | type | connects to | referenced by |")
    lines.append("|-------|------|------|-------------|---------------|")
    for e in entries:
        table_type = "junction" if e["is_junction"] else ""
        outgoing   = ", ".join(f"[[{t}]]" for t in e["outgoing"]) or "—"
        incoming   = ", ".join(f"[[{t}]]" for t in e["incoming"]) or "—"
        lines.append(
            f"| [[{e['table']}]] | {e['rows']:,} | {table_type} | {outgoing} | {incoming} |"
        )
    filepath = os.path.join(VAULT_DIR, "_index.md")
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        logger.info("✅ _index.md written")
    except OSError as exc:
        logger.error("Could not write _index.md: %s", exc)


engine = None

if __name__ == "__main__":
    main()