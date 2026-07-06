from enum import IntEnum
from typing import List, Dict, Any

class FriendListStatus(IntEnum):
    Invited = 0
    Removed = 1
    Blocking = 2
    Blocked = 3
    Friends = 4
    NoRelationship = 5

class Friend:
    def __init__(self, account_id: str, display_name: str, status: FriendListStatus, presence: str = "Offline"):
        self.account_id = account_id
        self.display_name = display_name
        self.status = status
        self.presence = presence

    def serialize(self) -> Dict[str, Any]:
        return {
            "accountID": self.account_id,
            "displayName": self.display_name,
            "status": self.status.value,
            "presence": self.presence
        }

class FriendsList:
    def __init__(self, account_id: str | None):
        self.account_id = account_id
        self.friends: Dict[str, Friend] = {}

    def add_friend(self, friend: Friend):
        self.friends[friend.account_id] = friend

    def remove_friend(self, account_id: str):
        if account_id in self.friends:
            del self.friends[account_id]

    def get_friend(self, account_id: str) -> Friend | None:
        return self.friends.get(account_id)

    def serialize(self) -> List[Dict[str, Any]]:
        return [friend.serialize() for friend in self.friends.values()]
