from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    lt_surges_strategy,
    lt_surges_strategy_condition,
)

card = SupporterCardDef(
    guid="29225ded-583d-5cec-a0c4-0a048aa5a8a0",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesStrategy.Name",
    display_name="Lt. Surge's Strategy",
    searchable_by=["Lt. Surge's Strategy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=60,
    set_code="HF",
    rarity=Rarities.Uncommon,
    condition=lt_surges_strategy_condition,
    effect=lt_surges_strategy
)
