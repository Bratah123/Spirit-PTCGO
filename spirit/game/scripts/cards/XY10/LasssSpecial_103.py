from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_basic_pokemon


async def lasss_special(ctx):
    """Draw a card for each of your opponent's Benched Basic Pokemon."""
    n = sum(1 for p in ctx.opponent_bench() if is_basic_pokemon(p))
    if n:
        await ctx.draw_cards(n)


card = SupporterCardDef(
    guid="1a44fea6-e882-53b6-be66-799e0c629b48",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LasssSpecial.Name",
    display_name="Lass's Special",
    searchable_by=["Lass's Special", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=lasss_special
)
