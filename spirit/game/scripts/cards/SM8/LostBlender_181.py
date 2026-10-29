from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    lost_blender,
    lost_blender_condition,
)

card = ItemCardDef(
    guid="798bfab3-56f4-5135-ae07-45ae52e24f7e",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostBlender.Name",
    display_name="Lost Blender",
    searchable_by=["Lost Blender", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=lost_blender,
    condition=lost_blender_condition,
)
