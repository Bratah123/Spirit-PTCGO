from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    custom_catcher,
)

card = ItemCardDef(
    guid="5a24ef95-4cb6-54f6-bc94-febcd8d2dc2b",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CustomCatcher.Name",
    display_name="Custom Catcher",
    searchable_by=["Custom Catcher", "Item"],
    subtypes=["Item"],
    collector_number=171,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=custom_catcher
)
