import copy

from typing import Dict, Any
from spirit.game.attributes import AttrID, CurrencyType
from spirit.database.player_data import get_wallet_by_account_id, update_wallet, get_decks_by_account_id, save_deck, delete_deck
from spirit.database.social import get_friends_by_account_id
from spirit.game.models.social import Friend, FriendsList, FriendListStatus

class Wallet:
    def __init__(self, account_id: str | None):
        self.account_id = account_id
        wallet_data = get_wallet_by_account_id(account_id)
        
        # Default fallback just in case DB fails
        coins = wallet_data.get('coins', 50000) if wallet_data else 50000
        gems = wallet_data.get('gems', 0) if wallet_data else 0
        tickets = wallet_data.get('tickets', 0) if wallet_data else 0

        self.balances: Dict[int, int] = {
            AttrID.TRAINER_TOKENS: coins,
            AttrID.REAL_CURRENCY: gems,
            AttrID.EVENT_TICKETS: tickets
        }

    def save(self):
        update_wallet(self.account_id, self.balances[AttrID.TRAINER_TOKENS], self.balances[AttrID.REAL_CURRENCY], self.balances[AttrID.EVENT_TICKETS])

    def serialize(self):
        currencies = []
        for name, value in self.balances.items():
            currencies.append({"name": name, "value": value})
        return {"currencies": currencies}

    def deduct_currency(self, currency_id: int, amount: int) -> bool:
        """Deducts currency from the wallet if funds are sufficient."""
        # Map internal enum names to match provided currency_id if needed
        # but AttrID matches are usually direct.
        current_balance = self.balances.get(currency_id, 0)
        if current_balance >= amount:
            self.balances[currency_id] -= amount
            self.save()
            return True
        return False

    def refresh_wallet(self):
        """Reloads wallet data from the database."""
        wallet_data = get_wallet_by_account_id(self.account_id)
        if wallet_data:
            self.balances[AttrID.TRAINER_TOKENS] = wallet_data.get('coins', 0)
            self.balances[AttrID.REAL_CURRENCY] = wallet_data.get('gems', 0)
            self.balances[AttrID.EVENT_TICKETS] = wallet_data.get('tickets', 0)

class Player:
    def __init__(self, account_data: Dict[str, Any]):
        self.account_id = account_data.get("account_id")
        self.username = account_data.get("username")
        self.screen_name = account_data.get("screen_name")
        
        # Load from Database
        self.wallet = Wallet(self.account_id)
        self.decks = get_decks_by_account_id(self.account_id, is_avatar=False)
        self.avatar_decks = get_decks_by_account_id(self.account_id, is_avatar=True)
        
        # Load Friends
        self.friends_list = FriendsList(self.account_id)
        self._load_friends()

    def _load_friends(self):
        friends_data = get_friends_by_account_id(self.account_id)
        for entry in friends_data:
            friend = Friend(
                account_id=entry['friend_id'],
                display_name=entry['screen_name'],
                status=FriendListStatus(entry['status']),
                presence="Offline" # Initial state
            )
            self.friends_list.add_friend(friend)

    def get_wallet_data(self):
        return self.wallet.serialize()

    def _inject_validation_attributes(self, deck_dict: Dict[str, Any], is_avatar: bool = False) -> Dict[str, Any]:
        """Overwrites deck attr 10860 (VALID_FORMATS) with the freshly computed format names."""
        from spirit.game import rules

        deck_copy = copy.deepcopy(deck_dict)
        attributes = deck_copy.setdefault("attributes", [])

        if is_avatar:
            names = ["Modified", "Expanded", "Unlimited", "Legacy"]
        else:
            names = rules.valid_format_names(deck_copy)

        # Recompute every time — formats.json may have changed since the deck was saved
        attributes[:] = [a for a in attributes if a.get("name") != AttrID.VALID_FORMATS.value]
        attributes.append({
            "name": AttrID.VALID_FORMATS.value,
            "value": names
        })

        return deck_copy

    def get_decks_data(self):
        # We assume deck_data in the DB contains the fully serialized SerializableDeck
        serialized_decks = [self._inject_validation_attributes(deck["deck_data"]) for deck in self.decks]
        return {"decks": serialized_decks}

    def get_avatar_decks_data(self):
        serialized_avatar_decks = [self._inject_validation_attributes(deck["deck_data"], is_avatar=True) for deck in self.avatar_decks]
        return {"decks": serialized_avatar_decks}

    def get_friends_roster_data(self):
        return {"roster": self.friends_list.serialize()}

    def save_deck_data(self, deck_dict: dict, is_avatar: bool = False):
        """Persists deck data and updates local state."""
        deck_id = deck_dict.get("deckID")
        deck_name = deck_dict.get("deckName", "")
        
        # Save to DB
        save_deck(self.account_id, deck_id, deck_name, deck_dict, is_avatar=is_avatar)
        
        # Update local list for immediate reflection
        target_list = self.avatar_decks if is_avatar else self.decks
        
        # Remove existing if it's an update
        target_list[:] = [d for d in target_list if d.get("id") != deck_id]
        
        # Add new/updated
        target_list.append({
            "id": deck_id,
            "account_id": self.account_id,
            "name": deck_name,
            "deck_data": deck_dict,
            "is_avatar": 1 if is_avatar else 0
        })

    def delete_deck_data(self, deck_id: str, is_avatar: bool = False):
        """Deletes deck data from DB and updates local state."""
        # Delete from DB
        delete_deck(self.account_id, deck_id)
        
        # Update local list for immediate reflection
        target_list = self.avatar_decks if is_avatar else self.decks
        target_list[:] = [d for d in target_list if d.get("id") != deck_id]

