from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card

card = SupporterCardDef(
    guid="416c5e23-c95a-5ec2-865b-d72965f1b66c",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Skyla.Name",
    display_name="Skyla",
    searchable_by=["Skyla", "Supporter"],
    subtypes=["Supporter"],
    collector_number=134,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(is_trainer_card, count=1, minimum=0, reveal=True,
                          prompt='Choose a Trainer card to put into your hand.')
)
