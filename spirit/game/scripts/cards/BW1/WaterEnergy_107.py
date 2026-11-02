from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f5285390-1c39-5724-bae9-02d6cf6033fb",
    key="BW1",
    name="Water Energy",
    display_name="Water Energy",
    searchable_by=["Water Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="BW1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.WATER,
    is_special=False
)
