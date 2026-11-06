from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_team_plasma_card


def _shadow_triad_condition(board, player_id, card=None):
    discard = board.find_player_area(player_id, "discard")
    return any(is_team_plasma_card(c) for c in (discard.children if discard else []))


async def shadow_triad(ctx):
    """Put a Team Plasma card from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if is_team_plasma_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Team Plasma card to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = SupporterCardDef(
    guid="459ba560-5f1b-5e37-8d5f-10648eb33d5d",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShadowTriad.Name",
    display_name="Shadow Triad",
    searchable_by=["Shadow Triad", "Supporter", "Team Plasma"],
    subtypes=["Supporter", "Team Plasma"],
    collector_number=102,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    effect=shadow_triad,
    condition=_shadow_triad_condition
)
