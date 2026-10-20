from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.attacks_common import count_prizes_remaining


async def n_effect(ctx):
    """Each player shuffles their hand into their deck and draws a card for
    each of their remaining Prize cards."""
    my_n = count_prizes_remaining("mine")(ctx)
    opp_n = count_prizes_remaining("opponent")(ctx)
    for pid, count in ((ctx.player_id, my_n), (ctx.opponent_id, opp_n)):
        await ctx.shuffle_into_deck(ctx.hand(pid), pid)
        await ctx.draw_cards(count, pid)


card = SupporterCardDef(
    guid="86272063-ca7a-53d5-a076-1c42657e95bc",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    effect=n_effect
)
