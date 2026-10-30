from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import professor_elms_training_method

card = SupporterCardDef(
    guid="66aafb48-0f1b-5a93-94ed-dabde6734c7c",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=professor_elms_training_method,
)
