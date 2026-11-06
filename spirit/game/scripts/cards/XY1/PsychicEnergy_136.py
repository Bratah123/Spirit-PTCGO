from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7d678c3a-bd06-5c23-83e9-cb25a899358b",
    key="XY1",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="XY1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
)
