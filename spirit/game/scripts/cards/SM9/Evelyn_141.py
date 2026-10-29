from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    evelyn,
    evelyn_condition,
)

card = SupporterCardDef(
    guid="ece2a15c-9062-5922-b9fb-3b4124fcd1fb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evelyn.Name",
    display_name="Evelyn",
    searchable_by=["Evelyn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=evelyn,
            condition=evelyn_condition,
        )
