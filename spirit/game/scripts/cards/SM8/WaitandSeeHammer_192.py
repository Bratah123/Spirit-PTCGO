from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    wait_and_see_hammer,
    wait_and_see_hammer_condition,
)

card = ItemCardDef(
    guid="47ea1480-4391-564a-bf66-9431401a4f86",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaitandSeeHammer.Name",
    display_name="Wait and See Hammer",
    searchable_by=["Wait and See Hammer", "Item"],
    subtypes=["Item"],
    collector_number=192,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=wait_and_see_hammer,
    condition=wait_and_see_hammer_condition,
)
