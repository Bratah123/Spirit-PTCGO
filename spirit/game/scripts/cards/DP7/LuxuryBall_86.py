"""Luxury Ball (DP7 #86)."""
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import luxury_ball, luxury_ball_condition

card = ItemCardDef(
    guid="d5c3c385-8cec-58eb-bc2b-aeddcee83f88",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuxuryBall.Name",
    display_name="Luxury Ball",
    searchable_by=["Luxury Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    condition=luxury_ball_condition,
    effect=luxury_ball(),
)
