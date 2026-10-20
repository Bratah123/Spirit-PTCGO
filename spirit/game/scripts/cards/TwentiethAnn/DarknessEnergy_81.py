from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="71e80fcb-6e20-523b-a186-010f12b1fb0b",
    key="TwentiethAnn",
    name="Darkness Energy",
    display_name="Darkness Energy",
    searchable_by=["Darkness Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.DARKNESS,
    is_special=False,
)
