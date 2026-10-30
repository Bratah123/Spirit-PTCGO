"""Dusk Ball (DP2 #110)."""
from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.card_effects.dp import dusk_ball

card = ItemCardDef(
    guid="29d30129-414d-55d1-90f4-f77f7db81c8f",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item"],
    subtypes=["Item"],
    collector_number=110,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    effect=dusk_ball(),
)
