from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="60a4f8db-ab6d-5882-b6be-bfae777a2b38",
    key="SWSH2",
    name="Horror Psychic Energy",
    display_name="Horror Psychic Energy",
    searchable_by=["Horror Psychic Energy", "Special"],
    subtypes=["Special"],
    collector_number=172,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
