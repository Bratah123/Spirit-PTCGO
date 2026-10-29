from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    adventure_bag,
)

card = ItemCardDef(
    guid="31a033b8-abc4-5eb5-b8ee-db577981eaa5",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventureBag.Name",
    display_name="Adventure Bag",
    searchable_by=["Adventure Bag", "Item"],
    subtypes=["Item"],
    collector_number=228,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    effect=adventure_bag
)
