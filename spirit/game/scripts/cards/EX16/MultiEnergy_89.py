"""EX13 Holon Phantoms — Multi Energy.
"""
from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    MultiEnergyPassive,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d6a32eb6-e3ad-5d68-9968-df8c74b24602",
    key="EX16",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX16",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=MultiEnergyPassive(),
)
