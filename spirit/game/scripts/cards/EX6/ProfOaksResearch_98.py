from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import oaks_research

card = SupporterCardDef(
    guid="55151212-9092-5d92-ab11-d9606709cc4c",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfOaksResearch.Name",
    display_name="Prof. Oak's Research",
    searchable_by=["Prof. Oak's Research", "Professor Oak's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    effect=oaks_research,
)
