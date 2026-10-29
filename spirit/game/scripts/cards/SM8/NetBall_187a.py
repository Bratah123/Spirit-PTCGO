from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    net_ball,
)

card = ItemCardDef(
    guid="30d002e9-0142-50bb-9e5d-5142c80afa2f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NetBall.Name",
    display_name="Net Ball",
    searchable_by=["Net Ball", "Item"],
    subtypes=["Item"],
    collector_number=238,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=net_ball
)
