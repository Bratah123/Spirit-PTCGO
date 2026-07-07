import json
import os
import logging
from spirit.database import db_session, Account, Wallet, Deck, Collection, ArchetypeFlag
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.scripts.products import loader as product_loader

# Resources granted to a brand-new account
STARTING_COINS = 1000
STARTING_GEMS = 0
STARTING_TICKETS = 100

# Coins awarded when a match completes (winner / loser rates)
COINS_PER_WIN = 1000
COINS_PER_LOSS = 200


def get_account_settings(account_id):
    """The account's persisted client settings dict {settingNumber(str): value} (attr 10230)."""
    try:
        with db_session() as session:
            account = session.query(Account).filter_by(account_id=account_id).first()
            return dict(account.settings_json or {}) if account else {}
    except Exception as e:
        logging.error(f"Error reading account settings for {account_id}: {e}")
        return {}


def get_screen_name(account_id):
    """The account's display name (screen_name, falling back to username)."""
    try:
        with db_session() as session:
            account = session.query(Account).filter_by(account_id=account_id).first()
            return (account.screen_name or account.username) if account else ""
    except Exception as e:
        logging.error(f"Error reading screen name for {account_id}: {e}")
        return ""


def merge_account_settings(account_id, new_settings):
    """Merges incoming {settingNumber: value} into the stored settings and persists."""
    try:
        with db_session() as session:
            account = session.query(Account).filter_by(account_id=account_id).first()
            if not account:
                return {}
            merged = dict(account.settings_json or {})
            for key, value in (new_settings or {}).items():
                merged[str(key)] = int(value)
            account.settings_json = merged  # reassign so JSONEncodedDict registers the change
            return merged
    except Exception as e:
        logging.error(f"Error merging account settings for {account_id}: {e}")
        return {}

def _wallet_to_dict(w):
    return {
        "account_id": w.account_id,
        "coins": w.coins,
        "gems": w.gems,
        "tickets": w.tickets
    }

def _deck_to_dict(d):
    return {
        "id": d.id,
        "account_id": d.account_id,
        "name": d.name,
        "deck_data": d.deck_data,
        "is_avatar": 1 if d.is_avatar else 0,
        "overall_wins": d.overall_wins,
        "overall_played": d.overall_played,
        "wins_since_last_edit": d.wins_since_last_edit,
        "played_since_last_edit": d.played_since_last_edit
    }

def _collection_to_dict(c):
    return {
        "account_id": c.account_id,
        "archetype_id": c.archetype_id,
        "tradable_count": c.tradable_count,
        "nontradable_count": c.nontradable_count
    }

def get_wallet_by_account_id(account_id):
    """Fetches the wallet for an account, or creates a default one if it doesn't exist."""
    try:
        with db_session() as session:
            w = session.query(Wallet).filter_by(account_id=account_id).first()
            if w:
                return _wallet_to_dict(w)
            else:
                # Create a default wallet
                new_w = Wallet(
                    account_id=account_id,
                    coins=STARTING_COINS,
                    gems=STARTING_GEMS,
                    tickets=STARTING_TICKETS
                )
                session.add(new_w)
                session.flush()
                return _wallet_to_dict(new_w)
    except Exception as e:
        logging.error(f"Error getting/creating wallet for {account_id}: {e}")
        return None

def update_wallet(account_id, coins, gems, tickets):
    """Updates an account's wallet."""
    try:
        with db_session() as session:
            w = session.query(Wallet).filter_by(account_id=account_id).first()
            if w:
                w.coins = coins
                w.gems = gems
                w.tickets = tickets
                return True
            else:
                new_w = Wallet(
                    account_id=account_id,
                    coins=coins,
                    gems=gems,
                    tickets=tickets
                )
                session.add(new_w)
                return True
    except Exception as e:
        logging.error(f"Error updating wallet for {account_id}: {e}")
        return False

def grant_coins(account_id, amount):
    """Adds coins to an account's wallet; returns the new balance or None."""
    try:
        with db_session() as session:
            w = session.query(Wallet).filter_by(account_id=account_id).first()
            if not w:
                w = Wallet(
                    account_id=account_id,
                    coins=STARTING_COINS,
                    gems=STARTING_GEMS,
                    tickets=STARTING_TICKETS
                )
                session.add(w)
            w.coins = (w.coins or 0) + amount
            session.flush()
            return w.coins
    except Exception as e:
        logging.error(f"Error granting {amount} coins to {account_id}: {e}")
        return None

