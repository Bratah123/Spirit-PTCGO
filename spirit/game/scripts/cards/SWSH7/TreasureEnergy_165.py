from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d193d412-b5e1-5751-a2ac-103c8ac26360",
    key="SWSH7",
    name="Treasure Energy",
    display_name="Treasure Energy",
    searchable_by=["Treasure Energy", "Special"],
    subtypes=["Special"],
    collector_number=165,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
