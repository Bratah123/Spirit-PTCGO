from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _opponent_id(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def echoing_horn_condition(board, player_id):
    opponent = _opponent_id(board, player_id)
    if not opponent:
        return False
    discard = board.find_player_area(opponent, "discard")
    if not discard or not any(is_basic_pokemon(c) for c in discard.children):
        return False
    bench = board.find_player_area(opponent, "bench")
    return bench is not None and len(bench.children) < effective_bench_capacity(board, opponent)


async def echoing_horn(ctx):
    """Put a Basic Pokemon from your opponent's discard pile onto their Bench."""
    candidates = [c for c in ctx.discard_pile(ctx.opponent_id) if is_basic_pokemon(c)]
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your opponent's discard pile to put onto their Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)


card = ItemCardDef(
    guid="0f436eba-266c-5569-9f0e-7bbf3e369626",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EchoingHorn.Name",
    display_name="Echoing Horn",
    searchable_by=["Echoing Horn", "Item", "Rapid Strike"],
    subtypes=["Item", "Rapid Strike"],
    collector_number=225,
    set_code="SWSH6",
    rarity=Rarities.RareSecret,
    effect=echoing_horn,
    condition=echoing_horn_condition,
)
