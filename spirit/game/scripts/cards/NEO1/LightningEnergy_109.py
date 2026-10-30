from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="32969d95-75f5-5d56-8647-d4efa43ae8ac",
    key="NEO1",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="NEO1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
