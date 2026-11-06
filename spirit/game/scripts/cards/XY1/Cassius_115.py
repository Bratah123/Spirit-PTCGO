from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import player_has_bench
from spirit.game.session.effects import full_stack


async def cassius(ctx):
    """Shuffle 1 of your Pokemon and all cards attached to it into your deck."""
    mine = ctx.my_pokemon_in_play()
    if not mine:
        return
    target = await ctx.choose_pokemon(mine, "Choose 1 of your Pokémon to shuffle into your deck")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.shuffle_into_deck(full_stack(target), ctx.player_id)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


card = SupporterCardDef(
    guid="9190592b-32c7-5093-9b78-20f93d475697",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cassius.Name",
    display_name="Cassius",
    searchable_by=["Cassius", "Supporter"],
    subtypes=["Supporter"],
    collector_number=115,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    effect=cassius,
    condition=player_has_bench
)
