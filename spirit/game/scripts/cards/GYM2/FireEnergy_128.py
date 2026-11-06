from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="47aa3566-7aca-5a94-a620-da6e23dd9404",
    key="GYM2",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="GYM2",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
