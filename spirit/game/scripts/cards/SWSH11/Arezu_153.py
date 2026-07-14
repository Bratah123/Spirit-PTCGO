from spirit.game.data_utils import SupporterCardDef, has_rule_box
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_evolution_pokemon


def _arezu_predicate(card):
    return is_evolution_pokemon(card) and not has_rule_box(
        getattr(card, "archetype_id", None) or ""
    )


card = SupporterCardDef(
    guid="0596d5c6-2a6a-5ea0-8af2-9e80f8d1561f",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Arezu.Name",
    display_name="Arezu",
    searchable_by=["Arezu", "Supporter"],
    subtypes=["Supporter"],
    collector_number=153,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _arezu_predicate, count=3,
        prompt="Choose up to 3 Evolution Pokémon that don't have a Rule Box.",
    ),
)
