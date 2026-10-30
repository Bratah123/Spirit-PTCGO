"""DP5 Majestic Dawn — wired.
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
)
