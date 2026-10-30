from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="64df2fda-f176-5d53-afd4-67fd336279f9",
    key="BASE1",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="BASE1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
