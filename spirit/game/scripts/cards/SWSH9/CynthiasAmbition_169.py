from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def cynthias_ambition(ctx):
    """Draw to 5, or to 8 if any of your Pokemon were KO'd last turn."""
    target = 8 if ctx.kos_suffered_last_turn() > 0 else 5
    await ctx.draw_until(target)


card = SupporterCardDef(
    guid="56aebdb5-d9d2-5ec4-bb56-5e13db8d1f95",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasAmbition.Name",
    display_name="Cynthia's Ambition",
    searchable_by=["Cynthia's Ambition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=169,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    effect=cynthias_ambition
)
