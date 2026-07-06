from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9d2a37c6-5431-5fbf-9293-4047c95eb3c3",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorMagnolia.Name",
    display_name="Professor's Research (Professor Magnolia)",
    searchable_by=["Professor's Research (Professor Magnolia)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    effect=professors_research
)
