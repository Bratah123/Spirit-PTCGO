from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


async def karen(ctx):
    """Each player shuffles all Pokemon in their discard pile into their deck."""
    for pid in (ctx.player_id, ctx.opponent_id):
        pool = [c for c in ctx.discard_pile(pid) if is_pokemon_card(c)]
        if pool:
            await ctx.shuffle_into_deck(pool, pid)


card = SupporterCardDef(
    guid="cb26bdcb-9b05-54e7-bc13-06b12e1518e7",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Karen.Name",
    display_name="Karen",
    searchable_by=["Karen", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    effect=karen
)
