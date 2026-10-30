"""Snowpoint Temple (DP6 #134)."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import snowpoint_temple_passive

card = StadiumCardDef(
    guid="f349fdc6-52b6-50d8-a701-0234e66b83f0",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SnowpointTemple.Name",
    display_name="Snowpoint Temple",
    searchable_by=["Snowpoint Temple", "Stadium"],
    subtypes=["Stadium"],
    collector_number=134,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    passive=snowpoint_temple_passive(),
)
