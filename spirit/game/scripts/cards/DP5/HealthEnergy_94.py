"""DP5 Majestic Dawn — wired.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="972c2e95-aabc-569f-b109-2c1af9875f55",
    key="DP5",
    name="Health Energy",
    display_name="Health Energy",
    searchable_by=["Health Energy", "Special"],
    subtypes=["Special"],
    collector_number=94,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
)
