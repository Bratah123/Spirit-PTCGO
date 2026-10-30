from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card, _other_player


def _grunt_condition(board, player_id):
    hand = board.find_player_area(_other_player(board, player_id), "hand")
    return bool(hand and hand.children)


async def _team_skull_grunt(ctx):
    """Your opponent reveals their hand. Discard 2 Energy cards from it."""
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    energies = [c for c in hand if is_energy_card(c)]
    n = min(2, len(energies))
    if n:
        picks = await ctx.choose_cards(energies, n, minimum=n, display_cards=hand,
                                       prompt="Choose 2 Energy cards to discard")
        if picks:
            await ctx.discard_cards(picks)


card = SupporterCardDef(
    guid="f720cf14-1b8b-5fff-a6c5-f214c017a59e",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamSkullGrunt.Name",
    display_name="Team Skull Grunt",
    searchable_by=["Team Skull Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    effect=_team_skull_grunt,
    condition=_grunt_condition
)
