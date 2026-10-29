from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    mixed_herbs,
)

card = ItemCardDef(
    guid="61b59328-f41d-5248-b72a-c0fd4ed8217d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MixedHerbs.Name",
    display_name="Mixed Herbs",
    searchable_by=["Mixed Herbs", "Item"],
    subtypes=["Item"],
    collector_number=184,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=mixed_herbs
)
