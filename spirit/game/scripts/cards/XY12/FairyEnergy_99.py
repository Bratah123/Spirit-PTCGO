from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="3b2904da-441d-55ac-b62c-db85d04afe6e",
    key="XY12",
    name="Fairy Energy",
    display_name="Fairy Energy",
    searchable_by=["Fairy Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="XY12",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FAIRY,
    is_special=False,
)
