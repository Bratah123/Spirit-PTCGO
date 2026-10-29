from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    wait_and_see_hammer,
    wait_and_see_hammer_condition,
)

card = ItemCardDef(
    guid="041f6216-a404-59e5-8716-2673b7e51768",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaitandSeeHammer.Name",
    display_name="Wait and See Hammer",
    searchable_by=["Wait and See Hammer", "Item"],
    subtypes=["Item"],
    collector_number=236,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    effect=wait_and_see_hammer,
    condition=wait_and_see_hammer_condition,
)
