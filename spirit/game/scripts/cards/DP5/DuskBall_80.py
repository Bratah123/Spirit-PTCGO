"""Dusk Ball (DP2 #110)."""
from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.card_effects.dp import dusk_ball

card = ItemCardDef(
    guid="43f0187a-fe1f-5ec4-ac49-dbf856ec752a",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=dusk_ball(),
)
