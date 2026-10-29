from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="36dd3291-1d97-5b47-ba6d-ab91a7f76a65",
    key="SM10",
    name="Triple Acceleration Energy",
    display_name="Triple Acceleration Energy",
    searchable_by=["Triple Acceleration Energy", "Special"],
    subtypes=["Special"],
    collector_number=234,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
)
