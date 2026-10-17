from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="1f851c75-dcb1-5ffe-9cc4-1f03ed218193",
    key="XY12",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="XY12",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
