from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities


async def _ilima(ctx):
    """Each player shuffles their hand into their deck and flips a coin:
    heads draws 6 cards, tails draws 3."""
    for pid in (ctx.player_id, ctx.opponent_id):
        await ctx.shuffle_into_deck(list(ctx.hand(pid)), pid)
    for pid in (ctx.player_id, ctx.opponent_id):
        label = "Ilima" if pid == ctx.player_id else "Ilima (opponent)"
        results = await ctx.flip_coins(1, label)
        await ctx.draw_cards(6 if results and results[0] else 3, pid)


card = SupporterCardDef(
    guid="468319ec-3f86-5a21-9543-d9eaaa60dca9",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ilima.Name",
    display_name="Ilima",
    searchable_by=["Ilima", "Supporter"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SM1",
    rarity=Rarities.RareUltra,
    effect=_ilima
)
