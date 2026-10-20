from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="919e4b38-ffb1-5249-9e5b-22c5f00b9df0",
    key="TwentiethAnn",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False,
)
