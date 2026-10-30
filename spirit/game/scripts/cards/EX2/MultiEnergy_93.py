from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    MultiEnergyPassive,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="b5e37251-ca98-54ae-9523-71a9cc154292",
    key="EX2",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=93,
    set_code="EX2",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=MultiEnergyPassive(),
)
