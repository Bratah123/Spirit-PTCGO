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

# Performance indexes for hot-path filters. create_all() only adds indexes to
# NEW tables, so a DB created before these were declared keeps the un-indexed
# tables — these statements backfill them (idempotent).
_INDEX_MIGRATIONS = [
    "CREATE INDEX IF NOT EXISTS ix_decks_account_id ON decks (account_id)",
    "CREATE INDEX IF NOT EXISTS ix_friends_friend_id ON friends (friend_id)",
    "CREATE INDEX IF NOT EXISTS ix_trade_offers_sender_id ON trade_offers (sender_id)",
    "CREATE INDEX IF NOT EXISTS ix_trade_offers_recipient_id ON trade_offers (recipient_id)",
    "CREATE INDEX IF NOT EXISTS ix_trade_offers_status_created ON trade_offers (status, created_at)",
    "CREATE INDEX IF NOT EXISTS ix_trade_offers_status_recipient ON trade_offers (status, recipient_id)",
    "CREATE INDEX IF NOT EXISTS ix_trade_offers_status_sender ON trade_offers (status, sender_id)",
    "CREATE INDEX IF NOT EXISTS ix_tournament_entries_tournament_id ON tournament_entries (tournament_id)",
    "CREATE INDEX IF NOT EXISTS ix_tournament_entries_account_id ON tournament_entries (account_id)",
]


def run_light_migrations():
    """Adds missing columns and performance indexes to existing tables
    (create_all only builds brand-new tables/indexes)."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = {row[0] for row in cursor.fetchall()}
        for table, columns in _COLUMN_MIGRATIONS.items():
            cursor.execute(f"PRAGMA table_info({table});")
            existing = [row[1] for row in cursor.fetchall()]
            if not existing:
                continue
            for col, col_type in columns.items():
                if col not in existing:
                    logging.info(f"[DB] Adding missing column {table}.{col}")
                    cursor.execute(f"ALTER TABLE {table} ADD COLUMN {col} {col_type};")
        for stmt in _INDEX_MIGRATIONS:
            table = stmt.split(" ON ")[1].split(" ")[0]
            if table in tables:
                cursor.execute(stmt)
        conn.commit()
        conn.close()
    except Exception as e:
        logging.error(f"[DB] Light migration failed: {e}")
