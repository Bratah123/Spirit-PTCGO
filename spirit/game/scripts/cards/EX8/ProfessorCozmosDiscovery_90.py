from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import professor_cozmos_discovery

card = SupporterCardDef(
    guid="b9aaee14-e388-5c7b-8376-c5529b761d6f",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorCozmosDiscovery.Name",
    display_name="Professor Cozmo's Discovery",
    searchable_by=["Professor Cozmo's Discovery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    effect=professor_cozmos_discovery,
)
