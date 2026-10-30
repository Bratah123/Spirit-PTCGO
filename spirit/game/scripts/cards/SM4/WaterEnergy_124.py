from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9add44b5-ffb5-5233-ab2c-927dfe22c2cc",
    key="SM4",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
