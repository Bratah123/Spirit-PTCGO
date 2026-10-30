"""Lake Boundary (DP2 #112)."""
from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import lake_boundary_passive

card = StadiumCardDef(
    guid="e58275a2-d98b-5056-acea-4a4170041551",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LakeBoundary.Name",
    display_name="Lake Boundary",
    searchable_by=["Lake Boundary", "Stadium"],
    subtypes=["Stadium"],
    collector_number=112,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    passive=lake_boundary_passive(),
)
