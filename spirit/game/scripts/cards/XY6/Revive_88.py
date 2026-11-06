from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def revive_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    bench = board.find_player_area(player_id, "bench")
    return bool(discard) and any(is_basic_pokemon(c) for c in discard.children) \
        and bench is not None and len(bench.children) < effective_bench_capacity(board, player_id)


async def revive(ctx):
    """Put a Basic Pokemon from your discard pile onto your Bench."""
    pool = [c for c in ctx.discard_pile() if is_basic_pokemon(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Pokémon")
        if picks:
            await ctx.bench_pokemon(picks[0])


card = ItemCardDef(
    guid="542cc576-c475-517e-bd7c-204db9742644",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=revive,
    condition=revive_condition
)
