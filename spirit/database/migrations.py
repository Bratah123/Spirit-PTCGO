import logging
from sqlalchemy import inspect

from spirit.database.connection import engine

# {table: {column: sqlite column def}} — columns added to pre-existing DBs
_COLUMN_MIGRATIONS = {
    "decks": {
        "overall_wins": "INTEGER DEFAULT 0",
        "overall_played": "INTEGER DEFAULT 0",
        "wins_since_last_edit": "INTEGER DEFAULT 0",
        "played_since_last_edit": "INTEGER DEFAULT 0",
    },
    "accounts": {
        "is_admin": "BOOLEAN DEFAULT 0",
        "settings_json": "TEXT",
    },
    "daily_login_progress": {
        "activations": "INTEGER DEFAULT 0",
    },
}

# Performance indexes for hot-path filters. create_all() only adds indexes to
# NEW tables, so a DB created before these were declared keeps the un-indexed
# tables — these statements backfill them (idempotent).
_INDEX_MIGRATIONS = [
    ("decks", "ix_decks_account_id", "account_id"),
    ("friends", "ix_friends_friend_id", "friend_id"),
    ("trade_offers", "ix_trade_offers_sender_id", "sender_id"),
    ("trade_offers", "ix_trade_offers_recipient_id", "recipient_id"),
    ("trade_offers", "ix_trade_offers_status_created", "status, created_at"),
    ("trade_offers", "ix_trade_offers_status_recipient", "status, recipient_id"),
    ("trade_offers", "ix_trade_offers_status_sender", "status, sender_id"),
    ("tournament_entries", "ix_tournament_entries_tournament_id", "tournament_id"),
    ("tournament_entries", "ix_tournament_entries_account_id", "account_id"),
]


def run_light_migrations():
    """Adds missing columns and performance indexes to existing tables
    (create_all only builds brand-new tables/indexes)."""
    try:
        with engine.begin() as conn:
            inspector = inspect(conn)
            tables = set(inspector.get_table_names())
            for table, columns in _COLUMN_MIGRATIONS.items():
                if table not in tables:
                    continue
                existing = {col["name"] for col in inspector.get_columns(table)}
                for col, col_type in columns.items():
                    if col not in existing:
                        logging.info("[DB] Adding missing column %s.%s", table, col)
                        conn.exec_driver_sql(f"ALTER TABLE {table} ADD COLUMN {col} {col_type}")
            for table, name, columns in _INDEX_MIGRATIONS:
                if table in tables and name not in {index["name"] for index in inspector.get_indexes(table)}:
                    conn.exec_driver_sql(f"CREATE INDEX {name} ON {table} ({columns})")
    except Exception as e:
        logging.error(f"[DB] Light migration failed: {e}")
        raise
