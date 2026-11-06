from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="47519a10-f8f4-50e1-8b44-0b9f55f3dc05",
    key="TwentiethAnn",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False,
)
