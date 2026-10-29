from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    morgan,
    morgan_condition,
)

card = SupporterCardDef(
    guid="b04c3743-5bbe-51cf-8a7a-da1c7b7beef7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name",
    display_name="Morgan",
    searchable_by=["Morgan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=morgan,
            condition=morgan_condition,
        )
