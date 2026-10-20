from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_trainer_card

card = SupporterCardDef(
    guid="dbe1e295-9fae-5436-9b5d-40beaa8b05a1",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Skyla.Name",
    display_name="Skyla",
    searchable_by=["Skyla", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    effect=search_to_hand(is_trainer_card, count=1, minimum=0, reveal=True,
                          prompt='Choose a Trainer card to put into your hand.')
)