def get_decks_by_account_id(account_id, is_avatar=False):
    """Fetches decks for an account."""
    try:
        with db_session() as session:
            rows = session.query(Deck).filter_by(account_id=account_id, is_avatar=is_avatar).all()
            return [_deck_to_dict(r) for r in rows]
    except Exception as e:
        logging.error(f"Error fetching decks for {account_id}: {e}")
        return []

def save_deck(account_id, deck_id, name, deck_data, is_avatar=False):
    """Saves or updates a deck for an account."""
    try:
        with db_session() as session:
            d = session.query(Deck).filter_by(id=deck_id).first()
            if d:
                d.account_id = account_id
                d.name = name
                d.deck_data = deck_data
                d.is_avatar = is_avatar
            else:
                new_d = Deck(
                    id=deck_id,
                    account_id=account_id,
                    name=name,
                    deck_data=deck_data,
                    is_avatar=is_avatar
                )
                session.add(new_d)
            return True
    except Exception as e:
        logging.error(f"Error saving deck {deck_id} for {account_id}: {e}")
        return False

def delete_deck(account_id, deck_id):
    """Deletes a deck for an account."""
    try:
        with db_session() as session:
            d = session.query(Deck).filter_by(id=deck_id, account_id=account_id).first()
            if d:
                session.delete(d)
                return True
            return False
    except Exception as e:
        logging.error(f"Error deleting deck {deck_id} for {account_id}: {e}")
        return False

_JSON_CACHE = {}

def _get_json_data(filename):
    """Helper to load and cache JSON data from the json_data folder."""
    if filename not in _JSON_CACHE:
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'json_data', f'{filename}.json'))
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    _JSON_CACHE[filename] = json.load(f)
                logging.info(f"[DB] Cached {len(_JSON_CACHE[filename])} entries from {filename}.json")
            except Exception as e:
                logging.error(f"[DB] Failed to load {filename}.json: {e}")
                _JSON_CACHE[filename] = []
        else:
            logging.warning(f"[DB] {filename}.json not found at {path}")
            _JSON_CACHE[filename] = []
    return _JSON_CACHE[filename]

def get_collection_by_account_id(account_id):
    """Fetches the collection for an account."""
    try:
        with db_session() as session:
            rows = session.query(Collection).filter_by(account_id=account_id).all()
            return [_collection_to_dict(r) for r in rows]
    except Exception as e:
        logging.error(f"Error fetching collection for {account_id}: {e}")
        return []

_FREE_ENERGY_GUIDS = None

def _free_energy_guids():
    """GUIDs of the basic-energy 'Free_Energy' cards, which every player owns unlimited copies of."""
    global _FREE_ENERGY_GUIDS
    if _FREE_ENERGY_GUIDS:
        return _FREE_ENERGY_GUIDS
    try:
        cards_data = card_loader.load_all()
    except Exception as e:
        logging.error(f"[DB] Failed to load card scripts for free-energy list: {e}")
        return set()
    _FREE_ENERGY_GUIDS = {card.guid.lower() for card in cards_data if card.key == "Free_Energy"}
    return _FREE_ENERGY_GUIDS


def get_merged_collection_payload(account_id):
    """The player's owned collection. Only DB-owned items plus unlimited basic energy."""
    cl = []
    seen_guids = set()

    # 1. Items the account actually owns in the database
    for item in get_collection_by_account_id(account_id):
        guid = item["archetype_id"].lower()
        if guid in seen_guids:
            continue
        seen_guids.add(guid)
        cl.append({
            "archetypeID": guid,
            "tradable": int(item["tradable_count"]),
            "nontradable": int(item["nontradable_count"])
        })

    # 2. Basic energy is free/unlimited for everyone (matches live PTCGO)
    for guid in _free_energy_guids():
        if guid in seen_guids:
            continue
        seen_guids.add(guid)
        cl.append({
            "archetypeID": guid,
            "tradable": 99,
            "nontradable": 0
        })

    return cl

