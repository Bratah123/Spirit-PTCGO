import os
import sys
import uuid
import hashlib
import sqlite3

# Ensure Python can find the 'spirit' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from spirit.database import Base, engine, db_session, Account
from spirit.database.connection import DB_PATH

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def setup_database():
    print("Initializing Database Tables via SQLAlchemy...")
    Base.metadata.create_all(engine)
    print(" - All tables ensured.")

    db_path = DB_PATH
    if os.path.exists(db_path):
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Query columns of 'decks' table
            cursor.execute("PRAGMA table_info(decks);")
            columns = [row[1] for row in cursor.fetchall()]
            
            # New columns in Deck model
            required_cols = {
                "overall_wins": "INTEGER DEFAULT 0",
                "overall_played": "INTEGER DEFAULT 0",
                "wins_since_last_edit": "INTEGER DEFAULT 0",
                "played_since_last_edit": "INTEGER DEFAULT 0"
            }
            
            for col, col_type in required_cols.items():
                if col not in columns:
                    print(f" - Altering table 'decks' to add missing column '{col}'...")
                    cursor.execute(f"ALTER TABLE decks ADD COLUMN {col} {col_type};")

            cursor.execute("PRAGMA table_info(accounts);")
            account_columns = [row[1] for row in cursor.fetchall()]
            if "is_admin" not in account_columns:
                print(" - Altering table 'accounts' to add missing column 'is_admin'...")
                cursor.execute("ALTER TABLE accounts ADD COLUMN is_admin BOOLEAN DEFAULT 0;")

            conn.commit()
            conn.close()
            print(" - Database schema migrations checked and applied successfully.")
        except Exception as e:
            print(f" - Warning: Auto-migration of decks table failed: {e}")

    # Insert test user 'brandon'
    test_username = "brandon"
    test_password = "password" # Simple default password for testing
    
    new_account_id = None
    with db_session() as session:
        acc = session.query(Account).filter_by(username=test_username).first()
        if not acc:
            acc_id = str(uuid.uuid4())
            pwd_hash = hash_password(test_password)
            new_acc = Account(
                account_id=acc_id,
                username=test_username,
                password_hash=pwd_hash,
                screen_name=test_username,
                is_admin=True
            )
            session.add(new_acc)
            new_account_id = acc_id
            print(f" - Seeded test account: '{test_username}' with password '{test_password}' (admin).")
        else:
            print(f" - Test account '{test_username}' already exists.")

    if new_account_id:
        try:
            from spirit.game.starter_content import grant_starter_content
            grant_starter_content(new_account_id)
            print(" - Granted starter decks and booster packs to seeded account.")
        except Exception as e:
            print(f" - Warning: Failed to grant starter content: {e}")

    print("Database setup complete!")

if __name__ == '__main__':
    setup_database()
