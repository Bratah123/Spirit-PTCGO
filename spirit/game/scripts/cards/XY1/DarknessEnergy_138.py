from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8bd25d9e-bfb2-59f5-9c48-307aff526f57",
    key="XY1",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="XY1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
)
