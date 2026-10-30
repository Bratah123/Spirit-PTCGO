from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9a8d53f8-858c-5431-b5aa-74c8c38450f4",
    key="GYM2",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="GYM2",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
