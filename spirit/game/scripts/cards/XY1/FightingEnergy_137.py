from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="0b790558-e129-5856-a25c-b92ac328933d",
    key="XY1",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="XY1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
