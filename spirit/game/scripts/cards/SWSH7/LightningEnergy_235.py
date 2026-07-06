from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c09f5ee2-7890-5d5a-82ed-0137d8df7ed0",
    key="SWSH7",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=235,
    set_code="SWSH7",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False
)
