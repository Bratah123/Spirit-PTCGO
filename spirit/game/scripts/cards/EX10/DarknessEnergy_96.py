"""STUB: effect not implemented — do not guess mechanics.
Darkness Energy (EX10 #96): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - If the Pokémon Darkness Energy is attached to attack, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance). Ignore this effect unless the Attacking Pokémon is Darkness or has Dark in its name. Darkness Energy provides Darkness Energy. (Doesn't count as a basic Energy card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="0f7d556d-3f59-5ed8-8029-58a6fadfcbd5",
    key="EX10",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=96,
    set_code="EX10",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
