from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="184b682e-642e-5d5d-a2c8-c89bc1535a1e",
    key="GYM2",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="GYM2",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
