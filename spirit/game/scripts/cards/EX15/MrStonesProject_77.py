from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import mr_stones_project

card = SupporterCardDef(
    guid="405bfbf7-8529-50a7-a5c2-aa09a0d86950",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrStonesProject.Name",
    display_name="Mr. Stone's Project",
    searchable_by=["Mr. Stone's Project", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    effect=mr_stones_project,
)
