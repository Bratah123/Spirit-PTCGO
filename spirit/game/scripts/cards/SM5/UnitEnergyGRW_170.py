from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm5 import UNIT_ENERGY_GRW

card = EnergyCardDef(
    guid="6045f77f-d7da-5ed4-864b-faea6c7c0f0b",
    key="SM5",
    name="Unit Energy {G}{R}{W}",
    display_name="Unit Energy {G}{R}{W}",
    searchable_by=["Unit Energy {G}{R}{W}", "Special"],
    subtypes=["Special"],
    collector_number=170,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=UNIT_ENERGY_GRW,
)
