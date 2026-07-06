from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="79600ad3-5c79-5840-af16-9cd0998cb490",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorsResearch.Name",
    display_name="Professor's Research",
    searchable_by=["Professor's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=60,
    set_code="SWSH45",
    rarity=Rarities.Rare,
    effect=professors_research
)
