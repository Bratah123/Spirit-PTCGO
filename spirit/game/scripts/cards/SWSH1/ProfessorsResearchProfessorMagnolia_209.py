from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d7ac94d8-b0af-50f0-b097-fcd6e671d9ae",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorMagnolia.Name",
    display_name="Professor's Research (Professor Magnolia)",
    searchable_by=["Professor's Research (Professor Magnolia)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SWSH1",
    rarity=Rarities.RareRainbow,
    effect=professors_research
)
