from spirit.game.data_utils import ItemCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.session.passives import trainer_play_blocked


def greedy_dice_playable(board, player_id):
    """Greedy Dice never plays from hand: its window is the prize-take prompt."""
    return False


async def greedy_dice(ctx):
    """Flip a coin. If heads, take 1 more Prize card."""
    results = await ctx.flip_coins(1, "Greedy Dice")
    if results and results[0]:
        await ctx.take_prizes(1)


async def greedy_dice_prize_window(ctx):
    """Taken as a face-down Prize: you may play it before it settles in hand."""
    ctx.suppress_announce = True
    board, pid = ctx.board, ctx.player_id
    pile = board.find_player_area(pid, "prizePile")
    if not pile or not pile.children:
        return
    if trainer_play_blocked(board, pid, ctx.source):
        return
    if not await ctx.ask_yes_no("Play Greedy Dice? Flip a coin. If heads, take 1 more Prize card."):
        return
    await ctx.session._execute_play_trainer(pid, ctx.source)


card = ItemCardDef(
    guid="648dacce-e658-5a62-8070-3236c9551900",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GreedyDice.Name",
    display_name="Greedy Dice",
    searchable_by=["Greedy Dice", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY11",
    rarity=Rarities.Uncommon,
    effect=greedy_dice,
    condition=greedy_dice_playable,
    abilities=[
        Ability(
            title="Greedy Dice",
            game_text="You can play this card only if you took it as a face-down Prize card, before you put it into your hand.",
            trigger=Triggers.ON_TAKEN_AS_PRIZE,
            effect=greedy_dice_prize_window,
        ),
    ]
)
