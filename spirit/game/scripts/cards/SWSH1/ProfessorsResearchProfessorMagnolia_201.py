from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1ac4130a-464a-5eb2-99d8-2884b9afb1ac",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorMagnolia.Name",
    display_name="Professor's Research (Professor Magnolia)",
    searchable_by=["Professor's Research (Professor Magnolia)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=201,
    set_code="SWSH1",
    rarity=Rarities.RareUltra,
    effect=professors_research
)
