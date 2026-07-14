from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="e23cc8a4-0ff4-581e-b32a-8f68f8adab44",
    key="CZ",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=156,
    set_code="CZ",
    rarity=Rarities.RareUltra,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False
)
