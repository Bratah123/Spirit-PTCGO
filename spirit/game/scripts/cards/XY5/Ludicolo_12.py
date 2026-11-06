from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_targets


def _rhythm_condition(board, player_id, pokemon=None):
    opp = next((p for p in board.player_ids if p != player_id), None)
    bench = board.find_player_area(opp, "bench") if opp else None
    return bool(bench and bench.children)


async def _captivating_rhythm(ctx):
    """Flip a coin. If heads, switch 1 of your opponent's Benched Pokemon with their Active."""
    results = await ctx.flip_coins(1, "Captivating Rhythm")
    bench = ctx.opponent_bench()
    if not (results and results[0]) or not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon")
    await ctx.switch_active(ctx.opponent_id, target or bench[0])


card = PokemonCardDef(
    guid="73dbf764-cff7-56d8-8907-f5a6d3098b27",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Captivating Rhythm",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_rhythm_condition,
            effect=_captivating_rhythm,
        ),
        Attack(
            title="Solar Ray",
            game_text="Heal 20 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=heal_targets(20, scope='each_own'),
        ),
    ],
)