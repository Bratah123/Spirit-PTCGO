from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    lure_ball,
    lure_ball_condition,
)

card = ItemCardDef(
    guid="ae5aff8d-6e25-5337-be44-b61d399090c0",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureBall.Name",
    display_name="Lure Ball",
    searchable_by=["Lure Ball", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    effect=lure_ball,
    condition=lure_ball_condition,
)
