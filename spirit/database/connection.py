import os
import sqlite3
import logging
from contextlib import contextmanager
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool

# Default DB path
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'ptcgo_server.db'))

def creator():
    # check_same_thread=False: connections are used from HTTP handler threads + the async loop
    return sqlite3.connect(DB_PATH, timeout=30.0, check_same_thread=False)

# NullPool opens/closes a connection per session so it is always closed in the thread
# that used it — avoids SQLite's cross-thread close error under the threaded HTTP server.
engine = create_engine(
    "sqlite://",
    creator=creator,
    poolclass=NullPool
)

# Listen for connection events to set WAL journal mode (matching db_manager.py exactly)
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    try:
        cursor.execute("PRAGMA journal_mode=WAL;")
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
