from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="369ee8c0-a888-5c2b-b6ea-703629493c5c",
    key="CZ",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
