import logging
import uuid

from spirit.game.attributes import AttrID, ProductType
from spirit.game.set_utils import eligible_booster_sets
from spirit.game.scripts.cards import loader as card_loader
from spirit.game.scripts.products import loader as product_loader
from spirit.database.player_data import (
    save_deck, add_to_collection, update_wallet,
    STARTING_COINS, STARTING_GEMS, STARTING_TICKETS,
)

STARTER_BOOSTER_PACK_COUNT = 10

# Default cosmetics granted to every new account (basic coin/sleeve/deck box)
STARTER_COIN_GUID = "B9A4EA96-949E-11E1-890F-EFB676C7909C"
STARTER_SLEEVE_GUID = "e079c0d3-b934-4fbd-b021-545106c75693"
STARTER_DECK_BOX_GUID = "e129b0d3-b934-4fbd-b021-545106c75694"
STARTER_COSMETICS = [STARTER_COIN_GUID, STARTER_SLEEVE_GUID, STARTER_DECK_BOX_GUID]

# PTCG-Live set codes (used by exported decklists) -> local card-script set codes
SET_CODE_MAP = {
    "SSH": "SWSH1",
    "RCL": "SWSH2",
    "DAA": "SWSH3",
    "CPA": "SWSH35",
    "VIV": "SWSH4",
    "SHF": "SWSH45",
    "BST": "SWSH5",
    "CRE": "SWSH6",
    "EVS": "SWSH7",
    "FST": "SWSH8",
    "BRS": "SWSH9",
    "ASR": "SWSH10",
    "LOR": "SWSH11",
    "SIT": "SWSH12",
    "CEL": "CEL25",
    "PGO": "PGO",
}

# (count, live set code, collector number)
LUGIA_VSTAR_DECKLIST = [
    (1, "FST", 207),   # Dunsparce
    (3, "SIT", 186),   # Lugia V
    (1, "SSH", 148),   # Oranguru
    (1, "LOR", 143),   # Snorlax
    (1, "BST", 117),   # Stoutland V
    (4, "SIT", 147),   # Archeops
    (2, "SIT", 139),   # Lugia VSTAR
    (1, "SHF", 46),    # Yveltal
    (1, "PGO", 11),    # Radiant Charizard
    (1, "VIV", 50),    # Raikou
    (1, "EVS", 76),    # Pumpkaboo
    (2, "BRS", 40),    # Lumineon V
    (1, "BRS", 41),    # Manaphy
    (3, "CEL", 24),    # Professor's Research
    (2, "SSH", 200),   # Marnie
    (2, "RCL", 189),   # Boss's Orders
    (1, "SIT", 193),   # Serena
    (1, "ASR", 186),   # Irida
    (4, "SSH", 216),   # Quick Ball
    (4, "SSH", 163),   # Evolution Incense
    (1, "LOR", 162),   # Lost Vacuum
    (1, "BRS", 135),   # Choice Belt
    (1, "BST", 125),   # Escape Rope
    (4, "BRS", 186),   # Ultra Ball
    (4, "DAA", 176),   # Powerful Colorless Energy
    (4, "SSH", 186),   # Aurora Energy
    (3, "RCL", 171),   # Capture Energy
    (2, "BRS", 151),   # Double Turbo Energy
    (1, "DAA", 174),   # Heat Fire Energy
    (1, "RCL", 173),   # Speed Lightning Energy
    (1, "SIT", 169),   # V Guard Energy
]

