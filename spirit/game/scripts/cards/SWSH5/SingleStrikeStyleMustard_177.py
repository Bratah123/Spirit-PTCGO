from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_bench


def _last_card_in_hand(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) == 1


def _is_single_strike_pokemon(card):
    return is_pokemon_card(card) and "Single Strike" in subtypes_for(card.archetype_id)


async def _draw_five(ctx, benched):
    await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="15d914ee-db10-5f19-aa8d-ce90ebd3b3e7",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SingleStrikeStyleMustard.Name",
    display_name="Single Strike Style Mustard",
    searchable_by=["Single Strike Style Mustard", "Supporter", "Single Strike"],
    subtypes=["Supporter", "Single Strike"],
    collector_number=177,
    set_code="SWSH5",
    rarity=Rarities.RareRainbow,
    condition=_last_card_in_hand,
    effect=search_to_bench(
        _is_single_strike_pokemon, count=1, then=_draw_five,
        prompt="Choose a Single Strike Pokémon to put onto your Bench.",
    ),
)
