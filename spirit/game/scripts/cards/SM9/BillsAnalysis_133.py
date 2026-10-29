from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    bills_analysis,
)

card = SupporterCardDef(
    guid="60363378-785f-56fb-9abe-55a1e4219a06",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsAnalysis.Name",
    display_name="Bill's Analysis",
    searchable_by=["Bill's Analysis", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    effect=bills_analysis,
)
