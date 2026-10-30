from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import professor_cozmos_discovery

card = SupporterCardDef(
    guid="52a71ff9-ebde-56a4-ae5b-665536d8b0f3",
    key="TK2A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorCozmosDiscovery.Name",
    display_name="Professor Cozmo's Discovery",
    searchable_by=["Professor Cozmo's Discovery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=10,
    set_code="TK2A",
    rarity=Rarities.Common,
    effect=professor_cozmos_discovery,
)
