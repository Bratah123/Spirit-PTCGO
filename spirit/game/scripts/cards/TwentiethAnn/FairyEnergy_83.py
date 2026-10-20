from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="36ced4ae-ba96-53f5-ac0f-863939f69c83",
    key="TwentiethAnn",
    name="Fairy Energy",
    display_name="Fairy Energy",
    searchable_by=["Fairy Energy", "Basic"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="TwentiethAnn",
    rarity=Rarities.Common,
    energy_type=PokemonTypes.FAIRY,
    is_special=False,
)
