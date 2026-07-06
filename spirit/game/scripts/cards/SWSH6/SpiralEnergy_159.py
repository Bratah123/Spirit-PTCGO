from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="864d97da-55bc-5a68-95d2-6f0c01b5dce9",
    key="SWSH6",
    name="Spiral Energy",
    display_name="Spiral Energy",
    searchable_by=["Spiral Energy", "Special", "Rapid Strike"],
    subtypes=["Special", "Rapid Strike"],
    collector_number=159,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
