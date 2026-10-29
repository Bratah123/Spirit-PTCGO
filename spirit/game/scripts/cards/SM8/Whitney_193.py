from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    whitney,
)

card = SupporterCardDef(
    guid="cf211409-753a-597d-8e7c-4dd579656076",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Whitney.Name",
    display_name="Whitney",
    searchable_by=["Whitney", "Supporter"],
    subtypes=["Supporter"],
    collector_number=193,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=whitney
)
