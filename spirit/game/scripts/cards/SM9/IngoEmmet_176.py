from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm9 import (
    ingo_emmet,
)

card = SupporterCardDef(
    guid="a8d45f54-163a-5ded-a20f-a0ab79d1b2f8",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IngoEmmet.Name",
    display_name="Ingo & Emmet",
    searchable_by=["Ingo & Emmet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    effect=ingo_emmet,
)
