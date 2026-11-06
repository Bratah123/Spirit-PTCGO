from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.ecard import is_ball_trainer


card = SupporterCardDef(
    guid="bf4491d5-d58a-51f0-a8a6-58513ca7244e",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=121,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        is_ball_trainer, count=2, minimum=0, reveal=True,
        prompt="Choose up to 2 Trainer cards with Ball in their names.",
    ),
)
