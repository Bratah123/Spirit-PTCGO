from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="5c8088f8-340a-5329-851b-45acd1709d9e",
    key="SM10",
    name="Triple Acceleration Energy",
    display_name="Triple Acceleration Energy",
    searchable_by=["Triple Acceleration Energy", "Special"],
    subtypes=["Special"],
    collector_number=190,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
)
