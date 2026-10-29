from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    morgan,
    morgan_condition,
)

card = SupporterCardDef(
    guid="a7ad922d-1bd6-5fcd-b378-830c4699c2af",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name",
    display_name="Morgan",
    searchable_by=["Morgan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=morgan,
            condition=morgan_condition,
        )
