from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    lost_blender,
    lost_blender_condition,
)

card = ItemCardDef(
    guid="b7c65064-dd78-5aa1-8e7b-2a0ce0dc14cc",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostBlender.Name",
    display_name="Lost Blender",
    searchable_by=["Lost Blender", "Item"],
    subtypes=["Item"],
    collector_number=233,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    effect=lost_blender,
    condition=lost_blender_condition,
)
