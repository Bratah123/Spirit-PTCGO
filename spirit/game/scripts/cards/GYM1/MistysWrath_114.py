from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import has_cards_in_deck
from spirit.game.card_effects.support_common import look_at_top


card = ItemCardDef(
    guid="98f60aaa-c7ea-5224-9da1-4051fba17a03",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysWrath.Name",
    display_name="Misty's Wrath",
    searchable_by=["Misty's Wrath"],
    subtypes=[],
    collector_number=114,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    condition=has_cards_in_deck,
    effect=look_at_top(
        7, take=2, rest="discard",
        prompt="Choose 2 of those cards to put into your hand.",
    ),
)
