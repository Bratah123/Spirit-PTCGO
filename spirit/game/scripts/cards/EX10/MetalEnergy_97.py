"""STUB: effect not implemented — do not guess mechanics.
Metal Energy (EX10 #97): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Damage done by attacks to the Pokémon that Metal Energy is attached to is reduced by 10 (after applying Weakness and Resistance). Ignore this effect if the Pokémon that Metal Energy is attached to isn't Metal. Metal Energy provides Metal Energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="91e9fad7-e694-5386-9b87-44ffe4e13e6b",
    key="EX10",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=97,
    set_code="EX10",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
