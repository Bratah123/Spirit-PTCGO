from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import professor_elms_training_method

card = SupporterCardDef(
    guid="ca1075c3-c906-5bc9-ba32-0707c6636521",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    effect=professor_elms_training_method,
)
