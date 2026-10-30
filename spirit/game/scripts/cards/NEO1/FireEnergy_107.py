from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c07ca101-9071-5e39-81b3-29624b34c7cc",
    key="NEO1",
    name="Fire Energy",
    display_name="Fire Energy",
    searchable_by=["Fire Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="NEO1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FIRE,
    is_special=False,
)
