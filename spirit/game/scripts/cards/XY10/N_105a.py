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
    guid="571125f2-970b-5bd1-b4f8-9ddc357f7975",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.N.Name",
    display_name="N",
    searchable_by=["N", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="XY10",
    rarity=Rarities.RareUltra,
    effect=n_effect
)
