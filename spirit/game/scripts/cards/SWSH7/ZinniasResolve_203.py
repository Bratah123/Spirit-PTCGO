from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least


async def zinnias_resolve(ctx):
    """Discard 2 other cards, then draw a card for each opposing Pokemon in play."""
    if not await ctx.discard_from_hand(2, prompt="Discard 2 cards for Zinnia's Resolve"):
        return
    await ctx.draw_cards(len(ctx.opponent_pokemon_in_play()))


card = SupporterCardDef(
    guid="06141105-31aa-5b68-b6ea-5bbd8ffa3b33",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ZinniasResolve.Name",
    display_name="Zinnia's Resolve",
    searchable_by=["Zinnia's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SWSH7",
    rarity=Rarities.RareUltra,
    effect=zinnias_resolve,
    condition=hand_size_at_least(3),
)
