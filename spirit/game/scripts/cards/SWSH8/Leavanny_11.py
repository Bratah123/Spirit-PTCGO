from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def healing_circle(ctx):
    """Heal all damage from each of your Benched Pokemon. If you healed any
    damage this way, shuffle this Pokemon and all attached cards into your
    deck."""
    healed_any = False
    for pokemon in ctx.my_bench():
        if await ctx.heal(ctx.max_hp(pokemon), pokemon) > 0:
            healed_any = True
    if not healed_any:
        return
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.opponent_id, f"{screen_name} has no Pokémon left"
            )

    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="5dad5f7a-4a87-5a64-8afe-be97109e30b9",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leavanny.Name",
    display_name="Leavanny",
    searchable_by=["Leavanny", "Stage 2", "Leavanny"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Healing Circle",
            game_text="Heal all damage from each of your Benched Pok\u00e9mon. If you healed any damage in this way, shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=healing_circle,
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)