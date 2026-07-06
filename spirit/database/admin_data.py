import logging
import os

from sqlalchemy import func

from spirit.database import db_session, Account
from spirit.database.accounts import hash_password


def any_admin_exists() -> bool:
    with db_session() as session:
        return session.query(Account).filter_by(is_admin=True).first() is not None


def set_admin(account_id: str, is_admin: bool) -> bool:
    with db_session() as session:
        acc = session.query(Account).filter_by(account_id=account_id).first()
        if not acc:
            return False
        acc.is_admin = bool(is_admin)
        return True


def verify_admin_login(username: str, password: str):
    """Returns {account_id, username} on success, else None.

    Bootstrap: while NO admin exists yet, the first valid account login is
    auto-promoted to admin (and loudly logged)."""
    with db_session() as session:
        acc = session.query(Account).filter(
            func.lower(Account.username) == (username or "").lower()).first()
        if not acc or acc.password_hash != hash_password(password or ""):
            return None
        if not acc.is_admin:
            has_admin = session.query(Account).filter_by(is_admin=True).first() is not None
            if has_admin:
                return None
            acc.is_admin = True
            logging.warning(f"[Admin] No admin existed — '{username}' auto-promoted to admin on first login.")
        return {"account_id": acc.account_id, "username": acc.username}


def bootstrap_admins_from_env():
    """Promotes accounts named in SPIRIT_ADMIN_USERS (comma-separated) at startup."""
    raw = os.environ.get("SPIRIT_ADMIN_USERS", "").strip()
    if not raw:
        return
    names = [n.strip() for n in raw.split(",") if n.strip()]
    if not names:
        return
    with db_session() as session:
        for name in names:
            acc = session.query(Account).filter_by(username=name).first()
            if acc and not acc.is_admin:
                acc.is_admin = True
                logging.info(f"[Admin] Promoted '{name}' to admin (SPIRIT_ADMIN_USERS).")
            elif not acc:
                logging.warning(f"[Admin] SPIRIT_ADMIN_USERS names unknown account '{name}'.")
