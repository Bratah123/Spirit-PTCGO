from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="bd3fcc7d-97b4-5b34-8f00-8a616d78d3ae",
    key="BW1",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
