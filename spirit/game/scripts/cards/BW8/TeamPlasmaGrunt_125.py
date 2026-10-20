from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_team_plasma_card


def _grunt_condition(board, player_id, card=None):
    hand = board.find_player_area(player_id, "hand")
    return any(is_team_plasma_card(c) for c in (hand.children if hand else []) if c is not card)


async def team_plasma_grunt(ctx):
    """Discard a Team Plasma card from your hand (required). Draw 4 cards."""
    gone = await ctx.discard_from_hand(1, minimum=1, predicate=is_team_plasma_card,
                                       prompt="Discard a Team Plasma card")
    if gone:
        await ctx.draw_cards(4)


card = SupporterCardDef(
    guid="2c39126b-92c3-5ab9-96a0-55801cdea99b",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamPlasmaGrunt.Name",
    display_name="Team Plasma Grunt",
    searchable_by=["Team Plasma Grunt", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=125,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=team_plasma_grunt,
    condition=_grunt_condition
)