def grant_all_cards(account_id, count=4, is_tradable=True):
    """Debug: ensure the account owns `count` copies of every non-basic card in one transaction."""
    try:
        cards = card_loader.load_all()
    except Exception as e:
        logging.error(f"[DB] grant_all_cards: failed to load cards: {e}")
        return 0
    granted = 0
    try:
        with db_session() as session:
            existing = {c.archetype_id: c for c in
                        session.query(Collection).filter_by(account_id=account_id).all()}
            for card in cards:
                if card.key == "Free_Energy":  # basic energy is already unlimited/free
                    continue
                row = existing.get(card.guid)
                if row is None:
                    row = Collection(account_id=account_id, archetype_id=card.guid,
                                     tradable_count=0, nontradable_count=0)
                    session.add(row)
                    existing[card.guid] = row
                if is_tradable:
                    row.tradable_count = max(row.tradable_count, count)
                else:
                    row.nontradable_count = max(row.nontradable_count, count)
                granted += 1
    except Exception as e:
        logging.error(f"[DB] grant_all_cards failed for {account_id}: {e}")
        return 0
    logging.info(f"[DB] grant_all_cards: gave {count}x of {granted} cards to {account_id}")
    return granted

def add_to_collection(account_id, archetype_id, count=1, is_tradable=False):
    """Adds an item to the account's collection."""
    logging.info(f"[DB] Adding {count}x {archetype_id} (tradable={is_tradable}) to account {account_id}")
    try:
        with db_session() as session:
            item = session.query(Collection).filter_by(account_id=account_id, archetype_id=archetype_id).first()
            if item:
                if is_tradable:
                    item.tradable_count += count
                else:
                    item.nontradable_count += count
            else:
                new_item = Collection(
                    account_id=account_id,
                    archetype_id=archetype_id,
                    tradable_count=count if is_tradable else 0,
                    nontradable_count=0 if is_tradable else count
                )
                session.add(new_item)
            return True
    except Exception as e:
        logging.error(f"Error adding to collection for {account_id}: {e}")
        return False

def remove_from_collection(account_id, archetype_id, count=1, is_tradable=False):
    """Removes an item from the account's collection."""
    logging.info(f"[DB] Removing {count}x {archetype_id} (tradable={is_tradable}) from account {account_id}")
    try:
        with db_session() as session:
            item = session.query(Collection).filter_by(account_id=account_id, archetype_id=archetype_id).first()
            if item:
                logging.info(f"[DB] Found item in collection. Before: tradable={item.tradable_count}, nontradable={item.nontradable_count}")
                if is_tradable:
                    item.tradable_count = max(0, item.tradable_count - count)
                else:
                    item.nontradable_count = max(0, item.nontradable_count - count)
                logging.info(f"[DB] After: tradable={item.tradable_count}, nontradable={item.nontradable_count}")
                return True
            else:
                # If they didn't have a row, they were using the virtual "default seeded" copy (which gives 1x tradable / 0x nontradable).
                # To consume it and prevent it from virtually reappearing, we must create a row with 0 copies!
                logging.info(f"[DB] Item not found in DB. Creating a row with 0 copies to override virtual seeding.")
                new_item = Collection(
                    account_id=account_id,
                    archetype_id=archetype_id,
                    tradable_count=0,
                    nontradable_count=0
                )
                session.add(new_item)
                return True
    except Exception as e:
        logging.error(f"Error removing from collection for {account_id}: {e}")
        return False

def set_archetype_flag(account_id, archetype_id, wanted=None, for_trade=None, review=None):
    """Sets a flag (wanted, for_trade, review) for a given archetype and account."""
    archetype_id = str(archetype_id).lower()
    try:
        with db_session() as session:
            flag = session.query(ArchetypeFlag).filter_by(account_id=account_id, archetype_id=archetype_id).first()
            if not flag:
                flag = ArchetypeFlag(
                    account_id=account_id,
                    archetype_id=archetype_id,
                    wanted=0,
                    for_trade=0,
                    review=0
                )
                session.add(flag)
            
            if wanted is not None:
                flag.wanted = int(wanted)
            if for_trade is not None:
                flag.for_trade = int(for_trade)
            if review is not None:
                flag.review = int(review)
            
            # If all flags are 0, we delete the row to keep the DB clean
            if flag.wanted == 0 and flag.for_trade == 0 and flag.review == 0:
                session.delete(flag)
                
            return True
    except Exception as e:
        logging.error(f"Error setting archetype flag for {account_id}, {archetype_id}: {e}")
        return False

def get_archetype_flags(account_id):
    """Fetches all archetype flags for a given account."""
    try:
        with db_session() as session:
            flags = session.query(ArchetypeFlag).filter_by(account_id=account_id).all()
            return [
                {
                    "archetypeID": f.archetype_id,
                    "wanted": f.wanted,
                    "forTrade": f.for_trade,
                    "review": f.review
                }
                for f in flags
            ]
    except Exception as e:
        logging.error(f"Error getting archetype flags for {account_id}: {e}")
        return []
