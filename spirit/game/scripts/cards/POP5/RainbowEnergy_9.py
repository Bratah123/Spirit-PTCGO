from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    DeltaRainbowEnergyPassive,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="be2a8ecd-9973-5d94-a989-7da8f9001ad5",
    key="POP5",
    name="δ Rainbow Energy",
    display_name="δ Rainbow Energy",
    searchable_by=["δ Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=9,
    set_code="POP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=DeltaRainbowEnergyPassive(),
)
