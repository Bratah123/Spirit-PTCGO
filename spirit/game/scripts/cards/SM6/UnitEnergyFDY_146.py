from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm6 import UNIT_ENERGY_FDY

card = EnergyCardDef(
    guid="f2afe5b0-5b2c-5c33-9e77-101b595436ad",
    key="SM6",
    name="Unit Energy {F}{D}{Y}",
    display_name="Unit Energy {F}{D}{Y}",
    searchable_by=["Unit Energy {F}{D}{Y}", "Special"],
    subtypes=["Special"],
    collector_number=146,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=UNIT_ENERGY_FDY,
)
