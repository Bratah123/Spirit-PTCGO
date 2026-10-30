from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="33c6845b-be95-5d9d-b255-09a11943a4be",
    key="BASE1",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=96,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
)
