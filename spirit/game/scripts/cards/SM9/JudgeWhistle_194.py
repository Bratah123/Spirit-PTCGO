from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    judge_whistle,
    judge_whistle_condition,
)

card = ItemCardDef(
    guid="86f89d7a-66b7-5155-bf49-5f7aa8fe4274",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JudgeWhistle.Name",
    display_name="Judge Whistle",
    searchable_by=["Judge Whistle", "Item"],
    subtypes=["Item"],
    collector_number=194,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    effect=judge_whistle,
            condition=judge_whistle_condition,
        )
