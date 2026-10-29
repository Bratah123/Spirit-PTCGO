from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm5 import UNIT_ENERGY_LPM

card = EnergyCardDef(
    guid="a442d5d3-b4ab-5ae9-a6de-246c31e31503",
    key="SM5",
    name="Unit Energy {L}{P}{M}",
    display_name="Unit Energy {L}{P}{M}",
    searchable_by=["Unit Energy {L}{P}{M}", "Special"],
    subtypes=["Special"],
    collector_number=171,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=UNIT_ENERGY_LPM,
)
