from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand


def _is_fusion_strike_pokemon(card):
    return is_pokemon_card(card) and "Fusion Strike" in subtypes_for(card.archetype_id)


card = SupporterCardDef(
    guid="1785ebb0-0bb9-5195-a65f-6edae527340e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChiliCilanCress.Name",
    display_name="Chili & Cilan & Cress",
    searchable_by=["Chili & Cilan & Cress", "Supporter", "Fusion Strike"],
    subtypes=["Supporter", "Fusion Strike"],
    collector_number=227,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        _is_fusion_strike_pokemon, count=3, reveal=True,
        prompt="Choose up to 3 Fusion Strike Pokémon.",
    ),
)
