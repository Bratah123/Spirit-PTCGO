from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


async def tierno(ctx):
    """Draw 3 cards."""
    await ctx.draw_cards(3)


card = SupporterCardDef(
    guid="7a08de01-1838-54b5-9af3-1231a99e11b2",
    key="XY0",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tierno.Name",
    display_name="Tierno",
    searchable_by=["Tierno", "Supporter"],
    subtypes=["Supporter"],
    collector_number=39,
    set_code="XY0",
    rarity=Rarities.Common,
    effect=tierno,
    condition=deck_nonempty
)
