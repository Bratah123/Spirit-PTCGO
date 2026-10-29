from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.sm5 import UNIT_ENERGY_LPM

card = EnergyCardDef(
    guid="f9104671-a5c1-5eb6-b0fe-fad555549982",
    key="SM5",
    name="Unit Energy {L}{P}{M}",
    display_name="Unit Energy {L}{P}{M}",
    searchable_by=["Unit Energy {L}{P}{M}", "Special"],
    subtypes=["Special"],
    collector_number=138,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=UNIT_ENERGY_LPM,
)
