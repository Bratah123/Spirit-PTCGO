from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="172259ba-93c5-5c01-b424-44d02a31d83c",
    key="XY1",
    name="Fairy Energy",
    display_name="Fairy Energy",
    searchable_by=["Fairy Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=140,
    set_code="XY1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FAIRY,
    is_special=False,
)
