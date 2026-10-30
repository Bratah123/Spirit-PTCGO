from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="88b00224-8d35-5ce2-99d3-f351428e1434",
    key="EX16",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
