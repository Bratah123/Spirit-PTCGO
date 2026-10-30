"""Cynthia's Feelings (DP6 #131)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import cynthias_feelings

card = SupporterCardDef(
    guid="51f05ec6-3d35-56d4-b3d2-9d30a7677fc3",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasFeelings.Name",
    display_name="Cynthia's Feelings",
    searchable_by=["Cynthia's Feelings", "Supporter"],
    subtypes=["Supporter"],
    collector_number=131,
    set_code="DP6",
    rarity=Rarities.Uncommon,
    effect=cynthias_feelings(),
)
