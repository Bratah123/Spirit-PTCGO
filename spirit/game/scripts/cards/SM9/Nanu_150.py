from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    nanu,
    nanu_condition,
)

card = SupporterCardDef(
    guid="f91f713c-dd7e-59a5-9c62-6be92884231f",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nanu.Name",
    display_name="Nanu",
    searchable_by=["Nanu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=nanu,
            condition=nanu_condition,
        )
