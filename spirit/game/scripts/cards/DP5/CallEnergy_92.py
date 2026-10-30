"""STUB: effect not implemented — do not guess mechanics.
Call Energy (DP5 #92): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Call Energy provides Colorless Energy. Once during your turn, if the Pokémon Call Energy is attached to is your Active Pokémon, you may search your deck for up to 2 Basic Pokémon and put them onto your Bench. If you do, shuffle your deck and your turn ends.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c86675bb-9641-5053-a149-bb26dd9e6469",
    key="DP5",
    name="Call Energy",
    display_name="Call Energy",
    searchable_by=["Call Energy", "Special"],
    subtypes=["Special"],
    collector_number=92,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
