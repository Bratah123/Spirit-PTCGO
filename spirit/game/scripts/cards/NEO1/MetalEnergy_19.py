"""STUB: effect not implemented — do not guess mechanics.
Metal Energy (NEO1 #19): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Damage done to the Pokémon Metal Energy is attached to is reduced by 10 (after applying Weakness and Resistance). If the Pokémon Metal Energy is attached to isn't Metal, whenever it damages a Pokémon, reduce that damage by 10 (before applying Weakness and Resistance).
Metal Energy provides Metal Energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9f9d6315-9756-59b0-a68b-28795c93ef45",
    key="NEO1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=19,
    set_code="NEO1",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
