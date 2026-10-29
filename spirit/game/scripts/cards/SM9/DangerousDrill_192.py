from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    dangerous_drill,
    dangerous_drill_condition,
)

card = ItemCardDef(
    guid="e2576c95-282f-5b91-abb8-dbae0cc31809",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DangerousDrill.Name",
    display_name="Dangerous Drill",
    searchable_by=["Dangerous Drill", "Item"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=dangerous_drill,
            condition=dangerous_drill_condition,
        )
