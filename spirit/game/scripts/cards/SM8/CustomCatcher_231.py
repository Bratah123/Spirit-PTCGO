from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    custom_catcher,
)

card = ItemCardDef(
    guid="af6f9c85-6eac-5492-83c8-46cc0089095f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CustomCatcher.Name",
    display_name="Custom Catcher",
    searchable_by=["Custom Catcher", "Item"],
    subtypes=["Item"],
    collector_number=231,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    effect=custom_catcher
)
