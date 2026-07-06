from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="a1be9557-4439-5c31-8c90-51a75824090f",
    key="SWSH8",
    name="Fusion Strike Energy",
    display_name="Fusion Strike Energy",
    searchable_by=["Fusion Strike Energy", "Fusion Strike", "Special"],
    subtypes=["Fusion Strike", "Special"],
    collector_number=244,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
