from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ea6c7c3d-b04f-547c-abca-e5e92777ed57",
    key="SWSH4",
    name="Wash Water Energy",
    display_name="Wash Water Energy",
    searchable_by=["Wash Water Energy", "Special"],
    subtypes=["Special"],
    collector_number=165,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
