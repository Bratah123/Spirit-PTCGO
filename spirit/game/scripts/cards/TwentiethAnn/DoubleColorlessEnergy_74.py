from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f9b4f3cb-64ef-51f3-9e10-f45203b5809b",
    key="TwentiethAnn",
    name="Double Colorless Energy",
    display_name="Double Colorless Energy",
    searchable_by=["Double Colorless Energy", "Special"],
    subtypes=["Special"],
    collector_number=74,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=[[PokemonTypes.COLORLESS, PokemonTypes.COLORLESS]],
)
