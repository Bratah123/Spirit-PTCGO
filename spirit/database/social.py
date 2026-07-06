import logging
from spirit.database import db_session, Friendship, Account

def get_friends_by_account_id(account_id):
    """Fetches the friends list for an account."""
    try:
        with db_session() as session:
            results = (
                session.query(Friendship.friend_id, Friendship.status, Account.screen_name)
                .join(Account, Friendship.friend_id == Account.account_id)
                .filter(Friendship.account_id == account_id)
                .all()
            )
            return [
                {
                    "friend_id": r.friend_id,
                    "status": r.status,
                    "screen_name": r.screen_name
                }
                for r in results
            ]
    except Exception as e:
        logging.error(f"Error fetching friends for {account_id}: {e}")
        return []

def get_incoming_invites_by_account_id(account_id):
    """Fetches pending invitations for an account."""
    try:
        with db_session() as session:
            results = (
                session.query(Friendship.account_id.label('friend_id'), Friendship.status, Account.screen_name)
                .join(Account, Friendship.account_id == Account.account_id)
                .filter(Friendship.friend_id == account_id, Friendship.status == 0)
                .all()
            )
            return [
                {
                    "friend_id": r.friend_id,
                    "status": r.status,
                    "screen_name": r.screen_name
                }
                for r in results
            ]
    except Exception as e:
        logging.error(f"Error fetching incoming invites for {account_id}: {e}")
        return []

def add_friend_relationship(account_id, friend_id, status):
    """Adds or updates a friend relationship."""
    try:
        with db_session() as session:
            rel = session.query(Friendship).filter_by(account_id=account_id, friend_id=friend_id).first()
            if rel:
                rel.status = status
            else:
                new_rel = Friendship(
                    account_id=account_id,
                    friend_id=friend_id,
                    status=status
                )
                session.add(new_rel)
            return True
    except Exception as e:
        logging.error(f"Error adding/updating friend relationship between {account_id} and {friend_id}: {e}")
        return False

def remove_friend_relationship(account_id, friend_id):
    """Removes a friend relationship."""
    try:
        with db_session() as session:
            rel = session.query(Friendship).filter_by(account_id=account_id, friend_id=friend_id).first()
            if rel:
                session.delete(rel)
                return True
            return False
    except Exception as e:
        logging.error(f"Error removing friend relationship between {account_id} and {friend_id}: {e}")
        return False
