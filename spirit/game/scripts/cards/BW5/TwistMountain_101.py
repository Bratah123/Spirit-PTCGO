from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_restored_pokemon
from spirit.game.session.passives import effective_bench_capacity


def _twist_mountain_condition(board, player_id, stadium=None):
    hand = board.find_player_area(player_id, "hand")
    bench = board.find_player_area(player_id, "bench")
    if not hand or bench is None:
        return False
    if len(bench.children) >= effective_bench_capacity(board, player_id):
        return False
    return any(is_restored_pokemon(c) for c in hand.children)


async def twist_mountain(ctx):
    """Flip a coin. If heads, you may play a Restored Pok\u00e9mon from your
    hand onto your Bench."""
    results = await ctx.flip_coins(1, "Twist Mountain")
    if not results or not results[0]:
        return
    restored = [c for c in ctx.hand() if is_restored_pokemon(c)]
    if not restored:
        return
    picks = await ctx.choose_cards(restored, 1, minimum=0,
                                   prompt="Choose a Restored Pok\u00e9mon to put onto your Bench")
    if picks:
        await ctx.bench_pokemon(picks[0])


TWIST_MOUNTAIN_ABILITY = Ability(
    title="Twist Mountain",
    game_text="Once during each player's turn, that player may flip a coin. If heads, that player may play a Restored Pok\u00e9mon from their hand onto their Bench.",
    activation=Activations.ONCE_PER_TURN,
    condition=_twist_mountain_condition,
    effect=twist_mountain,
)


card = StadiumCardDef(
    guid="2806afe9-470b-5e2a-97fc-70e5f49720a3",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TwistMountain.Name",
    display_name="Twist Mountain",
    searchable_by=["Twist Mountain", "Stadium"],
    subtypes=["Stadium"],
    collector_number=101,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    ability=TWIST_MOUNTAIN_ABILITY
)
