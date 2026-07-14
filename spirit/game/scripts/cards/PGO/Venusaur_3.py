from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


def _loopy_lasso_condition(board, player_id, pokemon=None):
    opponent = next((p for p in board.player_ids if p != player_id), None)
    bench = board.find_player_area(opponent, "bench") if opponent else None
    return bool(bench and bench.children)


async def loopy_lasso(ctx):
    """Once per turn: you may flip a coin. Heads: switch a Benched opponent
    Pokemon into the Active spot, and it becomes Asleep and Poisoned."""
    if not await ctx.ask_yes_no("Flip a coin?"):
        return
    if not (await ctx.flip_coins(1, "Loopy Lasso"))[0]:
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is None:
        return
    if not await ctx.switch_active(ctx.opponent_id, target):
        return
    await ctx.apply_special_condition(target, SpecialConditions.ASLEEP)
    await ctx.apply_special_condition(target, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="48e0438d-10e4-5279-98ed-e89ff00e9f81",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venusaur.Name",
    display_name="Venusaur",
    searchable_by=["Venusaur", "Stage 2", "Venusaur"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    family_id=1,
    abilities=[
        Ability(
            title="Loopy Lasso",
            game_text="Once during your turn, you may flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon, and the new Active Pok\u00e9mon is now Asleep and Poisoned.",
            activation=Activations.ONCE_PER_TURN,
            condition=_loopy_lasso_condition,
            effect=loopy_lasso,
        ),
        Attack(
            title="Solar Beam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
        ),
    ],
)