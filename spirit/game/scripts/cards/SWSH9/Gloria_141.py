from spirit.game.data_utils import SupporterCardDef, has_rule_box
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_basic_pokemon


def _no_rule_box_basic(card) -> bool:
    return is_basic_pokemon(card) and not has_rule_box(card.archetype_id)


card = SupporterCardDef(
    guid="043fc87d-233f-5a1b-8e38-ab7aecc0154c",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gloria.Name",
    display_name="Gloria",
    searchable_by=["Gloria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    effect=search_to_bench(
        _no_rule_box_basic, count=3,
        prompt="Choose up to 3 Basic Pokémon without a Rule Box to put onto your Bench.",
    ),
)
