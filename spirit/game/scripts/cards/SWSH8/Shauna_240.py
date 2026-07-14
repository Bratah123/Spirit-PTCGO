from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw

card = SupporterCardDef(
    guid="d0cb09b9-79ce-5b4f-af92-78a2e371c8b1",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Shauna.Name",
    display_name="Shauna",
    searchable_by=["Shauna", "Supporter"],
    subtypes=["Supporter"],
    collector_number=240,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=shuffle_hand_into_deck_draw(5)
)
