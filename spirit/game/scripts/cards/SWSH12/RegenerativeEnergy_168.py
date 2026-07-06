from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d5be181e-eb89-50ba-8e6e-cff7aa95420b",
    key="SWSH12",
    name="Regenerative Energy",
    display_name="Regenerative Energy",
    searchable_by=["Regenerative Energy", "Special"],
    subtypes=["Special"],
    collector_number=168,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
