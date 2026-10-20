from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.effects import full_stack


async def _silent_bite(ctx):
    """60; you may Paralyze the opponent's Active; if you do, shuffle this
    Pokemon and all attached cards into your deck."""
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or not await ctx.ask_yes_no("Paralyze your opponent's Active Pokémon and shuffle this Pokémon into your deck?"):
        return
    await ctx.apply_special_condition(target, SpecialConditions.PARALYZED)
    await ctx.flush_choreography()
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)

    async def _promote():
        if ctx.board.active_pokemon(ctx.player_id) is None \
                and not await ctx.session._promote_new_active(ctx.player_id):
            name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(ctx.opponent_id, f"{name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="6f80fe6e-99a8-5010-8d40-4df848a9b7c6",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatBREAK.Name",
    display_name="Crobat BREAK",
    searchable_by=["Crobat BREAK", "BREAK", "CrobatBREAK"],
    subtypes=["BREAK"],
    collector_number=181,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name",
    family_id=169,
    abilities=[
        Attack(
            title="Silent Bite",
            game_text="You may leave your opponent's Active Pok\u00e9mon Paralyzed. If you do, shuffle this Pok\u00e9mon and all cards attached to into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=_silent_bite,
        ),
    ],
)