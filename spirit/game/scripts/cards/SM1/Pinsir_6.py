from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def _roof_fling(ctx):
    """Flip a coin; heads: put the opponent's Active and all attached cards into their hand."""
    heads = (await ctx.flip_coins(1, "Roof Fling"))[0]
    if not heads:
        return
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.put_in_hand(full_stack(target), reveal=False)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="940b8253-3e10-53bc-820d-1056af4ce51e",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name",
    display_name="Pinsir",
    searchable_by=["Pinsir", "Basic", "Pinsir"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SM1",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Roof Fling",
            game_text="Flip a coin. If heads, put your opponent's Active Pok\u00e9mon and all cards attached to it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_roof_fling,
        ),
        Attack(
            title="Guillotine",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
    ],
)