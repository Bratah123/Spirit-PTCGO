"""Wired DP1 trainer."""

from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import rival_supporter

card = SupporterCardDef(
    guid="7469ca89-93f5-564b-9dc6-e2edd08045ca",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rival.Name",
    display_name="Rival",
    searchable_by=["Rival", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=rival_supporter()
)
