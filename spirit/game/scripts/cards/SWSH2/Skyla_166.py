from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_trainer_card
from spirit.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="0bd34f56-2959-5a7f-88aa-ba000a36e9b4",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Skyla.Name",
    display_name="Skyla",
    searchable_by=["Skyla", "Supporter"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_trainer_card, count=1, reveal=True, prompt="Choose a Trainer card."),
)
