from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.effects import full_stack


async def spinning_whip(ctx):
    """90. Opponent's Active is now Confused. Shuffle this Pokémon and all
    attached cards into your deck."""
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)
    await ctx.shuffle_into_deck(full_stack(ctx.attacker), ctx.player_id)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.player_id):
            screen_name = ctx.session.players[ctx.player_id].screen_name
            await ctx.session.end_game(
                ctx.opponent_id, f"{screen_name} has no Pokémon left"
            )

    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="a57b82ca-48a8-5ff7-88d1-9a179268b4cc",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name",
    display_name="Mienshao",
    searchable_by=["Mienshao", "Stage 1", "Rapid Strike", "Mienshao"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=77,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    family_id=619,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Spinning Whip",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. Shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=spinning_whip,
        ),
    ],
)