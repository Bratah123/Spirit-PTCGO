from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    hiker,
    hiker_condition,
)

card = SupporterCardDef(
    guid="6ec9927a-a69f-59e2-871a-6e7277eeb200",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hiker.Name",
    display_name="Hiker",
    searchable_by=["Hiker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="HF",
    rarity=Rarities.RareUltra,
    effect=hiker,
    condition=hiker_condition,
)
