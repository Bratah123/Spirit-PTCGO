from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def professor_oaks_hint(ctx):
    """Draw cards until you have 7 cards in your hand. Your turn ends."""
    await ctx.draw_until(7)
    ctx.ends_turn = True


card = SupporterCardDef(
    guid="50303223-e9c7-5a18-bb74-27048380401a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksHint.Name",
    display_name="Professor Oak's Hint",
    searchable_by=["Professor Oak's Hint", "Supporter"],
    subtypes=["Supporter"],
    collector_number=84,
    set_code="XY12",
    rarity=Rarities.Uncommon,
    effect=professor_oaks_hint
)
