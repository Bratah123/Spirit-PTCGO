from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    adventure_bag,
)

card = ItemCardDef(
    guid="5767eea9-0589-5ace-b7de-4fb230fa6a06",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventureBag.Name",
    display_name="Adventure Bag",
    searchable_by=["Adventure Bag", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=adventure_bag
)
