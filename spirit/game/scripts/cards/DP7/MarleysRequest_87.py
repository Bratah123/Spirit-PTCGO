"""Marley's Request (DP7 #87)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import marleys_request

card = SupporterCardDef(
    guid="95179315-1d39-5ea7-a6f3-90fbb0befae9",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarleysRequest.Name",
    display_name="Marley's Request",
    searchable_by=["Marley's Request", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    effect=marleys_request(),
)
