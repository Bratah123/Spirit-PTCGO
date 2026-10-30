from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="2e6cda20-7579-57fd-8b26-cdca56f5c4ef",
    key="EX16",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
)
