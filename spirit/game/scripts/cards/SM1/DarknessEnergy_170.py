from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="3fb448bc-3597-5295-8ef6-30c33ea5f3cc",
    key="SM1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=170,
    set_code="SM1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
)
