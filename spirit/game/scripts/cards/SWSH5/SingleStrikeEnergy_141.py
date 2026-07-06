from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="29bb9bbb-02ca-5e9a-8dc4-6b8ec78bbc53",
    key="SWSH5",
    name="Single Strike Energy",
    display_name="Single Strike Energy",
    searchable_by=["Single Strike Energy", "Special", "Single Strike"],
    subtypes=["Special", "Single Strike"],
    collector_number=141,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
