import logging
import uuid
import hashlib
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError
from spirit.database import db_session, Account
from spirit.game.starter_content import grant_starter_content

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def _account_to_dict(acc):
    if not acc:
        return None
    return {
        "id": acc.id,
        "account_id": acc.account_id,
        "username": acc.username,
        "password_hash": acc.password_hash,
        "screen_name": acc.screen_name,
        "created_at": acc.created_at
    }

def get_account_by_username(username):
    """Fetches an account from the database by username."""
    try:
        with db_session() as session:
            acc = session.query(Account).filter(func.lower(Account.username) == username.lower()).first()
            return _account_to_dict(acc)
    except Exception as e:
        logging.error(f"Error fetching account by username {username}: {e}")
        return None

def get_account_by_id(account_id):
    """Fetches an account from the database by account_id."""
    try:
        with db_session() as session:
            acc = session.query(Account).filter_by(account_id=account_id).first()
            return _account_to_dict(acc)
    except Exception as e:
        logging.error(f"Error fetching account by ID {account_id}: {e}")
        return None

def create_account(username, password):
    """Creates a new account (used for auto-registration)."""
    try:
        with db_session() as session:
            acc_id = str(uuid.uuid4())
            pwd_hash = hash_password(password)

            new_acc = Account(
                account_id=acc_id,
                username=username,
                password_hash=pwd_hash,
                screen_name=username
            )
            session.add(new_acc)
            session.flush()  # Populates id and created_at
            acc_dict = _account_to_dict(new_acc)
    except IntegrityError:
        # Username already exists
        return None
    except Exception as e:
        logging.error(f"Error creating account: {e}")
        return None

    # Grant starter decks/packs outside the session (grant opens its own sessions)
    try:
        grant_starter_content(acc_dict["account_id"])
    except Exception as e:
        logging.error(f"Error granting starter content to new account {username}: {e}")

    return acc_dict

def verify_password(stored_hash, provided_password):
    """Verifies a given password against the stored hash."""
    return stored_hash == hash_password(provided_password)
