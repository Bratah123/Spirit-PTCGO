from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    professor_elms_lecture,
)

card = SupporterCardDef(
    guid="b871a385-b9f5-5edf-bfb5-1cd576a90fcb",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsLecture.Name",
    display_name="Professor Elm's Lecture",
    searchable_by=["Professor Elm's Lecture", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    effect=professor_elms_lecture
)
