from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="547148db-8548-5873-a23b-fab024ff43d0",
    key="SWSH4",
    name="Stone Fighting Energy",
    display_name="Stone Fighting Energy",
    searchable_by=["Stone Fighting Energy", "Special"],
    subtypes=["Special"],
    collector_number=164,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
