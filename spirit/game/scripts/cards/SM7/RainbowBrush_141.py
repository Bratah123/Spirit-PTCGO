from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    rainbow_brush,
    rainbow_brush_condition,
)

card = ItemCardDef(
    guid="e52193d6-c1c9-5bf1-910b-2786a41ef753",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RainbowBrush.Name",
    display_name="Rainbow Brush",
    searchable_by=["Rainbow Brush", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=rainbow_brush,
    condition=rainbow_brush_condition,
)
