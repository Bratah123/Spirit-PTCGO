from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    electropower,
)

card = ItemCardDef(
    guid="7a21cce4-8939-5a11-b9d8-66f8ee0776bb",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electropower.Name",
    display_name="Electropower",
    searchable_by=["Electropower", "Item"],
    subtypes=["Item"],
    collector_number=232,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    effect=electropower
)
