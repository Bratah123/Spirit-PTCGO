from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="95b944d7-93e8-583b-be65-14cc1ce5eb58",
    key="GYM1",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="GYM1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
