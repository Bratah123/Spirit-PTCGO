from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm12 import professor_oaks_setup, professor_oaks_setup_condition

card = SupporterCardDef(
    guid="4d13404d-e3ba-599c-9796-9bd2c3ac4808",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksSetup.Name",
    display_name="Professor Oak's Setup",
    searchable_by=["Professor Oak's Setup", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    effect=professor_oaks_setup, condition=professor_oaks_setup_condition,
)
