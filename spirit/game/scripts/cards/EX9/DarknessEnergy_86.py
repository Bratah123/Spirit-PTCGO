"""STUB: effect not implemented — do not guess mechanics.
Darkness Energy (EX9 #86): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - If the Pokémon Darkness Energy is attached to attacks, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance). Ignore this effect unless the Attacking Pokémon is Darkness or has Dark in its name. Darkness Energy provides Darkness Energy. (Doesn't count as a Basic card.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5ae60ef7-09e1-5e28-add4-8ad286bbdfef",
    key="EX9",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Special"],
    subtypes=["Special"],
    collector_number=86,
    set_code="EX9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
