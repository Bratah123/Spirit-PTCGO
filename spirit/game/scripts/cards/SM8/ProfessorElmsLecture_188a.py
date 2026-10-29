from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    professor_elms_lecture,
)

card = SupporterCardDef(
    guid="77a3fea0-b17b-573f-9dbd-2f80f71c884d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsLecture.Name",
    display_name="Professor Elm's Lecture",
    searchable_by=["Professor Elm's Lecture", "Supporter"],
    subtypes=["Supporter"],
    collector_number=239,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=professor_elms_lecture
)
