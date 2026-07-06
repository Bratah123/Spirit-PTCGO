from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="7082710f-138c-56dd-895f-7bddbfe68231",
    key="SWSH4",
    name="Aromatic Grass Energy",
    display_name="Aromatic Grass Energy",
    searchable_by=["Aromatic Grass Energy", "Special"],
    subtypes=["Special"],
    collector_number=162,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
