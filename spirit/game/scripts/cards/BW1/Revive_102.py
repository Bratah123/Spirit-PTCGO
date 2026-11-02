from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.card_effects.support_common import requires_bench_space, requires_discard


def revive_condition(board, player_id):
    return (
        requires_bench_space(1)(board, player_id)
        and requires_discard(is_basic_pokemon)(board, player_id)
    )


async def revive(ctx):
    """Put a Basic Pokemon from your discard pile onto your Bench."""
    if len(ctx.my_bench()) >= BENCH_CAPACITY:
        return
    candidates = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon from your discard pile to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)


card = ItemCardDef(
    guid="cd12e318-73dd-53d2-ad1f-0b39c092ff6a",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    condition=revive_condition,
    effect=revive,
)
