from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    beast_ball,
    beast_ball_condition,
)

card = ItemCardDef(
    guid="97afc8bc-4058-5226-a109-58e7ee8cfa6a",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBall.Name",
    display_name="Beast Ball",
    searchable_by=["Beast Ball", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=beast_ball,
    condition=beast_ball_condition,
)
