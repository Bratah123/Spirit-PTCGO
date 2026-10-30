from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a5df5c41-f839-5603-9bfc-b68af71915a6",
    key="EX13",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="EX13",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
