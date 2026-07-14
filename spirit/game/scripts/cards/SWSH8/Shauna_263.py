from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw

card = SupporterCardDef(
    guid="8f400edd-55af-5aa8-bede-c92e7244312b",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=263,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    effect=shuffle_hand_into_deck_draw(5)
)
