from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import professor_cozmos_discovery

card = SupporterCardDef(
    guid="0eb2c268-d2d5-5c3d-8cba-f0d0998be3c2",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorCozmosDiscovery.Name",
    display_name="Professor Cozmo's Discovery",
    searchable_by=["Professor Cozmo's Discovery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    effect=professor_cozmos_discovery,
)
