from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm8 import (
    professor_elms_lecture,
)

card = SupporterCardDef(
    guid="e5c2c6c2-a6eb-5a40-b3fb-258eae3cc6f8",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsLecture.Name",
    display_name="Professor Elm's Lecture",
    searchable_by=["Professor Elm's Lecture", "Supporter"],
    subtypes=["Supporter"],
    collector_number=213,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    effect=professor_elms_lecture
)
