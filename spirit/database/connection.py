import os
import sqlite3
import logging
from contextlib import contextmanager
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import QueuePool

# Default DB path
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'ptcgo_server.db'))

# Pool sizing: covers asyncio.to_thread's executor (min(32, cpu+4)) plus the
# threaded HTTP handlers (admin API, CAS ticket, account creation) that open
# their own sessions. Env-overridable for constrained hosts.
_POOL_SIZE = int(os.environ.get("SPIRIT_DB_POOL_SIZE", "20"))
_POOL_OVERFLOW = int(os.environ.get("SPIRIT_DB_POOL_OVERFLOW", "80"))

def creator():
    # check_same_thread=False: connections are used from HTTP handler threads + the async loop.
    # timeout=30 installs a 30s busy handler so concurrent writers wait on the WAL
    # write lock instead of raising SQLITE_BUSY.
    return sqlite3.connect(DB_PATH, timeout=30.0, check_same_thread=False)

# A bounded QueuePool reuses connections instead of NullPool's connect+close per
# session (measured ~360x cheaper per read: the WAL pragma + connect churn moves
# from every op to pool-fill time). scoped_session opens AND closes each session in
# the same thread, so no connection is ever closed cross-thread — the reason NullPool
# was originally chosen is preserved. reset_on_return rolls back any dangling txn.
engine = create_engine(
    "sqlite://",
    creator=creator,
    poolclass=QueuePool,
    pool_size=_POOL_SIZE,
    max_overflow=_POOL_OVERFLOW,
    pool_timeout=30,
    pool_recycle=-1,
)

# Runs once per pooled connection (at fill time, not per op). synchronous=NORMAL is
# safe under WAL (a crash can lose only the last commit, never corrupt) and removes
# the per-commit fsync that dominated login/match-end write latency.
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("PRAGMA journal_mode=WAL;")
        cursor.execute("PRAGMA synchronous=NORMAL;")
        cursor.execute("PRAGMA busy_timeout=30000;")
        cursor.execute("PRAGMA cache_size=-16000;")   # ~16 MB page cache per connection
        cursor.execute("PRAGMA temp_store=MEMORY;")
    except Exception as e:
        logging.error(f"[DB] Error setting sqlite pragmas: {e}")
    finally:
        cursor.close()

# Thread-safe session factory
session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Session = scoped_session(session_factory)

@contextmanager
def db_session():
    """Context manager for thread-safe session lifecycle management.
    
    If the block succeeds, changes are committed automatically.
    If an exception occurs, the transaction is rolled back.
    Finally, the session is closed and released.
    """
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        logging.error(f"[DB] Session rollback due to exception: {e}")
        raise
    finally:
        Session.remove()
