from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professors_research

card = SupporterCardDef(
    guid="700c6bb8-8dc1-5c95-b345-86441d8f3fb4",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorJuniper.Name",
    display_name="Professor Juniper",
    searchable_by=["Professor Juniper", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    effect=professors_research
)
