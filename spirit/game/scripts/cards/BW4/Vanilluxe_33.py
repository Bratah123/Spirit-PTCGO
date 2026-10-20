from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.session.passives import effective_retreat_cost


def _defender_retreat(ctx):
    defender = ctx.defender
    return effective_retreat_cost(ctx.board, defender) if defender is not None else 0


def _slippery_soles_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    return bool(bench and bench.children)


async def _slippery_soles(ctx):
    """Switch your Active with a Benched Pokémon; then your opponent switches
    their Active with 1 of their Benched Pokémon."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is None:
        return
    await ctx.switch_active(ctx.player_id, target)
    opp_bench = ctx.opponent_bench()
    if opp_bench:
        opp_target = await ctx.choose_pokemon(
            opp_bench, "Choose your new Active Pokémon", player_id=ctx.opponent_id)
        if opp_target is not None:
            await ctx.switch_active(ctx.opponent_id, opp_target)


card = PokemonCardDef(
    guid="9d8bdbc4-454c-52f5-ac05-13fdd5fe6002",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="BW4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Ability(
            title="Slippery Soles",
            game_text="Once during your turn (before your attack), you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. If you do, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_slippery_soles_condition,
            effect=_slippery_soles,
        ),
        Attack(
            title="Crushing Ice",
            game_text="Does 10 more damage for each Colorless in the Defending Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=damage_per(_defender_retreat, 10, base=60),
        ),
    ],
)