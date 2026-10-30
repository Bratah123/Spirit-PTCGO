"""STUB: effect not implemented — do not guess mechanics.
Metal Energy (DP3 #130): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Damage done by attacks to the Pokémon that Metal Energy is attached to is reduced by 10 (after applying Weakness and Resistance). Ignore this effect if the Pokémon that Metal Energy is attached to isn't Metal. Metal Energy provides Metal Energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c4017d40-500f-5898-b5ac-31b56fb4167e",
    key="DP3",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Special"],
    subtypes=["Special"],
    collector_number=130,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
