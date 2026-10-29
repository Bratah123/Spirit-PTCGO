from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    sightseer,
    sightseer_condition,
)

card = SupporterCardDef(
    guid="ed9c6b83-624d-5988-8e78-05bc8da629d2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sightseer.Name",
    display_name="Sightseer",
    searchable_by=["Sightseer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=sightseer,
    condition=sightseer_condition,
)
