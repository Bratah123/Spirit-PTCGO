from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f6b2842e-a919-562a-a858-37ccbafa5268",
    key="CZ",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.GRASS,
    is_special=False
)
