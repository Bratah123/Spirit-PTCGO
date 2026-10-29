from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="3a95e682-6776-5a73-ab97-5487efec334c",
    key="SM1",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=162,
    set_code="SM1",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
)
