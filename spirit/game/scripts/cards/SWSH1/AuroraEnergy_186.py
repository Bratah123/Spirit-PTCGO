from spirit.game.card_effects.energies import (
    ALL_TYPES_ONE_AT_A_TIME,
    another_card_in_hand,
    aurora_attach_cost,
)
from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="cd7f0518-76e6-5249-bd0a-b7c75e76e096",
    key="SWSH1",
    name="Aurora Energy",
    display_name="Aurora Energy",
    searchable_by=["Aurora Energy", "Special"],
    subtypes=["Special"],
    collector_number=186,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    provides=ALL_TYPES_ONE_AT_A_TIME,
    attach_condition=another_card_in_hand,
    attach_cost=aurora_attach_cost
)
