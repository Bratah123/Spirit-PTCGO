from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e70831e0-807a-508f-b5df-b3dc63c134c6",
    key="GYM2",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="GYM2",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
