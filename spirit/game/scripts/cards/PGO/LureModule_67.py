from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


async def lure_module_effect(ctx):
    """Each player reveals the top 3 of their deck; Pokemon found go to hand,
    the rest is shuffled back."""
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(3, player_id=pid)
        if not top:
            continue
        await ctx.reveal_cards(top)
        matches = [c for c in top if is_pokemon_card(c)]
        if matches:
            await ctx.put_in_hand(matches, reveal=False)
        await ctx.shuffle_deck(player_id=pid)


card = ItemCardDef(
    guid="d17d2b10-6400-5d79-9ae6-63504e64447f",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureModule.Name",
    display_name="Lure Module",
    searchable_by=["Lure Module", "Item"],
    subtypes=["Item"],
    collector_number=67,
    set_code="PGO",
    rarity=Rarities.Uncommon,
    effect=lure_module_effect
)
