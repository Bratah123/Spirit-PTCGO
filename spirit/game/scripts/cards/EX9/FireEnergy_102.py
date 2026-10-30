from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="94c7719a-9a5b-5023-8b32-0045ff502097",
    key="EX9",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
