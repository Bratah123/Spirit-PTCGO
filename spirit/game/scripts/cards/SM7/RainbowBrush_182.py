from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    rainbow_brush,
    rainbow_brush_condition,
)

card = ItemCardDef(
    guid="fa9c4885-6550-5be3-a9a4-fb34bdb48261",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RainbowBrush.Name",
    display_name="Rainbow Brush",
    searchable_by=["Rainbow Brush", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    effect=rainbow_brush,
    condition=rainbow_brush_condition,
)
