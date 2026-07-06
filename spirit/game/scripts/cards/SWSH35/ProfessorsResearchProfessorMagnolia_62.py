from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4967081a-8bb8-57c6-8294-f9adbe972576",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearchProfessorMagnolia.Name",
    display_name="Professor's Research (Professor Magnolia)",
    searchable_by=["Professor's Research (Professor Magnolia)", "Supporter"],
    subtypes=["Supporter"],
    collector_number=62,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    effect=professors_research
)
