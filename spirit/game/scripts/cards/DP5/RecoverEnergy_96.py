"""STUB: effect not implemented — do not guess mechanics.
Recover Energy (DP5 #96): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Recover Energy provides Colorless Energy. When you attach this card from your hand to 1 of your Pokémon, remove all Special Conditions from that Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="36fcba75-b803-5ffb-8ae5-e62c34df7ec0",
    key="DP5",
    name="Recover Energy",
    display_name="Recover Energy",
    searchable_by=["Recover Energy", "Special"],
    subtypes=["Special"],
    collector_number=96,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
