"""Time-Space Distortion (DP2 #124)."""
from spirit.game.attributes import Rarities
from spirit.game.data_utils import ItemCardDef
from spirit.game.card_effects.dp import time_space_distortion

card = ItemCardDef(
    guid="9de91e32-e439-5bdf-b3b4-ff547d4ddbef",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeSpaceDistortion.Name",
    display_name="Time-Space Distortion",
    searchable_by=["Time-Space Distortion", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="DP2",
    rarity=Rarities.RareSecret,
    effect=time_space_distortion(),
)
