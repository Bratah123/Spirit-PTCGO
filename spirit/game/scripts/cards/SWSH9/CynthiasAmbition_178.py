from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def cynthias_ambition(ctx):
    """Draw to 5, or to 8 if any of your Pokemon were KO'd last turn."""
    target = 8 if ctx.kos_suffered_last_turn() > 0 else 5
    await ctx.draw_until(target)


card = SupporterCardDef(
    guid="e0bb2327-e325-57a8-8b71-ea5ffdaee07a",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiasAmbition.Name",
    display_name="Cynthia's Ambition",
    searchable_by=["Cynthia's Ambition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SWSH9",
    rarity=Rarities.RareRainbow,
    effect=cynthias_ambition
)
