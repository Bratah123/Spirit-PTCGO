from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.session.passives import effective_bench_capacity


def target_whistle_condition(board, player_id):
    opp = next((p for p in board.player_ids if p != player_id), None)
    bench = board.find_player_area(opp, "bench") if opp else None
    discard = board.find_player_area(opp, "discard") if opp else None
    return (bench is not None and len(bench.children) < effective_bench_capacity(board, opp)
            and bool(discard and any(is_basic_pokemon(c) for c in discard.children)))


async def target_whistle(ctx):
    """Put a Basic Pokemon from your opponent's discard pile onto their Bench."""
    cards = [c for c in ctx.discard_pile(ctx.opponent_id) if is_basic_pokemon(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a Basic Pokémon")
    if picks:
        await ctx.bench_pokemon(picks[0])


card = ItemCardDef(
    guid="2ba5e8c2-2986-59c8-936b-af875bdf0431",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TargetWhistleTeamFlareGear.Name",
    display_name="Target Whistle Team Flare Gear",
    searchable_by=["Target Whistle Team Flare Gear", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    effect=target_whistle,
    condition=target_whistle_condition
)
