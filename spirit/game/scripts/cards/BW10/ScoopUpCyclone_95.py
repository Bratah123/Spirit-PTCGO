from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import full_stack


async def scoop_up_cyclone(ctx):
    """ACE SPEC: put 1 of your Pokemon and all cards attached to it into your hand."""
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(),
                                      "Choose 1 of your Pokémon to put into your hand")
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.put_in_hand(full_stack(target), reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = ItemCardDef(
    guid="ef31f3c0-8c03-5904-9a30-af0472e7a8d2",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ScoopUpCyclone.Name",
    display_name="Scoop Up Cyclone",
    searchable_by=["Scoop Up Cyclone", "Item", "ACE SPEC"],
    subtypes=["Item", "ACE SPEC"],
    collector_number=95,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=scoop_up_cyclone
)
