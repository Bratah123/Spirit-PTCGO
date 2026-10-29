from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="ff687838-9bf4-541e-a542-176d0caa8987",
    key="SM2",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=168,
    set_code="SM2",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
