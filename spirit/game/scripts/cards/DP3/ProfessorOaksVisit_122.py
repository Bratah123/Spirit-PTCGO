"""Professor Oak's Visit (DP3 #122)."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import professor_oaks_visit

card = SupporterCardDef(
    guid="91023469-6138-59fd-ad9f-ad70b3aa872d",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksVisit.Name",
    display_name="Professor Oak's Visit",
    searchable_by=["Professor Oak's Visit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    effect=professor_oaks_visit(),
)
