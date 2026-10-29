from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    faba,
    faba_condition,
)

card = SupporterCardDef(
    guid="d6c7c051-7ae4-56d7-b392-dae6d04b6062",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Faba.Name",
    display_name="Faba",
    searchable_by=["Faba", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    effect=faba,
    condition=faba_condition,
)
