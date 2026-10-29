from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    dana,
    dana_condition,
)

card = SupporterCardDef(
    guid="f7b0941e-0a4d-5f1f-a46f-78a5f6b1467e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name",
    display_name="Dana",
    searchable_by=["Dana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=dana,
            condition=dana_condition,
        )
