"""STUB: effect not implemented — do not guess mechanics.
Darkness Energy (DP3 #129): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - If the Pokémon Darkness Energy is attached to attacks, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance). Ignore this effect if the Pokémon that Darkness Energy is attached to isn't Darkness. Darkness Energy provides Darkness Energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9e97ced3-fd64-57a8-a954-d9fdcaec809c",
    key="DP3",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=129,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
