from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="c6763808-6d99-5920-a5eb-fffb65f7529e",
    key="EX16",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=106,
    set_code="EX16",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
