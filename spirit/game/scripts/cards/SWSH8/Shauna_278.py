from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw

card = SupporterCardDef(
    guid="bef5ea69-139c-59e3-b17a-767aa89ff165",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=278,
    set_code="SWSH8",
    rarity=Rarities.RareRainbow,
    effect=shuffle_hand_into_deck_draw(5)
)
