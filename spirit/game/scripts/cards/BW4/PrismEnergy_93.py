from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="9c230178-86f2-5924-b042-09f1fa7e0ac2",
    key="BW4",
    name="Prism Energy",
    display_name="Prism Energy",
    searchable_by=["Prism Energy", "Special"],
    subtypes=["Special"],
    collector_number=93,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True
)
