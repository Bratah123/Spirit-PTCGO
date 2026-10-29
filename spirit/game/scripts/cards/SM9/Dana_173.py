from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    dana,
    dana_condition,
)

card = SupporterCardDef(
    guid="c30e707e-dfed-5d15-a697-d00df9cf6e0a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name",
    display_name="Dana",
    searchable_by=["Dana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=dana,
            condition=dana_condition,
        )
