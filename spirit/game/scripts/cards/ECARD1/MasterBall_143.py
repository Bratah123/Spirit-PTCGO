from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


async def master_ball(ctx):
    """Look at top 7; may take 1 Basic or Evolution Pokémon to hand (reveal)."""
    top = ctx.deck_top(7)
    if not top:
        return
    candidates = [c for c in top if is_pokemon_card(c)]
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="You may choose a Basic or Evolution Pokémon to put into your hand.",
        display_cards=top if len(candidates) < len(top) else None,
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ad5cd530-6545-577e-b08a-7cdb6e409f21",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MasterBall.Name",
    display_name="Master Ball",
    searchable_by=["Master Ball"],
    subtypes=[],
    collector_number=143,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    effect=master_ball,
)
