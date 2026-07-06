from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5f332293-66bb-58dc-bd80-1f8c1a7b30b7",
    key="SWSH6",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=231,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
