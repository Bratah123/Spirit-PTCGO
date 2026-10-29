from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    net_ball,
)

card = ItemCardDef(
    guid="5e41116c-5c19-58bb-9c05-9fa66e3aa013",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NetBall.Name",
    display_name="Net Ball",
    searchable_by=["Net Ball", "Item"],
    subtypes=["Item"],
    collector_number=187,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=net_ball
)
