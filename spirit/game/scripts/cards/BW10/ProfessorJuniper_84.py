from spirit.game.card_effects.trainers import professors_research
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="aa616cba-591d-50b8-bde4-e926885932c5",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorJuniper.Name",
    display_name="Professor Juniper",
    searchable_by=["Professor Juniper", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    effect=professors_research,
)
