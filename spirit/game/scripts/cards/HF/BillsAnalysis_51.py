from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    bills_analysis,
)

card = SupporterCardDef(
    guid="77d98f91-a8a6-5b96-99ca-7162fa1d19d3",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsAnalysis.Name",
    display_name="Bill's Analysis",
    searchable_by=["Bill's Analysis", "Supporter"],
    subtypes=["Supporter"],
    collector_number=51,
    set_code="HF",
    rarity=Rarities.Rare,
    effect=bills_analysis,
)
