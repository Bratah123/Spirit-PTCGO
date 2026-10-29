from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    faba,
    faba_condition,
)

card = SupporterCardDef(
    guid="19b3fbda-0050-5089-b588-306b9114aec0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Faba.Name",
    display_name="Faba",
    searchable_by=["Faba", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=faba,
    condition=faba_condition,
)
