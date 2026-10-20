from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn


def _flash_condition(board, player_id, pokemon=None):
    opp = next((p for p in board.player_ids if p != player_id), None)
    a = board.active_pokemon(opp) if opp else None
    bench = board.find_player_area(opp, "bench") if opp else None
    return a is not None and bool(board.attached_energies(a)) and bool(bench and bench.children)


async def _royal_flash(ctx):
    """Flip; heads, move an Energy from the opponent's Active to 1 of their Benched Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        d = ctx.opponent_active()
        await ctx.move_energy_freely([d], ctx.opponent_bench(), max_count=1)


card = PokemonCardDef(
    guid="0c4a1653-bf54-5d51-a0b0-a637ec5117b6",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowking.Name",
    display_name="Slowking",
    searchable_by=["Slowking", "Stage 1", "Slowking"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="XY9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Royal Flash",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, move an Energy from your opponent's Active Pok\u00e9mon to 1 of his or her Benched Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_flash_condition,
            effect=_royal_flash,
        ),
        Attack(
            title="Psych Up",
            game_text="During your next turn, this Pok\u00e9mon's Psych Up attack does 40 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=boost_own_next_turn(40, attack_title='Psych Up'),
        ),
    ],
)