from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ef958b98-1e55-58dd-8e39-ae69ba83ba9a",
    key="SWSH12",
    name="V Guard Energy",
    display_name="V Guard Energy",
    searchable_by=["V Guard Energy", "Special"],
    subtypes=["Special"],
    collector_number=215,
    set_code="SWSH12",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
