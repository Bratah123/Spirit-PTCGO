"""Deck pool for the queue AI's random opponent decks.

HAND_CURATED below holds the hand-written Standard lists; the scraped Limitless
top lists live in bot_decks_scraped.py (SCRAPED_DECK_LISTS) and are merged in
at import time -- curated lists win any name collision. Regenerate the scraped
module with `python spirit/tools/build_bot_decks.py --from-folder --emit` and
re-validate everything with `--check`. Restart the server after editing.

See `spirit/game/content/starter.py` for the four decks granted to new
accounts -- those stay out of this file on purpose.
"""


# name -> (count, live set code, collector number)
HAND_CURATED = {
    'Charizard VSTAR': [
        (4, 'BRS', 17),   # Charizard V
        (3, 'BRS', 18),   # Charizard VSTAR
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (4, 'CPA', 56),   # Marnie
        (3, 'EVS', 152),   # Raihan
        (2, 'BRS', 132),   # Boss's Orders
        (1, 'SIT', 164),   # Serena
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (2, 'BST', 129),   # Level Ball
        (3, 'ASR', 211),   # Choice Belt
        (3, 'BST', 125),   # Escape Rope
        (3, 'SSH', 183),   # Switch
        (3, 'SSH', 160),   # Energy Retrieval
        (1, 'SSH', 172),   # Pal Pad
        (1, 'RCL', 206),   # Big Charm
        (1, 'LOR', 162),   # Lost Vacuum
        (1, 'SIT', 156),   # Forest Seal Stone
        (10, 'FST', 284),   # Fire Energy
        (2, 'DAA', 174),   # Heat Fire Energy
    ],

    'Arceus Duraludon': [
        (4, 'BRS', 122),   # Arceus V
        (3, 'BRS', 123),   # Arceus VSTAR
        (3, 'EVS', 122),   # Duraludon V
        (2, 'EVS', 123),   # Duraludon VMAX
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (2, 'SIT', 164),   # Serena
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (4, 'SSH', 163),   # Evolution Incense
        (2, 'SSH', 180),   # Rare Candy
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'SSH', 156),   # Air Balloon
        (2, 'SSH', 160),   # Energy Retrieval
        (1, 'SSH', 172),   # Pal Pad
        (1, 'ASR', 213),   # Path to the Peak
        (2, 'EVS', 237),   # Metal Energy
        (2, 'CRE', 233),   # Fighting Energy
        (4, 'ASR', 216),   # Double Turbo Energy
        (3, 'DAA', 176),   # Powerful Colorless Energy
    ],

    'Rapid Strike Urshifu': [
        (4, 'BST', 87),   # Rapid Strike Urshifu V
        (3, 'BST', 88),   # Rapid Strike Urshifu VMAX
        (2, 'BST', 37),   # Octillery
        (3, 'CRE', 41),   # Sobble
        (2, 'CRE', 42),   # Drizzile
        (1, 'EVS', 227),   # Inteleon
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (1, 'BST', 128),   # Korrina's Focus
        (2, 'BRS', 132),   # Boss's Orders
        (3, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (2, 'BST', 129),   # Level Ball
        (2, 'SSH', 163),   # Evolution Incense
        (1, 'SSH', 180),   # Rare Candy
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'BST', 138),   # Tower of Waters
        (1, 'SSH', 172),   # Pal Pad
        (6, 'CRE', 233),   # Fighting Energy
        (4, 'CRE', 231),   # Water Energy
        (4, 'BST', 140),   # Rapid Strike Energy
    ],

    'Single Strike Urshifu': [
        (4, 'BST', 85),   # Single Strike Urshifu V
        (3, 'BST', 86),   # Single Strike Urshifu VMAX
        (4, 'BST', 95),   # Houndour
        (3, 'BST', 96),   # Houndoom
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (2, 'BST', 128),   # Korrina's Focus
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (3, 'BST', 129),   # Level Ball
        (2, 'SSH', 163),   # Evolution Incense
        (2, 'SSH', 180),   # Rare Candy
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'BST', 137),   # Tower of Darkness
        (1, 'SSH', 172),   # Pal Pad
        (1, 'RCL', 206),   # Big Charm
        (3, 'CRE', 233),   # Fighting Energy
        (3, 'EVS', 236),   # Darkness Energy
        (4, 'BST', 141),   # Single Strike Energy
    ],

    'Ice Rider Calyrex': [
        (4, 'CRE', 45),   # Ice Rider Calyrex V
        (3, 'CRE', 46),   # Ice Rider Calyrex VMAX
        (4, 'LOR', 51),   # Glastrier
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (4, 'ASR', 147),   # Irida
        (1, 'CRE', 145),   # Klara
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (3, 'BST', 129),   # Level Ball
        (2, 'SSH', 163),   # Evolution Incense
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (2, 'SSH', 160),   # Energy Retrieval
        (1, 'SSH', 172),   # Pal Pad
        (1, 'ASR', 213),   # Path to the Peak
        (1, 'CRE', 140),   # Fog Crystal
        (7, 'CRE', 231),   # Water Energy
        (3, 'ASR', 216),   # Double Turbo Energy
    ],

    'Shadow Rider Calyrex': [
        (4, 'CRE', 74),   # Shadow Rider Calyrex V
        (3, 'CRE', 75),   # Shadow Rider Calyrex VMAX
        (4, 'LOR', 81),   # Spectrier
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (1, 'LOR', 50),   # Cramorant
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (3, 'ASR', 135),   # Adaman
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (3, 'BST', 129),   # Level Ball
        (3, 'CRE', 140),   # Fog Crystal
        (2, 'SSH', 163),   # Evolution Incense
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'SSH', 156),   # Air Balloon
        (2, 'SSH', 160),   # Energy Retrieval
        (1, 'SSH', 172),   # Pal Pad
        (1, 'ASR', 213),   # Path to the Peak
        (7, 'CRE', 232),   # Psychic Energy
        (3, 'ASR', 216),   # Double Turbo Energy
    ],

    'Eternatus VMAX': [
        (4, 'DAA', 116),   # Eternatus V
        (3, 'DAA', 117),   # Eternatus VMAX
        (3, 'DAA', 104),   # Crobat V
        (3, 'SIT', 103),   # Zubat
        (2, 'SIT', 104),   # Golbat
        (2, 'BRS', 44),   # Eiscue
        (1, 'BRS', 40),   # Lumineon V
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (3, 'FST', 235),   # Judge
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (2, 'BST', 129),   # Level Ball
        (2, 'SSH', 163),   # Evolution Incense
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'SSH', 156),   # Air Balloon
        (2, 'SSH', 160),   # Energy Retrieval
        (1, 'SSH', 172),   # Pal Pad
        (1, 'RCL', 206),   # Big Charm
        (5, 'EVS', 236),   # Darkness Energy
        (3, 'DAA', 201),   # Capture Energy
    ],

    'Rayquaza VMAX': [
        (4, 'EVS', 110),   # Rayquaza V
        (3, 'EVS', 111),   # Rayquaza VMAX
        (2, 'VIV', 55),   # Joltik
        (2, 'FST', 280),   # Flaaffy
        (3, 'LOR', 54),   # Electrike
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (1, 'EVS', 164),   # Zinnia's Resolve
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (2, 'BST', 129),   # Level Ball
        (1, 'SSH', 163),   # Evolution Incense
        (1, 'SSH', 180),   # Rare Candy
        (1, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'FST', 282),   # Training Court
        (1, 'SSH', 172),   # Pal Pad
        (8, 'EVS', 235),   # Lightning Energy
        (5, 'FST', 284),   # Fire Energy
        (3, 'SSH', 186),   # Aurora Energy
    ],

    'Origin Palkia VSTAR': [
        (4, 'ASR', 39),   # Origin Forme Palkia V
        (3, 'ASR', 40),   # Origin Forme Palkia VSTAR
        (3, 'ASR', 46),   # Radiant Greninja
        (4, 'LOR', 79),   # Comfey
        (2, 'LOR', 50),   # Cramorant
        (2, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (3, 'ASR', 147),   # Irida
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (3, 'BST', 129),   # Level Ball
        (2, 'CRE', 140),   # Fog Crystal
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (2, 'SSH', 160),   # Energy Retrieval
        (1, 'SSH', 172),   # Pal Pad
        (1, 'ASR', 213),   # Path to the Peak
        (1, 'FST', 282),   # Training Court
        (2, 'CRE', 231),   # Water Energy
        (4, 'ASR', 216),   # Double Turbo Energy
    ],

    'Flying Pikachu VMAX': [
        (4, 'CEL', 6),   # Flying Pikachu V
        (3, 'CEL', 7),   # Flying Pikachu VMAX
        (3, 'SIT', 49),   # Pikachu
        (2, 'SIT', 50),   # Raichu
        (1, 'FST', 103),   # Boltund V
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (2, 'FST', 235),   # Judge
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (2, 'BST', 129),   # Level Ball
        (1, 'SSH', 163),   # Evolution Incense
        (1, 'SSH', 180),   # Rare Candy
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'BST', 138),   # Tower of Waters
        (1, 'SSH', 172),   # Pal Pad
        (8, 'EVS', 235),   # Lightning Energy
        (4, 'RCL', 173),   # Speed Lightning Energy
        (3, 'DAA', 201),   # Capture Energy
    ],

    'Giratina VSTAR': [
        (4, 'LOR', 130),   # Giratina V
        (3, 'LOR', 131),   # Giratina VSTAR
        (4, 'LOR', 79),   # Comfey
        (1, 'LOR', 50),   # Cramorant
        (1, 'LOR', 70),   # Sableye
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'LOR', 155),   # Colress's Experiment
        (3, 'BRS', 147),   # Professor's Research
        (2, 'CRE', 145),   # Klara
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (2, 'BRS', 150),   # Ultra Ball
        (2, 'BST', 129),   # Level Ball
        (4, 'LOR', 163),   # Mirage Gate
        (1, 'FST', 225),   # Battle VIP Pass
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'LOR', 162),   # Lost Vacuum
        (1, 'SSH', 172),   # Pal Pad
        (5, 'FST', 283),   # Grass Energy
        (6, 'CRE', 232),   # Psychic Energy
        (4, 'ASR', 216),   # Double Turbo Energy
    ],

    'Gengar VMAX': [
        (4, 'FST', 156),   # Gengar V
        (3, 'FST', 157),   # Gengar VMAX
        (4, 'LOR', 64),   # Gastly
        (3, 'LOR', 65),   # Haunter
        (2, 'DAA', 104),   # Crobat V
        (1, 'BRS', 40),   # Lumineon V
        (1, 'BRS', 41),   # Manaphy
        (4, 'BRS', 147),   # Professor's Research
        (3, 'CPA', 56),   # Marnie
        (3, 'FST', 235),   # Judge
        (2, 'BRS', 132),   # Boss's Orders
        (4, 'FST', 237),   # Quick Ball
        (3, 'BRS', 150),   # Ultra Ball
        (3, 'BST', 129),   # Level Ball
        (2, 'SSH', 163),   # Evolution Incense
        (2, 'SSH', 180),   # Rare Candy
        (2, 'ASR', 211),   # Choice Belt
        (2, 'BST', 125),   # Escape Rope
        (2, 'SSH', 183),   # Switch
        (1, 'BST', 137),   # Tower of Darkness
        (1, 'SSH', 172),   # Pal Pad
        (1, 'RCL', 206),   # Big Charm
        (4, 'EVS', 236),   # Darkness Energy
        (3, 'RCL', 172),   # Horror Psychic Energy
    ],

    # Limitless SWSH top list (HenryBrand, Late Night Series #5) -- the pilot
    # deck for deck_strategies.py.
    'Dragapult Inteleon': [
        (4, 'RCL', 92),   # Dragapult V
        (3, 'RCL', 93),   # Dragapult VMAX
        (4, 'CRE', 41),   # Sobble
        (4, 'SSH', 56),   # Drizzile
        (2, 'CRE', 43),   # Inteleon
        (1, 'SSH', 58),   # Inteleon
        (1, 'SSH', 117),   # Galarian Zigzagoon
        (4, 'CPA', 56),   # Marnie
        (3, 'SHF', 60),   # Professor's Research
        (2, 'SHF', 58),   # Boss's Orders
        (1, 'EVS', 152),   # Raihan
        (4, 'BST', 129),   # Level Ball
        (4, 'SSH', 163),   # Evolution Incense
        (4, 'CRE', 140),   # Fog Crystal
        (3, 'SSH', 179),   # Quick Ball
        (1, 'SSH', 183),   # Switch
        (1, 'RCL', 165),   # Scoop Up Net
        (1, 'BST', 125),   # Escape Rope
        (1, 'CPA', 66),   # Suspicious Food Tin
        (1, 'BST', 136),   # Tool Jammer
        (4, 'CRE', 148),   # Path to the Peak
        (4, 'RCL', 172),   # Horror Psychic Energy
        (3, 'CRE', 232),   # Psychic Energy
    ],
}

try:
    from spirit.game.content.bot_decks_scraped import SCRAPED_DECK_LISTS
except ImportError:  # scraped module not generated yet
    SCRAPED_DECK_LISTS = {}

# Curated lists win name collisions; scraped lists widen the pool.
BOT_DECK_LISTS = {**SCRAPED_DECK_LISTS, **HAND_CURATED}

# The queue AI may only draw decks that already have a strategic brain
# (spirit/game/content/deck_strategies.py). Add a deck's name here once its
# strategy script exists; remove it to retire the deck from the pool.
# While this list is being grown, STARTER_DECKS stay out of the AI pool too.
ACTIVE_BOT_DECKS = ["Dragapult Inteleon", "Rapid Strike Urshifu V",
                    "Shadow Rider Calyrex V", "Bronzor", "Eternatus V",
                    "Rayquaza V", "Sobble (suicune-ludicolo)"]

BOT_DECKS = [(name, decklist) for name, decklist in BOT_DECK_LISTS.items()
             if name in ACTIVE_BOT_DECKS]