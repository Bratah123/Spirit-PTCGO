from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import full_stack


async def az(ctx):
    """Put 1 of your Pokemon into your hand. (Discard all cards attached.)"""
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                      "Choose 1 of your Pokémon to put into your hand")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.discard_cards([c for c in full_stack(target) if c is not target])
    await ctx.put_in_hand([target], reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = SupporterCardDef(
    guid="bb3855cc-0a1e-5265-adc3-428851559235",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AZ.Name",
    display_name="AZ",
    searchable_by=["AZ", "Supporter"],
    subtypes=["Supporter"],
    collector_number=117,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    effect=az
)
