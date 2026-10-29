from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    kahili,
    kahili_condition,
)

card = SupporterCardDef(
    guid="aa3d3ea1-bbe9-52c8-bd17-edbd6e89b18c",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kahili.Name",
    display_name="Kahili",
    searchable_by=["Kahili", "Supporter"],
    subtypes=["Supporter"],
    collector_number=179,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=kahili,
    condition=kahili_condition,
)
