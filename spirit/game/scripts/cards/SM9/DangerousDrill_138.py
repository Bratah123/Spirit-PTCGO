from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    dangerous_drill,
    dangerous_drill_condition,
)

card = ItemCardDef(
    guid="d1f44010-4fbc-5195-be78-de8b65fb1949",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousDrill.Name",
    display_name="Dangerous Drill",
    searchable_by=["Dangerous Drill", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=dangerous_drill,
            condition=dangerous_drill_condition,
        )
