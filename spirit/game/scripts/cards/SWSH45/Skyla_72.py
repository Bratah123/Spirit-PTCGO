from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="41e1b8be-d7c3-5909-837b-321423cc335c",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Skyla.Name",
    display_name="Skyla",
    searchable_by=["Skyla", "Supporter"],
    subtypes=["Supporter"],
    collector_number=72,
    set_code="SWSH45",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_trainer_card, count=1, reveal=True, prompt="Choose a Trainer card."),
)
