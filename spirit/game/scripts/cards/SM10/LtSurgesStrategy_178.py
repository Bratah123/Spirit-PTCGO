from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    lt_surges_strategy,
    lt_surges_strategy_condition,
)

card = SupporterCardDef(
    guid="4adcd302-f528-5c6e-afe4-653e842e3ee5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesStrategy.Name",
    display_name="Lt. Surge's Strategy",
    searchable_by=["Lt. Surge's Strategy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    condition=lt_surges_strategy_condition,
    effect=lt_surges_strategy
)
