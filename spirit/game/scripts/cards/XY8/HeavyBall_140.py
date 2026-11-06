from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


def _retreat_3_or_more(card):
    return is_pokemon_card(card) and (card.get_attribute(AttrID.RETREAT_COST) or 0) >= 3


card = ItemCardDef(
    guid="ce38bce3-5702-5c19-991b-8dbde226fcea",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeavyBall.Name",
    display_name="Heavy Ball",
    searchable_by=["Heavy Ball", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _retreat_3_or_more, count=1, reveal=True,
        prompt="Choose a Pok\u00e9mon with a Retreat Cost of 3 or more to put into your hand.",
    )
)
