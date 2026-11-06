from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7913c4a1-277f-5921-8ba9-79030351e29e",
    key="ECARD1",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="ECARD1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