MEW_VMAX_DECKLIST = [
    (1, "FST", 42),    # Oricorio
    (4, "FST", 185),   # Genesect V
    (4, "FST", 251),   # Mew V
    (3, "FST", 114),   # Mew VMAX
    (3, "FST", 235),   # Judge
    (2, "RCL", 189),   # Boss's Orders
    (1, "ASR", 188),   # Roxanne
    (1, "ASR", 183),   # Cyllene
    (4, "BRS", 186),   # Ultra Ball
    (4, "SSH", 216),   # Quick Ball
    (4, "FST", 225),   # Battle VIP Pass
    (4, "FST", 281),   # Power Tablet
    (4, "FST", 229),   # Cram-o-matic
    (2, "LOR", 162),   # Lost Vacuum
    (2, "BST", 125),   # Escape Rope
    (2, "CPA", 64),    # Rotom Phone
    (1, "SSH", 172),   # Pal Pad
    (1, "SSH", 183),   # Switch
    (1, "BST", 127),   # Fan of Waves
    (2, "SIT", 156),   # Forest Seal Stone
    (1, "BRS", 135),   # Choice Belt
    (1, "DAA", 157),   # Big Parasol
    (2, "CRE", 148),   # Path to the Peak
    (2, "LOR", 161),   # Lost City
    (4, "BRS", 151),   # Double Turbo Energy
]

LOST_ZONE_BOX_DECKLIST = [
    (1, "SHF", 44),    # Crobat V
    (1, "LOR", 118),   # Drapion V
    (1, "EVS", 192),   # Dragonite V
    (1, "LOR", 92),    # Aerodactyl V
    (1, "LOR", 93),    # Aerodactyl VSTAR
    (1, "VIV", 61),    # Zeraora
    (4, "LOR", 79),    # Comfey
    (2, "LOR", 70),    # Sableye
    (1, "LOR", 50),    # Cramorant
    (1, "BRS", 40),    # Lumineon V
    (1, "BRS", 41),    # Manaphy
    (1, "ASR", 46),    # Radiant Greninja
    (4, "LOR", 155),   # Colress's Experiment
    (1, "CRE", 145),   # Klara
    (4, "LOR", 163),   # Mirage Gate
    (4, "FST", 225),   # Battle VIP Pass
    (4, "RCL", 165),   # Scoop Up Net
    (3, "BST", 125),   # Escape Rope
    (2, "ASR", 154),   # Switch Cart
    (2, "SSH", 179),   # Quick Ball
    (2, "BRS", 186),   # Ultra Ball
    (2, "LOR", 162),   # Lost Vacuum
    (1, "SSH", 171),   # Ordinary Rod
    (1, "BST", 124),   # Energy Recycler
    (1, "ASR", 146),   # Hisuian Heavy Ball
    (2, "SIT", 156),   # Forest Seal Stone
    (1, "SSH", 156),   # Air Balloon
    (1, "RCL", 169),   # Training Court
    (4, "Free_Energy", 3),  # Water Energy
    (2, "Free_Energy", 5),  # Psychic Energy
    (2, "Free_Energy", 4),  # Lightning Energy
    (1, "Free_Energy", 6),  # Fighting Energy
]

REGIGIGAS_DECKLIST = [
    (3, "ASR", 130),   # Regigigas
    (2, "ASR", 118),   # Regidrago
    (1, "EVS", 124),   # Regidrago
    (2, "ASR", 75),    # Regirock
    (1, "ASR", 51),    # Regieleki
    (1, "EVS", 60),    # Regieleki
    (2, "ASR", 108),   # Registeel
    (2, "ASR", 37),    # Regice
    (4, "CEL", 24),    # Professor's Research
    (4, "SSH", 200),   # Marnie
    (1, "SIT", 193),   # Serena
    (1, "RCL", 189),   # Boss's Orders
    (4, "RCL", 165),   # Scoop Up Net
    (4, "SSH", 216),   # Quick Ball
    (3, "ASR", 156),   # Trekking Shoes
    (3, "SSH", 171),   # Ordinary Rod
    (2, "BRS", 150),   # Ultra Ball
    (1, "ASR", 146),   # Hisuian Heavy Ball
    (1, "BST", 125),   # Escape Rope
    (3, "BRS", 135),   # Choice Belt
    (4, "CRE", 148),   # Path to the Peak
    (4, "SSH", 186),   # Aurora Energy
    (2, "RCL", 174),   # Twin Energy
    (2, "LOR", 171),   # Gift Energy
    (1, "RCL", 173),   # Speed Lightning Energy
    (1, "Free_Energy", 2),  # Fire Energy
    (1, "RCL", 171),   # Capture Energy
]

