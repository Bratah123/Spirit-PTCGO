from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="965eebb3-db8c-5781-89b8-2ecd7ad9ab38",
    key="SM3",
    name="Fairy Energy",
    display_name="Fairy Energy",
    searchable_by=["Fairy Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=169,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.FAIRY,
    is_special=False,
)
