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
    guid="d8b2f21a-fa75-59be-8458-4822b9066cd8",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamSkullGrunt.Name",
    display_name="Team Skull Grunt",
    searchable_by=["Team Skull Grunt", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=_team_skull_grunt,
    condition=_grunt_condition
)
