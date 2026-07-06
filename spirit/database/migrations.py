import logging
import sqlite3

from spirit.database.connection import DB_PATH

# {table: {column: sqlite column def}} — columns added to pre-existing DBs
_COLUMN_MIGRATIONS = {
    "accounts": {
        "is_admin": "BOOLEAN DEFAULT 0",
        "settings_json": "TEXT",
    },
}


def run_light_migrations():
    """Adds missing columns to existing tables (create_all only makes new tables)."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        for table, columns in _COLUMN_MIGRATIONS.items():
            cursor.execute(f"PRAGMA table_info({table});")
            existing = [row[1] for row in cursor.fetchall()]
            if not existing:
                continue
            for col, col_type in columns.items():
                if col not in existing:
                    logging.info(f"[DB] Adding missing column {table}.{col}")
                    cursor.execute(f"ALTER TABLE {table} ADD COLUMN {col} {col_type};")
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"[DB] Light migration failed: {e}")
