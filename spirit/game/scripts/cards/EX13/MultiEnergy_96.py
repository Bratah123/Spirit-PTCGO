"""EX13 Holon Phantoms — Multi Energy.
"""
from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    MultiEnergyPassive,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="78c5d046-c281-5df8-aa57-7249e5c0363f",
    key="EX13",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=96,
    set_code="EX13",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=MultiEnergyPassive(),
)
