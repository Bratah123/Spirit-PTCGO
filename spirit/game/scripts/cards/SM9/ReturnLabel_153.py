from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    return_label,
    return_label_condition,
)

card = ItemCardDef(
    guid="c60ee87a-7414-5475-ab8f-29dfa49dd9bb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReturnLabel.Name",
    display_name="Return Label",
    searchable_by=["Return Label", "Item"],
    subtypes=["Item"],
    collector_number=153,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=return_label,
            condition=return_label_condition,
        )
