from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def carry_off(ctx):
    """Choose 1 of your opponent's Benched Pokemon. They shuffle that Pokemon
    and all attached cards into their deck. Then, shuffle this Pokemon and
    all attached cards into your deck."""
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon"
        )
        if target is not None and not ctx.effects_blocked(target):
            await ctx.shuffle_into_deck(full_stack(target), ctx.opponent_id)
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.opponent_id, f"{screen_name} has no Pokémon left"
            )

    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="d32a9091-53f1-5364-8586-1063e19c2c05",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=144,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Carry Off",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. They shuffle that Pok\u00e9mon and all attached cards into their deck. Then, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=carry_off,
        ),
    ],
)