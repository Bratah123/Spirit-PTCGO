from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1217a418-0f3e-5bde-9fc8-2893c76cdd4b",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="PGO",
    rarity=Rarities.RareRainbow,
    effect=professors_research
)
