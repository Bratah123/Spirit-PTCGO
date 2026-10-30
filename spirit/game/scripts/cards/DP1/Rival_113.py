"""Wired DP1 trainer."""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import rival_supporter

card = SupporterCardDef(
    guid="64b27ae8-3da3-5f08-a38e-c7995762fb40",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rival.Name",
    display_name="Rival",
    searchable_by=["Rival", "Supporter"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=rival_supporter()
)
