from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    whitney,
)

card = SupporterCardDef(
    guid="8c5c5238-a591-51ef-97ce-959a0faadc5a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Whitney.Name",
    display_name="Whitney",
    searchable_by=["Whitney", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    effect=whitney
)
