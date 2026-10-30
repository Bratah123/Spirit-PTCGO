"""Mom's Kindness (DP5 #83)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import moms_kindness

card = SupporterCardDef(
    guid="b9049447-56cf-5789-a078-177bfe40243d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MomsKindness.Name",
    display_name="Mom's Kindness",
    searchable_by=["Mom's Kindness", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    effect=moms_kindness(),
)
