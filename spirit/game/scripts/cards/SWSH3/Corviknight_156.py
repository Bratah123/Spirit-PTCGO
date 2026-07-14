from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


def _is_corviknight(pokemon) -> bool:
    d = def_for(pokemon.archetype_id)
    return bool(d) and d.display_name == "Corviknight"


async def flying_taxi(ctx):
    """On evolve: you may put 1 of your Pokémon (except any Corviknight) and
    all attached cards into your hand."""
    candidates = [p for p in ctx.my_pokemon_in_play() if not _is_corviknight(p)]
    if not candidates:
        return
    if not await ctx.ask_yes_no(
            "Put 1 of your Pokémon (except Corviknight) and all attached cards into your hand?"):
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon (not Corviknight) to put into your hand")
    if target is None:
        return
    is_active = target is ctx.my_active()
    await ctx.put_in_hand(full_stack(target), reveal=False)
    if is_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(ctx.opponent_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="3878f503-8254-5362-8157-3818792e1f60",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Corviknight.Name",
    display_name="Corviknight",
    searchable_by=["Corviknight", "Stage 2", "Corviknight"],
    subtypes=["Stage 2"],
    collector_number=156,
    set_code="SWSH3",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corvisquire.Name",
    family_id=821,
    abilities=[
        Ability(
            title="Flying Taxi",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 1 of your Pok\u00e9mon, except any Corviknight, and all attached cards into your hand.",
            trigger=Triggers.ON_EVOLVE,
            effect=flying_taxi,
        ),
        Attack(
            title="Blasting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
        ),
    ],
)