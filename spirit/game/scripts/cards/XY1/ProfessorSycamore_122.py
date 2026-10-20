from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import professors_research

card = SupporterCardDef(
    guid="0eec28a7-2241-57ec-87ca-469cac9aa9db",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorSycamore.Name",
    display_name="Professor Sycamore",
    searchable_by=["Professor Sycamore", "Supporter"],
    subtypes=["Supporter"],
    collector_number=122,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=professors_research
)
