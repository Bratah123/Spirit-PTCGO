"""STUB: effect not implemented — do not guess mechanics.
Warp Energy (DP7 #95): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Warp Energy provides Colorless Energy. When you attach this card from your hand to your Active Pokémon, switch that Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5ff65047-c3e8-5678-9a70-78f8937aa84d",
    key="DP7",
    name="Warp Energy",
    display_name="Warp Energy",
    searchable_by=["Warp Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
