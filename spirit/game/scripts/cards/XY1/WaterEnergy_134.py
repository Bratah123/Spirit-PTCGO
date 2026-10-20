from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="90045d25-4ef5-55bc-a54d-abd2c342177b",
    key="XY1",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=134,
    set_code="XY1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
