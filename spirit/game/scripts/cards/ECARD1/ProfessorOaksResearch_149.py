from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw


card = SupporterCardDef(
    guid="8ed08e76-4e36-5cc5-a903-30b4ec0760ba",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksResearch.Name",
    display_name="Professor Oak's Research",
    searchable_by=["Professor Oak's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_into_deck_draw(5),
)
