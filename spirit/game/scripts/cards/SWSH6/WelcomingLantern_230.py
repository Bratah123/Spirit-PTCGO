from spirit.game.data_utils import ItemCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.session.effects import is_supporter_card


def _is_single_strike_supporter(card):
    return is_supporter_card(card) and "Single Strike" in subtypes_for(card.archetype_id)


card = ItemCardDef(
    guid="0e2e453f-ac42-5da4-be1c-26ecea0a0b34",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WelcomingLantern.Name",
    display_name="Welcoming Lantern",
    searchable_by=["Welcoming Lantern", "Item", "Single Strike"],
    subtypes=["Item", "Single Strike"],
    collector_number=230,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    condition=requires_discard(_is_single_strike_supporter),
    effect=recover_from_discard(
        _is_single_strike_supporter, count=1, minimum=1, reveal=False, to="hand",
        prompt="Choose a Single Strike Supporter card from your discard pile.",
    ),
)
