from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    judge_whistle,
    judge_whistle_condition,
)

card = ItemCardDef(
    guid="ad58126a-a0ae-58e9-a4ec-db600586365d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JudgeWhistle.Name",
    display_name="Judge Whistle",
    searchable_by=["Judge Whistle", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=judge_whistle,
            condition=judge_whistle_condition,
        )
