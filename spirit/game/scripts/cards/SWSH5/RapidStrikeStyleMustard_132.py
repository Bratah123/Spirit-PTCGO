from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def _last_card_in_hand(board, player_id):
    hand = board.find_player_area(player_id, "hand")
    return hand is not None and len(hand.children) == 1


def _is_rapid_strike_pokemon(card):
    return is_pokemon_card(card) and "Rapid Strike" in subtypes_for(card.archetype_id)


async def _rapid_strike_style_mustard(ctx):
    """Put a Rapid Strike Pokemon from your discard pile onto your Bench. If you do, draw 5 cards."""
    candidates = [c for c in ctx.discard_pile() if _is_rapid_strike_pokemon(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Put a Rapid Strike Pokémon from your discard pile onto your Bench",
    )
    if not picks:
        return
    if await ctx.bench_pokemon(picks[0]):
        await ctx.draw_cards(5)


card = SupporterCardDef(
    guid="4dceb2bf-4206-5709-a2ef-e167507a1ded",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RapidStrikeStyleMustard.Name",
    display_name="Rapid Strike Style Mustard",
    searchable_by=["Rapid Strike Style Mustard", "Supporter", "Rapid Strike"],
    subtypes=["Supporter", "Rapid Strike"],
    collector_number=132,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    effect=_rapid_strike_style_mustard,
    condition=_last_card_in_hand,
)
