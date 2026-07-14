from spirit.game.data_utils import ItemCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard


def _is_single_strike_energy(card):
    return "Single Strike" in subtypes_for(card.archetype_id)


card = ItemCardDef(
    guid="83364a3b-69b7-5dca-95ca-8d8827b32d34",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UrnofVitality.Name",
    display_name="Urn of Vitality",
    searchable_by=["Urn of Vitality", "Item", "Single Strike"],
    subtypes=["Item", "Single Strike"],
    collector_number=229,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    condition=requires_discard(_is_single_strike_energy),
    effect=recover_from_discard(
        _is_single_strike_energy, count=2, minimum=1, reveal=False, to="deck_shuffle",
        prompt="Choose up to 2 Single Strike Energy cards to shuffle into your deck.",
    ),
)
