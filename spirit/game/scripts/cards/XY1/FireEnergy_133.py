from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="94359c7a-0e11-570e-aa17-b2c3c506975b",
    key="XY1",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="XY1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