STARTER_DECKS = [
    ("Lugia VSTAR", LUGIA_VSTAR_DECKLIST),
    ("Mew VMAX", MEW_VMAX_DECKLIST),
    ("Lost Zone Box", LOST_ZONE_BOX_DECKLIST),
    ("Regigigas", REGIGIGAS_DECKLIST),
]

_CARD_INDEX = None


def _ensure_cards_loaded():
    if not card_loader.cards:
        card_loader.load_all()


def _ensure_products_loaded():
    if not product_loader.products:
        product_loader.load_all()


def _card_index():
    """{(set_code, collector_number): guid} over every loaded card script."""
    global _CARD_INDEX
    if _CARD_INDEX is None:
        _ensure_cards_loaded()
        index = {}
        for card in card_loader.cards:
            num = card.get_attribute_value(AttrID.COLLECTOR_NUMBER)
            if num is None:
                continue
            try:
                index[(card.key.upper(), int(num))] = card.guid
            except (ValueError, TypeError):
                continue
        _CARD_INDEX = index
    return _CARD_INDEX


def resolve_decklist(decklist) -> list:
    """Expands (count, live set code, collector number) entries into a flat GUID list."""
    guids = []
    index = _card_index()
    for count, live_code, number in decklist:
        set_code = SET_CODE_MAP.get(live_code, live_code)
        guid = index.get((set_code.upper(), number))
        if not guid:
            logging.warning(f"[Starter] Card not found: {live_code} {number} (set {set_code})")
            continue
        guids.extend([guid] * count)
    return guids


def build_deck_data(deck_name: str, decklist) -> dict:
    """Builds a client-shaped SerializableDeck dict for the given decklist."""
    return {
        "deckID": str(uuid.uuid4()),
        "deckName": deck_name,
        "piles": {"deck": resolve_decklist(decklist)},
        "attributes": [
            {"name": AttrID.SELECTED_COIN.value, "value": "B9A4EA96-949E-11E1-890F-EFB676C7909C"},
            {"name": AttrID.SELECTED_SLEEVE.value, "value": "e079c0d3-b934-4fbd-b021-545106c75693"},
            {"name": AttrID.SELECTED_DECK_BOX.value, "value": "e129b0d3-b934-4fbd-b021-545106c75694"},
        ],
    }


def starter_booster_packs() -> list:
    """Booster pack products for every set with more than 10 scripted cards."""
    _ensure_products_loaded()
    eligible = {code.upper() for code in eligible_booster_sets()}
    return [
        p for p in product_loader.products
        if p.product_type == ProductType.PACKS.value and p.key.upper() in eligible
    ]


def grant_starter_content(account_id: str) -> bool:
    """Grants the starter decks and booster packs to a freshly created account."""

    try:
        update_wallet(account_id, STARTING_COINS, STARTING_GEMS, STARTING_TICKETS)

        for deck_name, decklist in STARTER_DECKS:
            deck_data = build_deck_data(deck_name, decklist)
            deck_guids = deck_data["piles"]["deck"]
            if len(deck_guids) != 60:
                logging.warning(f"[Starter] Deck '{deck_name}' resolved {len(deck_guids)}/60 cards.")
            save_deck(account_id, deck_data["deckID"], deck_name, deck_data, is_avatar=False)

            # Own every card the deck uses
            counts = {}
            for guid in deck_guids:
                counts[guid] = counts.get(guid, 0) + 1
            for guid, count in counts.items():
                add_to_collection(account_id, guid, count=count, is_tradable=False)

        for pack in starter_booster_packs():
            add_to_collection(account_id, pack.guid, count=STARTER_BOOSTER_PACK_COUNT, is_tradable=False)

        for cosmetic_guid in STARTER_COSMETICS:
            add_to_collection(account_id, cosmetic_guid, count=1, is_tradable=False)

        logging.info(f"[Starter] Granted starter decks, booster packs, and cosmetics to account {account_id}.")
        return True
    except Exception as e:
        logging.error(f"[Starter] Failed to grant starter content to {account_id}: {e}")
        return False
