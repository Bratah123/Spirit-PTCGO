from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    net_ball,
)

card = ItemCardDef(
    guid="890e0328-debc-58b4-ba61-808a59bf0516",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NetBall.Name",
    display_name="Net Ball",
    searchable_by=["Net Ball", "Item"],
    subtypes=["Item"],
    collector_number=234,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    effect=net_ball
)
