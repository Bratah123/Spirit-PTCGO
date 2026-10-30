from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="fb55e70e-58a5-5fac-8214-ebf92d341897",
    key="GYM1",
    name="Psychic Energy",
    display_name="Psychic Energy",
    searchable_by=["Psychic Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=131,
    set_code="GYM1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.PSYCHIC,
    is_special=False,
)
