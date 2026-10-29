from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    jasmine,
)

card = SupporterCardDef(
    guid="cab8c0f0-2b8d-5bf7-8940-bc54a2b14b24",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jasmine.Name",
    display_name="Jasmine",
    searchable_by=["Jasmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=jasmine,
)
