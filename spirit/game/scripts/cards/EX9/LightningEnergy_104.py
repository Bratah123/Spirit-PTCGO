from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="671711ee-4d88-54e2-afa2-89101deb3519",
    key="EX9",
    name="Lightning Energy",
    display_name="Lightning Energy",
    searchable_by=["Lightning Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=104,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    energy_type=PokemonTypes.LIGHTNING,
    is_special=False,
)
