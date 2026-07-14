from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities


def _wyndon_stadium_in_play(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return False
    definition = def_for(getattr(stadium, "archetype_id", None) or "")
    return definition is not None and definition.display_name == "Wyndon Stadium"


async def league_staff(ctx):
    """Draw 2 cards. If Wyndon Stadium is in play, draw 2 more cards."""
    await ctx.draw_cards(2)
    if _wyndon_stadium_in_play(ctx):
        await ctx.draw_cards(2)


card = SupporterCardDef(
    guid="04da4d56-d324-5262-bad7-8599986b5234",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LeagueStaff.Name",
    display_name="League Staff",
    searchable_by=["League Staff", "Supporter"],
    subtypes=["Supporter"],
    collector_number=153,
    set_code="SWSH4",
    rarity=Rarities.Uncommon,
    effect=league_staff
)
