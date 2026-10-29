from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    ingo_emmet,
)

card = SupporterCardDef(
    guid="0f5a1f20-cd44-578b-9b9d-a1c8481903b5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IngoEmmet.Name",
    display_name="Ingo & Emmet",
    searchable_by=["Ingo & Emmet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    effect=ingo_emmet,
)
