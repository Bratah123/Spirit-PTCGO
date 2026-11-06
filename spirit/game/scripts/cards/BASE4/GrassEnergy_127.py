from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="719bb8dd-d0a6-53b8-a7b4-404b6cdbdbd1",
    key="BASE4",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="BASE4",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
