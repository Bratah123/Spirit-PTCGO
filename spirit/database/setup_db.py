import os
import sys
import uuid
import hashlib

# Ensure Python can find the 'spirit' module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from spirit.database import Base, engine, db_session, Account
from spirit import config
from spirit.database.migrations import run_light_migrations
from spirit.game.content.starter import grant_starter_content

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def setup_database():
    print("Initializing Database Tables via SQLAlchemy...")
    Base.metadata.create_all(engine)
    print(" - All tables ensured.")

    run_light_migrations()
    print(" - Database schema migrations checked and applied successfully.")

    if config.DATABASE_URL:
        print("Database setup complete. No development account seeded on MySQL/MariaDB.")
        return

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
            grant_starter_content(new_account_id)
            print(" - Granted starter decks and booster packs to seeded account.")
        except Exception as e:
            print(f" - Warning: Failed to grant starter content: {e}")

    print("Database setup complete!")

if __name__ == '__main__':
    setup_database()
