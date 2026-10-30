from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5a488477-7239-5d19-b5f8-bf31b1001bdd",
    key="EX16",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=105,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
