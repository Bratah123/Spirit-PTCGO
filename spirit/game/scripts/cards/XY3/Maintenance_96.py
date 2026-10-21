from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import hand_size_at_least


async def maintenance(ctx):
    """Shuffle 2 cards from your hand into your deck. Then, draw a card."""
    hand = [c for c in ctx.hand() if c is not ctx.source]
    if len(hand) < 2:
        return
    picks = await ctx.choose_cards(hand, 2, minimum=2,
                                   prompt="Choose 2 cards to shuffle into your deck")
    if not picks or len(picks) < 2:
        return
    await ctx.shuffle_into_deck(picks, ctx.player_id)
    await ctx.draw_cards(1)


card = ItemCardDef(
    guid="9ea50b4a-94e5-5594-bd1d-f5bf360a35c6",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    effect=maintenance,
    condition=hand_size_at_least(3)
)
