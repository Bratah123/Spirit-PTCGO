from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least


async def zinnias_resolve(ctx):
    """Discard 2 other cards, then draw a card for each opposing Pokemon in play."""
    if not await ctx.discard_from_hand(2, prompt="Discard 2 cards for Zinnia's Resolve"):
        return
    await ctx.draw_cards(len(ctx.opponent_pokemon_in_play()))


card = SupporterCardDef(
    guid="c68218d1-4f64-5bb9-a0e6-d2dbe06e7995",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ZinniasResolve.Name",
    display_name="Zinnia's Resolve",
    searchable_by=["Zinnia's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=225,
    set_code="SWSH7",
    rarity=Rarities.RareRainbow,
    effect=zinnias_resolve,
    condition=hand_size_at_least(3),
)
