from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    MultiEnergyPassive,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="8a514abf-635f-54a3-83ec-7f0ef5585be4",
    key="EX9",
    name="Multi Energy",
    display_name="Multi Energy",
    searchable_by=["Multi Energy", "Special"],
    subtypes=["Special"],
    collector_number=89,
    set_code="EX9",
    rarity=Rarities.Rare,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    passive=MultiEnergyPassive(),
)
