from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _witch_rondo_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


async def witch_rondo(ctx):
    """You may switch your Active with a Benched Pokémon; if you do, your
    opponent switches their Active with a Benched Pokémon too."""
    bench = ctx.my_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no(
            "Switch your Active Pokémon with 1 of your Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    opp_bench = ctx.opponent_bench()
    if opp_bench:
        opp_target = await ctx.choose_pokemon(
            opp_bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id
        )
        if opp_target is not None:
            await ctx.switch_active(ctx.opponent_id, opp_target)


card = PokemonCardDef(
    guid="19405b49-dd40-5516-beb3-1920a1dbdb9e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hatterene.Name",
    display_name="Hatterene",
    searchable_by=["Hatterene", "Stage 2", "Hatterene"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="SWSH6",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hattrem.Name",
    family_id=856,
    abilities=[
        Ability(
            title="Witch Rondo",
            game_text="Once during your turn, you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_witch_rondo_condition,
            effect=witch_rondo,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 50, base=30),
        ),
    ],
)