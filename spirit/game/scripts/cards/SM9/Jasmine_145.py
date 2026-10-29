from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    jasmine,
)

card = SupporterCardDef(
    guid="cde7cd61-daf1-5a13-8cc7-0440b28d8ca5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jasmine.Name",
    display_name="Jasmine",
    searchable_by=["Jasmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=jasmine,
)
