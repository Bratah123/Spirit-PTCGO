from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import mr_stones_project

card = SupporterCardDef(
    guid="44642344-d658-5304-beff-b358f79f774b",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrStonesProject.Name",
    display_name="Mr. Stone's Project",
    searchable_by=["Mr. Stone's Project", "Supporter"],
    subtypes=["Supporter"],
    collector_number=88,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    effect=mr_stones_project,
)
