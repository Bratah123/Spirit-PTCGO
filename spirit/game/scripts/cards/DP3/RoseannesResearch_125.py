"""Roseanne's Research (DP3 #125)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import roseannes_research

card = SupporterCardDef(
    guid="08e613b5-6a9e-5b82-ab58-d87070f8b593",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseannesResearch.Name",
    display_name="Roseanne's Research",
    searchable_by=["Roseanne's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=125,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=roseannes_research(),
)
