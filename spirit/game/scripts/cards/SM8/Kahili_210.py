from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    kahili,
    kahili_condition,
)

card = SupporterCardDef(
    guid="b7f0356f-1b0d-52b8-ad1b-d1333a43d713",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kahili.Name",
    display_name="Kahili",
    searchable_by=["Kahili", "Supporter"],
    subtypes=["Supporter"],
    collector_number=210,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    effect=kahili,
    condition=kahili_condition,
)
