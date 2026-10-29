from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm6 import UNIT_ENERGY_FDY

card = EnergyCardDef(
    guid="495d53df-e84d-5eaf-9104-d6389dddac5f",
    key="SM6",
    name="Unit Energy {F}{D}{Y}",
    display_name="Unit Energy {F}{D}{Y}",
    searchable_by=["Unit Energy {F}{D}{Y}", "Special"],
    subtypes=["Special"],
    collector_number=118,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=UNIT_ENERGY_FDY,
)
