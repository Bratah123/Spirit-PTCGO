from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="616713d7-e9f3-5aea-8ae5-7072c779b3e9",
    key="SWSH2",
    name="Twin Energy",
    display_name="Twin Energy",
    searchable_by=["Twin Energy", "Special"],
    subtypes=["Special"],
    collector_number=174,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # Provides 2 Colorless (for non-V/GX; the deck's Regis are all non-V).
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
)
