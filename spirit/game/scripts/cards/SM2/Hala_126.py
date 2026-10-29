from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import gx_used


async def hala(ctx):
    """Shuffle your hand into your deck. Draw 7 if you have used your GX
    attack this game, otherwise draw 4."""
    await ctx.shuffle_into_deck(ctx.hand())
    await ctx.draw_cards(7 if gx_used(ctx) else 4)


card = SupporterCardDef(
    guid="d32bcd94-b172-596f-af42-3a5df001fec5",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hala.Name",
    display_name="Hala",
    searchable_by=["Hala", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    effect=hala,
)
