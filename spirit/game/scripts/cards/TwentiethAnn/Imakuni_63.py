from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, SpecialConditions


async def imakuni(ctx):
    """Your Active Pokemon is now Confused."""
    a = ctx.my_active()
    if a is not None:
        await ctx.apply_special_condition(a, SpecialConditions.CONFUSED)


card = SupporterCardDef(
    guid="341cc365-8750-5f9e-b179-09265beb7dac",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Imakuni.Name",
    display_name="Imakuni?",
    searchable_by=["Imakuni?", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    effect=imakuni
)
