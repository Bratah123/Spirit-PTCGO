from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2c2ec311-a662-5d60-95eb-aea5abe5265d",
    key="SWSH7",
    name="Metal Energy",
    display_name="Metal Energy",
    searchable_by=["Metal Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=237,
    set_code="SWSH7",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.METAL,
    is_special=False
)
