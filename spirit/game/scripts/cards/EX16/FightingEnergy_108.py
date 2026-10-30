from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="65d6f01e-ae9e-56cb-b8c9-abbe2910caed",
    key="EX16",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False,
)
