from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7b5ec138-5c6e-55b6-86b1-5deb16587248",
    key="EX9",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
