"""EX13 Holon Phantoms — δ Rainbow Energy.
"""
from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    DeltaRainbowEnergyPassive,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="d4dfa59a-02cf-5cde-a3a7-f83eb2b8182d",
    key="EX15",
    name="δ Rainbow Energy",
    display_name="δ Rainbow Energy",
    searchable_by=["\u03b4 Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=88,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=DeltaRainbowEnergyPassive(),
)
