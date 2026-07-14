from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.effects import full_stack
from spirit.game.session.passives import effective_max_hp


def _colorless_damaged(board, player_id):
    return [
        p for p in board.pokemon_in_play(player_id)
        if PokemonTypes.COLORLESS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])
        and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
    ]


def cherens_care_condition(board, player_id):
    return bool(_colorless_damaged(board, player_id))


async def cherens_care(ctx):
    """Put 1 of your Colorless Pokemon with damage counters and all attached
    cards into your hand."""
    candidates = _colorless_damaged(ctx.board, ctx.player_id)
    target = await ctx.choose_pokemon(
        candidates,
        "Choose 1 of your Colorless Pokémon with damage counters on it",
    )
    if target is None:
        return
    was_active = target is ctx.my_active()
    await ctx.put_in_hand(full_stack(target), reveal=False)
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


card = SupporterCardDef(
    guid="40fdf63e-1337-5e11-a5c3-833cac79c35d",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CherensCare.Name",
    display_name="Cheren's Care",
    searchable_by=["Cheren's Care", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SWSH9",
    rarity=Rarities.RareUltra,
    effect=cherens_care,
    condition=cherens_care_condition,
)
