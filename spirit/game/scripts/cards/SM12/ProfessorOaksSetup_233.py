from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import professor_oaks_setup, professor_oaks_setup_condition

card = SupporterCardDef(
    guid="aafdd31e-3a3b-58fa-a406-3eb3bd99f3ab",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksSetup.Name",
    display_name="Professor Oak's Setup",
    searchable_by=["Professor Oak's Setup", "Supporter"],
    subtypes=["Supporter"],
    collector_number=233,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    effect=professor_oaks_setup, condition=professor_oaks_setup_condition,
)
