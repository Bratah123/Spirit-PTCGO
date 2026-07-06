from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="73c65f08-c971-5757-aeea-24da7388a716",
    key="SWSH5",
    name="Rapid Strike Energy",
    display_name="Rapid Strike Energy",
    searchable_by=["Rapid Strike Energy", "Special", "Rapid Strike"],
    subtypes=["Special", "Rapid Strike"],
    collector_number=140,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
