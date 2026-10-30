from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="95d27d26-603b-5b6b-91ad-122b12c07c70",
    key="NEO1",
    name="Grass Energy",
    display_name="Grass Energy",
    searchable_by=["Grass Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="NEO1",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.GRASS,
    is_special=False,
)
