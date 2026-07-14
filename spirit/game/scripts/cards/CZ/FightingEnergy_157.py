from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c7ca2142-c68a-5bd4-bf0d-b8a478048d89",
    key="CZ",
    name="Fighting Energy",
    display_name="Fighting Energy",
    searchable_by=["Fighting Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=157,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.FIGHTING,
    is_special=False
)
