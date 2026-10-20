from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def here_comes_team_rocket(ctx):
    """Each player turns all of their Prize cards face up for the rest of the game."""
    await ctx.turn_prizes_face_up(ctx.player_id)
    await ctx.turn_prizes_face_up(ctx.opponent_id)


card = SupporterCardDef(
    guid="f7f04d60-e7bd-5505-afa0-fa7a659625b4",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!", "Supporter"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="XY12",
    rarity=Rarities.RareSecret,
    effect=here_comes_team_rocket
)
