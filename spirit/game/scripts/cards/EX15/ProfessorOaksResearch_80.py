"""EX15 Dragon Frontiers — Professor Oak's Research."""
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import oaks_research

card = SupporterCardDef(
    guid="d5d9ad67-c5e3-5947-81af-2dadf8e1c5ac",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksResearch.Name",
    display_name="Professor Oak's Research",
    searchable_by=["Professor Oak's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=oaks_research,
)
