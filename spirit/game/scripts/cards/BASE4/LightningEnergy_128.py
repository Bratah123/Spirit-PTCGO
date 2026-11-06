from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="f06aea09-5efe-5a07-91c2-ad015e47806e",
    key="BASE4",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="BASE4",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
